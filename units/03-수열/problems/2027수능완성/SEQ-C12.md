---
id: SEQ-C12
unit: 03-수열
topic: 합과 항의 관계로 만든 등비수열
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 12번
exam: 2027-수능완성
origin: 기출
core: "이웃한 두 합을 빼면 aₙ이 남고 그것이 곧 등비 관계를 준다"
tags: [등비수열,수열의합,빈칸추론]
status: seed
added: 2026-09-07
answer: ③
---

## 문제

<p>모든 항이 양수인 수열 <span class="m">{a<sub>n</sub>}</span>은
<span class="m">a<sub>2</sub> = 4</span>, <span class="m">a<sub>6</sub> = 324</span>이고,
상수 <span class="m">c</span>와 모든 자연수 <span class="m">n</span>에 대하여</p>
<p class="eqx m">a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub> + ⋯ + a<sub>n</sub> = c a<sub>n+1</sub></p>
<p>을 만족시킨다. 다음은
<span class="m">(1/a<sub>1</sub>) × Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub></span>의
값을 구하는 과정이다.</p>
<span class="cond">수열 <span class="m">{a<sub>n</sub>}</span>의 모든 항이 양수이므로
<span class="m">c &gt; 0</span>이고,<br>
<span class="m">a<sub>1</sub> + ⋯ + a<sub>n</sub> = c a<sub>n+1</sub></span>,
<span class="m">a<sub>1</sub> + ⋯ + a<sub>n−1</sub> = c a<sub>n</sub> (n ≥ 2)</span><br>
에서 두 등식을 변끼리 빼면
<span class="m">a<sub>n</sub> = c a<sub>n+1</sub> − c a<sub>n</sub></span>이다. 즉,<br>
<span class="m">a<sub>n+1</sub> = ((c+1)/c) a<sub>n</sub> (n ≥ 2)</span><br>
이므로 수열 <span class="m">{a<sub>n</sub>}</span>은 둘째항부터 공비가
<span class="m">(c+1)/c</span>인 등비수열을 이룬다.<br><br>
그러므로 <span class="m">a<sub>6</sub> = ((c+1)/c)<sup>4</sup>a<sub>2</sub></span>에서
<span class="m">c = <b>(가)</b></span>이고
<span class="m">a<sub>1</sub> = <b>(나)</b></span>이다.<br>
따라서 <span class="m">(1/a<sub>1</sub>) × Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub> = <b>(다)</b></span>이다.</span>
<p>위의 <span class="m">(가), (나), (다)</span>에 알맞은 수를 각각
<span class="m">p, q, r</span>이라 할 때,
<span class="m">p + q + log<sub>3</sub>r</span>의 값은?</p>
<div class="choices"><span>① 21/2</span><span>② 11</span><span>③ 23/2</span>
<span>④ 12</span><span>⑤ 25/2</span></div>

## 발상

빈칸 추론은 <b>빈칸 다음 줄이 그 값을 어떻게 쓰는지 먼저 읽는 것</b>이 요령이다.<br><br>
그리고 마지막 <span class="m">(다)</span>는 <span class="m">10</span>개를 일일이 더하는 것이 아니다.
문제가 준 식 <span class="m">a<sub>1</sub>+⋯+a<sub>n</sub> = c a<sub>n+1</sub></span>에
<b><span class="m">n = 10</span>을 그대로 넣으면</b> 합이 한 항으로 바뀐다.

## 풀이

<p><span class="step">① (가) — 공비를 먼저 구한다.</span>
둘째항부터 공비가 <span class="m">(c+1)/c</span>인 등비수열이므로
<span class="m">a<sub>2</sub></span>에서 <span class="m">a<sub>6</sub></span>까지는
공비를 <b>네 번</b> 곱한 것이다.</p>
<p class="eqx m">a<sub>6</sub> = ((c+1)/c)<sup>4</sup> × a<sub>2</sub></p>
<p class="eqx m">324 = ((c+1)/c)<sup>4</sup> × 4 → ((c+1)/c)<sup>4</sup> = 81</p>
<p>모든 항이 양수이므로 공비도 양수다. 따라서 <span class="m">4</span>제곱근을 취할 때
음수는 버린다.</p>
<p class="eqx m">(c+1)/c = 3</p>
<p>양변에 <span class="m">c</span>를 곱한다.</p>
<p class="eqx m">c + 1 = 3c → 2c = 1 → c = 1/2</p>
<p class="m">p = 1/2</p>

