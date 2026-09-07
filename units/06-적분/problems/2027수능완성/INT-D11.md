---
id: INT-D11
unit: 06-적분
topic: 넓이의 최솟값
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 11번
exam: 2027-수능완성
origin: 기출
core: "f(b) − f(a) ≥ 2(b − a) 는 f(x) − 2x 가 증가한다는 뜻이고, 미분하면 f′(x) ≥ 2 가 된다"
tags: [넓이,평균변화율,증가함수,미분계수]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>구간 <span class="m">[−1, ∞)</span>에서 연속이고 구간
<span class="m">(−1, ∞)</span>에서 미분가능한 함수 <span class="m">f(x)</span>가
다음 조건을 만족시킨다.</p>

<div class="cond">
<span class="cond m">(가) −1 ≤ x ≤ 1일 때, f(x) = 2x<sup>3</sup> − 2x<sup>2</sup> + 5이다.</span>
<span class="cond m">(나) 1 ≤ a &lt; b인 임의의 두 실수 a, b에 대하여 f(b) − f(a) ≥ 2(b − a)이다.</span>
</div>

<p>곡선 <span class="m">y = f(x)</span>와 <span class="m">x</span>축 및 두 직선
<span class="m">x = −1</span>, <span class="m">x = 3</span>으로 둘러싸인 부분의
넓이의 최솟값은?</p>

<div class="fig">
<svg viewBox="0 0 360 220" role="img" aria-label="구간 마이너스 1부터 1까지는 삼차곡선이고 그 뒤로는 기울기가 2인 직선으로 이어지는 그래프. x축과 두 직선 x=-1, x=3 사이의 영역이 칠해져 있다.">
  <path class="rg" d="M50 190 L50 152 C70 145 90 143 110 146 C130 149 150 155 170 152 L330 40 L330 190 Z"/>
  <path class="ax" d="M30 190 L345 190"/>
  <path class="ax" d="M110 200 L110 25"/>
  <path class="cv" d="M50 152 C70 145 90 143 110 146 C130 149 150 155 170 152"/>
  <path class="cv" d="M170 152 L330 40"/>
  <path class="gd" d="M50 190 L50 152"/>
  <path class="gd" d="M330 190 L330 40"/>
  <circle class="pt" cx="170" cy="152" r="3.5"/>
  <text x="50"  y="205" text-anchor="middle">−1</text>
  <text x="170" y="205" text-anchor="middle">1</text>
  <text x="330" y="205" text-anchor="middle">3</text>
  <text x="103" y="22"  text-anchor="end">y</text>
  <text x="343" y="183" text-anchor="end">x</text>
  <text x="250" y="88"  text-anchor="middle">기울기 2</text>
</svg>
</div>

<div class="choices"><span>① 65/3</span><span>② 22</span><span>③ 67/3</span>
<span>④ 68/3</span><span>⑤ 23</span></div>

## 발상

<b>조건 (나)를 그대로 두면 손댈 수 없다. 한쪽으로 몰아서 읽어야 한다.</b>
<span class="m">f(b) − f(a) ≥ 2(b − a)</span>의 우변을 좌변으로 옮기면
<span class="m">(f(b) − 2b) − (f(a) − 2a) ≥ 0</span>이 된다.
여기서 <span class="m">g(x) = f(x) − 2x</span>라 하면 이 부등식은
<b><span class="m">a &lt; b</span>이면 <span class="m">g(a) ≤ g(b)</span></b>,
곧 <span class="m">g(x)</span>가 <span class="m">x ≥ 1</span>에서
<b>증가한다</b>는 뜻이다.
미분가능한 함수가 증가할 조건은 <span class="m">g′(x) ≥ 0</span>이므로
<span class="m">f′(x) ≥ 2</span>가 된다.<br><br>

<b>넓이를 최소로 만들려면 <span class="m">f(x)</span>를 가능한 한 작게 잡아야 한다.</b>
<span class="m">x &gt; 1</span>에서 <span class="m">f</span>가 가장 느리게 자라는 경우가
<span class="m">f′(x) = 2</span>인 경우, 곧 <b>기울기가 <span class="m">2</span>인 직선</b>이다.
그 직선은 <span class="m">x = 1</span>에서 조건 (가)의 곡선과 값도 미분계수도
그대로 이어져야 한다.

