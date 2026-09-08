---
id: DIF-C13-T3
parent: DIF-C13
unit: 05-미분
topic: b는 마음대로 정할 수 없다
level: 3점
difficulty: 중
source: 사다리 3단 (DIF-C13 에서 b 가 정해지는 이유)
origin: 사다리
core: "f(x+a) = f(x) + b 에 x = 0을 넣으면 b = f(a) − f(0) 이므로, b는 주어진 구간의 양 끝값이 정한다"
tags: [함수방정식,대입,평행이동]
status: variant
added: 2026-09-08
answer: 23
---

## 문제

<p>함수 <span class="m">f(x)</span>가
<span class="m">0 ≤ x ≤ 3</span>에서
<span class="m">f(x) = x<sup>2</sup> + 1</span>이고,
상수 <span class="m">b</span>에 대하여 모든 실수 <span class="m">x</span>에 대하여</p>
<p class="m">f(x + 3) = f(x) + b</p>
<p>를 만족시킬 때, <span class="m">f(8)</span>의 값을 구하시오.</p>

## 발상

<b>이 문제에는 <span class="m">b</span>의 값이 주어져 있지 않다.
그런데도 답이 하나로 정해진다.</b>
<span class="m">b</span>가 아무 값이나 될 수 없다는 뜻이다.<br><br>

<b>왜 그런지는 식에 <span class="m">x = 0</span>을 넣어 보면 바로 보인다.</b></p>
<p class="m">f(0 + 3) = f(0) + b → f(3) = f(0) + b</p>
<p><span class="m">0</span>과 <span class="m">3</span>은 <b>둘 다</b>
함수식이 주어진 구간 <span class="m">0 ≤ x ≤ 3</span>의 안에 있다.
그러므로 <span class="m">f(3)</span>과 <span class="m">f(0)</span>을
모두 계산할 수 있고, <span class="m">b</span>가 저절로 정해진다.</p>
<p class="m">b = f(3) − f(0)</p>
<p><b><span class="m">b</span>는 &lsquo;한 칸의 높이 차&rsquo;다.</b>
그래프를 계단처럼 그려 보면, 한 칸의 시작과 끝의 높이 차가 곧
<span class="m">b</span>다. 이것을 구하고 나면 나머지는 1단과 같다.

## 풀이

<p><span class="step">① 구간의 양 끝값을 구한다.</span>
<span class="m">0 ≤ x ≤ 3</span>에서
<span class="m">f(x) = x<sup>2</sup> + 1</span>이므로
양 끝인 <span class="m">x = 0</span>과 <span class="m">x = 3</span>에서의
값을 계산한다.</p>
<p class="m">f(0) = 0<sup>2</sup> + 1 = 1</p>
<p class="m">f(3) = 3<sup>2</sup> + 1 = 10</p>

<p><span class="step">② b를 구한다.</span>
주어진 식 <span class="m">f(x + 3) = f(x) + b</span>에
<span class="m">x = 0</span>을 대입한다.</p>
<p class="m">f(3) = f(0) + b</p>
<p>①에서 구한 값을 넣는다.</p>
<p class="m">10 = 1 + b → b = 9</p>
<p>따라서 주어진 조건은 다음과 같다.</p>
<p class="m">f(x + 3) = f(x) + 9</p>

<p><span class="step">③ f(8)을 아는 구간으로 끌고 온다.</span>
<span class="m">8</span>에서 <span class="m">3</span>씩 빼 내려간다.
<span class="m">8 − 3 = 5</span>, <span class="m">5 − 3 = 2</span>이고
<span class="m">2</span>는 구간 <span class="m">0 ≤ x ≤ 3</span> 안에 있다.
곧 <span class="m">8 = 2 + 3 × 2</span>이므로
<span class="m">3</span>칸을 두 번 간 것이다.</p>
<p class="m">f(8) = f(5) + 9 = (f(2) + 9) + 9 = f(2) + 18</p>

<p><span class="step">④ 값을 넣어 마무리한다.</span>
<span class="m">2</span>는 구간 안에 있으므로 주어진 식을 쓴다.</p>
<p class="m">f(2) = 2<sup>2</sup> + 1 = 5</p>
<p class="m">f(8) = 5 + 18 = 23</p>
<p class="m">답 23</p>

## 함정

<b><span class="m">b</span>를 모른다고 손을 놓으면 안 된다.</b>
<span class="m">b</span>가 문자로만 주어져 있어도,
<span class="m">x = 0</span>을 대입하면 <b>아는 값 두 개의 차</b>로 정해진다.
<b>함수방정식에서 가장 먼저 해 볼 일은 &lsquo;쉬운 수를 대입해 보는 것&rsquo;</b>이다.<br><br>

<b>상수항 <span class="m">1</span>을 빠뜨리면 안 된다.</b>
<span class="m">f(x) = x<sup>2</sup> + 1</span>이므로
<span class="m">f(0) = 0</span>이 아니라 <span class="m">1</span>이다.
<span class="m">f(0) = 0</span>으로 잘못 보면
<span class="m">b = 10</span>이 되어 답이 <span class="m">25</span>가 된다.
<b><span class="m">f(0)</span>이 <span class="m">0</span>일 것이라고 넘겨짚지 않는다.</b><br><br>

<b>몇 칸을 갔는지 잘못 세기 쉽다.</b>
<span class="m">8</span>에서 <span class="m">2</span>까지는
<span class="m">3</span>씩 <b>두 번</b> 뺀 것이므로
<span class="m">9</span>를 두 번 더한다.
불안하면 <span class="m">f(8) = f(5) + 9</span>,
<span class="m">f(5) = f(2) + 9</span>처럼 <b>한 줄씩 나누어 적는다.</b>

## 노하우

<b><span class="m">f(x + a) = f(x) + b</span>에서
<span class="m">b</span>는 항상 <span class="m">f(a) − f(0)</span>이다.</b>
<span class="m">x = 0</span>을 넣기만 하면 나온다.
그러므로 <b>문제가 <span class="m">b</span>를 주지 않아도 걱정할 것이 없다.</b>
거꾸로, 문제가 <span class="m">b</span>를 주었다면
그것은 <span class="m">f(a) − f(0)</span>과 반드시 같아야 하므로
<b>다른 미지수를 정하는 데 쓰인다.</b><br><br>

<b>함수방정식은 대입해 볼 수를 고르는 것이 요령이다.</b>
<span class="m">x = 0</span>을 먼저 넣어 보고,
그다음 <span class="m">x = a</span>, <span class="m">x = −a</span>를 넣어 본다.
<b>주어진 함수식을 쓸 수 있는 구간 안으로 들어오는 수</b>를 고르는 것이 핵심이다.<br><br>

<b>계단 그림을 그려 두면 실수가 줄어든다.</b>
가로로 <span class="m">a</span>, 세로로 <span class="m">b</span>인 칸을
비스듬히 쌓아 올린 모양이다.
<span class="m">f(8)</span>을 구하려면 그 칸을 몇 개 내려와야 하는지
그림에서 세면 된다.
