---
id: STA-D26
unit: 08-통계
topic: 모평균의 신뢰구간
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 2회 26번
exam: 2027-수능완성
origin: 기출
core: "신뢰구간의 중앙이 표본평균이고, 구간의 길이가 오차한계의 2배다"
tags: [신뢰구간,표본평균,모평균추정,오차한계]
status: seed
added: 2026-09-07
answer: ⑤
---

## 문제

<p>어느 지역에서 수확하는 수박의 무게는 평균이 <span class="m">m</span>,
표준편차가 <span class="m">σ</span>인 정규분포를 따른다고 한다.
이 지역에서 수확한 수박 <span class="m">196</span>개를 임의추출하여 얻은
수박의 무게의 표본평균이 <span class="m">6.3</span>일 때,
모평균 <span class="m">m</span>에 대한 신뢰도
<span class="m">95 %</span>의 신뢰구간이
<span class="m">4a ≤ m ≤ 5a</span>이다.
<span class="m">a × σ</span>의 값은?
(단, 무게의 단위는 <span class="m">kg</span>이고,
<span class="m">Z</span>가 표준정규분포를 따르는 확률변수일 때,
<span class="m">P(|Z| ≤ 1.96) = 0.95</span>로 계산한다.)</p>

<div class="choices"><span>① 4.2</span><span>② 4.9</span><span>③ 5.6</span>
<span>④ 6.3</span><span>⑤ 7</span></div>

## 발상

<b>신뢰구간은 &lsquo;표본평균 <span class="m">±</span> 오차한계&rsquo; 꼴이므로
두 가지 정보를 준다.</b>
하나는 <b>구간의 한가운데가 표본평균</b>이라는 것이고,
다른 하나는 <b>구간의 길이가 오차한계의 <span class="m">2</span>배</b>라는 것이다.<br><br>

구간이 <span class="m">4a ≤ m ≤ 5a</span>로 주어졌으므로,
가운데는 <span class="m">(4a + 5a)/2 = 4.5a</span>이고
길이는 <span class="m">5a − 4a = a</span>이다.
<b>가운데를 표본평균 <span class="m">6.3</span>과 견주면
<span class="m">a</span>가 나오고,
길이를 오차한계의 <span class="m">2</span>배와 견주면
<span class="m">σ</span>가 나온다.</b>
미지수 두 개에 식 두 개이므로 딱 맞아떨어진다.

## 풀이

<p><span class="step">① 신뢰구간의 꼴을 적는다.</span>
모표준편차가 <span class="m">σ</span>이고 표본의 크기가
<span class="m">n = 196</span>, 표본평균이 <span class="m">6.3</span>이므로,
신뢰도 <span class="m">95 %</span>의 신뢰구간은 다음과 같다.</p>
<p class="m">6.3 − 1.96 × σ/√196 ≤ m ≤ 6.3 + 1.96 × σ/√196</p>
<p><span class="m">√196 = 14</span>이므로 오차한계를 정리한다.</p>
<p class="m">1.96 × σ/14 = 0.14σ</p>
<p class="m">6.3 − 0.14σ ≤ m ≤ 6.3 + 0.14σ</p>

<p><span class="step">② 구간의 한가운데를 비교한다.</span>
주어진 신뢰구간 <span class="m">4a ≤ m ≤ 5a</span>의 한가운데는
두 끝의 평균이다.</p>
<p class="m">(4a + 5a)/2 = 9a/2 = 4.5a</p>
<p>①의 신뢰구간의 한가운데는 표본평균
<span class="m">6.3</span>이므로 두 값이 같다.</p>
<p class="m">4.5a = 6.3 → a = 6.3/4.5 = 1.4</p>

<p><span class="step">③ 구간의 길이를 비교한다.</span>
주어진 신뢰구간의 길이는 오른쪽 끝에서 왼쪽 끝을 뺀 것이다.</p>
<p class="m">5a − 4a = a = 1.4</p>
<p>①의 신뢰구간의 길이는 오차한계의 <span class="m">2</span>배이다.</p>
<p class="m">(6.3 + 0.14σ) − (6.3 − 0.14σ) = 0.28σ</p>
<p>두 값이 같으므로 <span class="m">σ</span>를 구한다.</p>
<p class="m">0.28σ = 1.4 → σ = 1.4/0.28 = 5</p>

<p><span class="step">④ 답을 만든다.</span></p>
<p class="m">a × σ = 1.4 × 5 = 7</p>
<p class="m">답 ⑤</p>

<p><span class="step">⑤ 검산한다.</span>
<span class="m">a = 1.4</span>이므로 주어진 신뢰구간은
<span class="m">5.6 ≤ m ≤ 7</span>이다.
①의 식에 <span class="m">σ = 5</span>를 넣으면
오차한계가 <span class="m">0.14 × 5 = 0.7</span>이므로</p>
<p class="m">6.3 − 0.7 = 5.6, &nbsp; 6.3 + 0.7 = 7</p>
<p>두 구간이 정확히 일치한다.</p>

## 함정

<b>구간의 길이를 오차한계 자체로 놓으면 안 된다.</b>
신뢰구간의 길이는 <b>오차한계의 <span class="m">2</span>배</b>이다.
<span class="m">0.14σ = 1.4</span>로 놓으면
<span class="m">σ = 10</span>이 되어 답이 <span class="m">14</span>가 된다.<br><br>

<b><span class="m">√n</span>을 <span class="m">n</span>으로 쓰면 안 된다.</b>
표본평균의 표준편차는
<span class="m">σ/√n</span>이다.
<span class="m">n = 196</span>이므로 나누는 것은
<span class="m">196</span>이 아니라 <span class="m">14</span>이다.
<b><span class="m">196</span>이라는 숫자가 주어진 이유는
제곱수라서 근호가 깔끔하게 벗겨지기 때문</b>이다.<br><br>

<b><span class="m">a</span>를 구하고 나서 <span class="m">σ</span>를
구하는 것을 잊지 않는다.</b>
구하는 것은 <span class="m">a</span>도 <span class="m">σ</span>도 아니고
<b>두 값의 곱</b>이다. 선택지에 <span class="m">6.3</span>이 있는데,
이는 표본평균을 그대로 고르게 하려는 함정이다.

## 노하우

<b>신뢰구간이 <span class="m">A ≤ m ≤ B</span> 꼴로 주어지면
두 가지를 바로 뽑는다.</b></p>
<p class="m">(표본평균) = (A + B)/2, &nbsp; 2 × (오차한계) = B − A</p>
<p><b>가운데와 길이</b>, 이 두 정보가 미지수 두 개를 정해 준다.
신뢰구간 문제의 거의 전부가 이 한 쌍으로 풀린다.<br><br>

<b>신뢰도에 따른 상수를 정확히 쓴다.</b>
신뢰도 <span class="m">95 %</span>이면
<span class="m">1.96</span>, <span class="m">99 %</span>이면
<span class="m">2.58</span>이다.
문제에서
<span class="m">P(|Z| ≤ 1.96) = 0.95</span>처럼
<b>직접 알려 주므로 그 값을 그대로 쓴다.</b><br><br>

<b>답을 구한 뒤 원래 구간에 넣어 확인한다.</b>
<span class="m">a</span>와 <span class="m">σ</span>를 모두 구했으므로
신뢰구간의 양 끝을 직접 계산해 볼 수 있다.
<b>두 표현이 같은 구간을 주는지 확인하는 데 몇 초면 충분하다.</b>
