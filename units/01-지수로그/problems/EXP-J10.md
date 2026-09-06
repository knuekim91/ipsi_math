---
id: EXP-J10
unit: 01-지수로그
topic: 로그의 연립
level: 4점
difficulty: 중상
source: 2027-06모평 10번
exam: 2027-06모평
origin: 기출
core: "log₃로 통일해 두 미지수의 일차연립으로 바꾼다"
tags: [로그,밑변환,연립]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>두 양수 <span class="m">a, b</span>가</p><span class="cond m">log<sub>9</sub>a + log<sub>3</sub>b = 2, &nbsp; log<sub>3</sub>a = 8 log<sub>9</sub>b</span><p>를 만족시킬 때, <span class="m">a/b</span>의 값은?</p><div class="choices"><span>① 1</span><span>② 3</span><span>③ 9</span><span>④ 27</span><span>⑤ 81</span></div>

## 발상

<b>밑이 9와 3으로 섞여 있다. <span class='m'>log<sub>9</sub>x = ½log<sub>3</sub>x</span>로 통일</b>하고 <span class='m'>A = log<sub>3</sub>a, B = log<sub>3</sub>b</span>로 두면 그냥 일차연립이다.

## 풀이

<p><span class="step">① 밑이 섞여 있다는 것을 먼저 본다.</span>
주어진 두 식에는 밑이 <span class="m">9</span>인 로그와 밑이 <span class="m">3</span>인 로그가 섞여 있다.
<span class="m">9 = 3<sup>2</sup></span>이므로 <b>작은 밑인 <span class="m">3</span>으로 통일</b>한다.</p>
<p class="m">log<sub>9</sub>x = log<sub>3</sub>x / log<sub>3</sub>9 = log<sub>3</sub>x / 2</p>

<p><span class="step">② 로그값을 문자로 둔다.</span>
<span class="m">a, b</span>를 직접 구하려 하면 지수 계산이 번거롭다.
<b>로그값 자체를 문자로 두면 로그 문제가 일차연립으로 내려온다.</b></p>
<p class="m">A = log<sub>3</sub>a, &nbsp; B = log<sub>3</sub>b</p>
<p>그러면 <span class="m">log<sub>9</sub>a = A/2</span>, <span class="m">log<sub>9</sub>b = B/2</span>이다.</p>

<p><span class="step">③ 첫 번째 조건을 옮겨 쓴다.</span></p>
<p class="m">log<sub>9</sub>a + log<sub>3</sub>b = 2 → A/2 + B = 2</p>
<p>양변에 <span class="m">2</span>를 곱해 분수를 없앤다.</p>
<p class="m">A + 2B = 4 &nbsp;&nbsp; … ㉠</p>

<p><span class="step">④ 두 번째 조건을 옮겨 쓴다.</span></p>
<p class="m">log<sub>3</sub>a = 8 log<sub>9</sub>b → A = 8 × (B/2) = 4B &nbsp;&nbsp; … ㉡</p>

<p><span class="step">⑤ 연립해서 A와 B를 구한다.</span>
㉡을 ㉠에 대입한다.</p>
<p class="m">4B + 2B = 4 → 6B = 4 → B = 2/3</p>
<p class="m">A = 4B = 8/3</p>

<p><span class="step">⑥ 구하는 값을 만든다.</span>
구하는 것은 <span class="m">a/b</span>인데,
<b>나눗셈은 로그에서 뺄셈</b>이므로 <span class="m">A − B</span>만 있으면 된다.
<span class="m">a</span>와 <span class="m">b</span>를 따로 구할 필요가 없다.</p>
<p class="m">log<sub>3</sub>(a/b) = log<sub>3</sub>a − log<sub>3</sub>b = A − B = 8/3 − 2/3 = 2</p>
<p>로그의 정의에 따라</p>
<p class="m">a/b = 3<sup>2</sup> = 9</p>
<p class="m">답 ③</p>

## 노하우

<b>밑이 섞이면 가장 작은 밑으로 통일한다.</b> <span class='m'>log<sub>a<sup>n</sup></sub>x = (1/n)log<sub>a</sub>x</span>. 그리고 <b>로그값 자체를 문자로 두면</b> 로그 문제가 일차연립으로 내려온다. 구하는 것이 <span class='m'>a/b</span>면 <span class='m'>log(a/b) = A − B</span>까지만 구하면 된다.
