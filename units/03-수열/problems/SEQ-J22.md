---
id: SEQ-J22
unit: 03-수열
topic: 귀납적으로 정의된 수열
level: 4점
difficulty: 상
source: 2027-06모평 22번
exam: 2027-06모평
origin: 기출
core: "번호를 거꾸로 따라가 1이나 3에 닿는 경로를 세면 된다"
tags: [귀납적정의,수열,경우의수]
status: seed
added: 2026-09-06
answer: 32
---

## 문제

<p>수열 <span class="m">{a<sub>n</sub>}</span>이 <span class="m">a<sub>1</sub> = 1</span>, <span class="m">a<sub>3</sub> = 4</span>이고, 모든 자연수 <span class="m">n</span>에 대하여</p><span class="cond m">a<sub>2n</sub> = a<sub>n</sub> + 1, &nbsp; a<sub>4n+3</sub> = a<sub>4n+1</sub> = a<sub>n</sub> + 4</span><p>를 만족시킨다. <span class="m">a<sub>k</sub> = 10</span>인 자연수 <span class="m">k</span>의 개수를 구하시오.</p>

## 발상

규칙을 <b>번호를 키우는 방향</b>으로 읽으면 길이 셋뿐이다. <span class='m'>m → 2m</span> (값 <b>+1</b>), <span class='m'>m → 4m+1</span> (값 <b>+4</b>), <span class='m'>m → 4m+3</span> (값 <b>+4</b>). 출발점은 <span class='m'>a<sub>1</sub>=1</span>과 <span class='m'>a<sub>3</sub>=4</span> 둘뿐. <b>10에 도달하는 &lsquo;+1과 +4의 조합&rsquo;을 세는 문제</b>다.

## 풀이

<p><span class="step">① 규칙을 &lsquo;번호를 키우는 방향&rsquo;으로 다시 쓴다.</span>
주어진 규칙을 그대로 보면 큰 번호를 작은 번호로 되돌리는 모양이다.
이것을 뒤집어 <b>작은 번호에서 큰 번호로 가는 이동</b>으로 읽으면
길이 세 가지뿐이라는 것이 보인다.</p>
<p class="m">m → 2m : 값이 +1</p>
<p class="m">m → 4m + 1 : 값이 +4</p>
<p class="m">m → 4m + 3 : 값이 +4</p>

<p><span class="step">② 출발점이 몇 개인지 확인한다.</span>
<span class="m">k &gt; 1</span>인 번호는 다음 셋 중 하나에 반드시 해당한다.</p>
<p class="m">k가 짝수 → k = 2m 꼴</p>
<p class="m">k를 4로 나눈 나머지가 1 → k = 4m + 1 꼴</p>
<p class="m">k를 4로 나눈 나머지가 3 → k = 4m + 3 꼴</p>
<p>그러므로 번호를 거꾸로 따라가면 결국 작은 번호에 닿는다.
문제가 값을 직접 준 것은 <span class="m">a<sub>1</sub> = 1</span>과 <span class="m">a<sub>3</sub> = 4</span> <b>두 개</b>다.
(<span class="m">a<sub>3</sub></span>는 <span class="m">a<sub>4m+3</sub></span>에 <span class="m">m = 0</span>을 넣으면
<span class="m">a<sub>0</sub></span>이 필요해지므로 규칙으로 만들어지지 않는다.
<b>따로 주어진 출발점</b>이다.)</p>

<p><span class="step">③ 값이 얼마나 오르는지 센다.</span>
<span class="m">+1</span>짜리 이동을 <span class="m">i</span>번,
<span class="m">+4</span>짜리 이동을 <span class="m">j</span>번 썼다면 도착값은</p>
<p class="m">(출발값) + i × 1 + j × 4</p>
<p>목표는 <span class="m">a<sub>k</sub> = 10</span>이다.</p>

<p><span class="step">④ 한 조합이 몇 가지 번호를 만드는지 센다.</span>
이동을 <span class="m">i + j</span>번 하는데
<b>그중 어느 자리에 <span class="m">+4</span>짜리를 놓을지</b> 고르는 방법이
<span class="m"><sub>i+j</sub>C<sub>j</sub></span>가지다.
게다가 <span class="m">+4</span>짜리 이동은 <span class="m">4m+1</span>과 <span class="m">4m+3</span> 두 종류이므로
<span class="m">j</span>번 각각에서 <span class="m">2</span>가지씩 갈린다.</p>
<p class="m">가짓수 = <sub>i+j</sub>C<sub>j</sub> × 2<sup>j</sup></p>

<p><span class="step">⑤ a<sub>1</sub> = 1에서 출발하는 경우를 센다.</span>
<span class="m">1</span>에서 <span class="m">10</span>까지 <span class="m">9</span>만큼 올려야 한다.</p>
<p class="m">i + 4j = 9 → (i, j) = (9, 0), (5, 1), (1, 2)</p>
<p class="m">(9, 0) : <sub>9</sub>C<sub>0</sub> × 2<sup>0</sup> = 1 × 1 = 1</p>
<p class="m">(5, 1) : <sub>6</sub>C<sub>1</sub> × 2<sup>1</sup> = 6 × 2 = 12</p>
<p class="m">(1, 2) : <sub>3</sub>C<sub>2</sub> × 2<sup>2</sup> = 3 × 4 = 12</p>
<p class="m">소계 1 + 12 + 12 = 25</p>

<p><span class="step">⑥ a<sub>3</sub> = 4에서 출발하는 경우를 센다.</span>
<span class="m">4</span>에서 <span class="m">10</span>까지 <span class="m">6</span>만큼 올려야 한다.</p>
<p class="m">i + 4j = 6 → (i, j) = (6, 0), (2, 1)</p>
<p class="m">(6, 0) : <sub>6</sub>C<sub>0</sub> × 2<sup>0</sup> = 1</p>
<p class="m">(2, 1) : <sub>3</sub>C<sub>1</sub> × 2<sup>1</sup> = 3 × 2 = 6</p>
<p class="m">소계 1 + 6 = 7</p>

<p><span class="step">⑦ 더한다.</span>
서로 다른 이동 경로는 서로 다른 번호를 만들므로 중복 없이 그대로 더하면 된다.</p>
<p class="m">25 + 7 = 32</p>
<p class="m">답 32</p>

## 함정

<span class='m'>a<sub>3</sub></span>는 규칙으로 만들어지지 않고 <b>따로 주어진 출발점</b>이다. (<span class='m'>a<sub>4n+3</sub></span>에 <span class='m'>n=0</span>을 넣으면 <span class='m'>a<sub>0</sub></span>이 필요해진다.) 1에서 출발하는 경로만 세면 25가 나와 틀린다.

## 노하우

<b>번호에 2배·4배가 등장하는 귀납적 수열은 &lsquo;번호를 거꾸로 접는&rsquo; 문제다.</b> 규칙을 <b>번호를 키우는 이동</b>으로 다시 쓰고, 각 이동이 값을 얼마나 올리는지 표로 만든 다음, <b>목표값까지의 이동 조합을 조합론으로 센다.</b> 이때 <b>출발점이 몇 개인지</b>를 먼저 확인하는 것이 함정을 피하는 길이다.
