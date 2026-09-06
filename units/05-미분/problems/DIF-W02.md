---
id: DIF-W02
unit: 05-미분
topic: 절댓값 함수의 미분가능성
level: 4점
difficulty: 상
source: 2021 수능 나형 30번
exam: 2021-수능
origin: 오답노트
core: "h(0)=0이 f−g의 중근을 만들고, x=1의 좌우 연결이 일차함수 g를 결정한다"
tags: [미분가능성,절댓값,삼차함수,중근]
status: wrong
added: 2026-09-06
answer: 39
---

## 문제

<p>함수 <span class="m">f(x)</span>는 최고차항의 계수가 1인 삼차함수이고, 함수 <span class="m">g(x)</span>는 일차함수이다. 함수 <span class="m">h(x)</span>를</p><span class="cond m">h(x) = |f(x) − g(x)| &nbsp; (x &lt; 1)<br>h(x) = f(x) + g(x) &nbsp;&nbsp;&nbsp; (x ≥ 1)</span><p>이라 하자. 함수 <span class="m">h(x)</span>가 실수 전체의 집합에서 미분가능하고, <span class="m">h(0) = 0</span>, <span class="m">h(2) = 5</span>일 때, <span class="m">h(4)</span>의 값을 구하시오.</p>

## 발상

<b><span class='m'>p(x) = f(x) − g(x)</span>로 묶는 것이 첫 수순.</b> <span class='m'>p</span>는 최고차 1인 삼차함수다.<br><br><span class='m'>h(0)=0</span>은 <span class='m'>0 &lt; 1</span>이라 <span class='m'>|p(0)| = 0</span>, 곧 <b><span class='m'>p(0) = 0</span></b>이다. 그런데 <span class='m'>x &lt; 1</span>에서 <span class='m'>|p|</span>가 미분가능하려면 <b>거기의 근은 부호가 안 바뀌는 중근</b>이어야 한다. 따라서 <b><span class='m'>p(x) = x<sup>2</sup>(x − r)</span></b>이다. 미지수가 <span class='m'>r</span> 하나로 줄었다.<br><br>남은 것은 <span class='m'>x = 1</span>에서 좌우를 잇는 일뿐이다.

## 풀이

<p><span class="step">① 두 함수를 하나로 묶는다.</span>
<span class="m">h</span>의 두 조각에는 <span class="m">f − g</span>와 <span class="m">f + g</span>가 각각 들어 있다.
<b>차를 한 덩어리로 묶으면</b> 합도 그 덩어리로 표현된다.</p>
<p class="m">p(x) = f(x) − g(x)</p>
<p><span class="m">f</span>는 최고차항의 계수가 <span class="m">1</span>인 삼차함수이고
<span class="m">g</span>는 일차함수이므로,
<b><span class="m">p</span>도 최고차항의 계수가 <span class="m">1</span>인 삼차함수</b>다.
그리고 <span class="m">f = p + g</span>이므로</p>
<p class="m">f + g = (p + g) + g = p + 2g</p>
<p>이제 미지수는 <span class="m">p</span>와 <span class="m">g</span> 둘뿐이다.</p>

<p><span class="step">② h(0) = 0에서 p의 근을 찾는다.</span>
<span class="m">0 &lt; 1</span>이므로 <span class="m">h(0)</span>은 위쪽 식을 쓴다.</p>
<p class="m">h(0) = |f(0) − g(0)| = |p(0)| = 0 → p(0) = 0</p>
<p>즉 <span class="m">x = 0</span>은 <span class="m">p</span>의 근이다.</p>

<p><span class="step">③ 그 근이 중근이어야 하는 이유를 확인한다.</span>
<span class="m">x &lt; 1</span>에서 <span class="m">h = |p|</span>인데,
<b>절댓값 함수는 안쪽이 부호를 바꾸는 곳에서 뾰족하게 꺾인다.</b>
<span class="m">h</span>가 모든 실수에서 미분가능해야 하므로
<span class="m">x = 0</span>에서 <span class="m">p</span>가 부호를 바꾸면 안 된다.
<b>근이면서 부호가 바뀌지 않으려면 중근</b>이어야 한다.</p>
<p>최고차항의 계수가 <span class="m">1</span>인 삼차함수이므로 나머지 근 하나를 <span class="m">r</span>이라 하면</p>
<p class="m">p(x) = x<sup>2</sup>(x − r)</p>
<p><b>미지수가 <span class="m">r</span> 하나로 줄었다.</b></p>

<p><span class="step">④ x = 1에서 좌우를 이을 준비를 한다.</span>
남은 것은 두 조각이 만나는 <span class="m">x = 1</span>이다.
연속과 미분, 두 조건을 쓴다.
그런데 왼쪽에서 <span class="m">|p|</span>가 <span class="m">p</span>인지 <span class="m">−p</span>인지는
<span class="m">p(1)</span>의 부호에 달려 있으므로 <b>경우를 나눠야</b> 한다.</p>

<p><span class="step">⑤ p(1) &gt; 0 인 경우를 확인한다.</span>
이때 <span class="m">x = 1</span>의 왼쪽 근처에서 <span class="m">|p| = p</span>이다.</p>
<p class="m">연속 : p(1) = p(1) + 2g(1) → 0 = 2g(1) → g(1) = 0</p>
<p class="m">미분 : p′(1) = p′(1) + 2g′(1) → 0 = 2g′(1) → g′(1) = 0</p>
<p>그런데 <span class="m">g</span>는 <b>일차함수</b>다.
일차함수의 기울기는 <span class="m">0</span>이 될 수 없다
(<span class="m">0</span>이면 상수함수라 일차함수가 아니다).
<b>모순이므로 이 경우는 없다.</b></p>

