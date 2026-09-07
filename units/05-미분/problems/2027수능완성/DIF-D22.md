---
id: DIF-D22
unit: 05-미분
topic: 직선다발과 최소 실근 함수의 불연속
level: 4점
difficulty: 최상
source: 2027 수능완성 실전 모의고사 2회 22번
exam: 2027-수능완성
origin: 기출
core: "y = tx + t = t(x+1) 은 (−1, 0)을 지나는 직선다발이므로, f(x)/(x+1) = t 로 바꾸면 t는 곡선의 높이가 된다"
tags: [직선다발,분수함수,최소실근,불연속,사차함수결정]
status: seed
added: 2026-09-07
answer: 32
---

## 문제

<p><span class="m">x &gt; −1</span>에서 정의된 사차함수
<span class="m">f(x)</span>에 대하여 <span class="m">x</span>에 대한 방정식
<span class="m">f(x) = tx + t</span>가 실근을 갖기 위한 실수
<span class="m">t</span>의 최댓값이 <span class="m">5</span>이다.
<span class="m">t ≤ 5</span>인 실수 <span class="m">t</span>에 대하여
<span class="m">x</span>에 대한 방정식
<span class="m">f(x) = tx + t</span>를 만족시키는 실수
<span class="m">x</span>의 최솟값을 <span class="m">g(t)</span>라 하자.
<span class="m">g(t)</span>가 다음 조건을 만족시킬 때,
<span class="m">|f(3)|</span>의 값을 구하시오.</p>

<div class="cond">
<span class="cond m">(가) g(1) = 0, g(5) = 2</span>
<span class="cond m">(나) lim<sub>t→1+</sub>g(t) − lim<sub>t→1−</sub>g(t) = 1</span>
</div>

## 발상

<b>직선 <span class="m">y = tx + t</span>를 인수분해하는 것이 첫걸음이다.</b></p>
<p class="m">tx + t = t(x + 1)</p>
<p><span class="m">t</span>가 무엇이든 <span class="m">x = −1</span>이면 값이
<span class="m">0</span>이므로, 이 직선들은 모두
<b>점 <span class="m">(−1, 0)</span>을 지나는 직선다발</b>이다.
<span class="m">t</span>는 그 직선의 기울기다.<br><br>

<b>정의역이 <span class="m">x &gt; −1</span>이므로
<span class="m">x + 1 &gt; 0</span>이고, 양변을 나눌 수 있다.</b></p>
<p class="m">f(x) = t(x + 1) ⟺ f(x)/(x + 1) = t</p>
<p><span class="m">h(x) = f(x)/(x + 1)</span>이라 하면,
방정식의 실근은 <b>곡선 <span class="m">y = h(x)</span>와
수평선 <span class="m">y = t</span>의 교점</b>이 된다.
직선다발 문제가 <b>수평선 문제</b>로 바뀌는 순간이다.<br><br>

이렇게 보면 조건들이 모두 <span class="m">h</span>의 그래프에 대한 말이 된다.
&lsquo;실근을 갖기 위한 <span class="m">t</span>의 최댓값이 <span class="m">5</span>&rsquo;는
<b><span class="m">h</span>의 최댓값이 <span class="m">5</span></b>라는 뜻이고,
<span class="m">g(t)</span>는 <b>수평선이 곡선과 만나는 가장 왼쪽 점의
<span class="m">x</span>좌표</b>다.<br><br>

<b>조건 (나)의 점프가 곡선의 모양을 결정한다.</b>
<span class="m">t</span>가 커지는데 가장 왼쪽 교점이 <b>오른쪽으로 뛴다</b>는 것은,
왼쪽 봉우리의 <b>꼭대기 높이가 딱 <span class="m">1</span></b>이어서
<span class="m">t</span>가 <span class="m">1</span>을 넘는 순간
그 봉우리가 수평선에 닿지 못하게 되고, 교점이 오른쪽 산으로 건너뛴다는 뜻이다.

## 풀이

