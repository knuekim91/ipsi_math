---
id: PRB-C28
unit: 07-경우의수확률
topic: 비증가 함수의 개수
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 28번
exam: 2027-수능완성
origin: 기출
core: "크기 순서가 정해진 함수는 중복조합으로 세고 f(2)≥f(4)라는 제약이 여사건을 줄인다"
tags: [중복조합,함수의개수,여사건]
status: seed
added: 2026-09-07
answer: ①
---

## 문제

<p>집합 <span class="m">X = {1, 2, 3, 4, 5, 6}</span>에 대하여
다음 조건을 만족시키는 함수 <span class="m">f : X → X</span>의 개수는?</p>
<span class="cond">(가) 집합 <span class="m">X</span>의 임의의 두 원소
<span class="m">x<sub>1</sub>, x<sub>2</sub></span>에 대하여<br>
<span class="m">x<sub>1</sub> &lt; x<sub>2</sub></span>이면
<span class="m">f(x<sub>1</sub>) ≥ f(x<sub>2</sub>)</span>이다.<br>
(나) <span class="m">f(2) × f(4) ≠ 6</span></span>
<div class="choices"><span>① 432</span><span>② 438</span><span>③ 444</span>
<span>④ 450</span><span>⑤ 456</span></div>

## 발상

(가)는 <b>함숫값이 커지지 않는다</b>는 뜻이다.</p>
<p class="m">f(1) ≥ f(2) ≥ f(3) ≥ f(4) ≥ f(5) ≥ f(6)</p>
<p>이렇게 <b>크기 순서가 미리 정해진 함수는 &lsquo;값을 고르기만 하면&rsquo; 배열이 저절로 정해진다.</b>
그래서 <span class="m">6</span>개의 값에서 중복을 허용해 <span class="m">6</span>개를 고르는
<b>중복조합</b>으로 센다.<br><br>
(나)는 <span class="m">≠</span>이므로 <b>여사건</b>이다.
그리고 (가) 때문에 <span class="m">f(2) ≥ f(4)</span>여야 하므로
곱이 <span class="m">6</span>인 경우가 크게 줄어든다.

## 풀이

<p><span class="step">① (가)만 만족시키는 함수의 개수를 센다.</span>
값들이 <span class="m">f(1) ≥ f(2) ≥ ⋯ ≥ f(6)</span>으로 줄어드는 순서로 놓이므로,
<b><span class="m">1</span>부터 <span class="m">6</span>까지의 값 중에서 중복을 허용해
<span class="m">6</span>개를 고르기만 하면</b> 나열 순서는 하나로 정해진다.</p>
<p class="m"><sub>6</sub>H<sub>6</sub> = <sub>6+6−1</sub>C<sub>6</sub> = <sub>11</sub>C<sub>6</sub> = 462</p>

<p><span class="step">② 여사건 f(2)×f(4) = 6 인 경우를 찾는다.</span>
<span class="m">2 &lt; 4</span>이므로 (가)에 의해
<b><span class="m">f(2) ≥ f(4)</span></b>여야 한다.
곱이 <span class="m">6</span>이 되는 순서쌍을 모두 적어 보면</p>
<p class="m">(1, 6), (2, 3), (3, 2), (6, 1)</p>
<p>이 중 <span class="m">f(2) ≥ f(4)</span>인 것만 남긴다.</p>
<p class="m">(f(2), f(4)) = (6, 1) 또는 (3, 2)</p>

<p><span class="step">③ (6, 1)인 경우를 센다.</span>
나머지 값들이 부등식을 지켜야 한다.</p>
<p class="m">f(1) ≥ f(2) = 6 → f(1) = 6 (1가지)</p>
<p class="m">6 = f(2) ≥ f(3) ≥ f(4) = 1 → f(3) ∈ {1,2,3,4,5,6} (6가지)</p>
<p class="m">1 = f(4) ≥ f(5) ≥ f(6) ≥ 1 → f(5) = f(6) = 1 (1가지)</p>
<p class="m">1 × 6 × 1 = 6</p>

<p><span class="step">④ (3, 2)인 경우를 센다.</span></p>
<p class="m">f(1) ≥ 3 → f(1) ∈ {3,4,5,6} (4가지)</p>
<p class="m">3 ≥ f(3) ≥ 2 → f(3) ∈ {2,3} (2가지)</p>
<p class="m">2 ≥ f(5) ≥ f(6) ≥ 1 → (f(5),f(6)) = (1,1),(2,1),(2,2) (3가지)</p>
<p class="m">4 × 2 × 3 = 24</p>

<p><span class="step">⑤ 여사건을 빼서 답을 만든다.</span></p>
<p class="m">6 + 24 = 30</p>
<p class="m">462 − 30 = 432</p>
<p class="m">답 ①</p>

## 함정

<b><span class="m">(2, 3)</span>과 <span class="m">(1, 6)</span>을 세면 안 된다.</b>
곱이 <span class="m">6</span>인 순서쌍은 네 개지만,
(가)가 <span class="m">f(2) ≥ f(4)</span>를 강제하므로
<span class="m">f(2) &lt; f(4)</span>인 두 개는 애초에 존재할 수 없다.
<b>여사건을 셀 때도 (가)는 계속 살아 있다.</b><br><br>
그리고 <span class="m">f(5), f(6)</span>을 셀 때
<b><span class="m">f(5) ≥ f(6)</span>이라는 순서까지 지켜야</b> 한다.
그냥 <span class="m">2 × 2 = 4</span>가지로 세면 <span class="m">(1,2)</span>가 끼어 틀린다.

## 노하우

<b>&lsquo;커지지 않는다&rsquo; 또는 &lsquo;작아지지 않는다&rsquo;는 함수는 중복조합으로 센다.</b>
순서가 이미 정해져 있으므로 <b>어떤 값을 몇 개 쓸지만 고르면</b> 되기 때문이다.</p>
<p class="m">X에서 X로 가는 비증가 함수의 개수 = <sub>n</sub>H<sub>n</sub> = <sub>2n−1</sub>C<sub>n</sub></p>
<p><b>구간을 나눠 세는 것도 익혀 둔다.</b>
<span class="m">f(2)</span>와 <span class="m">f(4)</span>가 정해지면
그 사이(<span class="m">f(3)</span>), 앞(<span class="m">f(1)</span>),
뒤(<span class="m">f(5), f(6)</span>)가 서로 독립적으로 정해지므로 곱하면 된다.
