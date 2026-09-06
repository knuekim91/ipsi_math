# -*- coding: utf-8 -*-
"""
ipsi_math - 웹앱 생성기

units/*/problems/*.md 를 읽어 하나의 HTML 학습 앱(dist/webapp.html)을 만든다.
이 파일을 Artifact로 게시하면 나은이가 폰/태블릿에서 열어 쓸 수 있다.

문항이 추가될 때마다 다시 실행하고, 같은 파일 경로로 재게시하면 URL이 유지된다.

  python build/make_webapp.py
"""
import datetime as dt
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist", "webapp.html")

UNIT_LABEL = {
    "01-지수로그": "지수·로그", "02-삼각함수": "삼각함수", "03-수열": "수열",
    "04-극한연속": "극한·연속", "05-미분": "미분", "06-적분": "적분",
    "07-경우의수확률": "경우의 수·확률", "08-통계": "통계",
}


def parse(path):
    raw = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    meta, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end != -1:
            for line in raw[4:end].split("\n"):
                if ":" in line and not line.lstrip().startswith("#"):
                    k, v = line.split(":", 1)
                    v = v.strip().strip('"').strip("'")
                    meta[k.strip()] = v
            body = raw[end + 5:]
    sec, cur = {}, None
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip(); sec[cur] = []
        elif cur:
            sec[cur].append(line)
    for k in sec:
        sec[k] = "\n".join(sec[k]).strip()
    return meta, sec


