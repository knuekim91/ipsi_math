---
id: DIF-J07
unit: 05-미분
topic: 삼차함수의 극대·극소
level: 3점
difficulty: 중
source: 2027-06모평 7번
exam: 2027-06모평
origin: 기출
core: "극대점을 f′=0에 넣어 미지수를 없앤 뒤 극소를 찾는다"
tags: [극값,삼차함수]
status: seed
added: 2026-09-06
answer: ②
---

## 문제

<p class="m">함수 f(x) = x<sup>3</sup> + ax + 9 는 x = −1에서 극대이다. 함수 f(x)의 극솟값은? (단, a는 상수)</p><div class="choices"><span>① 6</span><span>② 7</span><span>③ 8</span><span>④ 9</span><span>⑤ 10</span></div>

## 발상

<b>극대 조건 <span class='m'>f′(−1) = 0</span> 하나로 a가 결정</b>된다. 그 다음 f′을 인수분해하면 극소점이 보인다.

## 풀이

<p><span class="step">① 극대 조건을 식으로 바꾼다.</span>
미분가능한 함수가 <span class="m">x = −1</span>에서 극값을 가지면
그 점에서 접선이 수평이므로 <span class="m">f′(−1) = 0</span>이다.
<b>이 한 줄이 미지수 <span class="m">a</span>를 결정한다.</b></p>
<p class="m">f(x) = x<sup>3</sup> + ax + 9 → f′(x) = 3x<sup>2</sup> + a</p>
<p class="m">f′(−1) = 3 × (−1)<sup>2</sup> + a = 3 + a = 0</p>
<p class="m">a = −3</p>

<p><span class="step">② 도함수를 인수분해한다.</span>
<span class="m">a = −3</span>을 넣는다.</p>
<p class="m">f′(x) = 3x<sup>2</sup> − 3 = 3(x<sup>2</sup> − 1) = 3(x + 1)(x − 1)</p>
<p>따라서 <span class="m">f′(x) = 0</span>인 점은 <span class="m">x = −1</span>과 <span class="m">x = 1</span>이다.</p>

<p><span class="step">③ 어느 쪽이 극소인지 판정한다.</span>
<span class="m">f′(x)</span>는 아래로 볼록한 이차함수이므로 두 근 사이에서만 음수다.
즉 <span class="m">f</span>는 <b>증가 → 감소 → 증가</b>이고,
<b>작은 근에서 극대, 큰 근에서 극소</b>다.</p>
<p class="m">x = −1에서 극대 (문제 조건과 일치 ✓), &nbsp; x = 1에서 극소</p>

<p><span class="step">④ 극솟값을 계산한다.</span>
<span class="m">a = −3</span>을 넣은 <span class="m">f(x) = x<sup>3</sup> − 3x + 9</span>에
<span class="m">x = 1</span>을 대입한다.</p>
<p class="m">f(1) = 1 − 3 + 9 = 7</p>
<p class="m">답 ②</p>

## 노하우

<b>삼차함수는 최고차 계수가 양수면 작은 근에서 극대, 큰 근에서 극소.</b> 표를 그리기 전에 이것만 알아도 절반이 끝난다.
