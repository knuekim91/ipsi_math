---
id: DIF-W05-V3
parent: DIF-W05
unit: 05-미분
topic: k의 최댓값으로부터 삼차함수를 거꾸로 찾기
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W05 변형 · 역방향 추론)
origin: 유사문항
core: "M이 극소점이라는 것을 알고 있으면 M = −2a/3 한 줄로 a가 나온다. 조건에서 함수를 찾는 역방향 문제"
tags: [삼차함수,같은함숫값,극점,역추론,함수결정]
status: variant
added: 2026-10-17
answer: ③
---

## 문제

<p>최고차항의 계수가 <span class="m">1</span>인 삼차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키는 양의 실수
<span class="m">k</span>의 최댓값이 <span class="m">6</span>이다.</p>

<div class="cond">
<span class="cond m">x<sub>1</sub> &lt; x<sub>2</sub> ≤ k이고 f(x<sub>1</sub>) = f(x<sub>2</sub>)인 임의의 두 실수 x<sub>1</sub>, x<sub>2</sub>에 대하여</span>
<span class="cond m">x<sub>1</sub>x<sub>2</sub> ≤ 0이다.</span>
</div>

<p><span class="m">f(0) = 10</span>일 때, <span class="m">f(6)</span>의 값은?</p>

<div class="choices"><span>① −102</span><span>② −100</span><span>③ −98</span>
<span>④ −96</span><span>⑤ −94</span></div>

## 발상

<b>모문항은 함수를 주고 <span class="m">M</span>을 구했다.
이 문항은 <span class="m">M</span>을 주고 함수를 구한다.</b>
방향이 거꾸로다.<br><br>

<b>거꾸로 가려면 모문항에서 얻은 두 결론을 식으로 들고 있어야 한다.</b></p>
<p class="m">① 조건이 성립하려면 극대점이 0 → 일차항이 없다</p>
<p class="m">② k의 최댓값 M은 극소점 → M = −2a/3</p>
<p><b>②가 이 문항의 열쇠다.</b>
<span class="m">M = 6</span>을 넣으면 <span class="m">a</span>가 바로 나온다.
남은 상수항은 <span class="m">f(0)</span>이 알려 준다.<br><br>

<b>조건식이 하나뿐인데도 풀리는 이유</b>가 여기 있다.
<span class="m">M = 6</span>이라는 한 줄이 사실은
<b><span class="m">a</span>를 정하는 방정식</b>이기 때문이다.
<b>조건을 숫자로 번역할 수 있으면 미지수 하나가 사라진다.</b>

## 풀이

<p><span class="step">① 극대점이 0임을 밝힌다.</span>
극대점을 <span class="m">α</span>라 하면
<span class="m">α</span> 양옆에 같은 높이의 두 점을
<b>원하는 만큼 가깝게</b> 잡을 수 있다.
그 두 점은 <span class="m">α</span>와 같은 부호가 되므로
<span class="m">α ≠ 0</span>이면 곱이 양수가 되어 조건에 어긋난다.</p>
<p class="m">α = 0 → f′(0) = 0</p>

<p><span class="step">② f의 꼴을 적는다.</span>
<span class="m">f(x) = x<sup>3</sup> + ax<sup>2</sup> + bx + c</span>라 하면</p>
<p class="m">f′(x) = 3x<sup>2</sup> + 2ax + b</p>
<p class="m">f′(0) = b = 0</p>
<p class="m">f(x) = x<sup>3</sup> + ax<sup>2</sup> + c</p>

<p><span class="step">③ M이 극소점임을 쓴다.</span></p>
<p class="m">f′(x) = 3x<sup>2</sup> + 2ax = x(3x + 2a)</p>
<p>극소점은 <span class="m">x = −2a/3</span>이고,
극소점 양옆에 같은 높이의 두 점을 바싹 붙이면
<b>둘 다 양수</b>가 되어 조건을 어긴다.
그 쌍의 <span class="m">x<sub>2</sub></span>는 언제나 극소점보다 크므로
울타리를 극소점까지 밀 수 있다.</p>
<p class="m">M = −2a/3 = 6 → a = −9</p>

<p><span class="step">④ 상수항을 정한다.</span></p>
<p class="m">f(0) = c = 10</p>
<p class="m">f(x) = x<sup>3</sup> − 9x<sup>2</sup> + 10</p>

