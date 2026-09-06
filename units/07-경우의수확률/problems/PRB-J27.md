---
id: PRB-J27
unit: 07-경우의수확률
topic: 함수의 개수와 여사건
level: 3점
difficulty: 중
source: 2027-06모평 27번
exam: 2027-06모평
origin: 기출
core: "조건을 어기는 경우가 단 한 가지뿐이라 여사건이 압도적으로 짧다"
tags: [함수의개수,여사건]
status: seed
added: 2026-09-06
answer: ④
---

## 문제

<p>두 집합 <span class="m">X = {1, 2, 3, 4, 5}</span>, <span class="m">Y = {1, 2, 3}</span>에 대하여 <span class="m">X</span>에서 <span class="m">Y</span>로의 함수 <span class="m">f</span> 중 <span class="m">f(1) × f(2) ≠ 4</span>를 만족시키는 함수 <span class="m">f</span>의 개수는?</p><div class="choices"><span>① 189</span><span>② 198</span><span>③ 207</span><span>④ 216</span><span>⑤ 225</span></div>

## 발상

<b><span class='m'>≠</span> 조건은 여사건이다.</b> <span class='m'>f(1)f(2) = 4</span>가 되는 경우를 세서 전체에서 빼면 된다. <span class='m'>Y = {1,2,3}</span>이라 곱이 4인 조합은 <span class='m'>(2,2)</span> 하나뿐이다. <span class='m'>(1,4)</span>와 <span class='m'>(4,1)</span>은 <span class='m'>4 ∉ Y</span>라 불가능하다.

## 풀이

<p><span class="step">① &lsquo;≠&rsquo;를 보고 여사건을 택한다.</span>
조건이 <span class="m">f(1) × f(2) ≠ 4</span>이므로,
<b>곱이 <span class="m">4</span>가 되는 경우를 세서 전체에서 빼는 편</b>이 훨씬 짧다.</p>

<p><span class="step">② 전체 함수의 개수를 센다.</span>
<span class="m">X</span>의 원소 <span class="m">1, 2, 3, 4, 5</span> 각각에 대해
<span class="m">Y = {1, 2, 3}</span>의 값 하나를 정하면 함수가 하나 만들어진다.
각 원소마다 <span class="m">3</span>가지씩이므로</p>
<p class="m">3<sup>5</sup> = 243</p>

<p><span class="step">③ 곱이 4가 되는 경우를 센다.</span>
<span class="m">f(1)</span>과 <span class="m">f(2)</span>는 <b>둘 다 <span class="m">Y = {1, 2, 3}</span>의 원소</b>다.
곱이 <span class="m">4</span>가 되는 순서쌍을 찾는다.</p>
<p class="m">1 × 4 = 4 → 4는 Y에 없다 (불가능)</p>
<p class="m">2 × 2 = 4 → 가능</p>
<p class="m">4 × 1 = 4 → 4는 Y에 없다 (불가능)</p>
<p>따라서 가능한 것은 <b><span class="m">(f(1), f(2)) = (2, 2)</span> 하나뿐</b>이다.</p>

<p><span class="step">④ 나머지 값은 자유임을 확인한다.</span>
<span class="m">f(3), f(4), f(5)</span>에는 아무 조건이 없으므로 각각 <span class="m">3</span>가지다.</p>
<p class="m">1 × 3<sup>3</sup> = 27</p>

<p><span class="step">⑤ 빼서 답을 만든다.</span></p>
<p class="m">243 − 27 = 216</p>
<p class="m">답 ④</p>

## 함정

<span class='m'>1 × 4 = 4</span>, <span class='m'>4 × 1 = 4</span>를 습관적으로 세면 안 된다. <b>공역이 <span class='m'>{1,2,3}</span>이라 4는 함숫값이 될 수 없다.</b> 이 두 경우를 넣으면 <span class='m'>243 − 81 = 162</span>가 되어 보기에도 없다.

## 노하우

<b><span class='m'>≠</span>가 보이면 여사건부터 떠올린다.</b> 그리고 <b>곱이 특정 값인 순서쌍을 셀 때는 반드시 공역 안에 있는 수인지 확인</b>한다. 약수를 기계적으로 나열하다 공역 밖의 수를 쓰는 것이 이 유형의 대표 실수다.