<p><span class="step">① 방정식을 수평선 문제로 바꾼다.</span>
<span class="m">f(x) = tx + t = t(x + 1)</span>이고
정의역이 <span class="m">x &gt; −1</span>이므로
<span class="m">x + 1 &gt; 0</span>이다. 양변을
<span class="m">x + 1</span>로 나눈다.</p>
<p class="m">h(x) = f(x)/(x + 1)</p>
<p>라 하면 방정식은 <span class="m">h(x) = t</span>가 되고,
<span class="m">g(t)</span>는 이 방정식의 <b>가장 작은 실근</b>이다.</p>

<p><span class="step">② t의 최댓값 조건을 읽는다.</span>
방정식 <span class="m">h(x) = t</span>가 실근을 가지려면
<span class="m">t</span>가 <span class="m">h</span>의 치역에 들어 있어야 한다.
그런 <span class="m">t</span>의 최댓값이 <span class="m">5</span>이므로</p>
<p class="m">(h의 최댓값) = 5</p>
<p>이다. 조건 (가)에서 <span class="m">g(5) = 2</span>이므로
<span class="m">x = 2</span>에서 이 최댓값에 닿는다.</p>
<p class="m">h(2) = 5, &nbsp; h′(2) = 0</p>

<p><span class="step">③ 조건 (나)로 곡선의 왼쪽 모양을 정한다.</span>
<span class="m">g(t)</span>는 가장 왼쪽 교점의
<span class="m">x</span>좌표이다.
<span class="m">t</span>가 커질 때 <span class="m">g(t)</span>가
<b>오른쪽으로 뛰려면</b>, 왼쪽에 있던 교점이 사라져야 한다.
그것은 <b>왼쪽 봉우리의 극댓값이 정확히 <span class="m">1</span>일 때</b> 일어난다.
조건 (가)에서 <span class="m">g(1) = 0</span>이므로
그 봉우리의 꼭짓점이 <span class="m">x = 0</span>이다.</p>
<p class="m">h(0) = 1, &nbsp; h′(0) = 0</p>
<p><span class="m">t</span>가 <span class="m">1</span>보다 조금 커지면
이 봉우리는 더 이상 수평선에 닿지 못하므로,
가장 왼쪽 교점은 <b>오른쪽 산의 오르막</b>으로 옮겨 간다.
조건 (나)에서 그 뛴 거리가 <span class="m">1</span>이므로</p>
<p class="m">lim<sub>t→1+</sub>g(t) = 0 + 1 = 1 → h(1) = 1</p>

<p><span class="step">④ h의 조건을 f의 조건으로 옮긴다.</span>
<span class="m">h(x) = f(x)/(x + 1)</span>에서
<span class="m">f(x) = (x + 1)h(x)</span>이므로</p>
<p class="m">f(0) = 1 × h(0) = 1</p>
<p class="m">f(1) = 2 × h(1) = 2</p>
<p class="m">f(2) = 3 × h(2) = 15</p>
<p>도함수는 몫의 미분법으로 구한다.</p>
<p class="m">h′(x) = [f′(x)(x + 1) − f(x)] / (x + 1)<sup>2</sup></p>
<p>분모는 <span class="m">0</span>이 아니므로
<span class="m">h′ = 0</span>은 분자가 <span class="m">0</span>이라는 뜻이다.</p>
<p class="m">h′(0) = 0 → f′(0) × 1 − f(0) = 0 → f′(0) = 1</p>
<p class="m">h′(2) = 0 → f′(2) × 3 − f(2) = 0 → f′(2) = 15/3 = 5</p>

<p><span class="step">⑤ 사차함수를 세운다.</span>
<span class="m">f(x) = ax<sup>4</sup> + bx<sup>3</sup> + cx<sup>2</sup> + dx + e</span>라 하자.
④에서 얻은 다섯 개의 조건을 차례로 쓴다.
먼저 상수항과 일차항이 바로 정해진다.</p>
<p class="m">f(0) = e = 1</p>
<p class="m">f′(x) = 4ax<sup>3</sup> + 3bx<sup>2</sup> + 2cx + d → f′(0) = d = 1</p>

