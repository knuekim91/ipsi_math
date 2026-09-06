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

<p><span class="step">① a = 0에서 존재.</span> 분모가 0이므로 분자도 0이어야 한다.</p><p class="m">f(0+2) = f(2) = 0</p><p><span class="step">② a = 3에서 비존재.</span> 분모가 3에서 0이어야 한다.</p><p class="m">3(f(3) − 3) = 0 → f(3) = 3</p><p><span class="step">③ 일차함수를 정한다.</span> <span class="m">f(2) = 0, f(3) = 3</span>이므로 기울기 3.</p><p class="m">f(x) = 3(x − 2) = 3x − 6</p><p><span class="step">④ 확인.</span> 분모 <span class="m">= x(3x−9) = 3x(x−3)</span>, 분자 <span class="m">= 3x</span>.</p><p class="m">a = 0 : 3x/(3x(x−3)) = 1/(x−3) → −1/3 (존재)</p><p class="m">a = 3 : 분자 → 9 ≠ 0, 분모 → 0 (비존재)</p><p class="m">f(4) = 12 − 6 = 6</p>

## 함정

&lsquo;존재하지 않는다&rsquo;는 조건도 <b>정보</b>다. 그냥 버리면 미지수를 다 못 정한다. 분모가 그 점에서 0이 되어야 한다는 뜻으로 읽는다.

## 노하우

<b>분수 극한에서 &lsquo;존재&rsquo;와 &lsquo;비존재&rsquo;는 둘 다 방정식이다.</b> 존재 → (분모 0인 곳에서) 분자도 0. 비존재 → 분모는 0, 분자는 0이 아님. 일차함수처럼 미지수가 둘이면 조건도 두 개가 필요하고, 문제는 정확히 두 개를 준다.
