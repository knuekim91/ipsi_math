# -*- coding: utf-8 -*-
"""
ipsi_math - 수식 HTML을 LaTeX로 바꾸는 변환기

문항 파일의 수식은 유니코드 + <sub>/<sup> 로 적혀 있다.
이것을 KaTeX가 읽는 LaTeX로 옮긴다. 기호는 38종뿐이라 표 하나로 덮인다.

  python build/latex.py --check     # 전 문항을 변환해 결과를 JSON으로 뽑는다
  python build/latex.py --sample 5  # 표본을 눈으로 확인
"""
import argparse
import glob
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- 기호 표
SYM = {
    "−": "-",            # −  빼기(유니코드 마이너스)
    "→": r"\to ",
    "↦": r"\mapsto ",
    "⟺": r"\iff ",
    "≥": r"\ge ",
    "≤": r"\le ",
    "≠": r"\ne ",
    "≈": r"\approx ",
    "±": r"\pm ",
    "×": r"\times ",
    "·": r"\cdot ",
    "÷": r"\div ",
    "∈": r"\in ",
    "∩": r"\cap ",
    "∑": r"\sum ",        # Σ (수학 기호)
    "Σ": r"\sum ",        # Σ (그리스 대문자)
    "∫": r"\int ",
    "∠": r"\angle ",
    "°": r"^{\circ}",
    "′": "'",
    "…": r"\cdots ",
    "⌊": r"\lfloor ",
    "⌋": r"\rfloor ",
    "¼": r"\tfrac{1}{4}",
    "½": r"\tfrac{1}{2}",
    "α": r"\alpha ",
    "β": r"\beta ",
    "π": r"\pi ",
    "σ": r"\sigma ",
    "Δ": r"\Delta ",
}
# 수식 안에 섞여 들어온 글머리 기호 — 수식이 아니라 글자로 취급한다
AS_TEXT = ["①", "②", "③", "ㄱ", "ㄴ", "ㄷ"]

FUNCS = ["log", "sin", "cos", "tan", "lim", "max", "min", "gcd"]
COMBS = ["C", "H", "P"]       # nCr, nHr, nPr


def _entities(s):
    for a, b in (("&nbsp;", "~"), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"),
                 ("&minus;", "-"), ("&lsquo;", "'"), ("&rsquo;", "'"),
                 ("&middot;", r"\cdot ")):
        s = s.replace(a, b)
    return s


def _scripts(s):
    """<sub>x</sub> -> _{x},  <sup>x</sup> -> ^{x}"""
    s = re.sub(r"<sub>(.*?)</sub>", lambda m: "_{" + m.group(1) + "}", s, flags=re.S)
    s = re.sub(r"<sup>(.*?)</sup>", lambda m: "^{" + m.group(1) + "}", s, flags=re.S)
    return s


def _roots(s):
    """√7 -> \\sqrt{7},  √(a+b) -> \\sqrt{a+b},  ∛k -> \\sqrt[3]{k}"""
    def one(mark, cmd):
        out, i = [], 0
        while i < len(s_[0]):
            ch = s_[0][i]
            if ch != mark:
                out.append(ch); i += 1; continue
            i += 1
            if i < len(s_[0]) and s_[0][i] == "(":       # 괄호 묶음
                depth, j = 0, i
                while j < len(s_[0]):
                    if s_[0][j] == "(": depth += 1
                    elif s_[0][j] == ")":
                        depth -= 1
                        if depth == 0: break
                    j += 1
                out.append(cmd + "{" + s_[0][i + 1:j] + "}")
                i = j + 1
            else:                                        # 숫자/문자 덩어리
                j = i
                while j < len(s_[0]) and (s_[0][j].isalnum() or s_[0][j] == "."):
                    j += 1
                out.append(cmd + "{" + s_[0][i:j] + "}")
                i = j
        s_[0] = "".join(out)

    s_ = [s]
    one("√", r"\sqrt")      # √
    one("∛", r"\sqrt[3]")   # ∛
    return s_[0]


def _macron(s):
    """X̄ (결합 매크론) -> \\bar{X}"""
    return re.sub(r"([A-Za-z])̄", lambda m: r"\bar{" + m.group(1) + "}", s)


def _funcs(s):
    for f in FUNCS:
        s = re.sub(r"(?<![\\A-Za-z])" + f + r"(?![A-Za-z])", "\\\\" + f + " ", s)
    return s