<p><span class="step">⑥ 나머지 세 계수를 구한다.</span>
남은 세 조건을 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>에 대한 연립방정식으로 만든다.</p>
<p class="m">f(1) = a + b + c + 1 + 1 = 2 → a + b + c = 0</p>
<p class="m">f(2) = 16a + 8b + 4c + 2 + 1 = 15 → 4a + 2b + c = 3</p>
<p class="m">f′(2) = 32a + 12b + 4c + 1 = 5 → 8a + 3b + c = 1</p>
<p>두 번째 식에서 첫 번째 식을 빼고, 세 번째 식에서 첫 번째 식을 뺀다.</p>
<p class="m">3a + b = 3, &nbsp; 7a + 2b = 1</p>
<p>앞 식에서 <span class="m">b = 3 − 3a</span>를 얻어 뒤 식에 대입한다.</p>
<p class="m">7a + 2(3 − 3a) = 1 → 7a + 6 − 6a = 1 → a = −5</p>
<p class="m">b = 3 − 3(−5) = 18, &nbsp; c = −(a + b) = −(−5 + 18) = −13</p>
<p class="m">f(x) = −5x<sup>4</sup> + 18x<sup>3</sup> − 13x<sup>2</sup> + x + 1</p>

<p><span class="step">⑦ 최고차항의 계수가 음수인지 확인한다.</span>
<span class="m">a = −5 &lt; 0</span>이다.
<b>이것은 반드시 확인해야 하는 사항이다.</b>
<span class="m">a &gt; 0</span>이면 <span class="m">x → ∞</span>일 때
<span class="m">h(x) → ∞</span>가 되어 <span class="m">h</span>에
최댓값이 없고, &lsquo;<span class="m">t</span>의 최댓값이
<span class="m">5</span>&rsquo;라는 조건과 어긋난다.
지금은 <span class="m">a &lt; 0</span>이므로
<span class="m">x → ∞</span>일 때 <span class="m">h(x) → −∞</span>이고,
<span class="m">x → −1+</span>일 때는
<span class="m">f(−1) = −5 − 18 − 13 − 1 + 1 = −36 &lt; 0</span>이고
분모가 <span class="m">0</span>에 가까운 양수이므로
<span class="m">h(x) → −∞</span>이다.
따라서 <span class="m">h</span>는 최댓값 <span class="m">5</span>를 가진다.</p>

<div class="fig">
<svg viewBox="0 0 360 240" role="img" aria-label="곡선 y=h(x)의 개형. x가 마이너스 1에 가까워지면 아래로 내려가고, x=0에서 극댓값 1을 가진 뒤 잠시 내려갔다가 x=2에서 최댓값 5에 이르고 다시 내려간다. 수평선 y=1은 x=0과 x=1에서 곡선과 만난다.">
  <path class="ax" d="M14 120 L350 120"/>
  <path class="ax" d="M100 232 L100 34"/>
  <path class="gd" d="M20 232 L20 34"/>
  <path class="gd" d="M14 108 L350 108"/>
  <path class="gd" d="M14 60 L350 60"/>
  <path class="cv" d="M63 216 L68 175 L72 153 L76 137 L84 118 L92 110 L100 108 L116 112 L132 117 L146 119 L164 116 L180 108 L200 94 L220 78 L240 65 L260 60 L280 67 L300 92 L320 140 L332 182 L340 216"/>
  <circle class="pt" cx="100" cy="108" r="3.5"/>
  <circle class="pt" cx="180" cy="108" r="3.5"/>
  <circle class="pt" cx="260" cy="60"  r="3.5"/>
  <text x="20"  y="245" text-anchor="middle">−1</text>
  <text x="100" y="134" text-anchor="middle">0</text>
  <text x="180" y="134" text-anchor="middle">1</text>
  <text x="260" y="134" text-anchor="middle">2</text>
  <text x="12"  y="105" text-anchor="start">t = 1</text>
  <text x="12"  y="57"  text-anchor="start">t = 5</text>
  <text x="93"  y="31"  text-anchor="end">y</text>
  <text x="348" y="113" text-anchor="end">x</text>
</svg>
</div>

