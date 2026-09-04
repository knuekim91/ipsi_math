#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ipsi_math - 인쇄용 PDF 생성기

문항 파일(units/*/problems/*.md)을 읽어 두 개의 PDF를 만든다.
  1) <이름>_문제.pdf  : 문제 + 풀이 공간 (시험지처럼 인쇄)
  2) <이름>_해설.pdf  : 발상 + 풀이 + 노하우 + 정답

의존성 없음. 표준 라이브러리 + 시스템에 설치된 Chrome/Edge 헤드리스만 사용.

사용법
  python build/make_pdf.py --set sets/2026-09-05_지수로그.txt
  python build/make_pdf.py --unit 01-지수로그 --status wrong --name 지수로그_오답
  python build/make_pdf.py --ids EXP-001,EXP-004 --name 미니세트
  python build/make_pdf.py --all --name 전체
옵션
  --space 큼|보통|작음   문제지의 풀이 공간 크기 (기본 보통)
  --no-answer            해설지에 정답 요약표를 넣지 않음
"""
import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNITS_DIR = os.path.join(ROOT, "units")
DIST_DIR = os.path.join(ROOT, "dist")
CSS_PATH = os.path.join(ROOT, "build", "print.css")

EXAM_DATE = dt.date(2026, 11, 19)  # 2027학년도 수능

SPACE_MM = {"작음": 26, "보통": 46, "큼": 74}


# --------------------------------------------------------------------------
# 문항 파일 파싱
# --------------------------------------------------------------------------
def parse_problem(path):
    """front matter + '## 제목' 구획으로 나뉜 md 파일을 dict로 읽는다."""
    with open(path, encoding="utf-8") as f:
        raw = f.read().replace("\r\n", "\n")

    meta, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            head = raw[4:end]
            body = raw[end + 5:]
            for line in head.split("\n"):
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [t.strip() for t in v[1:-1].split(",") if t.strip()]
                else:
                    v = v.strip('"').strip("'")
                meta[k.strip()] = v

    sections, cur = {}, None
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            sections[cur] = []
        elif cur:
            sections[cur].append(line)
    for k in sections:
        sections[k] = "\n".join(sections[k]).strip()

    meta["_path"] = path
    meta["_sections"] = sections
    return meta


def load_all():
    out = {}
    for unit in sorted(os.listdir(UNITS_DIR)):
        pdir = os.path.join(UNITS_DIR, unit, "problems")
        if not os.path.isdir(pdir):
            continue
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            p = parse_problem(os.path.join(pdir, fn))
            pid = p.get("id") or os.path.splitext(fn)[0]
            p["id"] = pid
            p.setdefault("unit", unit)
            out[pid] = p
    return out


def read_set(path):
    """세트 파일: '# title: 이름' 지시자 + 문항 id 목록."""
    title, ids = None, []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                m = re.match(r"#\s*title\s*:\s*(.+)", line)
                if m:
                    title = m.group(1).strip()
                continue
            ids.append(line.split("#")[0].strip())
    return title, [i for i in ids if i]


# --------------------------------------------------------------------------
# HTML 생성
# --------------------------------------------------------------------------
def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def block(text):
    """섹션 본문: 빈 줄로 문단을 나눈다. 인라인 HTML은 그대로 둔다."""
    if not text:
        return ""
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    out = []
    for p in parts:
        if p.startswith("<"):
            out.append(p)
        else:
            out.append("<p>" + p.replace("\n", "<br>") + "</p>")
    return "\n".join(out)


def head(title, css):
    return (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f"<title>{esc(title)}</title><style>{css}</style></head><body>"
    )


def cover(title, subtitle, n, kind):
    dday = (EXAM_DATE - dt.date.today()).days
    return f"""
<header class="sheet-head">
  <div class="hl">
    <div class="ht">{esc(title)}</div>
    <div class="hs">{esc(subtitle)}</div>
  </div>
  <div class="hr">
    <div class="kind">{kind}</div>
    <div class="meta">{n}문항 · {dt.date.today():%Y.%m.%d} · 수능 D-{dday}</div>
  </div>
</header>"""


def render_questions(probs, space_mm):
    out = []
    for i, p in enumerate(probs, 1):
        s = p["_sections"]
        src = p.get("source", "")
        lvl = p.get("level", "")
        chips = " ".join(
            f'<span class="chip">{esc(c)}</span>'
            for c in [lvl, p.get("topic", ""), src] if c
        )
        out.append(f"""
<article class="q">
  <div class="qh"><span class="qn">{i}</span>{chips}<span class="qid">{esc(p['id'])}</span></div>
  <div class="stem">{block(s.get('문제',''))}</div>
  <div class="work" style="height:{space_mm}mm"></div>
</article>""")
    return "\n".join(out)


def render_solutions(probs, with_table):
    out = []
    if with_table:
        rows = "".join(
            f"<tr><td>{i}</td><td class='mono'>{esc(p['id'])}</td>"
            f"<td>{esc(p.get('topic',''))}</td>"
            f"<td class='ans'>{esc(p.get('answer',''))}</td></tr>"
            for i, p in enumerate(probs, 1)
        )
        out.append(
            "<section class='anstable'><h2>정답</h2><table>"
            "<thead><tr><th>번호</th><th>문항 ID</th><th>주제</th><th>정답</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></section>"
        )
    for i, p in enumerate(probs, 1):
        s = p["_sections"]
        parts = [f"""
<article class="s">
  <div class="qh"><span class="qn">{i}</span>
    <span class="chip">{esc(p.get('topic',''))}</span>
    <span class="qid">{esc(p['id'])}</span>
    <span class="ansbig">정답 {esc(p.get('answer',''))}</span></div>"""]
        if s.get("문제"):
            parts.append(f'<div class="restem">{block(s["문제"])}</div>')
        for label, cls in (("발상", "idea"), ("풀이", "sol"), ("다른 풀이", "alt"),
                           ("함정", "trap"), ("노하우", "know")):
            if s.get(label):
                parts.append(
                    f'<div class="{cls}"><span class="lab">{label}</span>{block(s[label])}</div>'
                )
        parts.append("</article>")
        out.append("\n".join(parts))
    return "\n".join(out)


# --------------------------------------------------------------------------
# PDF 변환
# --------------------------------------------------------------------------
def find_browser():
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in cands:
        if os.path.exists(c):
            return c
    for name in ("google-chrome", "chromium", "msedge"):
        w = shutil.which(name)
        if w:
            return w
    raise SystemExit("Chrome 또는 Edge를 찾지 못했습니다.")


def html_to_pdf(html, out_pdf):
    browser = find_browser()
    tmp = tempfile.mkdtemp(prefix="ipsi_")
    src = os.path.join(tmp, "page.html")
    with open(src, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        browser, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer",
        f"--user-data-dir={os.path.join(tmp, 'prof')}",
        f"--print-to-pdf={os.path.abspath(out_pdf)}",
        src,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if not os.path.exists(out_pdf):
        sys.stderr.write(r.stderr or "")
        raise SystemExit(f"PDF 생성 실패: {out_pdf}")
    shutil.rmtree(tmp, ignore_errors=True)
    return out_pdf


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set")
    ap.add_argument("--unit")
    ap.add_argument("--ids")
    ap.add_argument("--status")
    ap.add_argument("--tag")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--name")
    ap.add_argument("--space", default="보통", choices=list(SPACE_MM))
    ap.add_argument("--no-answer", action="store_true")
    args = ap.parse_args()

    all_p = load_all()
    if not all_p:
        raise SystemExit("문항이 없습니다. units/*/problems/*.md 를 먼저 만드세요.")

    title = args.name
    if args.set:
        t, ids = read_set(args.set)
        title = title or t or os.path.splitext(os.path.basename(args.set))[0]
        missing = [i for i in ids if i not in all_p]
        if missing:
            raise SystemExit("세트에 없는 문항 ID: " + ", ".join(missing))
        probs = [all_p[i] for i in ids]
    elif args.ids:
        ids = [i.strip() for i in args.ids.split(",") if i.strip()]
        probs = [all_p[i] for i in ids]
    else:
        probs = list(all_p.values())
        if args.unit:
            probs = [p for p in probs if args.unit in p.get("unit", "")]
        if args.status:
            probs = [p for p in probs if p.get("status") == args.status]
        if args.tag:
            probs = [p for p in probs if args.tag in (p.get("tags") or [])]
        probs.sort(key=lambda p: (p.get("unit", ""), p["id"]))

    if not probs:
        raise SystemExit("조건에 맞는 문항이 없습니다.")
    title = title or "연습세트"

    with open(CSS_PATH, encoding="utf-8") as f:
        css = f.read()

    units = sorted({p.get("unit", "") for p in probs})
    subtitle = " · ".join(u.split("-", 1)[-1] for u in units)
    os.makedirs(DIST_DIR, exist_ok=True)
    stamp = f"{dt.date.today():%Y%m%d}"

    q_html = (head(title + " 문제", css)
              + cover(title, subtitle, len(probs), "문제지")
              + render_questions(probs, SPACE_MM[args.space]) + "</body></html>")
    s_html = (head(title + " 해설", css)
              + cover(title, subtitle, len(probs), "해설지")
              + render_solutions(probs, not args.no_answer) + "</body></html>")

    qp = os.path.join(DIST_DIR, f"{stamp}_{title}_문제.pdf")
    sp = os.path.join(DIST_DIR, f"{stamp}_{title}_해설.pdf")
    html_to_pdf(q_html, qp)
    html_to_pdf(s_html, sp)
    print(f"문제지 : {qp}")
    print(f"해설지 : {sp}")
    print(f"문항수 : {len(probs)}  ({', '.join(p['id'] for p in probs)})")


if __name__ == "__main__":
    main()