## 풀이

<p><span class="step">① 조건 (나)를 미분 조건으로 바꾼다.</span>
<span class="m">g(x) = f(x) − 2x</span>라 하자.
조건 (나)의 부등식에서 <span class="m">2b</span>와 <span class="m">2a</span>를
각각 옮겨 정리하면 다음과 같다.</p>
<p class="m">f(b) − 2b ≥ f(a) − 2a → g(b) ≥ g(a)</p>
<p>즉 <span class="m">g(x)</span>는 <span class="m">x ≥ 1</span>에서 증가하는 함수이다.
<span class="m">g(x)</span>가 미분가능하므로 이는 다음 조건과 같다.</p>
<p class="m">g′(x) = f′(x) − 2 ≥ 0 → f′(x) ≥ 2 &nbsp; (x &gt; 1)</p>

<p><span class="step">② x = 1에서의 값과 미분계수를 구한다.</span>
조건 (가)에서 <span class="m">−1 ≤ x ≤ 1</span>일 때
<span class="m">f(x) = 2x<sup>3</sup> − 2x<sup>2</sup> + 5</span>이므로</p>
<p class="m">f(1) = 2 − 2 + 5 = 5</p>
<p class="m">f′(x) = 6x<sup>2</sup> − 4x → f′(1) = 6 − 4 = 2</p>
<p>함수 <span class="m">f</span>는 <span class="m">x = 1</span>에서 미분가능하므로
왼쪽에서 온 미분계수 <span class="m">2</span>가 오른쪽에서도 그대로 이어진다.
<b><span class="m">f′(1) = 2</span>는 ①에서 얻은 부등식
<span class="m">f′(x) ≥ 2</span>의 경계값이다.</b>
곧 조건 (나)는 <span class="m">x = 1</span>에서 아슬아슬하게 성립한다.</p>

<p><span class="step">③ 넓이가 최소가 되는 f를 잡는다.</span>
<span class="m">x &gt; 1</span>에서 <span class="m">f′(x) ≥ 2</span>이므로,
<span class="m">f</span>는 <span class="m">f(1) = 5</span>에서 출발하여
기울기가 항상 <span class="m">2</span> 이상으로 자란다. 따라서</p>
<p class="m">f(x) ≥ 5 + 2(x − 1) = 2x + 3 &nbsp; (x ≥ 1)</p>
<p>곡선이 <span class="m">x</span>축 위에 있는 동안에는
<span class="m">f(x)</span>가 클수록 넓이도 커진다.
그러므로 넓이가 최소가 되는 것은 <b>등호가 성립할 때</b>, 곧</p>
<p class="m">f(x) = 2x + 3 &nbsp; (1 ≤ x ≤ 3)</p>
<p>일 때이다. 이 직선은 <span class="m">x = 1</span>에서 값이
<span class="m">5</span>이고 기울기가 <span class="m">2</span>이므로
조건 (가)의 곡선과 매끄럽게 이어지고, 문제의 모든 조건을 만족시킨다.</p>

<p><span class="step">④ 넓이를 구하기 전에 부호를 확인한다.</span>
넓이를 정적분으로 그대로 계산하려면 곡선이 <span class="m">x</span>축 위에 있어야 한다.
<span class="m">−1 ≤ x ≤ 1</span>에서
<span class="m">f(x) = 2x<sup>3</sup> − 2x<sup>2</sup> + 5</span>의 최솟값을 확인한다.
<span class="m">f′(x) = 6x<sup>2</sup> − 4x = 2x(3x − 2)</span>이므로
<span class="m">x = 0</span>과 <span class="m">x = 2/3</span>이 극점이다.</p>
<p class="m">f(−1) = −2 − 2 + 5 = 1, &nbsp; f(0) = 5</p>
<p class="m">f(2/3) = 16/27 − 8/9 + 5 = −8/27 + 5 = 127/27</p>
<p>양 끝과 극점에서의 값이 모두 양수이므로
<span class="m">−1 ≤ x ≤ 1</span>에서 <span class="m">f(x) &gt; 0</span>이다.
<span class="m">1 ≤ x ≤ 3</span>에서도
<span class="m">f(x) = 2x + 3 ≥ 5 &gt; 0</span>이다.
따라서 넓이는 <span class="m">f(x)</span>를 그대로 적분하여 구한다.</p>

