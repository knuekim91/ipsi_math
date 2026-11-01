---
id: STA-W03
unit: 08-통계
topic: 원소의 기록값에서 표본평균의 확률을 정규 근사로 구하기
level: 4점
difficulty: 상
source: 확률과 통계 29번 (2026-11-01 나은이 풀이 사진)
origin: 오답노트
core: "X̄는 횟수가 아니라 평균이다. 반복 시행이라고 바로 이항분포로 가면 안 되고, 평균의 분포를 정규로 근사한다"
tags: [표본평균,정규분포근사,확률변수,순열,중심극한정리,이항분포함정]
status: wrong
added: 2026-11-01
answer: 994
---

## 문제

<p>네 정수 <span class="m">a, b, c, d</span>가
<span class="m">{a, b, c, d} = {1, 2, 3, 4}</span>를 만족시키는 모든 순서쌍
<span class="m">(a, b, c, d)</span>의 집합을 <span class="m">A</span>라 하자.
집합 <span class="m">A</span>에서 임의로 하나의 원소를 택할 때,
이 원소를 <span class="m">(a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, a<sub>4</sub>)</span>라 하고,
<span class="m">n + a<sub>n</sub></span>이 홀수가 되도록 하는
<span class="m">4</span> 이하의 자연수 <span class="m">n</span>의 개수를 기록한다.</p>

<p>이 시행을 <span class="m">7500</span>번 반복하여 기록된 <span class="m">7500</span>개의 수의 평균을
확률변수 <span class="m">X̄</span>라 하자.
표준정규분포표에서 <span class="m">P(0 ≤ Z ≤ z)</span>의 값은
<span class="m">z = 0.5, 1.0, 1.5, 2.0, 2.5</span>일 때 차례로
<span class="m">0.192, 0.341, 0.433, 0.477, 0.494</span>이다.</p>

<p><span class="m">P(X̄ ≥ 59/30)</span>의 값을 위 표를 이용하여 구한 값이 <span class="m">p</span>일 때,
<span class="m">1000 × p</span>의 값을 구하시오.</p>

## 발상

<b>먼저 시행 하나의 결과부터 본다.</b>
한 번 뽑아 기록되는 수는 <span class="m">n + a<sub>n</sub></span>이 홀수인
<span class="m">n</span>의 개수이고, 이 값은 <span class="m">0, 2, 4</span> 중 하나다.
<b>성공·실패 두 가지가 아니라 세 가지 값을 가진다.</b><br><br>

<b>그다음 7500번 반복했다는 것을 본다.</b>
반복 시행이라는 말 때문에 <span class="m">B(7500, p)</span>를 떠올리기 쉽다.
그런데 이 문항이 묻는 것은 <b>성공 횟수가 아니라 기록된 수들의 평균</b>이다.
<b>이항분포는 횟수에만 쓴다.</b><br><br>

<b>그러므로 평균의 분포를 쓴다.</b>
표본평균 <span class="m">X̄</span>의 평균은 한 번 기록의 평균과 같고,
분산은 한 번 기록의 분산을 시행 횟수로 나눈 값이다.
시행 횟수가 크므로 정규분포로 근사하고, 주어진 표로 확률을 읽는다.

## 풀이

<p><span class="step">① 한 번 기록되는 수 X의 분포를 구한다.</span>
<span class="m">A</span>의 원소는 <span class="m">4! = 24</span>개이므로
각각 확률 <span class="m">1/24</span>로 뽑힌다.
<span class="m">n + a<sub>n</sub></span>이 홀수이려면 <span class="m">n</span>과 <span class="m">a<sub>n</sub></span>의 홀짝이 달라야 한다.
네 순서쌍 모두에 대해 세어 보면</p>
<p class="m">P(X = 0) = 1/6, &nbsp; P(X = 2) = 2/3, &nbsp; P(X = 4) = 1/6</p>

<p><span class="step">② X의 평균과 분산을 구한다.</span></p>
<p class="m">E(X) = 0 · 1/6 + 2 · 2/3 + 4 · 1/6 = 2</p>
<p class="m">E(X²) = 0 + 4 · 2/3 + 16 · 1/6 = 16/3</p>
<p class="m">V(X) = E(X²) − {E(X)}² = 16/3 − 4 = 4/3</p>

