# -*- coding: utf-8 -*-
"""
ipsi_math - 정적 사이트용 데이터 생성기

units/*/problems/*.md 를 읽어 docs/data.js 로 내보낸다.
수식은 build/latex.py 로 LaTeX($...$)로 바꾼다.

  python build/make_site.py
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from latex import to_mixed  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "data.js")

# 과목 → 단원. 수능 출제 과목 기준으로 묶는다.
SUBJECTS = [
    {"key": "수학Ⅰ", "short": "수Ⅰ", "units": ["01-지수로그", "02-삼각함수", "03-수열"]},
    {"key": "수학Ⅱ", "short": "수Ⅱ", "units": ["04-극한연속", "05-미분", "06-적분"]},
    {"key": "확률과 통계", "short": "확통", "units": ["07-경우의수확률", "08-통계"]},
]

UNITS = {
    "01-지수로그":     {"label": "지수와 로그",     "hue": 38},
    "02-삼각함수":     {"label": "삼각함수",        "hue": 190},
    "03-수열":         {"label": "수열",            "hue": 265},
    "04-극한연속":     {"label": "극한과 연속",     "hue": 165},
    "05-미분":         {"label": "미분",            "hue": 345},
    "06-적분":         {"label": "적분",            "hue": 100},
    "07-경우의수확률": {"label": "경우의 수·확률",  "hue": 20},
    "08-통계":         {"label": "통계",            "hue": 215},
}

SECTIONS = [("문제", "q"), ("발상", "idea"), ("풀이", "sol"),
            ("다른 풀이", "alt"), ("함정", "trap"), ("노하우", "know")]


def parse(path):
    raw = io.open(path, encoding="utf-8").read().replace("\r\n", "\n")
    meta, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            for line in raw[4:end].split("\n"):
                if ":" in line and not line.lstrip().startswith("#"):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            body = raw[end + 5:]
    sec, cur = {}, None
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip(); sec[cur] = []
        elif cur:
            sec[cur].append(line)
    return meta, {k: "\n".join(v).strip() for k, v in sec.items()}


MATH_RE = re.compile(
    r"<(span|p)([^>]*)class=['\"]([^'\"]*\bm\b[^'\"]*)['\"]([^>]*)>(.*?)</\1>", re.S)


def latexify(html):
    """수식 컨테이너만 LaTeX로 바꾸고 나머지 HTML 구조는 살린다."""
    def rep(m):
        tag, cls, inner = m.group(1), m.group(3), m.group(5)
        tex = to_mixed(inner)
        if "cond" in cls:
            return '<div class="cond">%s</div>' % tex
        if tag == "p":
            return '<p class="eq">%s</p>' % tex
        return tex
    html = MATH_RE.sub(rep, html)

    # 선택지의 수식도 바꾼다 (①②③ 표시는 그대로 두고 뒤쪽만)
    def choice(m):
        inner = m.group(1)
        def one(mm):
            mark, body = mm.group(1), mm.group(2).strip()
            return "<span><i>%s</i>%s</span>" % (mark, (" " + to_mixed(body)) if body else "")
        inner = re.sub(r"<span>\s*([①-⑳])\s*(.*?)</span>", one, inner, flags=re.S)
        return '<div class="choices">%s</div>' % inner
    html = re.sub(r'<div class="choices">(.*?)</div>', choice, html, flags=re.S)
    return html


def plain(html):
    t = re.sub(r"<[^>]+>", " ", html or "")
    for a, b in (("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"),
                 ("&lsquo;", "'"), ("&rsquo;", "'")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def build():
    probs = []
    for unit in sorted(UNITS):
        d = os.path.join(ROOT, "units", unit, "problems")
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            meta, sec = parse(os.path.join(d, fn))
            item = {
                "id": meta.get("id", fn[:-3]),
                "unit": unit,
                "topic": meta.get("topic", ""),
                "level": meta.get("level", ""),
                "diff": meta.get("difficulty", ""),
                "source": meta.get("source", ""),
                "core": meta.get("core", ""),
                "answer": meta.get("answer", ""),
                "tags": [t.strip() for t in
                         meta.get("tags", "").strip("[]").split(",") if t.strip()],
            }
            for name, key in SECTIONS:
                item[key] = latexify(sec.get(name, "")) if sec.get(name) else ""
            # 기출 번호 (2027-09모평 12번 -> 12)
            m = re.search(r"(\d+)\s*번", item["source"])
            item["no"] = int(m.group(1)) if m else 999
            item["search"] = " ".join([
                item["id"], item["topic"], item["source"], item["level"], item["core"],
                " ".join(item["tags"]), plain(item["q"]),
                plain(item["idea"]), plain(item["know"]),
            ]).lower()
            probs.append(item)

    probs.sort(key=lambda p: p["no"])

    unit_meta = {k: dict(v, count=sum(1 for p in probs if p["unit"] == k))
                 for k, v in UNITS.items()}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    payload = {"problems": probs, "units": unit_meta, "subjects": SUBJECTS,
               "exam": "2026-11-19"}
    io.open(OUT, "w", encoding="utf-8").write(
        "window.DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n")
    print("문항 %d개 -> %s (%.0f KB)" % (len(probs), OUT, os.path.getsize(OUT) / 1024))
    for s in SUBJECTS:
        n = sum(unit_meta[u]["count"] for u in s["units"])
        print("  %s %d문항  (%s)" % (s["short"], n,
              ", ".join("%s %d" % (unit_meta[u]["label"], unit_meta[u]["count"])
                        for u in s["units"])))


if __name__ == "__main__":
    build()