def strip_html(h):
    """검색용 평문. 태그를 지우고 실체 참조를 되돌린다."""
    t = re.sub(r"<[^>]+>", " ", h or "")
    for a, b in (("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&"),
                 ("&lsquo;", "'"), ("&rsquo;", "'"), ("&middot;", "·")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def collect():
    out = []
    for unit in sorted(os.listdir(os.path.join(ROOT, "units"))):
        pdir = os.path.join(ROOT, "units", unit, "problems")
        if not os.path.isdir(pdir):
            continue
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            meta, sec = parse(os.path.join(pdir, fn))
            out.append({
                "id": meta.get("id", fn[:-3]),
                "unit": unit,
                "unitLabel": UNIT_LABEL.get(unit, unit),
                "topic": meta.get("topic", ""),
                "level": meta.get("level", ""),
                "diff": meta.get("difficulty", ""),
                "source": meta.get("source", ""),
                "origin": meta.get("origin") or
                          ("유사문항" if "자체 개발" in meta.get("source", "") else "기출"),
                "core": meta.get("core", ""),
                "answer": meta.get("answer", ""),
                "q": sec.get("문제", ""),
                "idea": sec.get("발상", ""),
                "sol": sec.get("풀이", ""),
                "alt": sec.get("다른 풀이", ""),
                "trap": sec.get("함정", ""),
                "know": sec.get("노하우", ""),
            })
            it = out[-1]
            it["qplain"] = strip_html(it["q"])
            it["search"] = " ".join([
                it["id"], it["topic"], it["source"], it["origin"], it["level"],
                it["core"], meta.get("tags", ""), it["qplain"],
                strip_html(it["idea"]), strip_html(it["know"]),
            ]).lower()
    return out


TEMPLATE = r"""<title>수능 수학 발상 트레이너</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Sans+KR:wght@300;400;500;600&display=swap">
<style>
:root{
  --paper:#EEF0F5; --card:#FFF; --ink:#151F38; --ink2:#4E5972; --ink3:#7A849A;
  --rule:#D2D8E4; --rule2:#E6EAF1; --indigo:#2E3F73;
  --mark:rgba(240,222,64,.55); --markline:#C9B32A;
  --ok:#2A6A58; --okbg:rgba(42,106,88,.10);
  --warn:#9A6B12; --warnbg:rgba(154,107,18,.11);
  --stop:#A33A29; --stopbg:rgba(163,58,41,.10);
  --new:#5B3FA0; --newbg:rgba(91,63,160,.13);
  --mine:#8A4A0E; --minebg:rgba(138,74,14,.13);
  --shadow:0 1px 2px rgba(21,31,56,.06);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0E121B; --card:#161C29; --ink:#E8EBF2; --ink2:#9BA5BA; --ink3:#7A849A;
  --rule:#2A3242; --rule2:#222937; --indigo:#A6B8EC;
  --mark:rgba(231,211,74,.22); --markline:#8E7F22;
  --ok:#7CC7AE; --okbg:rgba(124,199,174,.12);
  --warn:#DFB765; --warnbg:rgba(223,183,101,.12);
  --stop:#E39683; --stopbg:rgba(227,150,131,.12);
  --new:#C0AAF0; --newbg:rgba(192,170,240,.16);
  --mine:#E8B37A; --minebg:rgba(232,179,122,.16);
  --shadow:none;
}}
:root[data-theme="dark"]{
  --paper:#0E121B; --card:#161C29; --ink:#E8EBF2; --ink2:#9BA5BA; --ink3:#7A849A;
  --rule:#2A3242; --rule2:#222937; --indigo:#A6B8EC;
  --mark:rgba(231,211,74,.22); --markline:#8E7F22;
  --ok:#7CC7AE; --okbg:rgba(124,199,174,.12);
  --warn:#DFB765; --warnbg:rgba(223,183,101,.12);
  --stop:#E39683; --stopbg:rgba(227,150,131,.12);
  --new:#C0AAF0; --newbg:rgba(192,170,240,.16);
  --mine:#E8B37A; --minebg:rgba(232,179,122,.16);
  --shadow:none;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:'IBM Plex Sans KR',system-ui,'Malgun Gothic',sans-serif;
  font-size:15px;line-height:1.7;-webkit-font-smoothing:antialiased;
  padding-bottom:104px}
.wrap{max-width:720px;margin:0 auto;padding:0 16px}
/* 터치 기기: 탭 시 회색 깜빡임·글자 선택·더블탭 확대 방지 */
button,textarea{-webkit-tap-highlight-color:transparent;touch-action:manipulation}
button{-webkit-user-select:none;user-select:none}
/* 태블릿에서는 본문을 한 단계 키운다 */
@media (min-width:768px){
  body{font-size:16px}
  .wrap{max-width:768px;padding:0 24px}
}
h1,h2,h3{font-family:'Gowun Batang',Georgia,serif;font-weight:700;margin:0;text-wrap:balance}
.m,.stem i{font-family:Georgia,'Times New Roman','Gowun Batang',serif}
.eyebrow{font-size:10.5px;font-weight:600;letter-spacing:.16em;color:var(--ink3)}

/* ---- 헤더 ---- */
header{padding:26px 0 18px;border-bottom:1px solid var(--rule)}
header h1{font-size:26px;letter-spacing:-.01em}
.dday{display:flex;align-items:baseline;gap:10px;margin-top:12px;flex-wrap:wrap}
.ddnum{font-family:Georgia,serif;font-size:34px;font-weight:700;line-height:1;color:var(--indigo);font-variant-numeric:tabular-nums}
.ddtxt{font-size:12.5px;color:var(--ink2)}
.syncline{margin-top:10px;font-size:11.5px;color:var(--ink3);display:flex;align-items:center;gap:6px}
.dot{width:6px;height:6px;border-radius:50%;background:var(--ink3);flex:none}
.dot.on{background:var(--ok)}

/* ---- 진도 요약 ---- */
.summary{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--rule);
  border:1px solid var(--rule);margin:18px 0}
.summary div{background:var(--card);padding:12px 10px;text-align:center}
.summary .n{font-family:Georgia,serif;font-size:23px;font-weight:700;line-height:1.2;font-variant-numeric:tabular-nums}
.summary .l{font-size:11px;color:var(--ink3);margin-top:2px}
.summary .ok .n{color:var(--ok)} .summary .warn .n{color:var(--warn)} .summary .stop .n{color:var(--stop)}

/* ---- 검색 ---- */
.searchbox{position:relative;margin-top:16px}
.searchbox input{width:100%;font-family:inherit;font-size:16px;min-height:48px;
  padding:12px 44px 12px 14px;border:1px solid var(--rule);background:var(--card);
  color:var(--ink);border-radius:2px;-webkit-appearance:none;appearance:none}
.searchbox input::placeholder{color:var(--ink3)}
.searchbox input:focus{outline:2px solid var(--markline);outline-offset:-1px}
.searchbox input::-webkit-search-cancel-button{display:none}
.searchbox .clr{position:absolute;right:5px;top:50%;transform:translateY(-50%);
  width:38px;height:38px;border:0;background:none;color:var(--ink3);font-size:15px;
  cursor:pointer;display:none;font-family:inherit}
.searchbox.on .clr{display:block}
.psnip{display:block;font-size:11.5px;color:var(--ink2);margin-top:3px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.psnip b{background:linear-gradient(transparent 55%,var(--mark) 55%);font-weight:600}
.hitcount{font-size:12.5px;color:var(--ink2);margin-right:auto}
.hitcount b{color:var(--ink)}
.noresult{text-align:center;color:var(--ink3);font-size:14px;padding:28px 10px}
.noresult button{margin-top:10px;font-family:inherit;font-size:13.5px;min-height:44px;
  padding:0 16px;border:1px solid var(--rule);background:var(--card);color:var(--ink2);
  cursor:pointer;border-radius:2px}

/* ---- 필터 ---- */
.filters{display:flex;flex-wrap:wrap;gap:7px;padding:12px 0 0}
.filters.units{padding-top:7px}
.fchip{flex:none;font-size:13px;padding:0 13px;min-height:40px;border:1px solid var(--rule);
  background:var(--card);color:var(--ink2);cursor:pointer;white-space:nowrap;border-radius:2px;
  font-family:inherit;display:inline-flex;align-items:center}
.filters.units .fchip{font-size:12.5px;padding:0 11px;min-height:38px}
.fchip[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.fchip .c{opacity:.55;margin-left:5px;font-family:Georgia,serif}

/* ---- 문항 카드 ---- */
.list{margin-top:16px;display:flex;flex-direction:column;gap:9px}
.p{background:var(--card);border:1px solid var(--rule);box-shadow:var(--shadow)}
.p.s-ok{border-left:3px solid var(--ok)}
.p.s-mid{border-left:3px solid var(--warn)}
.p.s-no{border-left:3px solid var(--stop)}
.phead{display:flex;align-items:stretch}
.pmain{flex:1;min-width:0;text-align:left;background:none;border:0;padding:13px 15px;cursor:pointer;
  display:flex;align-items:center;gap:9px;font-family:inherit;color:inherit;font-size:15px}
.selbtn{flex:none;width:54px;background:none;border:0;border-left:1px solid var(--rule2);
  cursor:pointer;color:var(--ink3);font-family:inherit;font-size:15px;line-height:1;
  display:flex;align-items:center;justify-content:center}
.selbtn .box{width:22px;height:22px;border:1.5px solid var(--rule);border-radius:3px;
  display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700}
.selbtn[aria-pressed="true"] .box{background:var(--indigo);border-color:var(--indigo);color:#fff}
.p.sel{box-shadow:inset 3px 0 0 var(--indigo), var(--shadow)}
.listtools{display:flex;justify-content:flex-end;align-items:center;gap:12px;margin-top:12px}
.listtools button{font-size:12.5px;color:var(--ink2);background:none;border:0;cursor:pointer;
  font-family:inherit;padding:6px 2px;text-decoration:underline;text-underline-offset:3px}
.ptitle{flex:1;min-width:0}
.ptopic{font-weight:500;display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pmeta{font-size:11px;color:var(--ink3);display:block;margin-top:1px}
.badge{flex:none;font-size:10px;padding:2px 6px;border:1px solid var(--rule);color:var(--ink3);border-radius:2px}
.badge.hard{color:var(--stop);border-color:color-mix(in srgb,var(--stop) 45%,transparent)}
.badge.origin{font-weight:600;border-width:0;padding:3px 8px}
.badge.origin.o-new{color:var(--new);background:var(--newbg)}
.badge.origin.o-mine{color:var(--mine);background:var(--minebg)}
.fchip.o-new[aria-pressed="false"]{color:var(--new);border-color:color-mix(in srgb,var(--new) 40%,transparent)}
.fchip.o-new[aria-pressed="true"]{background:var(--new);border-color:var(--new);color:#fff}
.fchip.o-mine[aria-pressed="false"]{color:var(--mine);border-color:color-mix(in srgb,var(--mine) 40%,transparent)}
.fchip.o-mine[aria-pressed="true"]{background:var(--mine);border-color:var(--mine);color:#fff}
.arrow{flex:none;width:0;height:0;border-left:5px solid var(--ink3);
  border-top:4px solid transparent;border-bottom:4px solid transparent;transition:transform .15s}
.p[open] .arrow,.p.open .arrow{transform:rotate(90deg)}
.pbody{padding:0 15px 15px;border-top:1px solid var(--rule2);display:none}
.p.open .pbody{display:block}

.stem{font-size:15px;line-height:1.85;padding-top:13px}
.stem p{margin:0 0 7px}
.cond{display:block;margin:8px 0;padding:8px 11px;border:1px solid var(--rule)}
.choices{display:flex;flex-wrap:wrap;gap:5px 18px;margin-top:8px;font-family:Georgia,serif}

.reveal{margin-top:12px;display:flex;gap:7px;flex-wrap:wrap}
.rbtn{font-size:13.5px;padding:0 18px;min-height:44px;border:1px solid var(--rule);background:var(--card);
  color:var(--ink2);cursor:pointer;font-family:inherit;border-radius:2px;
  display:inline-flex;align-items:center}
.rbtn:hover{color:var(--ink);border-color:var(--ink3)}
.rbtn[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}

.panel{display:none;margin-top:12px;font-size:14.5px;line-height:1.8;color:var(--ink2)}
.panel.on{display:block}
.panel p{margin:0 0 8px} .panel p:last-child{margin-bottom:0}
.panel .step{color:var(--ink);font-weight:500}
.panel ol{margin:0 0 8px;padding-left:19px}
.lab{display:block;font-size:10px;letter-spacing:.15em;font-weight:600;color:var(--indigo);margin-bottom:4px}
.pidea{padding-left:11px;border-left:2px solid var(--indigo)}
.palt{padding:11px 13px;border:1px dashed var(--ink3);margin:10px 0}
.palt .lab{color:var(--ink3)}
.ptrap{padding:10px 12px;background:var(--stopbg);border-left:2px solid var(--stop);color:var(--ink2)}
.ptrap .lab{color:var(--stop)}
.pknow{padding:11px 13px;border:1px solid var(--rule)}
.pknow .lab{color:var(--ink3)}
.pknow b{background:linear-gradient(transparent 58%,var(--mark) 58%)}
.pans{margin-top:10px;font-size:13px;color:var(--ink3)}
.pans b{font-family:Georgia,serif;font-size:16px;color:var(--indigo)}

/* ---- 상태 버튼 ---- */
.marks{margin-top:15px;padding-top:13px;border-top:1px solid var(--rule2)}
.marks .lab{color:var(--ink3);margin-bottom:7px}
.mrow{display:flex;gap:7px}
.mbtn{flex:1;font-size:14px;padding:4px;min-height:48px;border:1px solid var(--rule);background:var(--card);
  color:var(--ink2);cursor:pointer;font-family:inherit;border-radius:2px}
.mbtn[aria-pressed="true"]{font-weight:600}
.mbtn.ok[aria-pressed="true"]{background:var(--okbg);border-color:var(--ok);color:var(--ok)}
.mbtn.mid[aria-pressed="true"]{background:var(--warnbg);border-color:var(--warn);color:var(--warn)}
.mbtn.no[aria-pressed="true"]{background:var(--stopbg);border-color:var(--stop);color:var(--stop)}
.note{margin-top:9px;width:100%;font-family:inherit;font-size:16px;padding:11px 12px;
  border:1px solid var(--rule);background:var(--paper);color:var(--ink);resize:vertical;min-height:58px;
  line-height:1.6}
.note:focus{outline:2px solid var(--markline);outline-offset:-1px}
.notehint{font-size:11.5px;color:var(--ink3);margin-top:6px;line-height:1.6}
.askbtn{width:100%;margin-top:9px;font-family:inherit;font-size:14px;min-height:48px;
  border:1px solid var(--indigo);background:var(--indigo);color:#fff;cursor:pointer;
  border-radius:2px;font-weight:500}
.askbtn:disabled{background:var(--card);color:var(--ink3);border-color:var(--rule);cursor:default;
  font-weight:400}
.askbox{font-family:Consolas,monospace;font-size:12.5px;line-height:1.7;color:var(--ink);
  background:var(--paper);border:1px solid var(--rule);padding:12px;margin:2px 0 10px;
  max-height:300px;overflow-y:auto;white-space:pre-wrap;word-break:break-word;
  user-select:text;-webkit-user-select:text}

/* ---- 하단 바 ---- */
.bar{position:fixed;left:0;right:0;bottom:0;background:var(--card);border-top:1px solid var(--rule);
  padding:10px 16px calc(10px + env(safe-area-inset-bottom));z-index:30}
.barin{max-width:720px;margin:0 auto;display:flex;align-items:center;gap:12px;justify-content:space-between}
.barin span{font-size:12px;color:var(--ink2)}
.barin b{color:var(--stop)}
.barbtn{font-size:13.5px;padding:0 18px;min-height:44px;border:1px solid var(--ink);background:var(--ink);
  color:var(--paper);cursor:pointer;font-family:inherit;border-radius:2px;flex:none}
.barlink{flex:1;min-width:0;text-align:left;font-size:13px;color:var(--ink2);
  background:none;border:0;padding:0 4px 0 0;min-height:44px;cursor:pointer;font-family:inherit;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:400px){ .barlink{font-size:12.5px} }
.barlink b{color:var(--ink);font-weight:600}
.barlink .go{color:var(--indigo);font-weight:600;margin-left:6px;white-space:nowrap}
.barlink[disabled]{cursor:default;color:var(--ink3)}
.barlink[disabled] .go{display:none}
.p.flash{outline:3px solid var(--markline);outline-offset:-1px}
.barsel{display:none;align-items:center;gap:10px;width:100%}
.barsel.on{display:flex}
.barsel .cnt{flex:1;font-size:13px;color:var(--ink)}
.barsel .cnt b{color:var(--indigo);font-weight:700;font-size:15px}
.ghost{font-size:13px;min-height:44px;padding:0 14px;border:1px solid var(--rule);
  background:none;color:var(--ink2);cursor:pointer;font-family:inherit;border-radius:2px;flex:none}
.toast{position:fixed;left:50%;transform:translateX(-50%);bottom:96px;z-index:60;
  background:var(--ink);color:var(--paper);font-size:13px;padding:10px 16px;border-radius:3px;
  opacity:0;pointer-events:none;transition:opacity .2s}
.toast.on{opacity:1}
.sheet .opt{width:100%;text-align:left;font-size:14.5px;min-height:56px;padding:12px 14px;
  margin-bottom:9px;border:1px solid var(--rule);background:var(--card);color:var(--ink);
  cursor:pointer;font-family:inherit}
.sheet .opt small{display:block;color:var(--ink3);font-size:12px;margin-top:2px}
.sheet .opt[disabled]{opacity:.45;cursor:default}
.sheet .hint{font-size:12px;color:var(--ink3);line-height:1.6;margin:4px 0 2px}
.sheet .idlist{font-family:Consolas,monospace;font-size:13px;line-height:1.9;color:var(--ink);
  background:var(--paper);border:1px solid var(--rule);padding:10px 12px;margin:2px 0 8px;
  max-height:180px;overflow-y:auto;user-select:text;-webkit-user-select:text;white-space:pre-wrap}
.barbtn[disabled]{opacity:.4;cursor:default}

/* ---- 모달 ---- */
.modal{position:fixed;inset:0;background:rgba(10,14,22,.55);z-index:40;display:none;
  align-items:flex-end;justify-content:center}
.modal.on{display:flex}
.sheet{background:var(--card);width:100%;max-width:720px;max-height:82vh;max-height:82dvh;overflow-y:auto;
  -webkit-overflow-scrolling:touch;border-top:2px solid var(--ink);
  padding:20px 18px calc(28px + env(safe-area-inset-bottom))}
.sheet h2{font-size:19px;margin-bottom:4px}
.sheet .sub{font-size:12.5px;color:var(--ink3);margin-bottom:16px}
.qitem{border-top:1px solid var(--rule2);padding:11px 0}
.qitem .t{font-weight:500;font-size:14px}
.qitem .m2{font-size:12px;color:var(--ink3);margin-top:2px}
.qitem .nt{font-size:13px;color:var(--ink2);margin-top:6px;padding:8px 10px;background:var(--paper)}
.close{margin-top:18px;width:100%;font-size:14px;min-height:48px;border:1px solid var(--rule);
  background:var(--card);color:var(--ink2);cursor:pointer;font-family:inherit}
.empty{color:var(--ink3);font-size:13.5px;padding:18px 0}

/* ---- 태블릿(아이패드) 가독성: 반드시 스타일시트 끝에 두어야 앞 규칙을 이긴다 ---- */
@media (min-width:768px){
  .stem{font-size:17px;line-height:1.9}
  .panel{font-size:16px;line-height:1.85}
  .phead{font-size:16px;padding:15px 17px}
  .pmeta{font-size:12px}
  .badge{font-size:11px}
  .choices{gap:7px 26px;font-size:17px}
  .cond{padding:10px 14px}
  .eyebrow{font-size:11.5px}
  header h1{font-size:30px}
  .summary .n{font-size:26px}
  .summary .l{font-size:12px}
  .syncline{font-size:12.5px}
  .barin span{font-size:13px}
  .notehint{font-size:12px}
}
:focus-visible{outline:2px solid var(--markline);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}

</style>

<div class="wrap">
  <header>
    <div class="eyebrow">수학Ⅰ · 수학Ⅱ · 확률과 통계</div>
    <h1>발상 트레이너</h1>
    <div class="dday">
      <span class="ddnum" id="dd">—</span>
      <span class="ddtxt">2027학년도 수능까지<br>2026년 11월 19일 (목)</span>
    </div>
    <div class="syncline"><span class="dot" id="syncdot"></span><span id="synctxt">불러오는 중…</span></div>
  </header>

  <div class="summary">
    <div class="ok"><div class="n" id="n-ok">0</div><div class="l">알겠음</div></div>
    <div class="warn"><div class="n" id="n-mid">0</div><div class="l">헷갈림</div></div>
    <div class="stop"><div class="n" id="n-no">0</div><div class="l">모르겠음</div></div>
  </div>

  <div class="searchbox" id="searchbox">
    <input id="q" type="search" inputmode="search" autocomplete="off"
           placeholder="주제 · 문제 내용 · 출처로 찾기 (예: 로그, 중복조합, 모평)"
           aria-label="문항 검색">
    <button class="clr" id="qclear" aria-label="검색어 지우기">✕</button>
  </div>
  <div class="filters" id="filters-origin"></div>
  <div class="filters units" id="filters-unit"></div>
  <div class="listtools"><span class="hitcount" id="hitcount"></span><button id="selall">보이는 문항 모두 선택</button></div>
  <div class="list" id="list"></div>
</div>

<div class="bar">
  <div class="barin" id="barnormal">
    <button class="barlink" id="nextbtn">—</button>
    <button class="barbtn" id="reviewbtn">다시 볼 문항</button>
  </div>
  <div class="barsel" id="barsel">
    <span class="cnt"><b id="selcount">0</b>개 선택</span>
    <button class="ghost" id="clearsel">해제</button>
    <button class="barbtn" id="printbtn">내보내기</button>
  </div>
</div>

<div class="modal" id="askmodal">
  <div class="sheet">
    <h2>이대로 전달하세요</h2>
    <div class="sub">아래 내용을 복사해 Claude 대화창에 붙여넣으면, 이 메모에 맞춘 문항을 만들어 드립니다.</div>
    <div class="askbox" id="askbox"></div>
    <button class="opt" id="askcopy">복사하기<small>복사가 안 되면 위 상자를 길게 눌러 직접 복사하거나 화면을 캡처해 보내세요</small></button>
    <button class="close" id="askclose">닫기</button>
  </div>
</div>

<div class="modal" id="pmodal">
  <div class="sheet">
    <h2>선택한 문항 내보내기</h2>
    <div class="sub" id="psub">—</div>
    <button class="opt" id="opt3">문항 번호 복사<small>클립보드에 담깁니다</small></button>
    <div class="idlist" id="idlist"></div>
    <div class="hint">이 번호를 전달하면 인쇄용 <b>문제지 · 해설지 PDF</b>를 만들어 드립니다.<br>
      복사가 안 되면 위 목록을 화면 캡처해서 보내도 됩니다.</div>
    <button class="close" id="pclose">닫기</button>
  </div>
</div>

<div class="toast" id="toast"></div>


<div class="modal" id="modal">
  <div class="sheet">
    <h2>다시 볼 문항</h2>
    <div class="sub">모르겠음·헷갈림으로 표시한 문항입니다. 이 목록이 다음 인쇄 세트가 됩니다.</div>
    <div id="reviewlist"></div>
    <button class="opt" id="askall">이 목록 전체를 질문으로 모으기<small>메모까지 함께 정리됩니다</small></button>
    <button class="close" id="closebtn">닫기</button>
  </div>
</div>

<script>
const PROBLEMS = __DATA__;
const EXAM = new Date(2026, 10, 19);

/* ---------- D-day ---------- */
(function(){
  const today = new Date(); today.setHours(0,0,0,0);
  const d = Math.round((EXAM - today) / 86400000);
  document.getElementById('dd').textContent = d >= 0 ? 'D-' + d : 'D+' + (-d);
})();

/* ---------- 저장소: db 있으면 공유, 없으면 이 기기에만 ---------- */
const LS = 'ipsi_math_progress_v1';
const LS_SEL = 'ipsi_math_selected_v1';
let selected = new Set();
function loadSel(){
  try { selected = new Set(JSON.parse(localStorage.getItem(LS_SEL) || '[]')); }
  catch (e) { selected = new Set(); }
}
function saveSel(){
  try { localStorage.setItem(LS_SEL, JSON.stringify([...selected])); } catch (e) {}
}
let state = {};        // id -> {status, note, at}
let db = null;

function loadLocal(){
  try { state = JSON.parse(localStorage.getItem(LS) || '{}'); }
  catch(e){ state = {}; }
}
function saveLocal(){
  try { localStorage.setItem(LS, JSON.stringify(state)); } catch(e){}
}
function setSync(on, text){
  document.getElementById('syncdot').classList.toggle('on', !!on);
  document.getElementById('synctxt').textContent = text;
}

loadLocal(); loadSel();
setSync(false, '이 기기에만 저장됩니다');

(async function(){
  let cap = null;
  try { cap = await claude.use('db'); } catch(e){ cap = null; }
  if (!cap) return;
  db = cap;
  try {
    db.collection('progress').onSnapshot(function(snap){
      snap.docs.forEach(function(doc){
        const v = doc.data() || {};
        state[doc.id] = { status: v.status || '', note: v.note || '', at: v.at || '' };
      });
      saveLocal(); render();
      setSync(true, '진도가 함께 보는 사람과 공유됩니다');
    }, function(){ setSync(false, '이 기기에만 저장됩니다'); });
  } catch(e){ db = null; }
})();

function put(id, patch, opts){
  const cur = state[id] || { status:'', note:'' };
  const next = Object.assign({}, cur, patch, { at: new Date().toISOString() });
  state[id] = next;
  saveLocal();
  // 메모 저장은 silent — 목록을 다시 그리면 입력창이 파괴되어 포커스가 날아간다
  if (!(opts && opts.silent)) render();
  if (db) {
    db.doc('progress/' + id).set({
      status: next.status || '', note: next.note || '', at: next.at
    }).catch(function(){ setSync(false, '이 기기에만 저장됩니다'); });
  }
}

/* ---------- 렌더 ---------- */
let filter = 'all';
let query = '';
const pendingFlush = new Set();   // 아직 저장되지 않았을 수 있는 메모 입력창들
function flushAll(){ pendingFlush.forEach(function(f){ try { f(); } catch (e) {} }); }
document.addEventListener('visibilitychange', function(){ if (document.hidden) flushAll(); });
window.addEventListener('pagehide', flushAll);
const opened = new Set();
const shown = {};   // id -> {idea:bool, sol:bool}

const UNITS = [];
PROBLEMS.forEach(function(p){
  if (!UNITS.some(function(u){ return u.key === p.unit; }))
    UNITS.push({ key: p.unit, label: p.unitLabel });
});

function originClass(o){ return o === '유사문항' ? 'o-new' : o === '기출' ? '' : 'o-mine'; }
function inChip(p){
  if (filter === 'all') return true;
  if (filter.indexOf('origin:') === 0) return p.origin === filter.slice(7);
  return p.unit === filter;
}
function inQuery(p){
  return query === '' || (p.search || '').indexOf(query) >= 0;
}
// 목록·바로가기·모두선택이 모두 '지금 보이는 것'을 기준으로 움직인다
function inFilter(p){ return inChip(p) && inQuery(p); }

// 검색어가 문제 본문에서 걸렸을 때 그 앞뒤를 조금 보여준다
function snippet(p){
  if (query === '') return '';
  if ((p.topic || '').toLowerCase().indexOf(query) >= 0) return '';
  const plain = p.qplain || '';
  const i = plain.toLowerCase().indexOf(query);
  if (i < 0) return '';
  const from = Math.max(0, i - 24);
  const head = (from > 0 ? '… ' : '') + plain.slice(from, i);
  const hit = plain.slice(i, i + query.length);
  const tail = plain.slice(i + query.length, i + query.length + 40);
  return '<span class="psnip">' + esc(head) + '<b>' + esc(hit) + '</b>' + esc(tail) + '…</span>';
}
function statusClass(s){
  return s === 'ok' ? 's-ok' : s === 'mid' ? 's-mid' : s === 'no' ? 's-no' : '';
}
function esc(s){
  return String(s == null ? '' : s)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;');
}

const ORIGIN_ORDER = ['유사문항', '오답노트'];

function renderFilters(){
  // 1줄: 전체 + 출처(유사문항·오답노트)
  const top = ['<button class="fchip" data-f="all" aria-pressed="' + (filter==='all') +
    '">전체<span class="c">' + PROBLEMS.length + '</span></button>'];
  const origins = ORIGIN_ORDER.filter(function(o){
    return PROBLEMS.some(function(p){ return p.origin === o; });
  });
  PROBLEMS.forEach(function(p){          // 앞으로 새 출처가 생겨도 빠지지 않게
    if (p.origin !== '기출' && origins.indexOf(p.origin) < 0) origins.push(p.origin);
  });
  origins.forEach(function(o){
    const n = PROBLEMS.filter(function(p){ return p.origin === o; }).length;
    const key = 'origin:' + o;
    top.push('<button class="fchip ' + originClass(o) + '" data-f="' + esc(key) +
      '" aria-pressed="' + (filter === key) + '">' + esc(o) + '<span class="c">' + n + '</span></button>');
  });

  // 2줄: 단원
  const units = UNITS.map(function(u){
    const n = PROBLEMS.filter(function(p){ return p.unit === u.key; }).length;
    return '<button class="fchip" data-f="' + esc(u.key) + '" aria-pressed="' +
      (filter===u.key) + '">' + esc(u.label) + '<span class="c">' + n + '</span></button>';
  });

  document.getElementById('filters-origin').innerHTML = top.join('');
  document.getElementById('filters-unit').innerHTML = units.join('');
  document.querySelectorAll('.filters .fchip').forEach(function(b){
    b.onclick = function(){ filter = b.dataset.f; lastJumpId = null; render(); };
  });
}

function renderList(){
  const items = PROBLEMS.filter(inFilter);
  if (!items.length) {
    const wider = query !== '' && filter !== 'all' &&
                  PROBLEMS.filter(inQuery).length > 0;
    document.getElementById('list').innerHTML =
      '<div class="noresult">찾는 문항이 없습니다.' +
      (wider ? '<br><button id="widen">전체에서 다시 찾기 (' +
               PROBLEMS.filter(inQuery).length + ')</button>' : '') + '</div>';
    if (wider) document.getElementById('widen').onclick = function(){
      filter = 'all'; lastJumpId = null; render();
    };
    return;
  }
  document.getElementById('list').innerHTML = items.map(function(p){
    const st = (state[p.id] || {}).status || '';
    const note = (state[p.id] || {}).note || '';
    const isOpen = opened.has(p.id);
    const isSel = selected.has(p.id);
    const sh = shown[p.id] || {};
    const hard = /상/.test(p.diff) && p.diff !== '중상';
    return '' +
    '<article class="p ' + statusClass(st) + (isOpen ? ' open' : '') + (isSel ? ' sel' : '') +
      '" data-id="' + esc(p.id) + '">' +
      '<div class="phead">' +
        '<button class="pmain" aria-expanded="' + isOpen + '">' +
          '<span class="arrow"></span>' +
          '<span class="ptitle"><span class="ptopic">' + esc(p.topic) + '</span>' +
            '<span class="pmeta">' + esc(p.unitLabel) + ' · ' + esc(p.source) + '</span>' +
            snippet(p) + '</span>' +
          (p.origin !== '기출'
            ? '<span class="badge origin ' + originClass(p.origin) + '">' + esc(p.origin) + '</span>' : '') +
          '<span class="badge' + (hard ? ' hard' : '') + '">' + esc(p.level) + '</span>' +
        '</button>' +
        '<button class="selbtn" aria-pressed="' + isSel + '" aria-label="인쇄할 문항으로 선택">' +
          '<span class="box">' + (isSel ? '✓' : '') + '</span></button>' +
      '</div>' +
      '<div class="pbody">' +
        '<div class="stem">' + p.q + '</div>' +
        '<div class="reveal">' +
          '<button class="rbtn" data-r="idea" aria-pressed="' + !!sh.idea + '">발상</button>' +
          '<button class="rbtn" data-r="sol" aria-pressed="' + !!sh.sol + '">풀이와 정답</button>' +
        '</div>' +
        '<div class="panel pidea' + (sh.idea ? ' on' : '') + '" data-panel="idea">' +
          '<span class="lab">발상</span>' + p.idea + '</div>' +
        '<div class="panel' + (sh.sol ? ' on' : '') + '" data-panel="sol">' +
          '<span class="lab">풀이</span>' + p.sol +
          (p.alt ? '<div class="palt"><span class="lab">다른 풀이</span>' + p.alt + '</div>' : '') +
          (p.trap ? '<div class="ptrap"><span class="lab">함정</span>' + p.trap + '</div>' : '') +
          '<div class="pknow"><span class="lab">노하우</span>' + p.know + '</div>' +
          '<div class="pans">정답 <b>' + esc(p.answer) + '</b></div>' +
        '</div>' +
        '<div class="marks">' +
          '<span class="lab">풀고 나서 표시하기</span>' +
          '<div class="mrow">' +
            '<button class="mbtn ok" data-m="ok" aria-pressed="' + (st==='ok') + '">알겠음</button>' +
            '<button class="mbtn mid" data-m="mid" aria-pressed="' + (st==='mid') + '">헷갈림</button>' +
            '<button class="mbtn no" data-m="no" aria-pressed="' + (st==='no') + '">모르겠음</button>' +
          '</div>' +
          '<textarea class="note" placeholder="어디까지 알겠고 어디부터 막히는지 적어 주세요. 적은 그대로 전달됩니다.">' +
            esc(note) + '</textarea>' +
          '<button class="askbtn" data-ask="' + esc(p.id) + '">이 내용으로 문항 만들어 달라고 하기</button>' +
          '<div class="notehint">누르면 <b>문제와 메모가 한 덩어리로 정리</b>됩니다. 그대로 복사해 Claude에게 붙여넣으세요.</div>' +
        '</div>' +
      '</div>' +
    '</article>';
  }).join('');
  pendingFlush.clear();
  bind();
}

function bind(){
  document.querySelectorAll('.p').forEach(function(card){
    const id = card.dataset.id;
    card.querySelector('.pmain').onclick = function(){
      if (opened.has(id)) opened.delete(id); else opened.add(id);
      render();
    };
    card.querySelector('.selbtn').onclick = function(){
      if (selected.has(id)) selected.delete(id); else selected.add(id);
      saveSel(); render();
    };
    card.querySelectorAll('.rbtn').forEach(function(b){
      b.onclick = function(){
        const k = b.dataset.r;
        shown[id] = shown[id] || {};
        shown[id][k] = !shown[id][k];
        render();
      };
    });
    card.querySelectorAll('.mbtn').forEach(function(b){
      b.onclick = function(){
        const cur = (state[id] || {}).status || '';
        put(id, { status: cur === b.dataset.m ? '' : b.dataset.m });
      };
    });
    const ab = card.querySelector('.askbtn');
    if (ab) {
      const refresh = function(){
        const v = state[id] || {};
        const ready = ((v.note || '').trim() !== '') || v.status === 'mid' || v.status === 'no';
        ab.disabled = !ready;
        ab.textContent = ready ? '이 내용으로 문항 만들어 달라고 하기'
                               : '메모를 적으면 여기서 전달할 수 있어요';
      };
      refresh();
      ab.onclick = function(){
        const p = PROBLEMS.filter(function(x){ return x.id === id; })[0];
        const t = card.querySelector('.note');
        if (t && ((state[id] || {}).note || '') !== t.value) put(id, { note: t.value }, { silent: true });
        openAsk(askText(p));
      };
    }
    const ta = card.querySelector('.note');
    if (ta) {
      let t = null;
      const flush = function(){
        clearTimeout(t); t = null;
        if (((state[id] || {}).note || '') !== ta.value) put(id, { note: ta.value }, { silent: true });
      };
      ta.oninput = function(){
        clearTimeout(t); t = setTimeout(flush, 400);
        if (ab) {
          const ready = ta.value.trim() !== '';
          ab.disabled = !ready && !((state[id] || {}).status === 'mid' || (state[id] || {}).status === 'no');
          ab.textContent = ab.disabled ? '메모를 적으면 여기서 전달할 수 있어요'
                                       : '이 내용으로 문항 만들어 달라고 하기';
        }
      };
      ta.onblur = flush;              // 입력창을 벗어날 때 확실히 저장
      pendingFlush.add(flush);        // 앱 전환·화면 닫힘 대비
    }
  });
}

function renderSummary(){
  let ok = 0, mid = 0, no = 0;
  PROBLEMS.forEach(function(p){
    const s = (state[p.id] || {}).status;
    if (s === 'ok') ok++; else if (s === 'mid') mid++; else if (s === 'no') no++;
  });
  document.getElementById('n-ok').textContent = ok;
  document.getElementById('n-mid').textContent = mid;
  document.getElementById('n-no').textContent = no;
  const left = PROBLEMS.length - ok - mid - no;
  const nb = document.getElementById('nextbtn');
  nb.innerHTML = left
    ? '아직 안 푼 문항 <b>' + left + '</b>개<span class="go">바로가기 →</span>'
    : '전부 표시했어요';
  nb.disabled = left === 0;
  const rb = document.getElementById('reviewbtn');
  rb.textContent = '다시 볼 문항 ' + (mid + no);
  rb.disabled = (mid + no) === 0;

  // 선택이 있으면 하단 바를 선택 모드로 바꾼다
  const has = selected.size > 0;
  document.getElementById('barnormal').style.display = has ? 'none' : 'flex';
  document.getElementById('barsel').classList.toggle('on', has);
  document.getElementById('selcount').textContent = selected.size;

  const vis = PROBLEMS.filter(inFilter);
  const allSel = vis.length > 0 && vis.every(function(p){ return selected.has(p.id); });
  document.getElementById('selall').textContent =
    allSel ? '선택 모두 해제' : '보이는 문항 모두 선택 (' + vis.length + ')';
  document.getElementById('selall').style.display = vis.length ? '' : 'none';
  document.getElementById('hitcount').innerHTML =
    query === '' ? '' : '검색 결과 <b>' + vis.length + '</b>개';
}

// 어떤 이유로든 다시 그릴 때 입력 중이던 메모의 포커스와 커서 위치를 복원한다
function render(){
  const ae = document.activeElement;
  let keep = null;
  if (ae && ae.classList && ae.classList.contains('note')) {
    const card = ae.closest('.p');
    if (card) keep = { id: card.dataset.id, val: ae.value,
                       s: ae.selectionStart, e: ae.selectionEnd };
  }
  renderFilters(); renderList(); renderSummary();
  if (keep) {
    const ta = document.querySelector('.p[data-id="' + keep.id + '"] .note');
    if (ta) {
      if (ta.value !== keep.val) ta.value = keep.val;
      ta.focus();
      try { ta.setSelectionRange(keep.s, keep.e); } catch (err) {}
    }
  }
}
render();

/* ---------- 검색 ---------- */
(function(){
  const box = document.getElementById('searchbox');
  const input = document.getElementById('q');
  const apply = function(){
    query = input.value.trim().toLowerCase();
    box.classList.toggle('on', input.value !== '');
    lastJumpId = null;
    render();                       // 검색창은 목록 밖이라 포커스가 유지된다
  };
  input.addEventListener('input', apply);
  input.addEventListener('keydown', function(e){
    if (e.key === 'Escape') { input.value = ''; apply(); input.blur(); }
  });
  document.getElementById('qclear').onclick = function(){
    input.value = ''; apply(); input.focus();
  };
})();

/* ---------- 선택 · 내보내기 ---------- */
document.getElementById('selall').onclick = function(){
  const vis = PROBLEMS.filter(inFilter);
  const allSel = vis.length > 0 && vis.every(function(p){ return selected.has(p.id); });
  vis.forEach(function(p){ if (allSel) selected.delete(p.id); else selected.add(p.id); });
  saveSel(); render();
};
document.getElementById('clearsel').onclick = function(){
  selected.clear(); saveSel(); render();
};

function toast(msg){
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('on');
  setTimeout(function(){ t.classList.remove('on'); }, 1800);
}
function selectedProblems(){
  return PROBLEMS.filter(function(p){ return selected.has(p.id); });
}

document.getElementById('printbtn').onclick = function(){
  const list = selectedProblems();
  document.getElementById('psub').textContent = list.length + '개 문항';
  document.getElementById('idlist').textContent =
    list.map(function(p){ return p.id; }).join(String.fromCharCode(10));
  document.getElementById('pmodal').classList.add('on');
};
document.getElementById('pclose').onclick = function(){
  document.getElementById('pmodal').classList.remove('on');
};
document.getElementById('pmodal').onclick = function(e){
  if (e.target === this) this.classList.remove('on');
};

const NL = String.fromCharCode(10);

function copyText(txt, okMsg){
  const done = function(){ toast(okMsg); };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(done, function(){ fallbackCopy(txt, done); });
  } else { fallbackCopy(txt, done); }
}
function fallbackCopy(txt, done){
  const ta = document.createElement('textarea');
  ta.value = txt; ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta); ta.select();
  try { document.execCommand('copy'); done(); }
  catch (e) { toast('복사가 안 돼요. 화면의 내용을 길게 눌러 복사하세요'); }
  document.body.removeChild(ta);
}

document.getElementById('opt3').onclick = function(){
  const txt = selectedProblems().map(function(p){ return p.id; }).join(NL);
  document.getElementById('pmodal').classList.remove('on');
  copyText(txt, '문항 번호 ' + selected.size + '개를 복사했어요');
};

/* ---------- 질문 만들기 ---------- */
const STATUS_LABEL = { ok: '알겠음', mid: '헷갈림', no: '모르겠음' };

function askText(p){
  const v = state[p.id] || {};
  const L = [];
  L.push('[ipsi_math 질문]');
  L.push('문항: ' + p.id + ' · ' + p.topic);
  L.push('단원: ' + p.unitLabel + ' / 출처: ' + p.source + ' / 배점: ' + p.level);
  if (v.status) L.push('나은이 표시: ' + (STATUS_LABEL[v.status] || v.status));
  L.push('');
  L.push('[문제]');
  L.push(p.qplain || '');
  L.push('');
  L.push('[나은이가 적은 것]');
  L.push((v.note || '').trim() || '(메모 없음)');
  L.push('');
  L.push('[요청] 위 메모에 맞춰 이 문항을 다룰 수 있게 해 주세요.');
  L.push('막힌 지점부터 다시 세울 도입 사다리와 같은 수준의 유사문항을 만들고,');
  L.push('저장소에 넣은 뒤 인쇄용 PDF까지 만들어 주세요.');
  return L.join(NL);
}

function openAsk(txt){
  document.getElementById('askbox').textContent = txt;
  document.getElementById('askmodal').classList.add('on');
}
document.getElementById('askcopy').onclick = function(){
  copyText(document.getElementById('askbox').textContent, '복사했어요. Claude에게 붙여넣으세요');
  document.getElementById('askmodal').classList.remove('on');
};
document.getElementById('askclose').onclick = function(){
  document.getElementById('askmodal').classList.remove('on');
};
document.getElementById('askmodal').onclick = function(e){
  if (e.target === this) this.classList.remove('on');
};

/* ---------- 안 푼 문항으로 이동 ---------- */
function unsolvedIn(list){
  return list.filter(function(p){ return !((state[p.id] || {}).status); });
}
let lastJumpId = null;   // 마지막으로 이동한 문항 (스크롤 위치보다 안정적)

document.getElementById('nextbtn').onclick = function(){
  let pool = unsolvedIn(PROBLEMS.filter(inFilter));
  if (!pool.length && filter !== 'all') {   // 지금 단원에 없으면 전체로 넓힌다
    filter = 'all'; lastJumpId = null; render();
    pool = unsolvedIn(PROBLEMS);
  }
  if (!pool.length) return;

  let start = 0;
  if (lastJumpId) {
    const i = pool.findIndex(function(p){ return p.id === lastJumpId; });
    if (i >= 0) {
      start = (i + 1) % pool.length;               // 바로 다음 안 푼 문항으로
    } else {
      // 방금 표시해서 목록에서 빠진 경우 -> 원래 있던 자리 다음부터
      const gone = PROBLEMS.findIndex(function(p){ return p.id === lastJumpId; });
      const j = pool.findIndex(function(p){ return PROBLEMS.indexOf(p) > gone; });
      start = j >= 0 ? j : 0;
    }
  }
  const target = pool[start];
  lastJumpId = target.id;

  opened.add(target.id);
  render();
  const el = document.querySelector('.p[data-id="' + target.id + '"]');
  if (!el) return;
  const smooth = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 12,
                    behavior: smooth ? 'smooth' : 'auto' });
  el.classList.add('flash');
  setTimeout(function(){ el.classList.remove('flash'); }, 1300);
};

/* ---------- 복습 목록 ---------- */
document.getElementById('reviewbtn').onclick = function(){
  const items = PROBLEMS.filter(function(p){
    const s = (state[p.id] || {}).status;
    return s === 'mid' || s === 'no';
  });
  document.getElementById('reviewlist').innerHTML = items.length ? items.map(function(p){
    const v = state[p.id] || {};
    return '<div class="qitem"><div class="t">' + esc(p.topic) + '</div>' +
      '<div class="m2">' + esc(p.unitLabel) + ' · ' + esc(p.id) + ' · ' +
      (v.status === 'no' ? '모르겠음' : '헷갈림') + '</div>' +
      (v.note ? '<div class="nt">' + esc(v.note) + '</div>' : '') + '</div>';
  }).join('') : '<div class="empty">아직 표시한 문항이 없습니다.</div>';
  document.getElementById('modal').classList.add('on');
};
document.getElementById('askall').onclick = function(){
  const items = PROBLEMS.filter(function(p){
    const st = (state[p.id] || {}).status;
    return st === 'mid' || st === 'no';
  });
  if (!items.length) return;
  const head = ['[ipsi_math 질문 · 다시 볼 문항 ' + items.length + '개]', ''];
  const body = items.map(function(p){
    const v = state[p.id] || {};
    return '─ ' + p.id + ' · ' + p.topic + ' (' + (STATUS_LABEL[v.status] || '') + ')' + NL +
           '  ' + (p.qplain || '').slice(0, 160) + '…' + NL +
           '  메모: ' + ((v.note || '').trim() || '(없음)');
  });
  const tail = ['', '[요청] 위 문항들의 공통된 약점을 짚고, 막힌 지점부터 세울 사다리와',
                '같은 수준의 유사문항을 만들어 저장소에 넣고 인쇄용 PDF까지 만들어 주세요.'];
  document.getElementById('modal').classList.remove('on');
  openAsk(head.concat(body).concat(tail).join(NL));
};
document.getElementById('closebtn').onclick = function(){
  document.getElementById('modal').classList.remove('on');
};
document.getElementById('modal').onclick = function(e){
  if (e.target === this) this.classList.remove('on');
};
</script>
"""


def main():
    probs = collect()
    data = json.dumps(probs, ensure_ascii=False).replace("</script>", "<\\/script>")
    html = TEMPLATE.replace("__DATA__", data)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"생성: {OUT}")
    print(f"문항 {len(probs)}개, {len(html):,} bytes")
    print("→ 이 파일을 같은 경로로 재게시하면 URL이 유지됩니다.")


if __name__ == "__main__":
    main()
