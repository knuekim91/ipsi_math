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

<p><span class="step">① 두 곡선의 세로 간격을 하나의 함수로 둔다.</span></p>
<p class="m">h(x) = f(x) − g(x)</p>
<p>문제에서 <span class="m">f(x) &gt; g(x)</span>라 했으므로 <span class="m">h(x) &gt; 0</span>이다.
<b>절댓값을 걱정하지 않아도 된다는 뜻</b>이라 이 조건이 중요하다.
그러면 넓이는 그대로 적분값이다.</p>
<p class="m">S(t) = ∫<sub>0</sub><sup>t</sup>h(x)dx</p>

<p><span class="step">② S′(t)가 무엇인지 확인한다.</span>
미적분의 기본정리에 따라 <b>넓이함수를 미분하면 그 자리의 세로 간격</b>이 된다.</p>
<p class="m">S′(t) = h(t)</p>
<p>문제가 <span class="m">S′(t) = t<sup>2</sup> − 2t + a</span>를 줬으므로</p>
<p class="m">h(t) = t<sup>2</sup> − 2t + a</p>

<p><span class="step">③ f(1) = g(1) + 1을 번역한다.</span>
이 식을 옮기면 <span class="m">f(1) − g(1) = 1</span>, 곧</p>
<p class="m">h(1) = 1</p>
<p><b>넓이가 1이라는 뜻이 아니라 세로 간격이 1</b>이라는 뜻이다.
②의 식에 <span class="m">t = 1</span>을 넣는다.</p>
<p class="m">1 − 2 + a = 1 → a = 2</p>
<p>따라서 <b>ㄱ(<span class="m">a = 1</span>)은 거짓</b>이다.</p>

<p><span class="step">④ S(t)를 구한다.</span>
<span class="m">h(x) = x<sup>2</sup> − 2x + 2</span>를 적분한다.
적분 구간이 <span class="m">0</span>에서 시작하므로 <span class="m">S(0) = 0</span>이고, 이것이 상수를 정해 준다.</p>
<p class="m">S(t) = t<sup>3</sup>/3 − t<sup>2</sup> + 2t</p>

<p><span class="step">⑤ ㄴ을 확인한다.</span></p>
<p class="m">S(3) = 27/3 − 9 + 6 = 9 − 9 + 6 = 6</p>
<p><b>ㄴ은 참</b>이다.</p>

<p><span class="step">⑥ ㄷ을 확인한다.</span>
<span class="m">x = −2</span>부터 <span class="m">x = 2</span>까지의 넓이를 계산한다.
<span class="m">h &gt; 0</span>이므로 절댓값 없이 적분하면 된다.
<span class="m">S</span>의 식을 그대로 쓸 수 있다.</p>
<p class="m">∫<sub>−2</sub><sup>2</sup>h dx = S(2) − S(−2)</p>
<p class="m">S(2) = 8/3 − 4 + 4 = 8/3</p>
<p class="m">S(−2) = −8/3 − 4 − 4 = −8/3 − 8</p>
<p class="m">S(2) − S(−2) = 8/3 + 8/3 + 8 = 16/3 + 24/3 = 40/3</p>
<p>이제 <span class="m">S(4)</span>와 비교한다.</p>
<p class="m">S(4) = 64/3 − 16 + 8 = 64/3 − 8 = 64/3 − 24/3 = 40/3</p>
<p>두 값이 같으므로 <b>ㄷ도 참</b>이다.</p>

<p><span class="step">⑦ 답을 고른다.</span>
옳은 것은 <b>ㄴ, ㄷ</b>.</p>
<p class="m">답 ⑤</p>

## 함정

<span class='m'>f(1) = g(1) + 1</span>을 &lsquo;넓이가 1&rsquo;로 읽으면 안 된다. <b>세로 간격이 1</b>이라는 뜻이고, 넓이의 <b>도함수 값</b>이 1이라는 정보다.

## 노하우

<b>넓이함수는 미분하면 세로 간격이 된다 — 이것이 미적분의 기본정리다.</b> <span class='m'>S(t) = ∫<sub>c</sub><sup>t</sup>h</span> → <span class='m'>S′(t) = h(t)</span>, 그리고 <span class='m'>S(c) = 0</span>이 적분상수를 결정한다. <b><span class='m'>h &gt; 0</span>이 주어졌으므로 절댓값을 걱정할 필요가 없다</b>는 것도 이 문제의 숨은 선물이다.
