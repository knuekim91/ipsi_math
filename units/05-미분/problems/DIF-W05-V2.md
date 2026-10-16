---
id: DIF-W05-V2
parent: DIF-W05
unit: 05-미분
topic: 같은 함숫값을 갖는 두 점의 합의 범위
level: 4점
difficulty: 상
source: 자체 개발 (DIF-W05 변형 · 합의 범위와 두 극점)
origin: 유사문항
core: "두 점의 중점은 언제나 극대점과 극소점 사이에 있다. 그래서 x₁+x₂의 범위의 양 끝은 두 극점의 두 배다"
tags: [삼차함수,같은함숫값,대칭식,판별식,극점]
status: variant
added: 2026-10-17
answer: 8
---

## 문제

<p>삼차함수 <span class="m">f(x) = x<sup>3</sup> − 6x<sup>2</sup> + 11</span>에 대하여
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>,
<span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>를 만족시키는 두 실수
<span class="m">x<sub>1</sub></span>, <span class="m">x<sub>2</sub></span>에 대하여
<span class="m">x<sub>1</sub> + x<sub>2</sub></span>의 값의 범위가</p>

<p class="m">α &lt; x<sub>1</sub> + x<sub>2</sub> &lt; β</p>

<p>일 때, <span class="m">α + β</span>의 값을 구하시오.</p>

## 발상

<b>앞 문항에서 범위를 구하느라 썼던 판별식이, 이번에는 답 그 자체다.</b>
<span class="m">s = x<sub>1</sub> + x<sub>2</sub></span>의 범위를 구하는 것이
문제의 전부이므로 <b>관계식을 세우고 판별식만 풀면 끝난다.</b><br><br>

<b>그런데 이 범위에는 뜻이 있다.</b>
<span class="m">s/2</span>는 두 점의 <b>중점</b>이다.
같은 높이의 두 점을 극대점에 바싹 붙이면 중점이 극대점으로 가고,
극소점에 바싹 붙이면 중점이 극소점으로 간다.
<b>곧 중점은 두 극점 사이를 꽉 채우며 움직인다.</b><br><br>

<b>그래서 양 끝은 두 극점의 두 배</b>이고,</p>
<p class="m">α + β = 2 × (극대점 + 극소점)</p>
<p>이 된다. <b>이것을 알면 판별식을 풀지 않고 미분 한 번으로 끝낼 수 있다.</b>
두 길을 모두 적어 둔다.

## 풀이

<p><span class="step">① 관계식을 세운다.</span>
<span class="m">f(x<sub>1</sub>) = f(x<sub>2</sub>)</span>,
<span class="m">x<sub>1</sub> ≠ x<sub>2</sub></span>에서</p>
<p class="m">x<sub>1</sub><sup>2</sup> + x<sub>1</sub>x<sub>2</sub> + x<sub>2</sub><sup>2</sup> − 6(x<sub>1</sub> + x<sub>2</sub>) = 0</p>
<p><span class="m">s = x<sub>1</sub> + x<sub>2</sub></span>,
<span class="m">p = x<sub>1</sub>x<sub>2</sub></span>로 놓으면</p>
<p class="m">s<sup>2</sup> − p − 6s = 0 → p = s<sup>2</sup> − 6s</p>

<p><span class="step">② 판별식으로 s의 범위를 구한다.</span>
<span class="m">x<sub>1</sub></span>, <span class="m">x<sub>2</sub></span>는
<span class="m">t<sup>2</sup> − st + p = 0</span>의 서로 다른 두 실근이다.</p>
<p class="m">s<sup>2</sup> − 4p = s<sup>2</sup> − 4(s<sup>2</sup> − 6s) = −3s<sup>2</sup> + 24s &gt; 0</p>
<p class="m">3s(s − 8) &lt; 0 → 0 &lt; s &lt; 8</p>

<p><span class="step">③ 답을 만든다.</span></p>
<p class="m">α = 0, &nbsp; β = 8 → α + β = 8</p>
<p class="m">답 8</p>

## 다른 풀이

