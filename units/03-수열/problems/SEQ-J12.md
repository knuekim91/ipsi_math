---
id: SEQ-J12
unit: 03-수열
topic: 등비수열의 연립
level: 4점
difficulty: 중상
source: 2027-06모평 12번
exam: 2027-06모평
origin: 기출
core: "두 식을 나누면 첫째항이 지워지고 공비만의 방정식이 된다"
tags: [등비수열,연립,공비]
status: seed
added: 2026-09-06
answer: ①
---

## 문제

<p>공비가 양수인 등비수열 <span class="m">{a<sub>n</sub>}</span>이</p><span class="cond m">2a<sub>1</sub>(a<sub>1</sub> + a<sub>3</sub>) = 5a<sub>2</sub>(a<sub>1</sub> + a<sub>2</sub>) = 20</span><p>을 만족시킬 때, <span class="m">a<sub>1</sub> × a<sub>6</sub></span>의 값은?</p><div class="choices"><span>① 1/27</span><span>② 1/9</span><span>③ 1/3</span><span>④ 1</span><span>⑤ 3</span></div>

## 발상

두 식 모두 <span class='m'>a<sub>1</sub><sup>2</sup></span>을 인수로 갖는다. <b>나누면 <span class='m'>a<sub>1</sub></span>이 사라지고 공비 <span class='m'>r</span>만의 방정식</b>이 된다.

## 풀이

<p><span class="step">① 모든 항을 첫째항과 공비로 바꾼다.</span>
첫째항을 <span class="m">a</span>, 공비를 <span class="m">r</span>이라 하면
<span class="m">a<sub>2</sub> = ar</span>, <span class="m">a<sub>3</sub> = ar<sup>2</sup></span>이다.
두 조건을 각각 옮겨 쓴다.</p>
<p class="m">2a<sub>1</sub>(a<sub>1</sub> + a<sub>3</sub>) = 2a(a + ar<sup>2</sup>) = 2a<sup>2</sup>(1 + r<sup>2</sup>) = 20 &nbsp;&nbsp; … ㉠</p>
<p class="m">5a<sub>2</sub>(a<sub>1</sub> + a<sub>2</sub>) = 5ar(a + ar) = 5a<sup>2</sup>r(1 + r) = 20 &nbsp;&nbsp; … ㉡</p>
<p><b>두 식 모두 <span class="m">a<sup>2</sup></span>을 인수로 갖는다</b>는 점에 주목한다.</p>

<p><span class="step">② 두 식을 나눠 a를 지운다.</span>
㉠을 ㉡으로 나눈다. 오른쪽은 <span class="m">20/20 = 1</span>이 되고
왼쪽에서는 <span class="m">a<sup>2</sup></span>이 약분된다.</p>
<p class="m">2(1 + r<sup>2</sup>) / (5r(1 + r)) = 1</p>

<p><span class="step">③ 분모를 없애고 정리한다.</span>
양변에 <span class="m">5r(1 + r)</span>을 곱한다.</p>
<p class="m">2(1 + r<sup>2</sup>) = 5r(1 + r)</p>
<p>양쪽을 전개한다.</p>
<p class="m">2 + 2r<sup>2</sup> = 5r + 5r<sup>2</sup></p>
<p>왼쪽 항을 모두 오른쪽으로 넘긴다.</p>
<p class="m">0 = 5r<sup>2</sup> − 2r<sup>2</sup> + 5r − 2</p>
<p class="m">3r<sup>2</sup> + 5r − 2 = 0</p>

<p><span class="step">④ 인수분해하고 공비를 고른다.</span></p>
<p class="m">(3r − 1)(r + 2) = 0 → r = 1/3 또는 r = −2</p>
<p>문제에서 <b>공비가 양수</b>라 했으므로 <span class="m">r = −2</span>는 버린다.</p>
<p class="m">r = 1/3</p>

<p><span class="step">⑤ a<sup>2</sup>을 구한다.</span>
㉠에 <span class="m">r = 1/3</span>을 넣는다.</p>
<p class="m">2a<sup>2</sup>(1 + 1/9) = 20 → 2a<sup>2</sup> × 10/9 = 20</p>
<p class="m">20a<sup>2</sup>/9 = 20 → a<sup>2</sup> = 9</p>
<p><b><span class="m">a</span>가 <span class="m">3</span>인지 <span class="m">−3</span>인지는 알 필요가 없다.</b>
다음 단계에서 <span class="m">a<sup>2</sup></span>만 쓰기 때문이다.</p>

<p><span class="step">⑥ 구하는 값을 만든다.</span></p>
<p class="m">a<sub>1</sub> × a<sub>6</sub> = a × ar<sup>5</sup> = a<sup>2</sup>r<sup>5</sup> = 9 × (1/3)<sup>5</sup> = 9/243 = 1/27</p>
<p class="m">답 ①</p>

## 노하우

<b>등비수열의 연립은 &lsquo;나눠서 첫째항을 지운다&rsquo;가 첫 수순.</b> 그리고 구하는 것이 <span class='m'>a<sub>1</sub>a<sub>6</sub></span>처럼 곱이면 <span class='m'>a<sup>2</sup>r<sup>5</sup></span> 꼴이라 <b>a를 따로 구할 필요 없이 a<sup>2</sup>만</b> 있으면 된다.