def _combs(s):
    """_{5}H_{3} -> {}_{5}\\mathrm{H}_{3}"""
    for c in COMBS:
        s = re.sub(r"_\{([^}]*)\}" + c + r"_\{([^}]*)\}",
                   lambda m, c=c: "{}_{" + m.group(1) + "}\\mathrm{" + c + "}_{" + m.group(2) + "}", s)
    return s


def _mathify(run):
    """한글이 없는 조각을 LaTeX 본문으로 바꾼다."""
    s = run
    s = _macron(s)
    s = _roots(s)
    for k, v in SYM.items():
        s = s.replace(k, v)
    s = _funcs(s)
    s = _combs(s)
    return re.sub(r"\s+", " ", s).strip()


HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
MATHY  = re.compile(r"[0-9A-Za-z\=<>+\-^_{}]")


def to_mixed(html):
    """수식 컨테이너를 '한글 텍스트 + $수식$' 이 섞인 문자열로 바꾼다.

    문제 본문은 수식 덩어리가 아니라 한글 문장 사이에 수식이 박힌 것이므로,
    통째로 감싸지 않고 조각내어 수식만 $...$ 로 만든다."""
    s = _scripts(html)
    s = re.sub(r"<b>(.*?)</b>", lambda mm: mm.group(1), s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = _entities(s)

    # 한글 덩어리를 경계로 자른다
    parts, buf, out = [], [], []
    is_ko = lambda ch: bool(HANGUL.match(ch))
    cur = None
    for ch in s:
        k = is_ko(ch)
        if cur is None or k == cur:
            buf.append(ch); cur = k
        else:
            parts.append((cur, "".join(buf))); buf = [ch]; cur = k
    if buf:
        parts.append((cur, "".join(buf)))

    for ko, run in parts:
        if ko:
            out.append(run)
            continue
        # 한글이 아닌 조각: 수식 문자가 있으면 $...$, 아니면 그대로
        core = run.strip()
        if not core or not MATHY.search(core):
            out.append(run); continue
        lead = run[:len(run) - len(run.lstrip())]
        tail = run[len(run.rstrip()):]
        # 앞뒤에 붙은 문장부호는 수식 밖으로 뺀다.
        # 닫는 괄호는 수식의 일부일 수 있으므로 건드리지 않는다.
        PUNCT = " ,.?!:;"
        i, j = 0, len(core)
        while i < j and core[i] in PUNCT: i += 1
        while j > i and core[j-1] in PUNCT: j -= 1
        head_p, body, tail_p = core[:i], core[i:j], core[j:]
        if not body or not MATHY.search(body):
            out.append(run); continue
        out.append(lead + head_p + "$" + _mathify(body) + "$" + tail_p + tail)
    return "".join(out)


def to_latex(html):
    """컨테이너 전체가 수식일 때 쓰는 순수 LaTeX 변환."""
    s = _scripts(html)
    s = re.sub(r"<b>(.*?)</b>", lambda mm: mm.group(1), s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = _entities(s)
    return _mathify(s)


MATH_RE = re.compile(
    r"<(span|p)([^>]*)class=['\"]([^'\"]*\bm\b[^'\"]*)['\"]([^>]*)>(.*?)</\1>", re.S)


def convert_file(path):
    s = io.open(path, encoding="utf-8").read()
    items = []
    for m in MATH_RE.finditer(s):
        raw = m.group(5)
        items.append({"file": os.path.basename(path), "raw": raw,
                      "mixed": to_mixed(raw),
                      "pure": to_latex(raw) if not HANGUL.search(raw) else None})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sample", type=int, default=0)
    a = ap.parse_args()

    all_items = []
    for p in sorted(glob.glob(os.path.join(ROOT, "units", "*", "problems", "*.md"))):
        all_items.extend(convert_file(p))

    if a.sample:
        for it in all_items[:a.sample]:
            print("RAW  :", it["raw"][:110])
            print("MIXED:", it["mixed"][:110])
            print("-" * 60)

    if a.check:
        out = os.path.join(ROOT, "dist", "_latex.json")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(
            json.dumps(all_items, ensure_ascii=False, indent=1))
        print("수식 %d개 -> %s" % (len(all_items), out))


if __name__ == "__main__":
    main()
