---
id: DIF-W04-V2
parent: DIF-W04
unit: 05-미분
topic: 실근의 개수가 같을 조건과 사차함수 결정
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W04 변형 · 극댓값이 8인 경우)
origin: 유사문항
core: "극댓값 m이 커지면 극소가 생기는 자리도 3m/4로 함께 옮겨간다. 자리를 먼저 찾고 최솟값을 0으로 놓는다"
tags: [실근의개수,사차함수,절댓값,경계값,그래프개형]
status: variant
added: 2026-10-16
answer: 64
---

## 문제

<p>최고차항의 계수가 양수이고 <span class="m">f′(0) = 0</span>인 사차함수
<span class="m">f(x)</span>에 대하여 다음 조건을 만족시키지 <b>않는</b> 실수
<span class="m">t</span>가 하나뿐일 때, <span class="m">f(−6)</span>의 값을
구하시오.</p>

<div class="cond">
<span class="cond m">x에 대한 두 방정식 |x|(2x + 8) = t, &nbsp; |x|(2x + 8) = f(t)의 서로 다른 실근의 개수가 같다.</span>
</div>

## 발상

<b>극댓값이 커지면 극소가 생기는 자리도 함께 옮겨간다.</b>
이것을 놓치면 엉뚱한 곳에서 최솟값을 구하게 된다.<br><br>

<span class="m">g(x) = |x|(2x + 8)</span>의 왼쪽 조각은
<span class="m">−2x<sup>2</sup> − 8x = −2(x + 2)<sup>2</sup> + 8</span>이므로
<b>극대 <span class="m">8</span></b>이다.
표의 경계가 <span class="m">0</span>과 <span class="m">8</span>이 된다.<br><br>

<b><span class="m">f(t) = a t<sup>3</sup>(t − 8) + 8</span>까지는 원문항과 같은 흐름이다.</b>
달라지는 것은 <span class="m">h(t) = t<sup>3</sup>(t − 8)</span>의 극소가
<span class="m">t = 6</span>에서 생긴다는 점이다.
원문항에서는 <span class="m">3/2</span>, 앞 문항에서는 <span class="m">3</span>이었다.
<b>언제나 극댓값의 <span class="m">3/4</span> 자리</b>다.

## 풀이

<p><span class="step">① g의 개형과 극댓값을 구한다.</span></p>
<p class="m">x ≥ 0 : g(x) = 2x<sup>2</sup> + 8x</p>
<p class="m">x &lt; 0 : g(x) = −2x<sup>2</sup> − 8x = −2(x + 2)<sup>2</sup> + 8</p>
<p><span class="m">x = −2</span>에서 극대 <span class="m">8</span>,
<span class="m">x = 0</span>에서 극소 <span class="m">0</span>이다.</p>

<p><span class="step">② 실근의 개수를 표로 만든다.</span></p>
<p class="m">k &lt; 0 → 1개 &nbsp;/&nbsp; k = 0 → 2개 &nbsp;/&nbsp; 0 &lt; k &lt; 8 → 3개</p>
<p class="m">k = 8 → 2개 &nbsp;/&nbsp; k &gt; 8 → 1개</p>

<p><span class="step">③ f의 꼴을 정한다.</span>
<span class="m">t = 0</span>의 좌우에서 안과 밖이 갈리므로
<span class="m">f(0) = 8</span>이어야 하고,
<span class="m">f′(0) = 0</span>이므로
<span class="m">f − 8</span>은 <span class="m">t = 0</span>에서 삼중근을 갖는다.
남은 인수의 근은 오른쪽 경계와 같아야 하므로</p>
<p class="m">f(t) = a t<sup>3</sup>(t − 8) + 8 &nbsp; (a &gt; 0)</p>

