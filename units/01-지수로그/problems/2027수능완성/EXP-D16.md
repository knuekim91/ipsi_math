---
id: EXP-D16
unit: 01-지수로그
topic: 밑이 다른 로그방정식
level: 3점
difficulty: 하
source: 2027 수능완성 실전 모의고사 2회 16번
exam: 2027-수능완성
origin: 기출
core: "밑을 3으로 통일한 뒤 진수를 비교하고, 마지막에 진수조건으로 근을 거른다"
tags: [로그방정식,밑변환,진수조건]
status: seed
added: 2026-09-07
answer: 3
---

## 문제

<p>방정식</p>
<p class="m">log<sub>3</sub>(x − 2) = log<sub>9</sub>(−2x + 7)</p>
<p>을 만족시키는 실수 <span class="m">x</span>의 값을 구하시오.</p>

## 발상

<b>밑이 다르면 로그끼리 비교할 수 없다. 먼저 밑을 맞춘다.</b>
왼쪽은 밑이 <span class="m">3</span>이고 오른쪽은 밑이
<span class="m">9 = 3<sup>2</sup></span>이다.
밑이 제곱 관계이므로 밑변환공식을 쓰면 오른쪽이
<span class="m">1/2</span>배가 되어 깔끔하게 정리된다.<br><br>

<b>로그방정식에서는 진수조건을 반드시 마지막에 확인한다.</b>
방정식을 풀면 이차방정식이 되어 근이 두 개 나오는데,
그중 하나는 진수를 <span class="m">0</span> 이하로 만들어 버린다.
<b>진수조건은 문제를 풀기 전에 미리 적어 두는 것이 안전하다.</b>

## 풀이

<p><span class="step">① 진수조건을 먼저 적어 둔다.</span>
로그의 진수는 양수여야 한다.
두 로그의 진수는 각각 <span class="m">x − 2</span>와
<span class="m">−2x + 7</span>이다.</p>
<p class="m">x − 2 &gt; 0 → x &gt; 2</p>
<p class="m">−2x + 7 &gt; 0 → x &lt; 7/2</p>
<p>따라서 <span class="m">x</span>는 다음 범위 안에 있어야 한다.</p>
<p class="m">2 &lt; x &lt; 7/2</p>

<p><span class="step">② 밑을 3으로 통일한다.</span>
<span class="m">9 = 3<sup>2</sup></span>이므로 밑변환공식을 쓴다.</p>
<p class="m">log<sub>9</sub>(−2x + 7) = log<sub>3</sub>(−2x + 7) / log<sub>3</sub>9</p>
<p class="m">= log<sub>3</sub>(−2x + 7) / 2</p>
<p>따라서 주어진 방정식은 다음과 같아진다.</p>
<p class="m">log<sub>3</sub>(x − 2) = (1/2) log<sub>3</sub>(−2x + 7)</p>

<p><span class="step">③ 계수를 없앤다.</span>
양변에 <span class="m">2</span>를 곱한 뒤, 좌변의 계수
<span class="m">2</span>를 진수의 지수로 올린다.</p>
<p class="m">2 log<sub>3</sub>(x − 2) = log<sub>3</sub>(−2x + 7)</p>
<p class="m">log<sub>3</sub>(x − 2)<sup>2</sup> = log<sub>3</sub>(−2x + 7)</p>

<p><span class="step">④ 진수를 비교한다.</span>
밑이 같은 로그의 값이 같으므로 진수가 같다.</p>
<p class="m">(x − 2)<sup>2</sup> = −2x + 7</p>

<p><span class="step">⑤ 이차방정식을 푼다.</span>
좌변을 전개하고 우변의 항을 모두 좌변으로 옮긴다.</p>
<p class="m">x<sup>2</sup> − 4x + 4 = −2x + 7</p>
<p class="m">x<sup>2</sup> − 4x + 2x + 4 − 7 = 0</p>
<p class="m">x<sup>2</sup> − 2x − 3 = 0</p>
<p>곱해서 <span class="m">−3</span>, 더해서 <span class="m">−2</span>가 되는
두 수는 <span class="m">−3</span>과 <span class="m">1</span>이다.</p>
<p class="m">(x − 3)(x + 1) = 0 → x = 3 또는 x = −1</p>

<p><span class="step">⑥ 진수조건으로 거른다.</span>
①에서 <span class="m">2 &lt; x &lt; 7/2</span>이어야 한다.
<span class="m">x = −1</span>은 이 범위 밖이므로 버린다.
실제로 <span class="m">x = −1</span>을 넣으면
<span class="m">x − 2 = −3 &lt; 0</span>이 되어 로그가 정의되지 않는다.
<span class="m">x = 3</span>은 <span class="m">2 &lt; 3 &lt; 3.5</span>이므로 조건을 만족시킨다.</p>
<p class="m">x = 3</p>

<p><span class="step">⑦ 답을 확인한다.</span>
<span class="m">x = 3</span>을 원래 방정식에 넣어 본다.</p>
<p class="m">(좌변) = log<sub>3</sub>(3 − 2) = log<sub>3</sub>1 = 0</p>
<p class="m">(우변) = log<sub>9</sub>(−6 + 7) = log<sub>9</sub>1 = 0</p>
<p>양변이 같으므로 <span class="m">x = 3</span>이 맞다.</p>
<p class="m">답 3</p>

## 함정

<b><span class="m">x = −1</span>을 버리지 않으면 그대로 틀린다.</b>
이차방정식의 근이 두 개 나오면 반드시 진수조건과 대조해야 한다.
<span class="m">(x − 2)<sup>2</sup></span>은 제곱이라
<span class="m">x = −1</span>에서도 양수가 되지만,
원래 진수는 <span class="m">x − 2</span>이지
<span class="m">(x − 2)<sup>2</sup></span>이 아니다.
<b>제곱으로 만드는 순간 없던 근이 생긴다.</b><br><br>

<b><span class="m">log<sub>9</sub></span>를
<span class="m">log<sub>3</sub></span>의 <span class="m">2</span>배로 놓으면 반대다.</b>
밑이 커지면 로그값은 작아지므로
<span class="m">log<sub>9</sub>A = (1/2)log<sub>3</sub>A</span>이다.
밑변환공식 <span class="m">log<sub>a</sub>b = log<sub>c</sub>b / log<sub>c</sub>a</span>에서
분모가 <span class="m">log<sub>3</sub>9 = 2</span>가 된다는 것을 확인하고 넘어간다.

## 노하우

<b>밑이 <span class="m">a</span>와 <span class="m">a<sup>2</sup></span>이면
<span class="m">1/2</span>배 관계다.</b>
<span class="m">log<sub>a<sup>n</sup></sub>b = (1/n)log<sub>a</sub>b</span>는
자주 쓰이므로 밑변환공식을 매번 쓰지 않고 바로 적용할 수 있게 익혀 둔다.<br><br>

<b>로그방정식은 진수조건을 맨 처음에 적는다.</b>
푼 뒤에 확인하려면 잊어버리기 쉽다.
문제를 읽자마자 진수조건을 옆에 써 두면
마지막에 근을 거를 때 저절로 눈에 들어온다.<br><br>

<b>계수를 지수로 올릴 때 진수의 부호가 바뀔 수 있음을 기억한다.</b>
<span class="m">2 log<sub>3</sub>A = log<sub>3</sub>A<sup>2</sup></span>은
<span class="m">A &gt; 0</span>일 때만 같은 식이다.
이 변형 때문에 무연근이 생기므로, 진수조건 확인이 <b>선택이 아니라 필수</b>다.