<p><span class="step">② (나) — 첫째항을 구한다.</span>
주어진 식에 <span class="m">n = 1</span>을 넣으면 왼쪽은 <span class="m">a<sub>1</sub></span> 하나뿐이다.</p>
<p class="eqx m">a<sub>1</sub> = c a<sub>2</sub> = (1/2) × 4 = 2</p>
<p class="m">q = 2</p>
<p>(<span class="m">a<sub>1</sub> = 2</span>이고 <span class="m">a<sub>2</sub> = 4</span>이므로
첫째항에서 둘째항으로 갈 때의 비는 <span class="m">2</span>여서
둘째항부터의 공비 <span class="m">3</span>과 다르다. 문제가 &lsquo;둘째항부터&rsquo;라고
못 박은 이유가 이것이다.)</p>

<p><span class="step">③ (다) — 합을 한 항으로 바꾼다.</span>
주어진 식에 <span class="m">n = 10</span>을 넣는다.</p>
<p class="eqx m">Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub> = c a<sub>11</sub></p>
<p><span class="m">a<sub>11</sub></span>은 <span class="m">a<sub>2</sub></span>에서
공비 <span class="m">3</span>을 <b>아홉 번</b> 곱한 것이다.</p>
<p class="eqx m">a<sub>11</sub> = a<sub>2</sub> × 3<sup>9</sup> = 4 × 3<sup>9</sup></p>
<p class="eqx m">Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub> = (1/2) × 4 × 3<sup>9</sup> = 2 × 3<sup>9</sup></p>
<p>이제 <span class="m">a<sub>1</sub> = 2</span>로 나눈다.</p>
<p class="eqx m">(1/a<sub>1</sub>) × Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub> = (1/2) × 2 × 3<sup>9</sup> = 3<sup>9</sup></p>
<p class="m">r = 3<sup>9</sup></p>

<p><span class="step">④ 답을 만든다.</span>
<span class="m">log<sub>3</sub>3<sup>9</sup> = 9</span>이다.</p>
<p class="eqx m">p + q + log<sub>3</sub>r = 1/2 + 2 + 9 = 23/2</p>
<p class="m">답 ③</p>

## 함정

<b>첫째항이 등비수열에 끼지 않는다.</b>
<span class="m">a<sub>1</sub> = 2, a<sub>2</sub> = 4</span>이니 비가 <span class="m">2</span>인데
둘째항부터의 공비는 <span class="m">3</span>이다.
<span class="m">a<sub>11</sub></span>을 구할 때 <span class="m">a<sub>1</sub></span>에서
<span class="m">10</span>번 곱하면 틀린다. <b><span class="m">a<sub>2</sub></span>에서 <span class="m">9</span>번</b>이다.<br><br>
그리고 <span class="m">((c+1)/c)<sup>4</sup> = 81</span>에서
<span class="m">(c+1)/c = ±3</span>이지만 <b>모든 항이 양수라는 조건이 음수를 버리게 한다.</b>

## 노하우

<b>합이 항으로 주어지면 <span class="m">n</span>과 <span class="m">n−1</span>을 빼서 점화식을 만든다.</b>
이 문제처럼 <span class="m">S<sub>n</sub> = c a<sub>n+1</sub></span> 꼴이면
빼는 순간 등비 관계가 튀어나온다.<br><br>
<b>그리고 같은 식을 &lsquo;합을 구할 때&rsquo; 한 번 더 쓴다.</b>
<span class="m">Σ<sub>k=1</sub><sup>10</sup>a<sub>k</sub></span>를 등비수열의 합 공식으로 계산하려 들면
첫째항이 예외라서 복잡해진다. 주어진 식에 <span class="m">n = 10</span>을 넣으면 한 줄이다.
<b>문제가 준 식은 조건이면서 동시에 계산 도구다.</b>
