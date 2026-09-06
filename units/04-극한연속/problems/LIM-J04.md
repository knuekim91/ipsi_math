---
id: LIM-J04
unit: 04-극한연속
topic: 그래프에서 좌우극한
level: 3점
difficulty: 하
source: 2027-06모평 4번
exam: 2027-06모평
origin: 기출
core: "한쪽 극한은 그 점의 함숫값이 아니라 다가가는 값이다"
tags: [좌극한,우극한,그래프]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>함수 <span class="m">y = f(x)</span>의 그래프가 그림과 같다. (<span class="m">x = −1</span>에서 왼쪽 가지는 <span class="m">−1</span>로, <span class="m">x = 1</span>에서 오른쪽 가지는 <span class="m">1</span>로 다가간다.)</p><p class="m">lim<sub>x→−1<sup>−</sup></sub> f(x) + lim<sub>x→1<sup>+</sup></sub> f(x)</p><p>의 값은?</p><div class="choices"><span>① −2</span><span>② −1</span><span>③ 0</span><span>④ 1</span><span>⑤ 2</span></div>

## 발상

<b>속이 빈 점(○)은 그 값을 취하지 않지만, 다가가는 값은 바로 그 자리</b>다. 채워진 점(●)에 속지 말 것.

## 풀이

<p><span class="step">① 한쪽 극한이 무엇을 묻는지 확인한다.</span>
<span class="m">lim<sub>x→a<sup>−</sup></sub>f(x)</span>는
<b><span class="m">x = a</span>를 빼고 왼쪽에서만 다가갈 때 <span class="m">y</span>가 어디로 향하는가</b>를 묻는다.
그 점의 <b>함숫값과는 상관이 없다.</b>
그래프에서 <b>속이 빈 점(○)</b>은 그 값을 취하지 않는다는 표시일 뿐,
<b>다가가는 값은 바로 그 자리</b>다.</p>

<p><span class="step">② 왼쪽에서 −1로 다가갈 때를 읽는다.</span>
<span class="m">x = −1</span>의 왼쪽 가지를 손가락으로 따라간다.
그 가지는 내려오는 직선이고 <span class="m">x = −1</span>에 이르렀을 때 <span class="m">y</span>는 <span class="m">−1</span>에 닿는다.</p>
<p class="m">lim<sub>x→−1<sup>−</sup></sub>f(x) = −1</p>

<p><span class="step">③ 오른쪽에서 1로 다가갈 때를 읽는다.</span>
<span class="m">x = 1</span>의 오른쪽 가지를 따라간다.
그 가지는 <span class="m">y = 1</span>에서 시작해 내려간다.</p>
<p class="m">lim<sub>x→1<sup>+</sup></sub>f(x) = 1</p>

<p><span class="step">④ 두 값을 더한다.</span></p>
<p class="m">(−1) + 1 = 0</p>
<p class="m">답 ③</p>

## 노하우

<b>한쪽 극한은 &lsquo;그 점을 빼고&rsquo; 다가가는 값이다.</b> 그래프 문제에서는 채워진 점(함숫값)과 빈 점(극한값)을 손가락으로 짚어 구분하면 실수가 사라진다.
