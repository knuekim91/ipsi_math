---
id: STA-W03-V3
parent: STA-W03
unit: 08-통계
topic: 표본평균 확률의 값으로부터 시행 횟수를 거꾸로 구하기
level: 4점
difficulty: 중상
source: 자체 개발 (STA-W03 변형 · 역방향)
origin: 유사문항
core: "표준화한 z 가 표의 값으로 정해지면 표준편차가 정해지고, 표준편차에서 시행 횟수 n 이 나온다. 확률에서 시작해 n 으로 거슬러 간다"
tags: [표본평균,정규분포근사,역추론,표준화,시행횟수]
status: variant
added: 2026-11-01
answer: 25
---

## 문제

<p>확률변수 <span class="m">X</span>는 값 <span class="m">1</span>과 <span class="m">3</span>을 각각
확률 <span class="m">1/2</span>로 가진다.
이 시행을 <span class="m">n</span>번 반복하여 얻은 <span class="m">n</span>개의 값의 평균을
<span class="m">X̄</span>라 하자.</p>

<p>표준정규분포표를 이용하여 구한 <span class="m">P(X̄ ≥ 2.3)</span>의 값을 <span class="m">p</span>라 하자.
<span class="m">1000 × p = 67</span>일 때, 자연수 <span class="m">n</span>의 값을 구하시오.</p>

## 발상

<b>이번에는 확률에서 시작해 거꾸로 간다.</b>
표준화한 <span class="m">z</span>가 표의 어떤 값과 맞는지 먼저 찾는다.<br><br>

<b>1000p = 67이므로 p = 0.067이다.</b>
표준정규분포표에서 <span class="m">0.5 − 0.433 = 0.067</span>이므로
<span class="m">P(0 ≤ Z ≤ z) = 0.433</span>, 곧 <span class="m">z = 1.5</span>이다.
이것이 이 문항의 첫 번째 열쇠다.

## 풀이

<p><span class="step">① 확률을 z 값으로 바꾼다.</span></p>
<p class="m">p = P(Z ≥ z) = 0.5 − P(0 ≤ Z ≤ z) = 0.067</p>
<p class="m">P(0 ≤ Z ≤ z) = 0.433 → z = 1.5</p>

<p><span class="step">② X의 평균과 분산을 구한다.</span></p>
<p class="m">E(X) = 2, &nbsp; E(X²) = 5, &nbsp; V(X) = 5 − 4 = 1</p>

<p><span class="step">③ 표준화한 식을 세운다.</span>
<span class="m">X̄</span>의 평균은 <span class="m">2</span>, 표준편차는 <span class="m">1/√n</span>이다.</p>
<p class="m">P(X̄ ≥ 2.3) = P(Z ≥ (2.3 − 2) / (1/√n)) = P(Z ≥ 0.3√n)</p>

<p><span class="step">④ n을 구한다.</span>
<span class="m">0.3√n = 1.5</span>이므로</p>
<p class="m">√n = 5 → n = 25</p>
<p class="m">답 25</p>

<p><span class="step">⑤ 확인한다.</span>
<span class="m">n = 25</span>이면 <span class="m">z = 0.3 × 5 = 1.5</span>이고
<span class="m">P(Z ≥ 1.5) = 0.5 − 0.433 = 0.067</span>이므로 <span class="m">1000p = 67</span>이다. ✓</p>

## 함정

<b>0.067을 그대로 z로 읽으면 안 된다.</b>
표에 있는 값은 <span class="m">0.433</span>이다.
<span class="m">0.067</span>은 표의 값을 <span class="m">0.5</span>에서 뺀 것이다.<br><br>

<b>표준편차를 <span class="m">√n</span>으로 두지 않는다.</b>
<span class="m">X̄</span>의 표준편차는 <span class="m">√(V(X)/n) = 1/√n</span>이다.
<span class="m">√n</span>을 그대로 쓰면 <span class="m">n</span>의 방향이 뒤집힌다.<br><br>

<b>제곱을 잊어서 <span class="m">n = 5</span>로 답하지 않는다.</b>
<span class="m">√n = 5</span>에서 <span class="m">n</span>을 구할 때는 제곱한다.

## 노하우

<b>역추론은 표준화 식을 그대로 두고 미지수 하나만 남긴다.</b></p>
<p class="m">z = (기준값 − 평균) / (σ/√n) → 미지수는 n 하나</p>
<p><b>표의 z 값과 1000p 를 먼저 대응시키면 방향이 잡힌다.</b>
