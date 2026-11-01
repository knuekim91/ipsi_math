---
id: STA-W03-V2
parent: STA-W03
unit: 08-통계
topic: 순열 다섯 개에서 기록값의 분포를 구한 뒤 표본평균 확률 구하기 (심화)
level: 4점
difficulty: 상
source: 자체 개발 (STA-W03 변형 · 원소 개수를 늘려 분포부터 세기)
origin: 유사문항
core: "기록값의 분포를 먼저 전부 세어야 평균과 분산이 나온다. 원소가 늘면 가짓수가 늘어도 분포가 몇 개의 값에 몰리는지 보면 계산이 줄어든다"
tags: [표본평균,정규분포근사,순열,확률분포,경우의수]
status: variant
added: 2026-11-01
answer: 23
---

## 문제

<p>집합 <span class="m">B</span>는 <span class="m">1, 2, 3, 4, 5</span>의 순열
<span class="m">(a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>4</sub>, a<sub>5</sub>)</span> 전체의 집합이다.
<span class="m">B</span>에서 임의로 하나의 원소를 택하고,
<span class="m">n + a<sub>n</sub></span>이 홀수가 되도록 하는 <span class="m">5</span> 이하의 자연수
<span class="m">n</span>의 개수를 기록한다.</p>

<p>이 시행을 <span class="m">400</span>번 반복하여 얻은 <span class="m">400</span>개의 값의 평균을
<span class="m">X̄</span>라 하자.</p>

<p>표준정규분포표에서 <span class="m">P(0 ≤ Z ≤ 2) = 0.477</span>일 때,
<span class="m">1000 × P(X̄ ≥ 2.52)</span>의 값을 구하시오.</p>

## 발상

<b>이 문제는 두 단계로 나뉜다.</b>
먼저 기록값의 분포를 세고, 그다음 표본평균의 확률을 구한다.
<b>분포를 세지 않으면 평균도 분산도 나오지 않는다.</b><br><br>

<b>원소가 다섯 개면 순열이 120개다.</b>
하나씩 세기보다 <b>n이 홀수인 자리와 짝을 맞춰</b> 보면
기록값이 몇 개의 값만 가진다는 것이 보인다. 그 값들이 짝수뿐이라는 것이 핵심이다.

## 풀이

<p><span class="step">① 한 번 기록되는 값 X의 분포를 세운다.</span>
<span class="m">n + a<sub>n</sub></span>이 홀수이려면 <span class="m">n</span>과 <span class="m">a<sub>n</sub></span>의 홀짝이 달라야 한다.
<span class="m">1 ~ 5</span>에는 홀수가 셋, 짝수가 둘 있으므로 짝을 맞추는 방식을 센다.
120개의 순열을 전부 세면 다음과 같다.</p>
<p class="m">P(X = 0) = 1/10, &nbsp; P(X = 2) = 3/5, &nbsp; P(X = 4) = 3/10</p>

<p><span class="step">② 평균과 분산을 구한다.</span></p>
<p class="m">E(X) = 0 · 1/10 + 2 · 3/5 + 4 · 3/10 = 6/5 + 6/5 = 12/5</p>
<p class="m">E(X²) = 0 + 4 · 3/5 + 16 · 3/10 = 12/5 + 24/5 = 36/5</p>
<p class="m">V(X) = 36/5 − (12/5)² = 180/25 − 144/25 = 36/25</p>

<p><span class="step">③ X̄의 평균과 분산을 구한다.</span></p>
<p class="m">E(X̄) = 12/5 = 2.4</p>
<p class="m">V(X̄) = (36/25) / 400 = 36/10000, &nbsp; σ(X̄) = 6/100 = 0.06</p>

<p><span class="step">④ 표준화한다.</span></p>
<p class="m">P(X̄ ≥ 2.52) = P(Z ≥ (2.52 − 2.4) / 0.06) = P(Z ≥ 2)</p>

<p><span class="step">⑤ 표로 읽는다.</span></p>
<p class="m">P(Z ≥ 2) = 0.5 − 0.477 = 0.023</p>
<p class="m">1000 × 0.023 = 23</p>
<p class="m">답 23</p>

## 함정

<b>원소의 개수 5와 반복 횟수 400을 혼동하지 않는다.</b>
순열의 원소는 5개이고, 반복은 400번이다.
<span class="m">400</span>은 분산을 나누는 수이고, <span class="m">5</span>는 자리의 개수다.<br><br>

<b>분산을 구할 때 E(X)²를 빼지 않는다.</b>
<span class="m">E(X²) = 36/5</span>만 쓰면 답이 전혀 다른 곳으로 간다.<br><br>

<b>기록값이 짝수뿐이라는 것을 확인하지 않고 분포를 추측한다.</b>
<span class="m">X</span>가 <span class="m">1</span>이나 <span class="m">3</span>을 가진다고 생각하면 평균이 맞지 않는다.
세 값 <span class="m">0, 2, 4</span>의 확률 합이 <span class="m">1</span>인지 꼭 확인한다.

## 노하우

<b>기록값의 분포는 &lsquo;짝수뿐인가&rsquo;부터 본다.</b>
홀짝이 한쪽으로 몰리면 가짓수가 줄어든다.
이 문항은 <span class="m">X</span>의 값이 짝수 셋뿐이어서 평균을 바로 구할 수 있었다.<br><br>

<b>표로 읽는 z 값은 세 자리로 맞춘다.</b>
기준값 <span class="m">2.52</span>는 <span class="m">2.4 + 2 × 0.06</span>으로 정해진 값이다.
표 값에 맞게 기준을 잡으면 답이 정수로 떨어진다.
