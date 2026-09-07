---
id: STA-C27
unit: 08-통계
topic: 표본평균의 평균·분산으로 확률분포 복원
level: 3점
difficulty: 중상
source: 2027 수능완성 실전 모의고사 1회 27번
exam: 2027-수능완성
origin: 기출
core: "E(15X̄+1)과 V(15X̄+1)에서 모평균과 모분산을 먼저 뽑아낸다"
tags: [이산확률분포,표본평균,평균과분산]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>어느 모집단의 이산확률변수 <span class="m">X</span>의 확률분포를
표로 나타내면 다음과 같다.</p>
<span class="cond"><span class="m">X</span> : 1, 2, 3, 4, 5 &nbsp; (합계)<br>
<span class="m">P(X=x)</span> : <span class="m">a</span>, <span class="m">1/5</span>,
<span class="m">2/5</span>, <span class="m">b</span>, <span class="m">c</span> &nbsp;
(합계 <span class="m">1</span>)</span>
<p>이 모집단에서 크기가 <span class="m">9</span>인 표본을 임의추출하여 구한 표본평균을
<span class="m">X̄</span>라 하자.
<span class="m">E(15X̄ + 1) = 46</span>이고
<span class="m">V(15X̄ + 1) = 30</span>일 때,
<span class="m">a + 2b + 3c</span>의 값은?</p>
<div class="choices"><span>① 3/5</span><span>② 2/3</span><span>③ 11/15</span>
<span>④ 4/5</span><span>⑤ 13/15</span></div>

## 발상

<b>표본평균의 평균은 모평균과 같고, 표본평균의 분산은 모분산을 <span class="m">n</span>으로 나눈 것</b>이다.</p>
<p class="m">E(X̄) = m, &nbsp; V(X̄) = σ<sup>2</sup>/n</p>
<p>주어진 두 조건에서 <span class="m">m</span>과 <span class="m">σ<sup>2</sup></span>을 먼저 뽑아내면,
확률의 합·평균·분산 세 식이 생겨 미지수 <span class="m">a, b, c</span> 세 개를 정확히 결정한다.

## 풀이

<p><span class="step">① 모평균 m을 구한다.</span>
상수배와 덧셈에 대해
<span class="m">E(aX+b) = aE(X) + b</span>이므로</p>
<p class="m">E(15X̄ + 1) = 15E(X̄) + 1 = 15m + 1 = 46</p>
<p class="m">15m = 45 → m = 3</p>

<p><span class="step">② 모분산 σ²을 구한다.</span>
분산에서는 <span class="m">V(aX+b) = a<sup>2</sup>V(X)</span>이고
상수 <span class="m">b</span>는 사라진다.</p>
<p class="m">V(15X̄ + 1) = 15<sup>2</sup>V(X̄) = 225 × σ<sup>2</sup>/9 = 25σ<sup>2</sup> = 30</p>
<p class="m">σ<sup>2</sup> = 30/25 = 6/5</p>

<p><span class="step">③ 세 식을 세운다.</span>
<b>확률의 합</b>이 <span class="m">1</span>이므로</p>
<p class="m">a + 1/5 + 2/5 + b + c = 1 → a + b + c = 2/5 &nbsp;&nbsp; … ㉠</p>
<p><b>평균</b>은 <span class="m">Σx P(X=x)</span>이므로</p>
<p class="m">a + 2(1/5) + 3(2/5) + 4b + 5c = 3</p>
<p class="m">a + 4b + 5c + 8/5 = 3 → a + 4b + 5c = 7/5 &nbsp;&nbsp; … ㉡</p>
<p><b>분산</b>은 <span class="m">E(X<sup>2</sup>) − m<sup>2</sup></span>이므로
먼저 <span class="m">E(X<sup>2</sup>)</span>를 구한다.</p>
<p class="m">E(X<sup>2</sup>) = σ<sup>2</sup> + m<sup>2</sup> = 6/5 + 9 = 51/5</p>
<p class="m">a + 4(1/5) + 9(2/5) + 16b + 25c = 51/5</p>
<p class="m">a + 16b + 25c + 22/5 = 51/5 → a + 16b + 25c = 29/5 &nbsp;&nbsp; … ㉢</p>

<p><span class="step">④ 연립방정식을 푼다.</span>
㉡에서 ㉠을 빼면 <span class="m">a</span>가 지워진다.</p>
<p class="m">3b + 4c = 7/5 − 2/5 = 1 &nbsp;&nbsp; … ㉣</p>
<p>㉢에서 ㉡을 빼면 역시 <span class="m">a</span>가 지워진다.</p>
<p class="m">12b + 20c = 29/5 − 7/5 = 22/5 &nbsp;&nbsp; … ㉤</p>
<p>㉣에 <span class="m">4</span>를 곱하면 <span class="m">12b + 16c = 4</span>이고,
이것을 ㉤에서 뺀다.</p>
<p class="m">4c = 22/5 − 4 = 2/5 → c = 1/10</p>
<p>㉣에 넣는다.</p>
<p class="m">3b + 4(1/10) = 1 → 3b = 1 − 2/5 = 3/5 → b = 1/5</p>
<p>㉠에 넣는다.</p>
<p class="m">a = 2/5 − 1/5 − 1/10 = 4/10 − 2/10 − 1/10 = 1/10</p>

<p><span class="step">⑤ 답을 만든다.</span></p>
<p class="m">a + 2b + 3c = 1/10 + 2(1/5) + 3(1/10) = 1/10 + 4/10 + 3/10 = 8/10 = 4/5</p>
<p class="m">답 ④</p>

## 함정

<b><span class="m">V(15X̄+1)</span>에서 <span class="m">+1</span>은 분산에 영향이 없다.</b>
그런데 <span class="m">15</span>는 <b>제곱해서</b> 곱해진다.
<span class="m">15V(X̄)</span>로 쓰면 <span class="m">σ<sup>2</sup></span>이 달라진다.<br><br>
그리고 <b><span class="m">V(X̄) = σ<sup>2</sup>/n</span>에서 <span class="m">n = 9</span>로 나누는 것</b>을
잊으면 안 된다. 표본평균은 모집단보다 덜 흩어진다.

## 노하우

<b><span class="m">E(aX+b) = aE(X)+b</span>, <span class="m">V(aX+b) = a<sup>2</sup>V(X)</span>.</b>
평균에는 상수가 그대로 더해지고, 분산에는 상수가 영향을 주지 않으며
배수는 제곱으로 커진다.<br><br>
<b>표본평균은 <span class="m">E(X̄) = m</span>, <span class="m">V(X̄) = σ<sup>2</sup>/n</span>.</b>
평균은 그대로이고 분산만 <span class="m">n</span>으로 나뉜다.<br><br>
그리고 <b>미지수가 셋이면 식도 셋이 필요하다.</b>
확률분포표 문제에서는 <b>확률의 합 · 평균 · 분산</b>이 그 셋이다.
