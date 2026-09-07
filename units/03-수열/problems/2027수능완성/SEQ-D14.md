---
id: SEQ-D14
unit: 03-수열
topic: 귀납적으로 정의된 수열의 주기
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 14번
exam: 2027-수능완성
origin: 기출
core: "a(n+1) = |a(n)| − 1 은 1씩 줄다가 0에 닿은 뒤 0과 −1을 되풀이한다. 곱이 −55이므로 a(m) = −1, 부분합 = 55다"
tags: [귀납적정의,절댓값,주기수열,부분합]
status: seed
added: 2026-09-07
answer: ①
---

## 문제

<p>첫째항이 자연수인 수열 <span class="m">{a<sub>n</sub>}</span>이 모든 자연수
<span class="m">n</span>에 대하여</p>
<p class="m">a<sub>n+1</sub> = |a<sub>n</sub>| − 1</p>
<p>을 만족시킨다. <span class="m">10 ≤ m ≤ 100</span>인 자연수
<span class="m">m</span>에 대하여</p>
<p class="m">a<sub>m</sub> × Σ<sub>k=1</sub><sup>m</sup> a<sub>k</sub> = −55</p>
<p>가 되도록 하는 모든 <span class="m">m</span>의 값의 합은?</p>

<div class="choices"><span>① 176</span><span>② 180</span><span>③ 184</span>
<span>④ 188</span><span>⑤ 192</span></div>

## 발상

<b>귀납적으로 정의된 수열은 몇 항만 직접 써 보면 규칙이 드러난다.</b>
첫째항을 <span class="m">a<sub>1</sub> = N</span>(자연수)이라 하고 차례로 적어 보자.
<span class="m">a<sub>n</sub></span>이 양수인 동안에는 절댓값이 아무 일도 하지 않으므로
<b><span class="m">1</span>씩 줄어들기만 한다.</b>
그러다 <span class="m">0</span>에 닿으면
<span class="m">|0| − 1 = −1</span>, 그 다음은
<span class="m">|−1| − 1 = 0</span>이 되어
<b><span class="m">0</span>과 <span class="m">−1</span>이 번갈아 나오는 주기</b>에 갇힌다.<br><br>

<b>곱이 <span class="m">−55</span>라는 조건이 경우를 거의 다 걸러 준다.</b>
곱이 <span class="m">0</span>이 아니므로 <span class="m">a<sub>m</sub> ≠ 0</span>이다.
그런데 <span class="m">m ≥ 10</span>이고 값은
<b>양수 구간</b>이거나 <b>주기 구간의 <span class="m">−1</span></b>뿐이다.
양수라면 부분합도 양수이므로 곱이 양수가 되어 <span class="m">−55</span>가 될 수 없다.
그러므로 <b><span class="m">a<sub>m</sub> = −1</span>이고 부분합은
<span class="m">55</span></b>여야 한다.

## 풀이

<p><span class="step">① 수열의 모습을 파악한다.</span>
<span class="m">a<sub>1</sub> = N</span>(자연수)이라 하자.
<span class="m">a<sub>n</sub> &gt; 0</span>인 동안에는
<span class="m">a<sub>n+1</sub> = a<sub>n</sub> − 1</span>이므로
<span class="m">1</span>씩 줄어든다.</p>
<p class="m">a<sub>1</sub> = N, a<sub>2</sub> = N − 1, … , a<sub>N</sub> = 1, a<sub>N+1</sub> = 0</p>
<p>그 뒤로는 다음과 같이 두 값이 되풀이된다.</p>
<p class="m">a<sub>N+2</sub> = |0| − 1 = −1, &nbsp; a<sub>N+3</sub> = |−1| − 1 = 0, &nbsp; a<sub>N+4</sub> = −1, …</p>
<p>정리하면 <span class="m">n ≥ N + 1</span>에서
<span class="m">n − (N + 1)</span>이 짝수이면
<span class="m">a<sub>n</sub> = 0</span>, 홀수이면
<span class="m">a<sub>n</sub> = −1</span>이다.</p>

<p><span class="step">② a(m)이 −1임을 밝힌다.</span>
곱이 <span class="m">−55 ≠ 0</span>이므로
<span class="m">a<sub>m</sub> ≠ 0</span>이다.
<span class="m">a<sub>m</sub></span>이 될 수 있는 값은 양수 또는
<span class="m">−1</span>뿐이다.<br>
만약 <span class="m">a<sub>m</sub> &gt; 0</span>이면
<span class="m">m ≤ N</span>이고, 이때 부분합은 양수인 항들만 더한 것이므로
양수이다. 그러면 곱도 양수가 되어 <span class="m">−55</span>가 될 수 없다.
따라서</p>
<p class="m">a<sub>m</sub> = −1</p>
<p>이고, 곱이 <span class="m">−55</span>이므로 부분합이 정해진다.</p>
<p class="m">(−1) × Σ<sub>k=1</sub><sup>m</sup> a<sub>k</sub> = −55 → Σ<sub>k=1</sub><sup>m</sup> a<sub>k</sub> = 55</p>

