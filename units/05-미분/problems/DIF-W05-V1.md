---
id: DIF-W05-V1
parent: DIF-W05
unit: 05-미분
topic: 같은 함숫값을 갖는 두 점의 곱의 최솟값
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W05 변형 · 관계식으로 최솟값 구하기)
origin: 유사문항
core: "x₁x₂ = s² + as + b 로 바꾸면 곱의 최솟값이 s에 대한 이차함수의 최솟값이 된다. 그래프로는 보이지 않는 것을 식이 보여 준다"
tags: [삼차함수,같은함숫값,대칭식,이차함수최솟값,판별식]
status: variant
added: 2026-10-17
answer: ③
---

## 문제

<p>삼차함수 <span class="m">f(x) = x<sup>3</sup> − 4x<sup>2</sup> + 10</span>에 대하여
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>,
<span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>를 만족시키는 두 실수
<span class="m">x<sub>1</sub></span>, <span class="m">x<sub>2</sub></span>에 대하여
<span class="m">x<sub>1</sub>x<sub>2</sub></span>의 최솟값은?</p>

<div class="choices"><span>① −6</span><span>② −5</span><span>③ −4</span>
<span>④ −3</span><span>⑤ −2</span></div>

## 발상

<b>이 문제는 그래프로 손도 못 댄다.</b>
개형을 그려 봐야 <span class="m">x<sub>1</sub>x<sub>2</sub></span>라는
<b>두 수의 곱</b>은 그림 위에 나타나지 않는다.
<b>부등식의 성립 여부를 묻는 것이 아니라 곱의 값 자체를 묻고 있으므로,
식으로 바꿔야 한다.</b><br><br>

모문항에서 세운 관계식을 그대로 쓴다.</p>
<p class="m">x<sub>1</sub>x<sub>2</sub> = (x<sub>1</sub> + x<sub>2</sub>)<sup>2</sup> + a(x<sub>1</sub> + x<sub>2</sub>) + b</p>
<p><b>곱이 합의 이차식으로 바뀐다.</b>
그러면 <span class="m">s = x<sub>1</sub> + x<sub>2</sub></span> 하나만 변수로 두고
<b>이차함수의 최솟값</b>을 구하는 문제가 된다.<br><br>

<b>단, <span class="m">s</span>는 아무 값이나 될 수 없다.</b>
<span class="m">x<sub>1</sub></span>, <span class="m">x<sub>2</sub></span>가
<b>실수</b>여야 하므로 판별식 조건이 붙는다.
<b>그 범위를 먼저 구하고, 그 안에서 최솟값을 찾는다.</b>
이것이 이 유형의 전부다.

## 풀이

<p><span class="step">① 관계식을 세운다.</span>
<span class="m">f(x<sub>1</sub>) − f(x<sub>2</sub>) = 0</span>을 인수분해한다.</p>
<p class="m">(x<sub>1</sub><sup>3</sup> − x<sub>2</sub><sup>3</sup>) − 4(x<sub>1</sub><sup>2</sup> − x<sub>2</sub><sup>2</sup>) = 0</p>
<p class="m">(x<sub>1</sub> − x<sub>2</sub>){(x<sub>1</sub><sup>2</sup> + x<sub>1</sub>x<sub>2</sub> + x<sub>2</sub><sup>2</sup>) − 4(x<sub>1</sub> + x<sub>2</sub>)} = 0</p>
<p><span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>이므로 뒤 괄호가
<span class="m">0</span>이다.
<span class="m">s = x<sub>1</sub> + x<sub>2</sub></span>,
<span class="m">p = x<sub>1</sub>x<sub>2</sub></span>로 놓으면
<span class="m">x<sub>1</sub><sup>2</sup> + x<sub>1</sub>x<sub>2</sub> + x<sub>2</sub><sup>2</sup> = s<sup>2</sup> − p</span>이므로</p>
<p class="m">s<sup>2</sup> − p − 4s = 0 → p = s<sup>2</sup> − 4s</p>