<p><span class="step">③ 표본평균 X̄의 평균과 분산을 구한다.</span>
시행을 <span class="m">7500</span>번 반복하므로 평균은 그대로이고 분산은 <span class="m">7500</span>으로 나눈다.</p>
<p class="m">E(X̄) = E(X) = 2</p>
<p class="m">V(X̄) = V(X) / 7500 = (4/3) / 7500 = 4/22500</p>
<p class="m">σ(X̄) = √(4/22500) = 2/150 = 1/75</p>

<p><span class="step">④ 표준화한다.</span>
<span class="m">X̄</span>를 표준화하면</p>
<p class="m">P(X̄ ≥ 59/30) = P(Z ≥ (59/30 − 2) / (1/75))</p>
<p class="m">= P(Z ≥ (−1/30) × 75) = P(Z ≥ −5/2)</p>

<p><span class="step">⑤ 표준정규분포표로 읽는다.</span>
표는 <span class="m">0</span>부터의 넓이만 주므로, <span class="m">0</span>을 기준으로 둘로 나눈다.
구간 <span class="m">Z ≥ −5/2</span>는 <span class="m">−5/2 ≤ Z ≤ 0</span>과 <span class="m">Z ≥ 0</span>의 합이다.
정규분포는 <span class="m">0</span>에 대하여 대칭이므로
<span class="m">P(−5/2 ≤ Z ≤ 0) = P(0 ≤ Z ≤ 5/2)</span>이다.</p>
<p class="m">P(Z ≥ −2.5) = P(0 ≤ Z ≤ 2.5) + P(Z ≥ 0) = 0.494 + 0.5 = 0.994</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">p = 0.994, &nbsp; 1000 × p = 994</p>
<p class="m">답 994</p>

## 함정

<b>7500번 반복이라는 말에 끌려 이항분포로 넘어가면 안 된다.</b>
이항분포는 <b>성공과 실패 두 가지 결과의 횟수</b>에만 쓰인다.
이 문항의 시행 결과는 <span class="m">0, 2, 4</span> 세 값이므로
한 번의 시행도 이항 시행이 아니다.
<b>반복 시행이라고 바로 이항분포라고 쓰지 않는다.
평균을 묻는 문제는 평균의 분포(정규 근사)로 간다.</b><br><br>

<b><span class="m">B(7500, p)</span>로 쓰고 나면 평균이 안 맞아 막힌다.</b>
이항분포의 평균 <span class="m">np</span>는 <span class="m">7500p</span>인데,
<span class="m">X̄</span>의 평균은 <span class="m">2</span>다.
<b>평균이 횟수와 다른 값으로 나오면 분포 선택이 틀린 것이다.</b><br><br>

<b>분산을 시행 횟수로 나누는 것을 잊으면 표준화가 크게 틀어진다.</b>
<span class="m">V(X̄)</span>에 <span class="m">4/3</span>을 그대로 쓰면
표준편차가 <span class="m">√(4/3) ≈ 1.15</span>가 되어 <span class="m">z</span>가 거의 0에 가까워진다.
<b>표준편차는 <span class="m">V(X)/n</span>의 제곱근이다.</b><br><br>

<b>표는 0부터 z까지의 넓이다. 0.5를 더하는 것을 잊지 않는다.</b>
<span class="m">z = −2.5</span>는 음수이므로 <span class="m">P(Z ≥ −2.5)</span>는
<span class="m">0.5 + 0.494</span>이다. 표의 값만 그대로 쓰면 <span class="m">494</span>가 나온다.

## 노하우

<b>평균을 묻는 문제는 세 줄로 정리한다.</b></p>
<p class="m">E(X̄) = E(X) &nbsp;&nbsp; V(X̄) = V(X) / n &nbsp;&nbsp; n 이 크면 X̄ 는 정규분포에 가깝다</p>
<p><b>&lsquo;반복&rsquo;은 분산을 나누는 이유이지 이항분포의 이유가 아니다.</b><br><br>

<b>이항분포인지 판단하는 두 가지를 먼저 본다.</b>
시행 결과가 성공·실패 두 가지인가, 그리고 묻는 것이 성공 횟수인가.
둘 중 하나라도 아니면 이항분포가 아니다.<br><br>

<b>표를 주었다면 정규 근사가 의도된 길이다.</b>
이항분포로 가면 표가 필요 없고 계산이 훨씬 무겁다.
<b>문제가 표준정규분포표를 준 이유를 먼저 생각한다.</b>
