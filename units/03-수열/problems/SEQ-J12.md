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

<p><span class="step">① 첫째항과 공비로 쓴다.</span> <span class="m">a<sub>1</sub> = a</span>, 공비 <span class="m">r</span>.</p><p class="m">2a·a(1 + r<sup>2</sup>) = 2a<sup>2</sup>(1 + r<sup>2</sup>) = 20</p><p class="m">5ar·a(1 + r) = 5a<sup>2</sup>r(1 + r) = 20</p><p><span class="step">② 나눈다.</span></p><p class="m">(1 + r<sup>2</sup>) / (r(1 + r)) · (2/5) = 1 → 2(1 + r<sup>2</sup>) = 5r(1 + r)</p><p class="m">3r<sup>2</sup> + 5r − 2 = 0 → (3r − 1)(r + 2) = 0</p><p>공비가 양수이므로 <span class="m">r = 1/3</span>.</p><p><span class="step">③ a<sup>2</sup>을 구한다.</span> <span class="m">2a<sup>2</sup>(1 + 1/9) = 20 → a<sup>2</sup> = 9</span></p><p><span class="step">④</span> <span class="m">a<sub>1</sub>a<sub>6</sub> = a · ar<sup>5</sup> = a<sup>2</sup>r<sup>5</sup> = 9 · (1/3)<sup>5</sup> = 1/27</span></p>

## 노하우

<b>등비수열의 연립은 &lsquo;나눠서 첫째항을 지운다&rsquo;가 첫 수순.</b> 그리고 구하는 것이 <span class='m'>a<sub>1</sub>a<sub>6</sub></span>처럼 곱이면 <span class='m'>a<sup>2</sup>r<sup>5</sup></span> 꼴이라 <b>a를 따로 구할 필요 없이 a<sup>2</sup>만</b> 있으면 된다.