<p><span class="step">⑤ 답을 만든다.</span></p>
<p class="m">f(6) = 216 − 324 + 10 = −98</p>
<p class="m">답 ③</p>

<p><span class="step">⑥ 확인한다.</span>
<span class="m">f′(x) = 3x(x − 6)</span>이므로
극대점은 <span class="m">0</span>, 극소점은 <span class="m">6</span>이다.
<span class="m">k = 6</span>일 때 <span class="m">x<sub>2</sub> ≤ 6</span>인
모든 쌍은 <span class="m">x<sub>1</sub> ≤ 0 ≤ x<sub>2</sub></span>가 되어
조건을 지킨다. <b><span class="m">M = 6</span>이 맞다.</b></p>

## 함정

<b><span class="m">M</span>을 극대점으로 착각하지 않는다.</b>
극대점은 <span class="m">0</span>이고 <span class="m">k</span>는 양수여야 하므로
<span class="m">M</span>이 극대점일 수는 없다.
<b>울타리는 오른쪽에 있으므로 오른쪽 극점, 곧 극소점</b>이다.<br><br>

<b><span class="m">f(6)</span>이 극솟값이라는 것을 알아채면 검산이 된다.</b>
<span class="m">6</span>은 극소점이므로
<span class="m">f(6) = −98</span>이 <span class="m">f</span>의 극솟값이다.
<span class="m">f(0) = 10</span>이 극댓값이므로
<b>극댓값 &gt; 극솟값</b>이 맞는지 보면 부호 실수를 잡을 수 있다.<br><br>

<b><span class="m">b = 0</span>을 빼먹으면 미지수가 둘 남아 막힌다.</b>
조건에서 얻을 수 있는 식이 <span class="m">M = 6</span>과
<span class="m">f(0) = 10</span> 둘뿐이므로,
<b><span class="m">b = 0</span>을 먼저 확보해야 미지수가 둘로 줄어든다.</b>
&lsquo;극대점이 <span class="m">0</span>&rsquo;이 곧
&lsquo;일차항이 없다&rsquo;임을 잊지 않는다.<br><br>

<b>계산에서 <span class="m">9 × 36 = 324</span>를 틀리기 쉽다.</b>
<span class="m">6<sup>3</sup> = 216</span>,
<span class="m">9 × 6<sup>2</sup> = 324</span>이고
<span class="m">216 − 324 = −108</span>이다.
<b><span class="m">−108 + 10 = −98</span></b>이다.
선지가 <span class="m">2</span>씩 떨어져 있으니 한 자리만 틀려도 걸린다.

## 노하우

<b>조건에서 함수를 찾는 문제는 &lsquo;조건 하나 = 식 하나&rsquo;로 번역한다.</b>
미지수가 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span> 셋이면 식 셋이 필요하다.
이 문항에서는</p>
<p class="m">극대점이 0 → b = 0</p>
<p class="m">M = 6 → a = −9</p>
<p class="m">f(0) = 10 → c = 10</p>
<p><b>번역표를 먼저 만들고 하나씩 채운다.</b>
머릿속으로 한꺼번에 하려 들면 꼭 하나가 빈다.<br><br>

<b>모문항을 풀었으면 이 문항은 세 줄이다.</b>
모문항에서 <span class="m">M = −2a/3</span>을 <b>결론으로 챙겨 두었는지</b>가
갈림길이다.
<b>답만 맞히고 넘어가면 다음에 또 처음부터 그린다.</b>
문제를 푼 뒤에는 <b>&lsquo;무엇이 무엇을 정했나&rsquo;</b>를 한 줄로 적어 둔다.<br><br>

<b>삼차함수에서 챙겨 둘 두 줄</b></p>
<p class="m">극점 : x = 0, −2a/3 &nbsp; (일차항이 없을 때)</p>
<p class="m">두 극점의 합 = −2a/3, 변곡점 = −a/3</p>
<p><b>일차항이 없는 삼차함수는 극점 하나가 원점</b>이라 계산이 매우 가볍다.
문제가 <span class="m">f′(0) = 0</span>을 주거나
그것을 끌어내게 만들면 <b>반가운 신호</b>로 받아들인다.
