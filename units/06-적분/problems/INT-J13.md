---
id: INT-J13
unit: 06-적분
topic: 넓이함수의 미분
level: 4점
difficulty: 상
source: 2027-06모평 13번
exam: 2027-06모평
origin: 기출
core: "S′(t)가 곧 두 곡선의 세로 간격 f(t)−g(t)이다"
tags: [넓이,미적분기본정리,보기]
status: seed
added: 2026-09-06
answer: ⑤
---

## 문제

<p>두 함수 <span class="m">f(x), g(x)</span>가 모든 실수 <span class="m">x</span>에 대하여 <span class="m">f(x) &gt; g(x)</span>이고 <span class="m">f(1) = g(1) + 1</span>이다. <span class="m">t &gt; 0</span>인 실수 <span class="m">t</span>에 대하여 두 곡선 <span class="m">y = f(x), y = g(x)</span> 및 두 직선 <span class="m">x = 0, x = t</span>로 둘러싸인 부분의 넓이를 <span class="m">S(t)</span>라 하자.</p><span class="cond m">S′(t) = t<sup>2</sup> − 2t + a</span><p>일 때, &lt;보기&gt;에서 옳은 것만을 있는 대로 고른 것은? (단, <span class="m">a</span>는 상수)</p><span class="cond">ㄱ. <span class="m">a = 1</span>이다.<br>ㄴ. <span class="m">S(3) = 6</span>이다.<br>ㄷ. 두 곡선 <span class="m">y = f(x), y = g(x)</span> 및 두 직선 <span class="m">x = −2, x = 2</span>로 둘러싸인 부분의 넓이는 <span class="m">S(4)</span>와 같다.</span><div class="choices"><span>① ㄱ</span><span>② ㄷ</span><span>③ ㄱ, ㄴ</span><span>④ ㄱ, ㄷ</span><span>⑤ ㄴ, ㄷ</span></div>

## 발상

<b><span class='m'>S′(t)</span>는 넓이의 &lsquo;늘어나는 속도&rsquo;, 곧 그 자리의 세로 간격이다.</b> <span class='m'>h(x) = f(x) − g(x)</span>로 두면 <span class='m'>S(t) = ∫<sub>0</sub><sup>t</sup>h</span>이고 <span class='m'>S′(t) = h(t)</span>. 문제가 준 <span class='m'>f(1) = g(1)+1</span>은 곧 <span class='m'>h(1) = 1</span> 하나뿐인 값 정보다.

## 풀이

<p><span class="step">① a를 정한다.</span> <span class="m">h(t) = S′(t) = t<sup>2</sup> − 2t + a</span>이고 <span class="m">h(1) = f(1) − g(1) = 1</span>.</p><p class="m">1 − 2 + a = 1 → a = 2 &nbsp; → &nbsp; ㄱ은 거짓</p><p><span class="step">② S(t)를 구한다.</span> <span class="m">h(x) = x<sup>2</sup>−2x+2</span>이고 <span class="m">S(0) = 0</span>이므로</p><p class="m">S(t) = t<sup>3</sup>/3 − t<sup>2</sup> + 2t</p><p class="m">S(3) = 9 − 9 + 6 = 6 &nbsp; → &nbsp; ㄴ은 참</p><p><span class="step">③ ㄷ.</span> <span class="m">h &gt; 0</span>이므로 <span class="m">x = −2</span>부터 <span class="m">x = 2</span>까지의 넓이는 그대로 적분값이다.</p><p class="m">∫<sub>−2</sub><sup>2</sup>h = S(2) − S(−2) = (8/3 − 4 + 4) − (−8/3 − 4 − 4) = 40/3</p><p class="m">S(4) = 64/3 − 16 + 8 = 40/3 &nbsp; → &nbsp; ㄷ은 참</p><p>따라서 <b>ㄴ, ㄷ</b>.</p>

## 함정

<span class='m'>f(1) = g(1) + 1</span>을 &lsquo;넓이가 1&rsquo;로 읽으면 안 된다. <b>세로 간격이 1</b>이라는 뜻이고, 넓이의 <b>도함수 값</b>이 1이라는 정보다.

## 노하우

<b>넓이함수는 미분하면 세로 간격이 된다 — 이것이 미적분의 기본정리다.</b> <span class='m'>S(t) = ∫<sub>c</sub><sup>t</sup>h</span> → <span class='m'>S′(t) = h(t)</span>, 그리고 <span class='m'>S(c) = 0</span>이 적분상수를 결정한다. <b><span class='m'>h &gt; 0</span>이 주어졌으므로 절댓값을 걱정할 필요가 없다</b>는 것도 이 문제의 숨은 선물이다.
