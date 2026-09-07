---
id: STA-C25
unit: 08-통계
topic: 신뢰구간에서 거꾸로 읽기
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 1회 25번
exam: 2027-수능완성
origin: 기출
core: "신뢰구간의 가운데가 표본평균이고 절반 너비가 오차한계다"
tags: [신뢰구간,표본평균,정규분포]
status: seed
added: 2026-09-07
answer: ③
---

## 문제

<p>정규분포 <span class="m">N(m, σ<sup>2</sup>) (σ &gt; 0)</span>을 따르는 모집단에서
크기가 <span class="m">144</span>인 표본을 임의추출하여 얻은 표본평균이
<span class="m">x̄</span>일 때, 모평균 <span class="m">m</span>에 대한 신뢰도
<span class="m">95 %</span>의 신뢰구간이
<span class="m">49.51 ≤ m ≤ 50.49</span>이다.
<span class="m">σ × x̄</span>의 값은?
(단, <span class="m">Z</span>가 표준정규분포를 따르는 확률변수일 때,
<span class="m">P(|Z| ≤ 1.96) = 0.95</span>로 계산한다.)</p>
<div class="choices"><span>① 50</span><span>② 100</span><span>③ 150</span>
<span>④ 200</span><span>⑤ 250</span></div>

## 발상

신뢰구간은 <b>표본평균을 가운데 두고 좌우로 같은 만큼 벌린 구간</b>이다.</p>
<p class="m">x̄ − 1.96·σ/√n &nbsp; ≤ m ≤ &nbsp; x̄ + 1.96·σ/√n</p>
<p>그러므로 <b>구간의 가운데가 <span class="m">x̄</span></b>이고,
<b>구간 길이의 절반이 <span class="m">1.96σ/√n</span></b>이다.
이 두 가지를 읽어내면 <span class="m">x̄</span>와 <span class="m">σ</span>가 각각 나온다.

## 풀이

<p><span class="step">① 표본평균을 읽는다.</span>
구간의 가운데가 표본평균이므로 두 끝값의 평균을 구한다.</p>
<p class="m">x̄ = (49.51 + 50.49)/2 = 100/2 = 50</p>

<p><span class="step">② 오차한계를 읽는다.</span>
구간 길이의 절반이 오차한계다.</p>
<p class="m">(50.49 − 49.51)/2 = 0.98/2 = 0.49</p>
<p>이 값이 <span class="m">1.96 × σ/√144</span>와 같다.</p>

<p><span class="step">③ σ를 구한다.</span>
<span class="m">√144 = 12</span>이므로</p>
<p class="m">1.96 × σ/12 = 0.49</p>
<p>양변에 <span class="m">12</span>를 곱한다.</p>
<p class="m">1.96σ = 5.88</p>
<p>양변을 <span class="m">1.96</span>으로 나눈다.</p>
<p class="m">σ = 5.88 ÷ 1.96 = 3</p>

<p><span class="step">④ 답을 만든다.</span></p>
<p class="m">σ × x̄ = 3 × 50 = 150</p>
<p class="m">답 ③</p>

## 함정

<b>구간의 &lsquo;길이&rsquo;와 &lsquo;길이의 절반&rsquo;을 헷갈리면 안 된다.</b>
<span class="m">50.49 − 49.51 = 0.98</span>은 <b>전체 길이</b>이고,
오차한계는 그 절반인 <span class="m">0.49</span>다.
전체 길이를 그대로 쓰면 <span class="m">σ = 6</span>이 되어
답이 <span class="m">300</span>이 된다.<br><br>
그리고 <b><span class="m">√n</span>이지 <span class="m">n</span>이 아니다.</b>
<span class="m">144</span>가 아니라 <span class="m">12</span>로 나눈다.

## 노하우

<b>신뢰구간 문제는 &lsquo;가운데&rsquo;와 &lsquo;절반 너비&rsquo; 두 개만 읽으면 된다.</b></p>
<p class="m">가운데 = x̄, &nbsp; 절반 너비 = z × σ/√n</p>
<p>신뢰도 <span class="m">95 %</span>면 <span class="m">z = 1.96</span>,
<span class="m">99 %</span>면 <span class="m">z = 2.58</span>이다.<br><br>
<b>구간이 주어지고 <span class="m">σ</span>나 <span class="m">n</span>을 물으면
거꾸로 읽는 문제</b>다. 공식을 세워 놓고 아는 값을 넣어 미지수를 남긴다.
