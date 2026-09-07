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
# 시험 이름 규칙 : "<학년도>-<시험>"  (06모평 / 09모평 / 수능)
TERM_ORDER = {"06모평": 1, "09모평": 2, "수능": 3}
# 시험이 아닌 교재. 모의평가·수능 뒤에 놓는다.
BOOKS = {"수능특강": 4, "수능완성": 5}


def exam_parts(e):
    """'2027-06모평' -> ('2027', '6월 모평', '2027학년도 6월 모의평가', 1)"""
    yy, _, term = e.partition("-")
    if term == "수능":
        return yy, "수능", "%s학년도 수능" % yy, 3
    if term in BOOKS:
        return yy, term, "%s %s" % (yy, term), BOOKS[term]
    mm = term.replace("모평", "").lstrip("0")
    return yy, "%s월 모평" % mm, "%s학년도 %s월 모의평가" % (yy, mm),         TERM_ORDER.get(term, 9)


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


def stamp(n):
    """index.html 의 app.css / data.js / app.js 에 ?v=... 를 붙인다.

    안 붙이면 나은이 브라우저가 옛 data.js 를 그대로 써서
    새 문항이나 고친 풀이가 안 보인다. 실제로 한 번 겪었다.
    """
    import datetime
    v = datetime.datetime.now().strftime("%Y%m%d%H%M")
    p = os.path.join(ROOT, "docs", "index.html")
    s = io.open(p, encoding="utf-8").read()
    for f in ("app.css", "config.js", "data.js", "app.js", "auth.js"):
        s = re.sub('"' + re.escape(f) + r'(\?v=\d+)?"',
                   '"%s?v=%s"' % (f, v), s)
    io.open(p, "w", encoding="utf-8").write(s)


def build():
    probs = []
    for unit in sorted(UNITS):
        d = os.path.join(ROOT, "units", unit, "problems")
        if not os.path.isdir(d):
            continue
        # problems/ 바로 아래와 그 하위 폴더(2027수능완성 등)를 모두 읽는다
        files = []
        for root, dirs, names in os.walk(d):
            dirs[:] = [x for x in dirs if not x.startswith((".", "_"))]
            for fn in names:
                if fn.endswith(".md") and not fn.startswith("_"):
                    files.append(os.path.join(root, fn))
        for path in sorted(files, key=lambda x: os.path.basename(x)):
            fn = os.path.basename(path)
            meta, sec = parse(path)
            item = {
                "id": meta.get("id", fn[:-3]),
                "unit": unit,
                "topic": meta.get("topic", ""),
                "level": meta.get("level", ""),
                "diff": meta.get("difficulty", ""),
                "source": meta.get("source", ""),
                "exam": meta.get("exam", ""),
                "origin": meta.get("origin", "기출"),
                "lecture": meta.get("lecture", ""),
                "parent": meta.get("parent", "").strip(),
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
            item["year"] = item["exam"].partition("-")[0]
            item["search"] = " ".join([
                item["id"], item["topic"], item["source"], item["level"], item["core"],
                " ".join(item["tags"]), plain(item["q"]),
                plain(item["idea"]), plain(item["know"]),
            ]).lower()
            probs.append(item)

    # 최신 학년도가 위로, 한 학년도 안에서는 시행 순서(6월→9월→수능) → 문항 번호
    def order(p):
        yy, _, _, t = exam_parts(p["exam"])
        return (-int(yy) if yy.isdigit() else 0, t, p["no"])
    probs.sort(key=order)

    # 부모가 있는 문항(유사문항·사다리)은 목록과 집계에서 뺀다.
    # 부모 카드 안에서만 보이므로 "기출 몇 문항" 숫자가 흔들리지 않는다.
    kids = {}
    for p in probs:
        if p["parent"]:
            kids.setdefault(p["parent"], []).append(p)
    for v in kids.values():
        v.sort(key=lambda p: p["id"])
    main = [p for p in probs if not p["parent"]]
    for p in main:
        p["kids"] = [k["id"] for k in kids.get(p["id"], [])]
    orphan = sorted(set(kids) - {p["id"] for p in main})
    if orphan:
        print("  ! 부모를 찾지 못한 문항: %s" % ", ".join(orphan))

    unit_meta = {k: dict(v, count=sum(1 for p in main if p["unit"] == k))
                 for k, v in UNITS.items()}

    ex_ids = {p["exam"] for p in main if p["exam"]}
    bucket = {}
    for e in ex_ids:
        yy, label, full, t = exam_parts(e)
        bucket.setdefault(yy, []).append(
            {"id": e, "label": label, "full": full, "sort": t,
             "count": sum(1 for p in main if p["exam"] == e)})
    years = []
    for yy in sorted(bucket, key=lambda v: -int(v) if v.isdigit() else 0):
        lst = sorted(bucket[yy], key=lambda v: v["sort"])
        for v in lst:
            v.pop("sort")
        years.append({"id": yy, "label": yy + "학년도", "short": yy,
                      "count": sum(v["count"] for v in lst), "exams": lst})
    exams = [v for y in years for v in y["exams"]]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    payload = {"problems": main, "units": unit_meta, "subjects": SUBJECTS,
               "years": years, "exams": exams, "exam": "2026-11-19",
               "kids": {k: v for k, v in
                        ((pid, [dict(x) for x in lst]) for pid, lst in kids.items())}}
    io.open(OUT, "w", encoding="utf-8").write(
        "window.DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n")
    stamp(len(probs))
    n_kid = sum(len(v) for v in kids.values())
    print("문항 %d개 (+ 딸림 %d개) -> %s (%.0f KB)"
          % (len(main), n_kid, OUT, os.path.getsize(OUT) / 1024))
    for y in years:
        print("  %s  %d문항  (%s)" % (y["label"], y["count"],
              ", ".join("%s %d" % (v["label"], v["count"]) for v in y["exams"])))
    for s in SUBJECTS:
        n = sum(unit_meta[u]["count"] for u in s["units"])
        print("  %s %d문항  (%s)" % (s["short"], n,
              ", ".join("%s %d" % (unit_meta[u]["label"], unit_meta[u]["count"])
                        for u in s["units"])))


if __name__ == "__main__":
    build()