<p><span class="step">⑧ 답을 만든다.</span>
<span class="m">x = 3</span>을 대입한다.</p>
<p class="m">f(3) = −5 × 81 + 18 × 27 − 13 × 9 + 3 + 1</p>
<p class="m">= −405 + 486 − 117 + 4 = −32</p>
<p class="m">|f(3)| = 32</p>
<p class="m">답 32</p>

## 함정

<b><span class="m">tx + t</span>를 <span class="m">t(x + 1)</span>로 묶지 못하면
문제가 열리지 않는다.</b>
이 묶음이 &lsquo;모든 직선이 <span class="m">(−1, 0)</span>을 지난다&rsquo;는 사실과
&lsquo;양변을 <span class="m">x + 1</span>로 나눌 수 있다&rsquo;는 사실을 동시에 준다.
정의역이 <span class="m">x &gt; −1</span>로 주어진 이유가 바로
<b><span class="m">x + 1 &gt; 0</span>이라 부호 걱정 없이 나눌 수 있게</b>
하기 위해서다.<br><br>

<b>점프의 방향을 반대로 읽으면 안 된다.</b>
조건 (나)는 <span class="m">(우극한) − (좌극한) = 1</span>로
<b>양수</b>이다. 곧 <span class="m">t</span>가 커질 때
가장 왼쪽 근이 <b>오른쪽으로</b> 뛴다.
이것은 왼쪽 봉우리가 &lsquo;사라지는&rsquo; 상황이지,
새 근이 왼쪽에 생기는 상황이 아니다.
방향을 뒤집으면 곡선 모양을 정반대로 잡게 된다.<br><br>

<b><span class="m">g(1) = 0</span>은 &lsquo;<span class="m">h(0) = 1</span>&rsquo;만이 아니다.</b>
<span class="m">x = 0</span>이 <b>가장 작은</b> 근이어야 하고,
동시에 그 자리가 <b>극대점</b>이어야 점프가 생긴다.
그래서 <span class="m">h′(0) = 0</span>이라는 조건이 하나 더 나온다.
이 조건을 놓치면 미지수가 하나 남아 답이 정해지지 않는다.<br><br>

<b>최고차항의 계수가 음수여야 한다는 확인을 빠뜨리지 않는다.</b>
&lsquo;<span class="m">t</span>의 최댓값이 존재한다&rsquo;는 조건은
<span class="m">h</span>가 위로 유계라는 뜻이고,
그러려면 <span class="m">a &lt; 0</span>이어야 한다.

## 노하우

<b><span class="m">y = t(x − p) + q</span> 꼴은 한 점을 지나는 직선다발이다.</b>
<span class="m">t</span>가 문자로 된 상수인 직선 문제를 만나면
<b>먼저 <span class="m">t</span>로 묶어 항상 지나는 점을 찾는다.</b>
그리고 <span class="m">t = (f(x) − q)/(x − p)</span> 꼴로 옮기면
<b>기울기가 곡선의 높이</b>가 되어, 수평선 문제로 바뀐다.
이 변형 하나로 문제의 난이도가 크게 떨어진다.<br><br>

<b>&lsquo;최소 실근 함수&rsquo;가 불연속인 자리는 극댓값의 높이다.</b>
수평선을 아래에서 위로 올릴 때,
왼쪽 봉우리의 <b>꼭대기를 지나는 순간</b> 그 봉우리와의 교점이 사라지고
가장 왼쪽 교점이 오른쪽으로 건너뛴다.
<b>점프의 크기는 &lsquo;극대점의 <span class="m">x</span>좌표&rsquo;와
&lsquo;오른쪽 가지에서 같은 높이가 되는 <span class="m">x</span>좌표&rsquo;의 차</b>다.<br><br>

<b>미지수의 개수와 조건의 개수를 먼저 세어 본다.</b>
사차함수의 계수는 <span class="m">5</span>개이고,
이 문제에서 얻은 조건도
<span class="m">f(0)</span>, <span class="m">f(1)</span>,
<span class="m">f(2)</span>, <span class="m">f′(0)</span>,
<span class="m">f′(2)</span>로 정확히 <span class="m">5</span>개다.
<b>개수가 맞는지 확인하고 나서 연립하면</b> 조건을 빠뜨렸는지 바로 알 수 있다.