<p><span class="step">⑥ p(1) ≤ 0 인 경우로 확정한다.</span>
<span class="m">p(x) = x<sup>2</sup>(x − r)</span>이므로
<span class="m">p(1) = 1 − r ≤ 0</span>, 곧 <span class="m">r ≥ 1</span>이다.
이때 <span class="m">0 &lt; x &lt; 1</span>에서도 <span class="m">x − r &lt; 0</span>이라
<span class="m">p</span>가 계속 음수이므로 <span class="m">|p| = −p</span>다.</p>
<p class="m">연속 : −p(1) = p(1) + 2g(1)</p>
<p><span class="m">p(1)</span>을 왼쪽으로 넘긴다.</p>
<p class="m">−2p(1) = 2g(1) → g(1) = −p(1) = −(1 − r) = r − 1</p>
<p class="m">미분 : −p′(1) = p′(1) + 2g′(1)</p>
<p><span class="m">p′(x) = 3x<sup>2</sup> − 2rx</span>이므로 <span class="m">p′(1) = 3 − 2r</span>이고,
같은 방식으로 정리하면</p>
<p class="m">g′(1) = −p′(1) = −(3 − 2r) = 2r − 3</p>
<p>일차함수는 기울기와 한 점이면 정해지므로</p>
<p class="m">g(x) = (2r − 3)(x − 1) + (r − 1) &nbsp; (단 2r − 3 ≠ 0)</p>

<p><span class="step">⑦ h(2) = 5로 r을 구한다.</span>
<span class="m">2 ≥ 1</span>이므로 아래쪽 식 <span class="m">h = p + 2g</span>를 쓴다.</p>
<p class="m">p(2) = 4(2 − r) = 8 − 4r</p>
<p class="m">g(2) = (2r − 3)(2 − 1) + (r − 1) = 2r − 3 + r − 1 = 3r − 4</p>
<p class="m">h(2) = (8 − 4r) + 2(3r − 4) = 8 − 4r + 6r − 8 = 2r</p>
<p><b>깔끔하게 <span class="m">2r</span>만 남는다.</b></p>
<p class="m">2r = 5 → r = 5/2</p>
<p><span class="m">r = 5/2 ≥ 1</span>이고 <span class="m">2r − 3 = 2 ≠ 0</span>이므로 조건에 모두 맞는다.</p>

<p><span class="step">⑧ h(4)를 계산한다.</span></p>
<p class="m">p(4) = 16(4 − r) = 64 − 16r</p>
<p class="m">g(4) = (2r − 3)(4 − 1) + (r − 1) = 3(2r − 3) + r − 1 = 7r − 10</p>
<p class="m">h(4) = (64 − 16r) + 2(7r − 10) = 64 − 16r + 14r − 20 = 44 − 2r</p>
<p class="m">h(4) = 44 − 2 × (5/2) = 44 − 5 = 39</p>

<p><span class="step">⑨ 검산한다.</span>
<span class="m">r = 5/2</span>를 넣으면</p>
<p class="m">p(x) = x<sup>2</sup>(x − 5/2), &nbsp; g(x) = 2x − 1/2, &nbsp; f(x) = x<sup>3</sup> − (5/2)x<sup>2</sup> + 2x − 1/2</p>
<p class="m">x = 1 좌 : −p(1) = −(1 − 5/2) = 3/2 &nbsp;/&nbsp; 우 : f(1) + g(1) = 0 + 3/2 = 3/2 ✓</p>
<p class="m">x = 1 좌 : −p′(1) = −(3 − 5) = 2 &nbsp;/&nbsp; 우 : f′(1) + g′(1) = 0 + 2 = 2 ✓</p>
<p class="m">답 39</p>

## 함정

<b><span class='m'>p(1) &gt; 0</span> 갈래를 그냥 넘어가면 안 된다.</b> 그 갈래가 죽는 이유는 &lsquo;<span class='m'>g′(1) = 0</span>인데 <span class='m'>g</span>는 일차함수&rsquo;라는 것뿐이다. <b>&lsquo;일차함수&rsquo;라는 말에 &lsquo;기울기 ≠ 0&rsquo;이 숨어 있다</b>는 걸 놓치면 부호를 못 정하고 헤맨다.<br><br>또 <span class='m'>x &lt; 1</span> 구간의 미분가능성을 <span class='m'>x = 1</span>에서의 연결만 확인하고 끝내면 안 된다. <b>구간 <b>안쪽</b>에서 <span class='m'>|p|</span>가 꺾이지 않을 조건(중근)</b>이 이 문제의 절반이다.

## 노하우

<b><span class='m'>|F(x)|</span>가 미분가능 ⟺ <span class='m'>F</span>가 그 점에서 부호를 바꾸지 않는다 ⟺ 근이라면 중근.</b> 절댓값이 씌워진 다항함수가 나오면 이 문장부터 쓴다.<br><br>그리고 <b>두 함수의 차 <span class='m'>f−g</span>와 합 <span class='m'>f+g</span>가 같이 나오면 <span class='m'>p = f−g</span> 하나로 묶는다.</b> 합은 <span class='m'>f+g = p + 2g</span>로 다시 쓸 수 있어 미지수가 <span class='m'>p</span>와 <span class='m'>g</span> 둘로 정리된다. 여기서 <span class='m'>g</span>는 일차함수라 값·기울기 두 개면 완전히 결정되고, 그 두 개를 <span class='m'>x=1</span>의 연속·미분 조건이 정확히 하나씩 준다.
