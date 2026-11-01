---
id: STA-W03-V1
parent: STA-W03
unit: 08-통계
topic: 두 값을 갖는 확률변수의 표본평균을 정규 근사로 구하기 (기본)
level: 4점
difficulty: 하
source: 자체 개발 (STA-W03 변형 · 기본형, 이항분포 함정 없이 평균의 분포만)
origin: 유사문항
core: "표본평균의 평균은 E(X), 분산은 V(X)/n 이다. 이것만 지키면 표준정규분포표로 바로 읽힌다"
tags: [표본평균,정규분포근사,확률변수,표준화]
status: variant
added: 2026-11-01
answer: 159
---

## 문제

<p>확률변수 <span class="m">X</span>는 값 <span class="m">1</span>과 <span class="m">3</span>을 각각
확률 <span class="m">1/2</span>로 가진다.
이 시행을 <span class="m">100</span>번 반복하여 얻은 <span class="m">100</span>개의 값의 평균을
<span class="m">X̄</span>라 하자.</p>

<p>표준정규분포표에서 <span class="m">P(0 ≤ Z ≤ 1) = 0.341</span>일 때,
<span class="m">1000 × P(X̄ ≥ 2.1)</span>의 값을 구하시오.</p>

## 발상

<b>이 문제는 두 가지만 하면 된다.</b>
평균 하나, 분산 하나를 구해 표준화하는 것이다.<br><br>

<b>반복했다고 이항분포를 떠올리지 않는다.</b>
묻는 것이 평균이므로 <b>평균의 분포</b>를 쓴다.

## 풀이

<p><span class="step">① X의 평균과 분산을 구한다.</span></p>
<p class="m">E(X) = 1 · 1/2 + 3 · 1/2 = 2</p>
<p class="m">E(X²) = 1 · 1/2 + 9 · 1/2 = 5</p>
<p class="m">V(X) = 5 − 4 = 1</p>

<p><span class="step">② X̄의 평균과 분산을 구한다.</span></p>
<p class="m">E(X̄) = 2, &nbsp; V(X̄) = 1/100, &nbsp; σ(X̄) = 1/10</p>

<p><span class="step">③ 표준화한다.</span></p>
<p class="m">P(X̄ ≥ 2.1) = P(Z ≥ (2.1 − 2) / (1/10)) = P(Z ≥ 1)</p>

<p><span class="step">④ 표로 읽는다.</span></p>
<p class="m">P(Z ≥ 1) = 0.5 − P(0 ≤ Z ≤ 1) = 0.5 − 0.341 = 0.159</p>
<p class="m">1000 × 0.159 = 159</p>
<p class="m">답 159</p>

## 함정

<b>표준화할 때 표준편차에 시행 횟수를 곱하지 않는다.</b>
<span class="m">σ(X̄) = 1/10</span>이므로 <span class="m">0.1</span>로 나누어야 한다.
<span class="m">1</span>로 나누면 <span class="m">z = 0.1</span>이 되어 답이 크게 달라진다.<br><br>

<b>0.5를 빼는 것을 잊는다.</b>
표는 <span class="m">0</span>부터의 넓이이므로 <span class="m">P(Z ≥ 1)</span>은
<span class="m">0.5 − 0.341</span>이다. 표의 값 <span class="m">0.341</span>을 그대로 쓰면 <span class="m">341</span>이 된다.

## 노하우

<b>표본평균 문제는 세 줄이다.</b></p>
<p class="m">E(X̄) = E(X) &nbsp;&nbsp; V(X̄) = V(X) / n &nbsp;&nbsp; (X̄ − E) / σ(X̄) 를 표준화</p>
<p><b>&lsquo;n번 반복&rsquo;은 분산을 나누는 이유다.</b>
