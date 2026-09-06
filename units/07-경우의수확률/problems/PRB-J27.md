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

<b><span class='m'>≠</span> 조건은 여사건이다.</b> <span class='m'>f(1)f(2) = 4</span>가 되는 경우를 세서 전체에서 빼면 된다. <span class='m'>Y = {1,2,3}</span>이라 곱이 4인 조합은 <span class='m'>(2,2)</span> 하나뿐 — <span class='m'>(1,4)</span>와 <span class='m'>(4,1)</span>은 <span class='m'>4 ∉ Y</span>라 불가능하다.

## 풀이

<p><span class="step">① 전체.</span> 원소 5개가 각각 3가지 → <span class="m">3<sup>5</sup> = 243</span></p><p><span class="step">② 여사건 f(1)f(2) = 4.</span> <span class="m">f(1), f(2) ∈ {1,2,3}</span>이므로 곱이 4가 되는 순서쌍은</p><p class="m">(f(1), f(2)) = (2, 2) &nbsp; 뿐</p><p><span class="m">f(3), f(4), f(5)</span>는 자유이므로 <span class="m">3<sup>3</sup> = 27</span>가지.</p><p><span class="step">③</span></p><p class="m">243 − 27 = 216</p>

## 함정

<span class='m'>1 × 4 = 4</span>, <span class='m'>4 × 1 = 4</span>를 습관적으로 세면 안 된다. <b>공역이 <span class='m'>{1,2,3}</span>이라 4는 함숫값이 될 수 없다.</b> 이 두 경우를 넣으면 <span class='m'>243 − 81 = 162</span>가 되어 보기에도 없다.

## 노하우

<b><span class='m'>≠</span>가 보이면 여사건부터 떠올린다.</b> 그리고 <b>곱이 특정 값인 순서쌍을 셀 때는 반드시 공역 안에 있는 수인지 확인</b>한다. 약수를 기계적으로 나열하다 공역 밖의 수를 쓰는 것이 이 유형의 대표 실수다.
