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

<p><span class="step">① 조건이 표본공간을 줄인다는 것을 본다.</span>
&lsquo;다섯 눈의 곱이 홀수&rsquo;라는 조건이 붙어 있다.
곱이 홀수가 되려면 <b>다섯 눈이 모두 홀수</b>여야 한다.
하나라도 짝수가 섞이면 곱이 짝수가 되기 때문이다.
그러므로 <b>세상이 <span class="m">\{1, 3, 5\}</span>만 나오는 세상으로 좁아졌다.</b></p>
<p class="m">분모(조건 사건의 경우의 수) = 3<sup>5</sup> = 243</p>
<p><b><span class="m">6<sup>5</sup></span>으로 두면 안 된다.</b>
조건부확률의 분모는 조건 사건이다.</p>

<p><span class="step">② 합이 15인 경우를 세기 좋게 바꾼다.</span>
각 눈은 <span class="m">1, 3, 5</span> 중 하나이므로
<span class="m">2b + 1</span> (<span class="m">b = 0, 1, 2</span>)로 쓸 수 있다.
다섯 개를 더하면</p>
<p class="m">합 = 2(b<sub>1</sub> + b<sub>2</sub> + ⋯ + b<sub>5</sub>) + 5</p>
<p>이것이 <span class="m">15</span>여야 하므로</p>
<p class="m">2(b<sub>1</sub> + ⋯ + b<sub>5</sub>) = 10 → b<sub>1</sub> + ⋯ + b<sub>5</sub> = 5</p>
<p>즉 <b><span class="m">0</span> 이상 <span class="m">2</span> 이하인 정수 다섯 개의 합이 <span class="m">5</span></b>인 경우의 수를 세면 된다.</p>

<p><span class="step">③ 상한을 무시하고 센 뒤 넘치는 것을 뺀다.</span>
먼저 <b>상한 없이</b> 음이 아닌 정수 다섯 개의 합이 <span class="m">5</span>인 경우를 센다.
중복조합(칸막이)으로</p>
<p class="m"><sub>5+5−1</sub>C<sub>5−1</sub> = <sub>9</sub>C<sub>4</sub> = 126</p>

<p><span class="step">④ 상한을 넘는 경우를 뺀다.</span>
어떤 <span class="m">b</span>가 <span class="m">3</span> 이상인 경우다.
합이 <span class="m">5</span>뿐이므로 <b><span class="m">3</span> 이상인 것이 둘일 수는 없다.</b>
(둘이면 합이 <span class="m">6</span> 이상이 된다.)
그러니 중복해서 뺄 걱정이 없다.</p>
<p>어느 하나를 골라(<span class="m">5</span>가지) 거기서 <span class="m">3</span>을 미리 떼어 놓으면
남은 합은 <span class="m">2</span>이고, 다시 상한 없이 세면 된다.</p>
<p class="m">5 × <sub>2+5−1</sub>C<sub>4</sub> = 5 × <sub>6</sub>C<sub>4</sub> = 5 × 15 = 75</p>
<p class="m">126 − 75 = 51</p>

<p><span class="step">⑤ 확률을 계산하고 약분한다.</span></p>
<p class="m">51/243</p>
<p>분자와 분모를 <span class="m">3</span>으로 나눈다.</p>
<p class="m">= 17/81</p>

<p><span class="step">⑥ 답을 만든다.</span>
문제가 확률을 <span class="m">q/p</span>로 썼으므로
<span class="m">q = 17</span>, <span class="m">p = 81</span>이고 둘은 서로소다.</p>
<p class="m">p + q = 81 + 17 = 98</p>
<p class="m">답 98</p>

## 함정

<b>분모를 <span class='m'>6<sup>5</sup></span>으로 두면 안 된다.</b> &lsquo;곱이 홀수일 때&rsquo;라는 조건이 이미 표본공간을 <span class='m'>3<sup>5</sup></span>으로 줄여 놓았다. 조건부확률의 분모는 <b>조건 사건</b>이다.

## 노하우

<b>조건부확률은 &lsquo;세상이 좁아진 것&rsquo;으로 읽는다.</b> <span class='m'>P(B|A) = (A와 B가 함께) ÷ (A)</span>인데, 여기서는 <b>A 안에서만 세면</b> 분모가 저절로 A가 된다. 그리고 <b>&lsquo;각 변수에 상한이 있는 정수해의 개수&rsquo;는 상한을 무시하고 센 뒤 넘치는 경우를 빼는 것</b>이 정석이다.
