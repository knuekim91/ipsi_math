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

<p>함수 <span class="m">y = f(x)</span>의 그래프가 그림과 같다.</p>
<div class="fig">
<svg viewBox="0 0 330 240" role="img" aria-label="y = f(x)의 그래프. x = −1에서 왼쪽 가지는 −1로, x = 1에서 오른쪽 가지는 1로 다가간다.">
  <!-- 안내선 -->
  <path class="gd" d="M105 66 H150 M105 192 H150 M105 66 V192 M195 108 V150"/>
  <!-- 축 -->
  <path class="ax" d="M28 150 H305 M150 226 V38"/>
  <path class="ax" d="M305 150 l-6 -3.5 v7 z" fill="currentColor"/>
  <path class="ax" d="M150 38 l-3.5 6 h7 z" fill="currentColor"/>
  <!-- 왼쪽 가지 : 내려오는 직선, (−1, −1) 에서 끝난다 -->
  <path class="cv" d="M42 112 L105 192"/>
  <!-- 가운데 곡선 : (−1, 2) 에서 (1, 0) 까지 -->
  <path class="cv" d="M105 66 C145 66 155 150 195 150"/>
  <!-- 오른쪽 가지 : (1, 1) 에서 시작해 내려간다 -->
  <path class="cv" d="M195 108 L288 195"/>
  <!-- 점 -->
  <circle class="po" cx="105" cy="66"  r="4.2"/>
  <circle class="pt" cx="105" cy="108" r="4.2"/>
  <circle class="po" cx="105" cy="192" r="4.2"/>
  <circle class="po" cx="195" cy="108" r="4.2"/>
  <circle class="pt" cx="195" cy="150" r="4.2"/>
  <!-- 눈금 글자 -->
  <text x="56"  y="168" text-anchor="middle">−2</text>
  <text x="101" y="168" text-anchor="middle">−1</text>
  <text x="141" y="168" text-anchor="end">O</text>
  <text x="195" y="168" text-anchor="middle">1</text>
  <text x="240" y="168" text-anchor="middle">2</text>
  <text x="143" y="70"  text-anchor="end">2</text>
  <text x="143" y="112" text-anchor="end">1</text>
  <text x="143" y="197" text-anchor="end">−1</text>
  <text class="v" x="313" y="146" text-anchor="middle">x</text>
  <text class="v" x="158" y="46">y</text>
  <text class="v" x="243" y="100">y = f(x)</text>
</svg>
</div><p class="m">lim<sub>x→−1<sup>−</sup></sub> f(x) + lim<sub>x→1<sup>+</sup></sub> f(x)</p><p>의 값은?</p><div class="choices"><span>① −2</span><span>② −1</span><span>③ 0</span><span>④ 1</span><span>⑤ 2</span></div>

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
그림에서 <span class="m">x = −1</span>의 <b>왼쪽</b> 가지를 따라간다. 그 가지는 내려오는 직선이고, <span class="m">x = −1</span>에 이르렀을 때 <b>빈 점 <span class="m">(−1, −1)</span></b>에 닿는다.<br><span class="m">x = −1</span>에는 채운 점 <span class="m">(−1, 1)</span>도 있지만 그것은 <b>함숫값 <span class="m">f(−1) = 1</span></b>일 뿐, 왼쪽에서 다가가는 값과는 상관이 없다.</p>
<p class="m">lim<sub>x→−1<sup>−</sup></sub>f(x) = −1</p>

<p><span class="step">③ 오른쪽에서 1로 다가갈 때를 읽는다.</span>
그림에서 <span class="m">x = 1</span>의 <b>오른쪽</b> 가지를 따라간다. 그 가지는 <b>빈 점 <span class="m">(1, 1)</span></b>에서 시작해 내려간다.<br>여기서도 채운 점 <span class="m">(1, 0)</span>은 함숫값 <span class="m">f(1) = 0</span>일 뿐이므로 쓰지 않는다.</p>
<p class="m">lim<sub>x→1<sup>+</sup></sub>f(x) = 1</p>

<p><span class="step">④ 두 값을 더한다.</span></p>
<p class="m">(−1) + 1 = 0</p>
<p class="m">답 ③</p>

## 노하우

<b>한쪽 극한은 &lsquo;그 점을 빼고&rsquo; 다가가는 값이다.</b> 그래프 문제에서는 채워진 점(함숫값)과 빈 점(극한값)을 손가락으로 짚어 구분하면 실수가 사라진다.