<p><span class="step">⑤ 앞쪽 넓이를 적분한다.</span>
적분구간 <span class="m">[−1, 1]</span>은 원점에 대하여 대칭이므로
홀수 차수 항인 <span class="m">2x<sup>3</sup></span>의 정적분은
<span class="m">0</span>이다.</p>
<p class="m">∫<sub>−1</sub><sup>1</sup>(2x<sup>3</sup> − 2x<sup>2</sup> + 5)dx
= 0 − 2 × ∫<sub>−1</sub><sup>1</sup>x<sup>2</sup>dx + 5 × 2</p>
<p class="m">= −2 × (2/3) + 10 = −4/3 + 10 = 26/3</p>

<p><span class="step">⑥ 뒤쪽 넓이를 적분한다.</span></p>
<p class="m">∫<sub>1</sub><sup>3</sup>(2x + 3)dx
= [x<sup>2</sup> + 3x]<sub>1</sub><sup>3</sup></p>
<p class="m">= (9 + 9) − (1 + 3) = 18 − 4 = 14</p>

<p><span class="step">⑦ 답을 만든다.</span>
두 조각의 넓이를 더한다.</p>
<p class="m">(넓이의 최솟값) = 26/3 + 14 = 26/3 + 42/3 = 68/3</p>
<p class="m">답 ④</p>

## 함정

<b>조건 (나)를 그냥 &lsquo;증가함수&rsquo;로만 읽으면 부족하다.</b>
<span class="m">f(b) ≥ f(a)</span>가 아니라
<span class="m">f(b) − f(a) ≥ 2(b − a)</span>이므로,
증가하는 <b>정도</b>까지 정해져 있다.
<span class="m">2(b − a)</span>를 좌변으로 옮겨
<span class="m">f(x) − 2x</span>를 만드는 것이 유일한 출발점이다.
이 변형을 못 하면 문제 전체가 열리지 않는다.<br><br>

<b><span class="m">x</span>축 위인지 확인하지 않으면 넓이가 틀린다.</b>
곡선이 <span class="m">x</span>축 아래로 내려가는 구간에서는
<span class="m">−f(x)</span>를 적분해야 한다.
이 문제에서는 항상 위에 있지만, 확인하는 한 줄을 빠뜨리면
비슷한 문제에서 그대로 틀린다.<br><br>

<b><span class="m">x &gt; 1</span>에서 <span class="m">f</span>를 마음대로 정할 수 있다고
착각하면 안 된다.</b> <span class="m">x = 1</span>에서
값이 <span class="m">5</span>로 이어져야 하고 미분계수도
<span class="m">2</span>로 이어져야 한다. 이 두 가지가
직선 <span class="m">y = 2x + 3</span>을 완전히 결정한다.

## 노하우

<b>부등식에 <span class="m">b − a</span>가 통째로 들어 있으면 한쪽으로 몬다.</b>
<span class="m">f(b) − f(a) ≥ k(b − a)</span> 꼴은 언제나
<span class="m">f(x) − kx</span>가 증가한다는 뜻이고, 미분하면
<span class="m">f′(x) ≥ k</span>가 된다.
부등호가 반대이면 <span class="m">f(x) − kx</span>가 감소한다.<br><br>

<b>넓이의 최솟값을 물으면 함수의 최솟값을 잡는다.</b>
곡선이 <span class="m">x</span>축 위에 있는 동안에는
함수가 작을수록 넓이도 작다. 부등식의
<b>등호가 성립하는 경우</b>가 곧 답이 되는 경우다.<br><br>

<b>대칭인 구간의 적분은 반으로 줄인다.</b>
<span class="m">∫<sub>−a</sub><sup>a</sup></span> 꼴에서
홀수 차수 항의 정적분은 <span class="m">0</span>이고,
짝수 차수 항은 <span class="m">2∫<sub>0</sub><sup>a</sup></span>가 된다.
계산이 짧아지는 만큼 실수도 줄어든다.
