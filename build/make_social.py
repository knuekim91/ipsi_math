#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""사회·문화 표 자료 분석 페이지 생성기.

social/table-analysis.json 을 읽어 docs/social.html 을 만든다.
수학 쪽과 같은 app.css 를 쓰므로 화면 느낌이 그대로 이어진다.

사용법
  python build/make_social.py
"""
import io
import json
import os
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "social", "table-analysis.json")
OUT = os.path.join(ROOT, "docs", "social.html")
EXAM_DATE = dt.date(2026, 11, 19)

LEVEL_CLASS = {"중": "lv-mid", "상": "lv-high", "킬러": "lv-kill"}


def esc(s):
    return s if s else ""


def table_html(t):
    if not t:
        return ""
    out = ['<div class="tw"><table class="dt">']
    if t.get("caption"):
        out.append("<caption>%s</caption>" % esc(t["caption"]))
    out.append("<thead><tr>")
    for h in t["head"]:
        out.append("<th>%s</th>" % esc(h))
    out.append("</tr></thead><tbody>")
    for r in t["rows"]:
        out.append("<tr>")
        for i, c in enumerate(r):
            tag = "th" if (i == 0 and len(t["head"]) == len(r) and
                           t["head"][0] in ("구분", "")) else "td"
            out.append("<%s>%s</%s>" % (tag, esc(c), tag))
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def item_html(it, no):
    p = ['<article class="p sp" data-id="%s">' % it["id"]]
    p.append('<div class="phd"><span class="pno">%d</span>'
             '<div class="pti"><b>%s</b>'
             '<span class="psub">%s · %s</span></div>'
             '<span class="lv %s">%s</span></div>'
             % (no, esc(it["ask"]), it["id"],
                esc(it.get("src", "자체 개발")),
                LEVEL_CLASS.get(it["level"], "lv-mid"), it["level"]))

    p.append('<div class="pbody">')
    p.append('<div class="stem">%s' % esc(it["given"]))
    p.append(table_html(it.get("table")))
    if it.get("formula"):
        p.append('<div class="fml">%s</div>' % it["formula"])
    if it.get("boxes"):
        p.append('<div class="bogi"><div class="bgt">&lt; 보 기 &gt;</div><ol>')
        for b in it["boxes"]:
            p.append("<li>%s</li>" % esc(b))
        p.append("</ol></div>")
    p.append('<ol class="choices5">')
    for c in it["choices"]:
        p.append("<li>%s</li>" % esc(c))
    p.append("</ol></div>")

    p.append('<div class="acts">'
             '<button class="act" data-t="idea">발상 보기</button>'
             '<button class="act" data-t="sol">풀이 보기</button>'
             '<button class="act" data-t="ans">정답</button></div>')

    p.append('<section class="pane" data-t="idea"><h4>발상</h4><p>%s</p></section>'
             % esc(it["idea"]))

    sol = ['<section class="pane" data-t="sol"><h4>풀이</h4>']
    for i, (head, body) in enumerate(it["steps"], 1):
        sol.append('<p><span class="step">%s %s</span> %s</p>'
                   % ("①②③④⑤⑥⑦⑧"[i - 1], esc(head), esc(body)))
    if it.get("trap"):
        sol.append("<h4>함정</h4><p>%s</p>" % esc(it["trap"]))
    if it.get("tip"):
        sol.append("<h4>노하우</h4><p>%s</p>" % esc(it["tip"]))
    sol.append("</section>")
    p.append("".join(sol))

    p.append('<section class="pane" data-t="ans"><div class="ansbig">정답 '
             "<b>%s</b></div></section>" % it["answer"])
    p.append("</div></article>")
    return "".join(p)


def build():
    data = json.load(io.open(SRC, encoding="utf-8"))
    dday = (EXAM_DATE - dt.date.today()).days
    n = sum(len(g["items"]) for g in data["groups"])

    body = []
    no = 0
    for g in data["groups"]:
        body.append('<section class="grp" id="g-%s">' % g["key"])
        body.append('<h2><span class="gk">%s</span> %s '
                    '<span class="gn">%d문항</span></h2>'
                    % (g["key"], esc(g["name"]), len(g["items"])))
        body.append('<p class="why">%s</p>' % esc(g["why"]))
        for it in g["items"]:
            no += 1
            body.append(item_html(it, no))
        body.append("</section>")

    nav = "".join('<a class="nv" href="#g-%s">%s. %s</a>' % (g["key"], g["key"], g["name"])
                  for g in data["groups"])

    html = PAGE % {
        "title": esc(data["title"]),
        "subtitle": esc(data["subtitle"]),
        "note": esc(data["note"]),
        "n": n,
        "dday": dday,
        "nav": nav,
        "body": "".join(body),
        "v": dt.datetime.now().strftime("%Y%m%d%H%M"),
    }
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("사회문화 %d문항 -> %s (%d KB)" % (n, OUT, len(html.encode("utf-8")) // 1024))
    print("  D-%d" % dday)
    for g in data["groups"]:
        print("  %s. %-18s %d문항  (%s)"
              % (g["key"], g["name"], len(g["items"]),
                 ", ".join(i["level"] for i in g["items"])))


PAGE = u"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s · ipsi</title>
<link rel="stylesheet" href="app.css?v=%(v)s">
<style>
/* 사회문화 전용 — 수학 쪽 토큰을 그대로 쓴다 */
.sp .phd{align-items:flex-start}
.sp .pti b{font-weight:600;line-height:1.5;display:block}
.psub{display:block;font:500 12px/1.6 var(--mono);color:var(--tx3);margin-top:3px}
.lv{flex:none;font:700 11px/1 var(--mono);padding:5px 8px;border-radius:999px;
    border:1px solid var(--line)}
.lv-mid{color:#3b82f6}.lv-high{color:#f59e0b}.lv-kill{color:#ef4444}
.stem p{margin:0 0 10px}
.tw{overflow-x:auto;margin:12px 0}
table.dt{border-collapse:collapse;width:100%%;font-size:14px;min-width:min(100%%,420px)}
table.dt caption{caption-side:top;text-align:left;font:600 12px/1.6 var(--mono);
    color:var(--tx3);padding-bottom:6px}
table.dt th,table.dt td{border:1px solid var(--line);padding:7px 10px;text-align:center;
    font-variant-numeric:tabular-nums}
table.dt thead th{background:var(--card2);font-weight:600}
table.dt tbody th{background:var(--card2);font-weight:600;white-space:nowrap}
.fml{border:1px dashed var(--line);border-radius:10px;padding:10px 12px;margin:12px 0;
     font-size:13px;line-height:1.9;color:var(--tx2)}
.bogi{border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:12px 0}
.bgt{text-align:center;font:600 13px/1 var(--mono);color:var(--tx3);margin-bottom:8px}
.bogi ol{margin:0;padding-left:1.5em;list-style:none}
.bogi li{counter-increment:bg;margin:5px 0;position:relative}
.bogi li::before{content:counter(bg,hanja);position:absolute;left:-1.5em;
    font-weight:600;color:var(--tx3)}
.bogi{counter-reset:bg}
ol.choices5{list-style:none;margin:12px 0 0;padding:0;counter-reset:ch}
ol.choices5 li{counter-increment:ch;margin:6px 0;padding-left:1.7em;position:relative;
    line-height:1.7}
/* circled-decimal 은 브라우저마다 없을 수 있어 직접 정의한다 */
@counter-style circ{system:fixed;symbols:"①" "②" "③" "④" "⑤";suffix:" "}
@counter-style hanja{system:fixed;symbols:"ㄱ" "ㄴ" "ㄷ" "ㄹ";suffix:". "}
ol.choices5 li::before{content:counter(ch,circ);
    position:absolute;left:0;color:var(--tx3);font-weight:600}
.grp{margin:38px 0 0}
.grp h2{font:700 20px/1.4 var(--disp);margin:0 0 6px;display:flex;align-items:center;gap:9px}
.gk{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:9px;
    background:var(--gen);color:#fff;font:700 15px/1 var(--mono)}
.gn{font:500 12px/1 var(--mono);color:var(--tx3)}
.why{color:var(--tx2);font-size:14px;line-height:1.85;margin:0 0 16px;
     border-left:3px solid var(--line);padding-left:12px}
.navbar{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}
.nv{font:600 13px/1 var(--mono);padding:9px 12px;border:1px solid var(--line);
    border-radius:999px;color:var(--tx2);text-decoration:none}
.nv:hover{border-color:var(--gen);color:var(--gen)}
.back{display:inline-block;margin-bottom:14px;font:600 13px/1 var(--mono);
      color:var(--tx3);text-decoration:none}
.back:hover{color:var(--gen)}
.hero-s{padding:30px 0 22px;border-bottom:1px solid var(--line);margin-bottom:6px}
.hero-s h1{font:700 clamp(26px,5vw,40px)/1.26 var(--disp);margin:0 0 10px}
.lead{color:var(--tx2);font-size:15px;line-height:1.8;margin:0 0 8px}
.note{color:var(--tx3);font-size:13.5px;line-height:1.8;margin:0 0 14px}
.chips{display:flex;gap:9px;flex-wrap:wrap}
.chip{font:600 12px/1 var(--mono);color:var(--tx2);border:1px solid var(--line);
      border-radius:999px;padding:9px 13px}
.chip b{color:var(--tx)}
.act.on{border-color:var(--gen);color:var(--gen)}
.ft{margin:46px 0 60px;padding-top:20px;border-top:1px solid var(--line)}
.ft p{color:var(--tx2);font-size:14px;line-height:1.85;margin:0 0 8px}
.cr{color:var(--tx3);font-size:12.5px}
@media print{
  /* 인쇄물은 흰 바탕 검은 글씨로 뽑는다. 화면용 다크 토큰을 전부 덮어쓴다 */
  :root{--bg:#fff;--bg2:#fff;--card:#fff;--card2:#fff;
        --line:#999;--line2:#bbb;--tx:#000;--tx2:#222;--tx3:#555;--gen:#444;--glow:none}
  body{background:#fff;color:#000}
  .acts,.navbar,.back{display:none}
  .pane{display:block!important}
  .p.sp{break-inside:avoid;border:1px solid #999;box-shadow:none;margin-bottom:14px}
  .grp{break-before:auto}
  .gk,.xi{background:#444}
  .lv{border-color:#999;color:#000}
  table.dt th,table.dt td{border-color:#666}
  table.dt thead th,table.dt tbody th{background:#eee}
  .pane h4{margin-top:10px}
}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="./">&larr; 수학으로 돌아가기</a>
  <header class="hero-s">
    <h1>%(title)s</h1>
    <p class="lead">%(subtitle)s</p>
    <p class="note">%(note)s</p>
    <div class="chips"><span class="chip"><b>%(n)d</b> 문항</span>
      <span class="chip">수능 D-%(dday)d</span></div>
    <nav class="navbar">%(nav)s</nav>
  </header>
  %(body)s
  <footer class="ft">
    <p>표 자료 분석은 계산이 어려워서가 아니라 <b>읽는 순서를 몰라서</b> 틀립니다.
       각 문항의 &lsquo;발상&rsquo;을 먼저 보고, 막히면 그때 풀이를 여세요.</p>
    <p class="cr">문항은 2027학년도 6월·9월 평가원 모의평가의 출제 패턴을 참고해
       새로 만든 것입니다. 모든 수치는 분수로 검산했습니다.</p>
  </footer>
</div>
<script>
document.addEventListener('click', function (e) {
  var b = e.target.closest('.act'); if (!b) return;
  var card = b.closest('.p');
  var pane = card.querySelector('.pane[data-t="' + b.dataset.t + '"]');
  var on = pane.classList.toggle('on');
  b.classList.toggle('on', on);
});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    build()
