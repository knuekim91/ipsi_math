---
id: DIF-C22
unit: 05-미분
topic: 절댓값 그래프와 수평선의 교점 개수
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 22번
exam: 2027-수능완성
origin: 기출
core: "g(t)가 뛰는 곳은 t가 |f|의 극값을 지날 때뿐이고 그 뜀의 크기가 L을 만든다"
tags: [삼차함수,절댓값,교점개수,불연속]
status: seed
added: 2026-09-07
answer: 73
---

## 문제

<p>최고차항의 계수가 <span class="m">1</span>인 삼차함수
<span class="m">f(x)</span>가 다음 조건을 만족시킨다.</p>
<span class="cond">(가) 방정식 <span class="m">f(x) = f(−2)</span>의
서로 다른 실근의 개수는 <span class="m">2</span>이다.<br>
(나) <span class="m">f′(−2) &gt; 0</span>이고
<span class="m">f′(−2) = f′(4)</span>이다.</span>
<p>실수 <span class="m">t</span>에 대하여 함수
<span class="m">y = |f(x)|</span>의 그래프와 직선 <span class="m">y = t</span>가 만나는
서로 다른 점의 개수를 <span class="m">g(t)</span>라 하자.
집합 <span class="m">L = {l | l = lim<sub>t→k+</sub>g(t) − lim<sub>t→k−</sub>g(t), k는 실수}</span>의
모든 원소의 합이 <span class="m">2</span>일 때, 모든
<span class="m">f(0)</span>의 값의 합은 <span class="m">q/p</span>이다.
<span class="m">p + q</span>의 값을 구하시오.
(단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

(나)의 <span class="m">f′(−2) = f′(4)</span>부터 쓴다.
<span class="m">f′</span>은 이차함수이므로 <b>두 점에서 값이 같다는 것은
그 두 점이 축에 대해 대칭</b>이라는 뜻이고, 축은
<span class="m">x = (−2+4)/2 = 1</span>이다. 이것이 계수 하나를 결정한다.<br><br>
그 다음 (가)가 계수 하나를 더 정하고, <b>상수항만 남는다.</b>
남은 상수항을 정하는 것이 <span class="m">L</span> 조건이다.<br><br>
<span class="m">g(t)</span>는 <b><span class="m">y = |f(x)|</span>에 수평선을 긋고
교점을 세는 것</b>이므로, <span class="m">|f|</span>의 그래프에서
<b>극값의 높이를 지날 때만</b> 개수가 뛴다.

## 풀이

<p><span class="step">① (나)의 대칭 조건으로 계수를 잡는다.</span>
<span class="m">f(x) = x<sup>3</sup> + bx<sup>2</sup> + cx + d</span>라 하면</p>
<p class="m">f′(x) = 3x<sup>2</sup> + 2bx + c</p>
<p><span class="m">f′(−2) = f′(4)</span>이므로</p>
<p class="m">12 − 4b + c = 48 + 8b + c</p>
<p><span class="m">c</span>가 양변에서 지워진다.</p>
<p class="m">12 − 4b = 48 + 8b → −36 = 12b → b = −3</p>
<p class="m">f(x) = x<sup>3</sup> − 3x<sup>2</sup> + cx + d, &nbsp; f′(x) = 3x<sup>2</sup> − 6x + c</p>
<p>또 <span class="m">f′(−2) = 12 + 12 + c = 24 + c &gt; 0</span>이므로
<b><span class="m">c &gt; −24</span></b>임을 기억해 둔다.</p>

<p><span class="step">② (가)로 c를 정한다.</span>
<span class="m">f(x) − f(−2) = 0</span>은 <span class="m">x = −2</span>를 근으로 갖는
삼차방정식이다. 조립제법으로 나누면</p>
<p class="m">f(x) − f(−2) = (x + 2)(x<sup>2</sup> − 5x + c + 10)</p>
<p>서로 다른 실근이 <span class="m">2</span>개가 되려면 <b>중근이 하나 있어야</b> 한다.
두 가지 경우를 따진다.</p>
<p><b>경우 1</b> — 뒤쪽 이차식이 중근을 갖는다.</p>
<p class="m">판별식 = 25 − 4(c + 10) = 0 → −4c = 15 → c = −15/4</p>
<p>이때 중근은 <span class="m">x = 5/2</span>이고 <span class="m">−2</span>와 다르므로
근은 <span class="m">−2, 5/2</span> 두 개다. ✓</p>
<p><b>경우 2</b> — 뒤쪽 이차식이 <span class="m">x = −2</span>를 근으로 갖는다.</p>
<p class="m">4 + 10 + c + 10 = 0 → c = −24</p>
<p>그런데 ①에서 <span class="m">c &gt; −24</span>여야 하므로 <b>불가능</b>하다.</p>
<p>따라서 <span class="m">c = −15/4</span>이다.</p>
<p class="m">f(x) = x<sup>3</sup> − 3x<sup>2</sup> − (15/4)x + d</p>

<p><span class="step">③ 극값을 d로 나타낸다.</span></p>
<p class="m">f′(x) = 3x<sup>2</sup> − 6x − 15/4 = 0</p>
<p>양변에 <span class="m">4/3</span>을 곱한다.</p>
<p class="m">4x<sup>2</sup> − 8x − 5 = 0 → (2x − 5)(2x + 1) = 0 → x = 5/2, x = −1/2</p>
<p>최고차항의 계수가 양수이므로 작은 쪽에서 극대, 큰 쪽에서 극소다.</p>
<p class="m">극댓값 M = f(−1/2) = −1/8 − 3/4 + 15/8 + d = 1 + d</p>
<p class="m">극솟값 m = f(5/2) = 125/8 − 75/4 − 75/8 + d = −25/2 + d</p>
<p>두 값의 차는 <span class="m">M − m = 27/2</span>로 <b><span class="m">d</span>와 무관하다.</b></p>

<p><span class="step">④ g(t)가 어디서 뛰는지 정리한다.</span>
수평선 <span class="m">y = s</span>와 <span class="m">y = f(x)</span>의 교점 수를
<span class="m">N(s)</span>라 하면</p>
<p class="m">s &gt; M 또는 s &lt; m : 1개 &nbsp;/&nbsp; s = M 또는 s = m : 2개 &nbsp;/&nbsp; m &lt; s &lt; M : 3개</p>
<p><span class="m">|f(x)| = t</span>는 <span class="m">f(x) = t</span> 또는
<span class="m">f(x) = −t</span>이므로, <span class="m">t &gt; 0</span>일 때</p>
<p class="m">g(t) = N(t) + N(−t)</p>
<p>이고 <span class="m">t &lt; 0</span>이면 <span class="m">g(t) = 0</span>이다.
따라서 <b>뜀이 생기는 곳은 <span class="m">t = 0</span>과
<span class="m">t</span>가 <span class="m">M</span> 또는 <span class="m">−m</span>과 같아지는 곳</b>뿐이다.</p>

<p><span class="step">⑤ 경우를 나눠 L을 구한다.</span></p>
<p><b>[가] <span class="m">m &lt; 0 &lt; M</span>이고 <span class="m">M ≠ −m</span></b> —
<span class="m">t = 0</span>에서 <span class="m">0 → 6</span>으로 뛰고,
<span class="m">M</span>과 <span class="m">−m</span>에서 각각 <span class="m">2</span>씩 줄어든다.</p>
<p class="m">L = {6, −2, 0} → 합 4 (조건에 맞지 않음)</p>
<p><b>[나] <span class="m">m &lt; 0 &lt; M</span>이고 <span class="m">M = −m</span></b> —
두 뜀이 같은 자리에서 겹쳐 한 번에 <span class="m">4</span>가 줄어든다.</p>
<p class="m">L = {6, −4, 0} → 합 2 ✓</p>
<p class="m">M = −m → 1 + d = 25/2 − d → 2d = 23/2 → d = 23/4</p>
<p><b>[다] <span class="m">M = 0</span></b> (곧 <span class="m">d = −1</span>) —
<span class="m">t = 0</span>에서 <span class="m">0 → 4</span>, <span class="m">t = −m</span>에서 <span class="m">2</span> 감소.</p>
<p class="m">L = {4, −2, 0} → 합 2 ✓</p>
<p><b>[라] <span class="m">m = 0</span></b> (곧 <span class="m">d = 25/2</span>) —
같은 이유로 <span class="m">L = {4, −2, 0}</span> → 합 2 ✓</p>
<p><b>[마] <span class="m">m &gt; 0</span> 또는 <span class="m">M &lt; 0</span></b> —
<span class="m">L = {2, −2, 0}</span> → 합 0 (맞지 않음)</p>

<p><span class="step">⑥ 답을 만든다.</span>
조건을 만족시키는 <span class="m">d</span>는 세 개이고,
<span class="m">f(0) = d</span>이다.</p>
<p class="m">23/4 + (−1) + 25/2 = 23/4 − 4/4 + 50/4 = 69/4</p>
<p><span class="m">69</span>와 <span class="m">4</span>는 서로소이므로
<span class="m">q = 69</span>, <span class="m">p = 4</span>이다.</p>
<p class="m">p + q = 4 + 69 = 73</p>
<p class="m">답 73</p>

## 함정

<b><span class="m">L</span>은 집합이라 <span class="m">0</span>도 원소다.</b>
뜀이 없는 <span class="m">k</span>에서는 <span class="m">l = 0</span>이므로
<span class="m">0</span>이 항상 들어간다. 합에는 영향이 없지만
원소를 셀 때 빠뜨리면 헷갈린다.<br><br>
<b>그리고 경계 경우 [다], [라]를 빠뜨리기 쉽다.</b>
<span class="m">M = 0</span>이나 <span class="m">m = 0</span>이면
<span class="m">t = 0</span>에서의 뜀이 <span class="m">6</span>이 아니라 <span class="m">4</span>가 된다.
<b>&lsquo;모든 <span class="m">f(0)</span>의 값의 합&rsquo;이라는 말이
답이 여러 개라는 예고</b>이므로 경계를 반드시 확인해야 한다.

## 노하우

<b><span class="m">f′(p) = f′(q)</span>는 &lsquo;<span class="m">p</span>와
<span class="m">q</span>가 <span class="m">f′</span>의 축에 대해 대칭&rsquo;이라는 뜻이다.</b>
<span class="m">f′</span>이 이차함수이므로 축은 두 점의 중점이고,
이 한 줄이 <span class="m">x<sup>2</sup></span>의 계수를 바로 준다.<br><br>
<b><span class="m">|f(x)| = t</span>는 <span class="m">f(x) = t</span>와
<span class="m">f(x) = −t</span> 두 개로 갈라 센다.</b>
그러면 교점 개수가 뛰는 자리가 <b>극값의 높이</b>로 정리되고,
<span class="m">t = 0</span>에서의 뜀은 <span class="m">f</span>의 실근 개수가 정한다.<br><br>
<b>&lsquo;모든 값의 합&rsquo;을 물으면 경계 경우를 반드시 따로 확인한다.</b>
부등호가 등호로 바뀌는 순간이 답에 포함되는 경우가 대부분이다.
