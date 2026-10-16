#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""인쇄물 목록 페이지 생성기.

docs/pdf/ 에 올린 PDF 를 한 쪽에 모아 docs/prints.html 을 만든다.
PDF 가 늘 때마다 아래 SETS 에 한 줄 추가하고 다시 돌린다.

사용법
  python build/make_pdflist.py
"""
import datetime as dt
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "prints.html")
EXAM_DATE = dt.date(2026, 11, 19)

# (날짜, 제목, 한 줄 설명, 파일이름 앞부분, 문항 수)
SETS = [
    ("2026-10-17", "부호가 걸린 정수 순서쌍", "10월 30번. |x|+x 는 음수를 0으로 뭉갠다. 양수끼리는 크기가 남는다.",
     "signed-integer-tuples", 4),
    ("2026-10-17", "역함수인 두 곡선과 직선", "10월 22번. 교점은 y=x 위에 있고, 직선은 늘 (1,1)을 지난다.",
     "inverse-pair-curves", 4),
    ("2026-10-17", "같은 함숫값을 갖는 두 점", "10월 15번. 수평선으로 보고, 보이지 않는 것은 합과 곱의 관계식으로.",
     "same-value-pair", 4),
    ("2026-10-16", "실근의 개수가 같을 조건", "수학 15번. 개수표를 만들고 경계에 스치는 자리를 찾는다.",
     "root-count", 4),
    ("2026-10-11", "동전 뒤집기와 조건부확률", "확통 30번. 분모는 홀짝으로, 분자는 상태표로.",
     "coin-tetrahedron", 7),
    ("2026-10-09", "멈추는 시행의 횟수와 기댓값", "설맞이 57번. 순서를 나열하지 말고 누적합 상태만 따라간다.",
     "stopping-trials", 6),
    ("2026-10-04", "순서가 정해진 나열", "2016 9월 B형 15번. 분모를 구별해 세었으면 분자도 그렇게.",
     "order-arrangement", 7),
    ("2026-09-30", "동전 뒤집기", "확통 28번. 뒷면 개수의 홀짝만 본다.",
     "coin-flip", 5),
]

# 문제지·해설지가 따로 없는 한 장짜리
SINGLES = [
    ("2026-10-05", "사회·문화 표 자료 분석", "평가원 6월·9월 표 문항 패턴 변형 9제.",
     "social-table-analysis", 9),
]


def build():
    d = (EXAM_DATE - dt.date.today()).days
    rows = []
    for day, title, desc, slug, n in SETS:
        rows.append(
            '<li class="pr">'
            '<div class="pm"><b>%s</b><span class="pd">%s · %d문항</span>'
            '<span class="pz">%s</span></div>'
            '<div class="pl"><a href="pdf/%s-problems.pdf">문제지</a>'
            '<a href="pdf/%s-solutions.pdf">해설지</a></div></li>'
            % (title, day, n, desc, slug, slug))
    for day, title, desc, slug, n in SINGLES:
        rows.append(
            '<li class="pr">'
            '<div class="pm"><b>%s</b><span class="pd">%s · %d문항</span>'
            '<span class="pz">%s</span></div>'
            '<div class="pl"><a href="pdf/%s.pdf">문제 + 해설</a></div></li>'
            % (title, day, n, desc, slug))

    html = PAGE % {"rows": "\n".join(rows), "dday": d,
                   "n": len(SETS) + len(SINGLES),
                   "v": dt.datetime.now().strftime("%Y%m%d%H%M")}
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("인쇄물 %d묶음 -> %s" % (len(SETS) + len(SINGLES), OUT))
    for day, title, _, slug, n in SETS:
        print("   %s  %-22s %d문항  pdf/%s-*.pdf" % (day, title, n, slug))
    for day, title, _, slug, n in SINGLES:
        print("   %s  %-22s %d문항  pdf/%s.pdf" % (day, title, n, slug))


PAGE = u"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>인쇄물 · ipsi</title>
<link rel="stylesheet" href="app.css?v=%(v)s">
<style>
.back{display:inline-block;margin:18px 0 14px;font:600 13px/1 var(--mono);
      color:var(--tx3);text-decoration:none}
.back:hover{color:var(--gen)}
.hd{padding:8px 0 22px;border-bottom:1px solid var(--line);margin-bottom:8px}
.hd h1{font:700 clamp(26px,5vw,38px)/1.26 var(--disp);margin:0 0 10px}
.hd p{color:var(--tx2);font-size:15px;line-height:1.8;margin:0 0 14px}
.chips{display:flex;gap:9px;flex-wrap:wrap}
.chip{font:600 12px/1 var(--mono);color:var(--tx2);border:1px solid var(--line);
      border-radius:999px;padding:9px 13px}
.chip b{color:var(--tx)}
ul.prs{list-style:none;margin:0;padding:0}
.pr{display:flex;gap:16px;align-items:center;flex-wrap:wrap;
    padding:16px 0;border-bottom:1px solid var(--line2)}
.pm{flex:1;min-width:240px}
.pm b{display:block;color:var(--tx);font-size:16px;font-weight:600;margin-bottom:4px}
.pd{display:block;font:500 12px/1.6 var(--mono);color:var(--tx3)}
.pz{display:block;color:var(--tx2);font-size:13.5px;line-height:1.7;margin-top:5px}
.pl{display:flex;gap:9px;flex:none}
.pl a{font:600 13px/1 var(--mono);padding:11px 15px;border:1px solid var(--line);
      border-radius:999px;color:var(--tx2);text-decoration:none;white-space:nowrap}
.pl a:hover{border-color:var(--gen);color:var(--gen)}
.ft{margin:34px 0 60px;color:var(--tx3);font-size:13px;line-height:1.85}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="./">&larr; 수학으로 돌아가기</a>
  <header class="hd">
    <h1>인쇄물</h1>
    <p>풀어 본 뒤 해설지로 채점하세요. 문제지에는 풀이 공간이 들어 있습니다.</p>
    <div class="chips"><span class="chip"><b>%(n)d</b> 묶음</span>
      <span class="chip">수능 D-%(dday)d</span></div>
  </header>
  <ul class="prs">
%(rows)s
  </ul>
  <p class="ft">새 문제를 가져오면 같은 자리에 쌓입니다.
     폰에서 눌러도 바로 열리고, 집 프린터로 그대로 인쇄됩니다.</p>
</div>
</body>
</html>
"""


if __name__ == "__main__":
    build()