<p><span class="step">③ 부분합을 N과 m으로 나타낸다.</span>
<span class="m">k = 1</span>부터 <span class="m">k = N + 1</span>까지는
<span class="m">N, N − 1, … , 1, 0</span>이므로 그 합은
<span class="m">1</span>부터 <span class="m">N</span>까지의 합이다.</p>
<p class="m">Σ<sub>k=1</sub><sup>N+1</sup> a<sub>k</sub> = N(N + 1)/2</p>
<p><span class="m">k = N + 2</span>부터 <span class="m">k = m</span>까지는
<span class="m">−1</span>과 <span class="m">0</span>이 번갈아 나온다.
<span class="m">d = m − (N + 1)</span>이라 하면
<span class="m">a<sub>m</sub> = −1</span>이므로 <span class="m">d</span>는 홀수이고,
이 구간에 들어 있는 <span class="m">−1</span>의 개수는
<span class="m">(d + 1)/2</span>이다.</p>
<p class="m">Σ<sub>k=1</sub><sup>m</sup> a<sub>k</sub> = N(N + 1)/2 − (d + 1)/2 = 55</p>

<p><span class="step">④ d를 N으로 나타낸다.</span>
위 식의 양변에 <span class="m">2</span>를 곱한다.</p>
<p class="m">N(N + 1) − (d + 1) = 110</p>
<p class="m">d = N(N + 1) − 111</p>
<p><span class="m">N(N + 1)</span>은 연속한 두 자연수의 곱이므로 항상 짝수이고,
따라서 <span class="m">d</span>는 항상 홀수이다.
<b>홀수여야 한다는 조건은 저절로 만족된다.</b>
남은 조건은 <span class="m">d ≥ 1</span>이다.</p>
<p class="m">N(N + 1) ≥ 112</p>
<p><span class="m">10 × 11 = 110 &lt; 112</span>이고
<span class="m">11 × 12 = 132 ≥ 112</span>이므로
<span class="m">N ≥ 11</span>이다.</p>

<p><span class="step">⑤ m을 N으로 나타낸다.</span></p>
<p class="m">m = N + 1 + d = N + 1 + N(N + 1) − 111</p>
<p class="m">m = N<sup>2</sup> + 2N − 110</p>

<p><span class="step">⑥ 범위 조건을 확인한다.</span>
<span class="m">N ≥ 11</span>인 자연수에 대하여
<span class="m">m</span>의 값을 차례로 구하고
<span class="m">10 ≤ m ≤ 100</span>인 것만 고른다.</p>
<p class="m">N = 11 : m = 121 + 22 − 110 = 33</p>
<p class="m">N = 12 : m = 144 + 24 − 110 = 58</p>
<p class="m">N = 13 : m = 169 + 26 − 110 = 85</p>
<p class="m">N = 14 : m = 196 + 28 − 110 = 114</p>
<p><span class="m">N = 14</span>부터는 <span class="m">m &gt; 100</span>이고
<span class="m">m</span>은 <span class="m">N</span>에 대하여 증가하므로
그 뒤로는 볼 필요가 없다.</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">33 + 58 + 85 = 176</p>
<p class="m">답 ①</p>

## 함정

<b>첫째항이 고정되어 있지 않다는 점을 놓치면 안 된다.</b>
<span class="m">a<sub>1</sub></span>은 &lsquo;자연수&rsquo;일 뿐 값이 주어지지 않았다.
그러므로 <span class="m">N</span>을 문자로 두고
<span class="m">N</span>마다 <span class="m">m</span>을 구해야 한다.
<span class="m">N</span> 하나에 <span class="m">m</span> 하나가 대응된다.<br><br>

<b><span class="m">−1</span>의 개수를 세는 데서 실수가 나온다.</b>
<span class="m">k = N + 2</span>부터 시작해서
<span class="m">−1, 0, −1, 0, …</span> 순서이므로,
<span class="m">d</span>개의 항 중 <span class="m">−1</span>은
<span class="m">(d + 1)/2</span>개다.
<span class="m">d/2</span>로 잘못 세면 부분합이 어긋난다.<br><br>

<b>양수 구간의 경우를 제대로 배제해야 한다.</b>
<span class="m">a<sub>m</sub> &gt; 0</span>이면 부분합도 양수이므로
곱이 양수가 된다. 이 한 줄을 쓰지 않으면
경우를 다 따져야 하는 것처럼 보여 시간을 잃는다.

## 노하우

<b>귀납적 수열은 무조건 처음 대여섯 항을 손으로 적는다.</b>
<span class="m">a<sub>n+1</sub> = |a<sub>n</sub>| − 1</span>처럼 절댓값이 붙은 식은
<b>부호가 바뀌는 순간</b>에 성격이 달라진다.
직접 적어 보면 &lsquo;줄어드는 구간&rsquo;과 &lsquo;주기 구간&rsquo;이 눈에 보인다.<br><br>

<b>곱이 특정한 값이라는 조건은 인수를 좁히는 데 쓴다.</b>
<span class="m">a<sub>m</sub> × (부분합) = −55</span>에서
<span class="m">a<sub>m</sub></span>이 가질 수 있는 값이 몇 개 안 되면,
곱의 조건 하나로 두 인수가 모두 정해진다.
<b>부호부터 따지는 것</b>이 가장 빠르다.<br><br>

<b>정수 조건은 마지막에 확인한다.</b>
<span class="m">d = N(N + 1) − 111</span>에서
<span class="m">N(N + 1)</span>이 항상 짝수라는 사실 덕분에
<span class="m">d</span>의 홀짝 조건이 저절로 해결된다.
연속한 두 자연수의 곱은 짝수라는 것은 자주 쓰이는 성질이다.
