---
id: SEQ-C18
unit: 03-수열
topic: 합의 차로 항 구하기
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 1회 18번
exam: 2027-수능완성
origin: 기출
core: "S_{n+1} − Sₙ 은 정의상 a_{n+1} 이다"
tags: [등차수열,수열의합]
status: seed
added: 2026-09-07
answer: 44
---

## 문제

<p>등차수열 <span class="m">{a<sub>n</sub>}</span>의 첫째항부터 제
<span class="m">n</span>항까지의 합을 <span class="m">S<sub>n</sub></span>이라 하자.
수열 <span class="m">{S<sub>n</sub>}</span>이 다음 조건을 만족시킬 때,
<span class="m">a<sub>k</sub> &gt; 100</span>을 만족시키는 자연수
<span class="m">k</span>에 대하여 <span class="m">a<sub>1</sub> + k</span>의 최솟값을 구하시오.</p>
<span class="cond">모든 자연수 <span class="m">n</span>에 대하여
<span class="m">S<sub>n+1</sub> − S<sub>n</sub> = 3n + 14</span>이다.</span>

## 발상

<b><span class="m">S<sub>n+1</sub></span>은 <span class="m">S<sub>n</sub></span>보다
항을 하나 더 더한 것</b>이다. 그러므로 둘의 차는 그 하나, 곧
<span class="m">a<sub>n+1</sub></span>이다.<br><br>
주어진 조건은 겉보기에 <span class="m">S</span>에 대한 것이지만
<b>사실은 항을 직접 알려 주고 있다.</b>

## 풀이

<p><span class="step">① 차가 곧 다음 항임을 쓴다.</span>
<span class="m">S<sub>n</sub> = a<sub>1</sub> + ⋯ + a<sub>n</sub></span>,
<span class="m">S<sub>n+1</sub> = a<sub>1</sub> + ⋯ + a<sub>n</sub> + a<sub>n+1</sub></span>이므로</p>
<p class="m">S<sub>n+1</sub> − S<sub>n</sub> = a<sub>n+1</sub></p>
<p>따라서 주어진 조건은 다음과 같다.</p>
<p class="m">a<sub>n+1</sub> = 3n + 14 &nbsp; (n ≥ 1)</p>

<p><span class="step">② 일반항으로 고친다.</span>
위 식은 <span class="m">2</span>번째 항부터를 알려 준다.
<span class="m">m = n + 1</span>로 놓으면 <span class="m">n = m − 1</span>이므로</p>
<p class="m">a<sub>m</sub> = 3(m − 1) + 14 = 3m + 11 &nbsp; (m ≥ 2)</p>
<p><b>첫째항도 이 식을 따르는지 확인한다.</b>
등차수열이므로 공차는 <span class="m">3</span>이고,
<span class="m">a<sub>2</sub> = 3 × 2 + 11 = 17</span>에서 공차를 빼면</p>
<p class="m">a<sub>1</sub> = 17 − 3 = 14</p>
<p><span class="m">m = 1</span>을 식에 넣어도 <span class="m">3 + 11 = 14</span>로 같다.
따라서 모든 <span class="m">m</span>에 대해 다음이 성립한다.</p>
<p class="m">a<sub>m</sub> = 3m + 11</p>

<p><span class="step">③ 조건을 만족시키는 k를 찾는다.</span></p>
<p class="m">a<sub>k</sub> &gt; 100 → 3k + 11 &gt; 100 → 3k &gt; 89 → k &gt; 89/3 = 29.67…</p>
<p><span class="m">k</span>는 자연수이므로 가장 작은 값은 <span class="m">30</span>이다.
(<span class="m">a<sub>29</sub> = 98</span>로 <span class="m">100</span>보다 작고,
<span class="m">a<sub>30</sub> = 101</span>로 크다.)</p>

<p><span class="step">④ 답을 만든다.</span>
<span class="m">a<sub>1</sub></span>은 <span class="m">14</span>로 고정된 값이므로
<span class="m">k</span>가 가장 작을 때 합도 가장 작다.</p>
<p class="m">a<sub>1</sub> + k = 14 + 30 = 44</p>
<p class="m">답 44</p>

## 함정

<b><span class="m">S<sub>n+1</sub> − S<sub>n</sub> = a<sub>n+1</sub></span>이지
<span class="m">a<sub>n</sub></span>이 아니다.</b> 첨자를 하나 잘못 보면
일반항이 <span class="m">3n + 14</span>가 되어 <span class="m">a<sub>1</sub> = 17</span>,
<span class="m">k = 29</span>로 답이 <span class="m">46</span>이 된다.<br><br>
그리고 <b><span class="m">k &gt; 29.67</span>이므로 <span class="m">k = 30</span></b>이다.
부등호가 <span class="m">&gt;</span>라서 <span class="m">a<sub>k</sub> = 100</span>인 경우는
포함되지 않는다는 것도 확인해 둔다.

## 노하우

<b><span class="m">S<sub>n</sub></span>과 <span class="m">a<sub>n</sub></span>의 관계는
&lsquo;합의 차가 항&rsquo;이다.</b>
<span class="m">a<sub>n</sub> = S<sub>n</sub> − S<sub>n−1</sub> (n ≥ 2)</span>,
<span class="m">a<sub>1</sub> = S<sub>1</sub></span>.
첨자를 <b>반드시 종이에 적어 놓고</b> 확인한다.<br><br>
그리고 <b>일반항을 구했으면 <span class="m">n = 1</span>에서도 성립하는지 확인</b>한다.
성립하면 그대로 쓰고, 아니면 첫째항을 따로 적어야 한다.
이 문제는 다행히 <span class="m">n = 1</span>에서도 맞는다.
