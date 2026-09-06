---
id: LIM-J11
unit: 04-극한연속
topic: 극한의 존재와 비존재
level: 4점
difficulty: 상
source: 2027-06모평 11번
exam: 2027-06모평
origin: 기출
core: "존재하면 분자도 0, 존재하지 않으면 분자는 0이 아니다 — 두 조건이 각각 식을 준다"
tags: [극한존재,비존재,일차함수]
status: seed
added: 2026-09-06
answer: ①
---

## 문제

<p>일차함수 <span class="m">f(x)</span>에 대하여</p><p class="m">lim<sub>x→a</sub> f(x+2) / (x(f(x) − 3))</p><p>의 값이 <span class="m">a = 0</span>일 때 존재하고 <span class="m">a = 3</span>일 때 존재하지 않는다. <span class="m">f(4)</span>의 값은?</p><div class="choices"><span>① 6</span><span>② 7</span><span>③ 8</span><span>④ 9</span><span>⑤ 10</span></div>

## 발상

분모 <span class='m'>x(f(x)−3)</span>은 <span class='m'>x = 0</span>에서 항상 0이다. <b>0에서 존재한다 → 분자도 0</b>, <b>3에서 존재하지 않는다 → 분모는 0인데 분자는 0이 아니다.</b> 두 문장이 각각 식 하나씩을 준다.

## 풀이

<p><span class="step">① 분모가 언제 0이 되는지 본다.</span>
분모는 <span class="m">x(f(x) − 3)</span>이다.
<b><span class="m">x = 0</span>을 넣으면 앞의 <span class="m">x</span> 때문에 무조건 0</b>이 된다.
즉 <span class="m">a = 0</span>에서는 분모가 반드시 0이다.</p>

<p><span class="step">② &lsquo;a = 0에서 존재한다&rsquo;를 식으로 바꾼다.</span>
분모가 0으로 가는데 극한이 존재하려면
<b>분자도 함께 0으로 가야</b> 한다. 그러지 않으면 값이 무한히 커진다.
분자는 <span class="m">f(x + 2)</span>이고 <span class="m">x → 0</span>이면 <span class="m">f(2)</span>가 되므로</p>
<p class="m">f(2) = 0 &nbsp;&nbsp; … ㉠</p>

<p><span class="step">③ &lsquo;a = 3에서 존재하지 않는다&rsquo;도 식으로 바꾼다.</span>
<b>&lsquo;존재하지 않는다&rsquo;도 버리는 말이 아니라 정보다.</b>
<span class="m">x = 3</span>에서 극한이 없으려면
<b>분모는 0인데 분자는 0이 아니어야</b> 한다.
분모에 <span class="m">x = 3</span>을 넣으면</p>
<p class="m">3 × (f(3) − 3) = 0</p>
<p><span class="m">3 ≠ 0</span>이므로 괄호 안이 0이어야 한다.</p>
<p class="m">f(3) = 3 &nbsp;&nbsp; … ㉡</p>

<p><span class="step">④ 일차함수를 결정한다.</span>
일차함수는 <b>두 점이면 정해진다.</b>
㉠과 ㉡에서 <span class="m">(2, 0)</span>과 <span class="m">(3, 3)</span>을 지난다.</p>
<p class="m">기울기 = (3 − 0)/(3 − 2) = 3</p>
<p class="m">f(x) = 3(x − 2) = 3x − 6</p>

<p><span class="step">⑤ 정말 조건을 만족하는지 확인한다.</span>
분모와 분자를 실제로 써 본다.</p>
<p class="m">분모 = x(3x − 6 − 3) = x(3x − 9) = 3x(x − 3)</p>
<p class="m">분자 = f(x + 2) = 3(x + 2) − 6 = 3x</p>
<p><span class="m">a = 0</span>일 때 : 분자와 분모의 <span class="m">3x</span>가 약분된다.</p>
<p class="m">3x / (3x(x − 3)) = 1/(x − 3) → x → 0이면 −1/3 (극한 존재 ✓)</p>
<p><span class="m">a = 3</span>일 때 : 분자는 <span class="m">9</span>로 0이 아니고 분모는 0이다. (극한 없음 ✓)</p>

<p><span class="step">⑥ 답을 계산한다.</span></p>
<p class="m">f(4) = 3 × 4 − 6 = 6</p>
<p class="m">답 ①</p>

## 함정

&lsquo;존재하지 않는다&rsquo;는 조건도 <b>정보</b>다. 그냥 버리면 미지수를 다 못 정한다. 분모가 그 점에서 0이 되어야 한다는 뜻으로 읽는다.

## 노하우

<b>분수 극한에서 &lsquo;존재&rsquo;와 &lsquo;비존재&rsquo;는 둘 다 방정식이다.</b> 존재 → (분모 0인 곳에서) 분자도 0. 비존재 → 분모는 0, 분자는 0이 아님. 일차함수처럼 미지수가 둘이면 조건도 두 개가 필요하고, 문제는 정확히 두 개를 준다.
