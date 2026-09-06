---
id: PRB-J29
unit: 07-경우의수확률
topic: 조건부확률
level: 4점
difficulty: 중상
source: 2027-06모평 29번
exam: 2027-06모평
origin: 기출
core: "조건이 걸리면 표본공간이 3^5로 줄어든다"
tags: [조건부확률,주사위,경우의수]
status: seed
added: 2026-09-06
answer: 98
---

## 문제

<p>서로 다른 다섯 개의 주사위를 동시에 던져 나온 다섯 개의 눈의 수의 곱이 홀수일 때, 이 다섯 개의 눈의 수의 합이 15일 확률은 <span class="m">q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오. (단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

<b>곱이 홀수 ⟺ 다섯 눈이 전부 홀수.</b> 하나라도 짝수면 곱이 짝수가 되기 때문. 그러니 표본공간이 <span class='m'>{1,3,5}<sup>5</sup></span>로 줄어들고, 그 안에서 합이 15인 경우만 세면 된다.

## 풀이

<p><span class="step">① 조건을 표본공간으로 바꾼다.</span> 다섯 눈이 모두 <span class="m">1, 3, 5</span> 중 하나 → <span class="m">3<sup>5</sup> = 243</span>가지.</p><p><span class="step">② 합이 15인 경우를 센다.</span> 각 눈을 <span class="m">2b + 1 (b = 0, 1, 2)</span>로 두면</p><p class="m">합 = 2(b<sub>1</sub>+⋯+b<sub>5</sub>) + 5 = 15 → b<sub>1</sub>+⋯+b<sub>5</sub> = 5</p><p>즉 <span class="m">0 이상 2 이하</span>인 정수 5개의 합이 5인 경우의 수.</p><p><span class="step">③ 제한이 없다고 보고 빼기.</span> 합이 5인 음이 아닌 정수해는 <span class="m"><sub>9</sub>C<sub>4</sub> = 126</span>가지. 여기서 <b>어떤 <span class="m">b</span>가 3 이상</b>인 경우를 뺀다. (둘 이상이 3 이상일 수는 없다.)</p><p class="m">어느 하나를 3 이상으로 고정 : 5 × (합이 2인 해) = 5 × <sub>6</sub>C<sub>4</sub> = 5 × 15 = 75</p><p class="m">126 − 75 = 51</p><p><span class="step">④ 확률.</span></p><p class="m">51/243 = 17/81</p><p class="m">p = 81, q = 17 → p + q = 98</p>

## 함정

<b>분모를 <span class='m'>6<sup>5</sup></span>으로 두면 안 된다.</b> &lsquo;곱이 홀수일 때&rsquo;라는 조건이 이미 표본공간을 <span class='m'>3<sup>5</sup></span>으로 줄여 놓았다. 조건부확률의 분모는 <b>조건 사건</b>이다.

## 노하우

<b>조건부확률은 &lsquo;세상이 좁아진 것&rsquo;으로 읽는다.</b> <span class='m'>P(B|A) = (A와 B가 함께) ÷ (A)</span>인데, 여기서는 <b>A 안에서만 세면</b> 분모가 저절로 A가 된다. 그리고 <b>&lsquo;각 변수에 상한이 있는 정수해의 개수&rsquo;는 상한을 무시하고 센 뒤 넘치는 경우를 빼는 것</b>이 정석이다.