<p><span class="step">④ 극소가 생기는 자리를 찾는다.</span></p>
<p class="m">h(t) = t<sup>3</sup>(t − 8) = t<sup>4</sup> − 8t<sup>3</sup></p>
<p class="m">h′(t) = 4t<sup>3</sup> − 24t<sup>2</sup> = 4t<sup>2</sup>(t − 6)</p>
<p><span class="m">(0, 8)</span> 안에서 <span class="m">t = 6</span>이 극소다.</p>
<p class="m">h(6) = 216 × (6 − 8) = −432</p>

<p><span class="step">⑤ 최솟값이 0이 되도록 a를 정한다.</span>
<span class="m">f</span>의 <span class="m">(0, 8)</span>에서의 최솟값은
<span class="m">8 − 432a</span>이다.
이것이 양수면 어긋나는 곳이 없고, 음수면 구간으로 생긴다.</p>
<p class="m">8 − 432a = 0 → a = 8/432 = 1/54</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">f(t) = (1/54)t<sup>3</sup>(t − 8) + 8</p>
<p class="m">f(−6) = (1/54) × (−216) × (−6 − 8) + 8</p>
<p class="m">= (1/54) × (−216) × (−14) + 8</p>
<p><span class="m">−216 ÷ 54 = −4</span>이므로</p>
<p class="m">= (−4) × (−14) + 8 = 56 + 8 = 64</p>
<p class="m">답 64</p>

## 함정

<b>극소가 생기는 자리를 <span class="m">3/2</span>나
<span class="m">3</span>으로 쓰면 안 된다.</b>
<span class="m">h′(t) = 4t<sup>2</sup>(t − m)</span>에서
<span class="m">t = m</span>이 아니라
<b><span class="m">h(t) = t<sup>3</sup>(t − m)</span>을 미분해서</b>
나오는 <span class="m">3m/4</span>다.
<span class="m">m = 8</span>이면 <span class="m">6</span>이다.<br><br>

<b><span class="m">h(6)</span>을 계산할 때 <span class="m">6<sup>3</sup> = 216</span>을 쓴다.</b>
<span class="m">6<sup>4</sup> − 8 × 6<sup>3</sup></span>로 풀어 써도 되지만
<span class="m">6<sup>3</sup>(6 − 8)</span>로 묶으면 훨씬 짧다.
<b>묶인 꼴을 풀지 않고 그대로 계산</b>하는 것이 안전하다.<br><br>

<b>약분을 먼저 하면 큰 수를 다루지 않는다.</b>
<span class="m">(1/54) × (−216)</span>을 먼저 <span class="m">−4</span>로 만들고
<span class="m">−14</span>를 곱한다.
<span class="m">216 × 14</span>를 먼저 계산하면 <span class="m">3024</span>가 되어
실수하기 쉽다.

## 노하우

<b>이 유형의 뼈대는 언제나 같다.</b></p>
<p class="m">g의 극댓값 m을 구한다 → f(t) = a t<sup>3</sup>(t − m) + m</p>
<p class="m">→ 극소는 t = 3m/4 → 최솟값을 0으로 놓고 a를 구한다</p>
<p><b>세 문항을 풀고 나면 이 네 줄이 손에 붙는다.</b>
그러면 남는 일은 산수뿐이다.<br><br>

<b><span class="m">m</span>이 커질수록 <span class="m">a</span>는 급격히 작아진다.</b>
<span class="m">a = 256/(27m<sup>3</sup>)</span>이기 때문이다.
<span class="m">m = 2</span>면 <span class="m">32/27</span>,
<span class="m">m = 4</span>면 <span class="m">4/27</span>,
<span class="m">m = 8</span>이면 <span class="m">1/54</span>이다.
<b>답이 이 흐름에 맞는지 보면 중간에 틀렸는지 알 수 있다.</b><br><br>

<b>묻는 점은 계산이 깔끔해지도록 고른 것이다.</b>
<span class="m">f(−6)</span>에서 <span class="m">(−6)<sup>3</sup> = −216</span>이
<span class="m">54</span>로 나누어떨어진다.
<b>묻는 점의 세제곱이 분모와 약분되는지</b> 보면
계산이 맞게 가고 있는지 확인할 수 있다.