<p><span class="step">① 두 극점을 구한다.</span></p>
<p class="m">f′(x) = 3x<sup>2</sup> − 12x = 3x(x − 4)</p>
<p>극대점은 <span class="m">x = 0</span>, 극소점은
<span class="m">x = 4</span>다.</p>

<p><span class="step">② 중점이 두 극점 사이를 움직인다.</span>
같은 높이의 두 점을 극대점 양옆에 바싹 붙이면 중점이
<span class="m">0</span>에 가까워지고,
극소점 양옆에 바싹 붙이면 중점이 <span class="m">4</span>에 가까워진다.
두 점이 겹치면 안 되므로 양 끝은 포함하지 않는다.</p>
<p class="m">0 &lt; (x<sub>1</sub> + x<sub>2</sub>)/2 &lt; 4</p>
<p class="m">0 &lt; x<sub>1</sub> + x<sub>2</sub> &lt; 8</p>
<p class="m">α + β = 8</p>

<p><b>미분 한 번으로 끝난다.</b>
판별식을 풀지 않아도 되므로 시간이 반으로 줄어든다.</p>

## 함정

<b><span class="m">α</span>를 <span class="m">0</span>이 아닌 수로 쓰지 않는다.</b>
<span class="m">f(x) = x<sup>3</sup> − 6x<sup>2</sup> + 11</span>에는
일차항이 없어서 극대점이 마침 <span class="m">x = 0</span>이다.
<b>일차항이 있으면 <span class="m">α</span>는 <span class="m">0</span>이 아니다.</b>
공식처럼 <span class="m">α = 0</span>을 외우지 않는다.<br><br>

<b>상수항 <span class="m">11</span>과 세 실근을 구하려 들지 않는다.</b>
<span class="m">f(x) = 0</span>의 근을 구해 봐야 아무 쓸모가 없다.
<b>관계식에는 상수항이 들어오지 않는다.</b><br><br>

<b>판별식의 부등호 방향을 뒤집지 않는다.</b>
<span class="m">−3s<sup>2</sup> + 24s &gt; 0</span>의 양변을
<span class="m">−3</span>으로 나누면 <b>부등호가 바뀌어</b>
<span class="m">s<sup>2</sup> − 8s &lt; 0</span>이 된다.
방향을 놓치면 <span class="m">s &lt; 0</span> 또는
<span class="m">s &gt; 8</span>이라는 엉뚱한 답이 나온다.

## 노하우

<b><span class="m">x<sub>1</sub> + x<sub>2</sub></span>의 범위는 두 극점이 정해 준다.</b></p>
<p class="m">2 × 극대점 &lt; x<sub>1</sub> + x<sub>2</sub> &lt; 2 × 극소점</p>
<p><span class="m">f(x) = x<sup>3</sup> + ax<sup>2</sup> + bx + c</span>에서
두 극점의 합은 <span class="m">−2a/3</span>이므로</p>
<p class="m">α + β = 2 × (−2a/3) = −4a/3</p>
<p><b><span class="m">b</span>와 <span class="m">c</span>는 답에 끼어들지 못한다.</b>
<span class="m">a = −6</span>이므로 <span class="m">8</span>이다.
<b>이 식 하나로 검산하면 몇 초 만에 끝난다.</b><br><br>

<b>이 성질이 모문항의 <span class="m">M</span>을 설명한다.</b>
두 점을 극소점에 바싹 붙이면 <b>둘 다 극소점 근처의 양수</b>가 되어
<span class="m">x<sub>1</sub>x<sub>2</sub> &gt; 0</span>이 된다.
그 쌍의 <span class="m">x<sub>2</sub></span>는 언제나 극소점보다 크므로
<b>울타리를 극소점까지 밀 수 있다.</b>
그래서 <span class="m">M</span>이 극소점이었다.
<b>세 문항이 같은 성질을 다른 각도에서 묻고 있다.</b><br><br>

<b>중점으로 생각하는 습관을 들인다.</b>
<span class="m">s</span> 자체보다 <span class="m">s/2</span>가 그래프 위에서
의미를 갖는다. <b>합이 나오면 반으로 나눠 중점으로 바꿔 본다.</b>