<p><span class="step">② s의 범위를 판별식으로 구한다.</span>
<span class="m">x<sub>1</sub></span>, <span class="m">x<sub>2</sub></span>는
<span class="m">t<sup>2</sup> − st + p = 0</span>의 서로 다른 두 실근이므로</p>
<p class="m">s<sup>2</sup> − 4p &gt; 0</p>
<p class="m">s<sup>2</sup> − 4(s<sup>2</sup> − 4s) = −3s<sup>2</sup> + 16s &gt; 0</p>
<p class="m">s(3s − 16) &lt; 0 → 0 &lt; s &lt; 16/3</p>

<p><span class="step">③ 이차함수의 최솟값을 구한다.</span></p>
<p class="m">p = s<sup>2</sup> − 4s = (s − 2)<sup>2</sup> − 4</p>
<p><span class="m">s = 2</span>는 <span class="m">0 &lt; s &lt; 16/3</span> 안에 있으므로
꼭짓점에서 최솟값을 얻는다.</p>
<p class="m">최솟값 = −4</p>
<p class="m">답 ③</p>

<p><span class="step">④ 확인한다.</span>
<span class="m">s = 2</span>, <span class="m">p = −4</span>이면
<span class="m">t<sup>2</sup> − 2t − 4 = 0</span>에서
<span class="m">t = 1 ± √5</span>이다.</p>
<p class="m">x<sub>1</sub> = 1 − √5, &nbsp; x<sub>2</sub> = 1 + √5</p>
<p class="m">x<sub>1</sub>x<sub>2</sub> = 1 − 5 = −4</p>
<p>두 값을 <span class="m">f</span>에 넣어 보면 함숫값이 같다.</p>

## 함정

<b>판별식을 빼먹으면 틀린다.</b>
<span class="m">p = s<sup>2</sup> − 4s</span>만 보고
&lsquo;이차함수니까 꼭짓점&rsquo;이라고 바로 답하면 이번에는 맞지만,
<b>꼭짓점이 범위 밖에 있는 문제에서는 통째로 틀린다.</b>
<span class="m">s</span>의 범위를 먼저 적는 습관을 들인다.<br><br>

<b>등호에 주의한다.</b>
<span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>이므로 판별식은
<span class="m">&gt; 0</span>이고 범위도 <b>열린 구간</b>이다.
<span class="m">s = 0</span>이나 <span class="m">s = 16/3</span>은
두 점이 한 점으로 겹치는 경우여서 애초에 자격이 없다.<br><br>

<b>상수항 <span class="m">10</span>은 끝까지 쓰이지 않는다.</b>
관계식에 <span class="m">c</span>가 아예 들어오지 않기 때문이다.
<b><span class="m">10</span> 대신 <span class="m">999</span>를 넣어도 답은
<span class="m">−4</span>다.</b>
쓰이지 않는 수를 억지로 끼워 넣으려다 길을 잃지 않는다.

## 노하우

<b>&lsquo;곱&rsquo;이나 &lsquo;합&rsquo;을 물으면 관계식, &lsquo;부등식의 성립&rsquo;을 물으면 그래프다.</b>
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span> 문제를 만나면
<b>묻는 것이 무엇인지로 도구를 고른다.</b>
모문항처럼 &lsquo;임의의 두 실수에 대하여 ~이다&rsquo;는 그래프가 빠르고,
이 문항처럼 <span class="m">x<sub>1</sub>x<sub>2</sub></span>나
<span class="m">x<sub>1</sub> + x<sub>2</sub></span>의 값을 물으면 관계식뿐이다.<br><br>

<b>관계식 세 줄은 통째로 외워 둔다.</b></p>
<p class="m">① p = s<sup>2</sup> + as + b &nbsp; (f(x) = x<sup>3</sup> + ax<sup>2</sup> + bx + c)</p>
<p class="m">② 실근 조건 : 3s<sup>2</sup> + 4as + 4b &lt; 0</p>
<p class="m">③ 구하는 것을 s의 식으로 바꿔 범위 안에서 최대·최소</p>
<p><b>①을 유도하는 데 걸리는 시간이 아까우면 ②까지 외운다.</b>
②는 <span class="m">s<sup>2</sup> − 4p</span>에 ①을 대입해 정리한 것이다.<br><br>

<b>상수항은 관계식에 들어오지 않는다.</b>
그래프를 위아래로 평행이동해도 <b>같은 높이의 두 점은 그대로</b>이기 때문이다.
<b>상수항이 안 쓰이는 문제인지 미리 알면 계산이 훨씬 가볍다.</b>
