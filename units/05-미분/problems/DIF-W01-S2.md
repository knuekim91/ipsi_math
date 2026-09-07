---
id: DIF-W01-S2
unit: 05-미분
parent: DIF-W01
topic: 부등식으로 갈래를 죽이기
level: 3점
difficulty: 중
source: 사다리 2단 (DIF-W01 풀이 ②③)
origin: 사다리
core: "≤ 0 인 값은 1이 될 수 없으므로 그 갈래는 그 자리에서 죽는다"
tags: [평균변화율,부등식,경우나누기]
status: variant
added: 2026-09-07
answer: 풀이 참조
---

## 문제

<p><b>(1)</b> 함수 <span class="m">f(x)</span>에서 <span class="m">x</span>의 값이
<span class="m">3</span>에서 <span class="m">5</span>까지 변할 때의 평균변화율을
<span class="m">f(3)</span>, <span class="m">f(5)</span>로 나타내시오.</p>

<p><b>(2)</b> 그 평균변화율이 <b>양수가 아닐 때</b>,
<span class="m">f(3)</span>과 <span class="m">f(5)</span> 사이에 성립하는 부등식을 쓰시오.</p>

<p><b>(3)</b> 두 실수 <span class="m">A, B</span>가
<span class="m">A(B − 1) = 0</span>과 <span class="m">B ≤ 0</span>을 만족시킨다.
<span class="m">A</span>의 값을 구하시오.</p>

<p><b>(4)</b> 함수 <span class="m">f(x)</span>가
<span class="m">f(4)[f(5) − f(3) − 1] = 0</span>을 만족시키고,
<span class="m">x</span>의 값이 <span class="m">3</span>에서 <span class="m">5</span>까지 변할 때의
평균변화율이 양수가 아니다. <span class="m">f(4)</span>의 값을 구하시오.</p>

## 발상

곱이 <span class="m">0</span>이면 <b>둘 중 하나는 0</b>이다.
그런데 <b>부등식이 한쪽을 미리 죽여 놓으면 남은 쪽이 강제된다.</b>
그러니 부등식 조건은 답을 검산하는 도구가 아니라
<b>갈래를 쳐내는 칼</b>로 먼저 써야 한다.

## 풀이

<p><span class="step">(1) 평균변화율의 정의.</span>
<span class="m">x</span>가 <span class="m">a</span>에서 <span class="m">b</span>까지 변할 때의 평균변화율은
<b>y의 변화량을 x의 변화량으로 나눈 것</b>이다.</p>
<p class="m">(f(5) − f(3)) / (5 − 3) = (f(5) − f(3)) / 2</p>

<p><span class="step">(2) 양수가 아니다 = 0 이하다.</span>
&lsquo;양수가 아니다&rsquo;는 <span class="m">&gt; 0</span>이 아니라는 뜻이므로
<span class="m">≤ 0</span>이다. (<span class="m">0</span>도 포함한다.)</p>
<p class="m">(f(5) − f(3)) / 2 ≤ 0</p>
<p>양변에 <span class="m">2</span>를 곱한다. <b>2는 양수이므로 부등호 방향은 그대로다.</b></p>
<p class="m">f(5) − f(3) ≤ 0</p>

<p><span class="step">(3) 부등식이 한쪽을 죽인다.</span>
<span class="m">B ≤ 0</span>이므로 양변에서 <span class="m">1</span>을 빼면</p>
<p class="m">B − 1 ≤ −1</p>
<p>즉 <span class="m">B − 1</span>은 <b>항상 음수</b>라서 <span class="m">0</span>이 될 수 없다.
곱이 <span class="m">0</span>인데 뒤쪽이 <span class="m">0</span>이 아니므로 앞쪽이 <span class="m">0</span>이어야 한다.</p>
<p class="m">A = 0</p>

<p><span class="step">(4) 둘을 합친다.</span>
<span class="m">A = f(4)</span>, <span class="m">B = f(5) − f(3)</span>으로 놓으면
주어진 식은 정확히 <span class="m">A(B − 1) = 0</span> 꼴이다.
그리고 (2)에서 <span class="m">B ≤ 0</span>임을 이미 얻었다.
따라서 (3)이 그대로 적용된다.</p>
<p class="m">f(4) = 0</p>

<p><b>원래 문제에서는 이 논리를 두 번 쓴다.</b>
<span class="m">n = 4</span>에서 <span class="m">f(4) = 0</span>,
<span class="m">n = 5</span>에서 같은 이유로 <span class="m">f(5) = 0</span>이 나온다.</p>

## 노하우

<b>&lsquo;<span class="m">A × B = 0</span>&rsquo; 과 &lsquo;<span class="m">B ≤ 0</span>&rsquo; 이 함께 있으면
<span class="m">B</span>가 <span class="m">1</span>이 되는 갈래는 <b>읽는 순간 사망</b>이다.</b>
부등식 조건을 만나면 <b>맨 처음에 부등호로 바꿔 적어 두는 습관</b>이
경우의 수를 몇 배로 줄인다.<br><br>
또 하나. <b>&lsquo;양수가 아니다&rsquo;는 <span class="m">≤ 0</span>이지 <span class="m">&lt; 0</span>이 아니다.</b>
<span class="m">0</span>이 포함되는지 아닌지가 답을 가르는 문제가 많으니
말로 된 조건은 반드시 부등호로 옮겨 적는다.
