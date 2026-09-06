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

<p><span class="step">① 문자로 바꾼다.</span> <span class="m">A = log<sub>3</sub>a</span>, <span class="m">B = log<sub>3</sub>b</span>라 하면 <span class="m">log<sub>9</sub>a = A/2</span>, <span class="m">log<sub>9</sub>b = B/2</span>.</p><p class="m">A/2 + B = 2 → A + 2B = 4</p><p class="m">A = 8·(B/2) = 4B</p><p><span class="step">② 연립.</span> <span class="m">4B + 2B = 4 → B = 2/3, A = 8/3</span></p><p><span class="step">③ 구하는 값.</span></p><p class="m">log<sub>3</sub>(a/b) = A − B = 8/3 − 2/3 = 2 → a/b = 3<sup>2</sup> = 9</p>

## 노하우

<b>밑이 섞이면 가장 작은 밑으로 통일한다.</b> <span class='m'>log<sub>a<sup>n</sup></sub>x = (1/n)log<sub>a</sub>x</span>. 그리고 <b>로그값 자체를 문자로 두면</b> 로그 문제가 일차연립으로 내려온다. 구하는 것이 <span class='m'>a/b</span>면 <span class='m'>log(a/b) = A − B</span>까지만 구하면 된다.
