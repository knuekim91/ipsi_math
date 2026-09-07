---
id: DIF-C19
unit: 05-미분
topic: 증가·감소 구간이 주는 k의 범위
level: 3점
difficulty: 중상
source: 2027 수능완성 실전 모의고사 1회 19번
exam: 2027-수능완성
origin: 기출
core: "f′의 두 근이 곧 α와 β인데 k의 부호에 따라 큰 쪽 작은 쪽이 뒤바뀐다"
tags: [삼차함수,증가감소,도함수,경우나누기]
status: seed
added: 2026-09-07
answer: 90
---

## 문제

<p>두 실수 <span class="m">α, β (α &lt; β)</span>와 삼차함수
<span class="m">f(x) = x<sup>3</sup> + 2kx<sup>2</sup> − 4k<sup>2</sup>x + 5</span>가
다음 조건을 만족시키도록 하는 모든 실수 <span class="m">k</span>의 값의 범위는
<span class="m">a &lt; k &lt; b</span>이다.
<span class="m">120 × a × b</span>의 값을 구하시오.</p>
<span class="cond">(가) 함수 <span class="m">f(x)</span>는 구간
<span class="m">(−∞, α]</span>와 구간 <span class="m">[β, ∞)</span>에서 증가하고,
닫힌구간 <span class="m">[α, β]</span>에서 감소한다.<br>
(나) <span class="m">−1 &lt; α &lt; 1</span>, <span class="m">β &gt; 1</span></span>

## 발상

(가)는 <b><span class="m">α</span>와 <span class="m">β</span>가 바로
<span class="m">f′(x) = 0</span>의 두 근</b>이라는 뜻이다.
증가 → 감소 → 증가로 바뀌는 지점이기 때문이다.<br><br>
<b>그런데 <span class="m">f′</span>의 두 근을 구해 보면 어느 쪽이 큰지가
<span class="m">k</span>의 부호에 따라 뒤바뀐다.</b>
그래서 <span class="m">k &gt; 0</span>과 <span class="m">k &lt; 0</span>으로 갈라야 한다.
이 갈래를 놓치면 답이 나오지 않는다.

## 풀이

<p><span class="step">① 도함수를 구해 인수분해한다.</span></p>
<p class="m">f′(x) = 3x<sup>2</sup> + 4kx − 4k<sup>2</sup></p>
<p>곱이 <span class="m">3 × (−4k<sup>2</sup>) = −12k<sup>2</sup></span>,
합이 <span class="m">4k</span>가 되도록 쪼개면
<span class="m">6k</span>와 <span class="m">−2k</span>이다.</p>
<p class="m">f′(x) = (3x − 2k)(x + 2k)</p>
<p>(전개해서 확인하면
<span class="m">3x<sup>2</sup> + 6kx − 2kx − 4k<sup>2</sup> = 3x<sup>2</sup> + 4kx − 4k<sup>2</sup></span> ✓)</p>
<p class="m">f′(x) = 0 → x = 2k/3 또는 x = −2k</p>

<p><span class="step">② α와 β가 무엇인지 정한다.</span>
최고차항의 계수가 <span class="m">1</span>로 양수이므로
<span class="m">f</span>는 <b>증가 → 감소 → 증가</b> 모양이고,
(가)의 <span class="m">α, β</span>는 위 두 근이다.
다만 <span class="m">α &lt; β</span>여야 하므로 <b>어느 쪽이 작은지 따져야 한다.</b></p>
<p class="m">k &gt; 0 : 2k/3 &gt; 0 &gt; −2k → α = −2k, β = 2k/3</p>
<p class="m">k &lt; 0 : 2k/3 &lt; 0 &lt; −2k → α = 2k/3, β = −2k</p>
<p><span class="m">k = 0</span>이면 <span class="m">f′(x) = 3x<sup>2</sup> ≥ 0</span>이라
감소하는 구간이 없어 (가)에 어긋난다. 따라서 <span class="m">k ≠ 0</span>이다.</p>

<p><span class="step">③ k &gt; 0인 경우를 확인한다.</span>
(나)의 두 조건을 각각 쓴다.</p>
<p class="m">−1 &lt; α &lt; 1 → −1 &lt; −2k &lt; 1</p>
<p>각 변을 <span class="m">−2</span>로 나눈다. <b>음수로 나누므로 부등호가 뒤집힌다.</b></p>
<p class="m">1/2 &gt; k &gt; −1/2, 곧 −1/2 &lt; k &lt; 1/2</p>
<p><span class="m">k &gt; 0</span>과 합치면 <span class="m">0 &lt; k &lt; 1/2</span>이다.</p>
<p>한편 <span class="m">β &gt; 1</span>은</p>
<p class="m">2k/3 &gt; 1 → k &gt; 3/2</p>
<p><span class="m">k &lt; 1/2</span>이면서 <span class="m">k &gt; 3/2</span>일 수는 없다.
<b>이 경우는 불가능하다.</b></p>

<p><span class="step">④ k &lt; 0인 경우를 확인한다.</span></p>
<p class="m">−1 &lt; α &lt; 1 → −1 &lt; 2k/3 &lt; 1</p>
<p>각 변에 <span class="m">3/2</span>을 곱한다. <b>양수를 곱하므로 방향은 그대로다.</b></p>
<p class="m">−3/2 &lt; k &lt; 3/2</p>
<p><span class="m">k &lt; 0</span>과 합치면 <span class="m">−3/2 &lt; k &lt; 0</span>이다.</p>
<p>다음으로 <span class="m">β &gt; 1</span>은</p>
<p class="m">−2k &gt; 1 → k &lt; −1/2</p>
<p>두 범위를 겹친다.</p>
<p class="m">−3/2 &lt; k &lt; −1/2</p>

<p><span class="step">⑤ 답을 만든다.</span>
따라서 <span class="m">a = −3/2</span>, <span class="m">b = −1/2</span>이다.</p>
<p class="m">120 × (−3/2) × (−1/2) = 120 × 3/4 = 90</p>
<p class="m">답 90</p>

## 함정

<b><span class="m">k</span>의 부호를 나누지 않으면 답이 안 나온다.</b>
<span class="m">α = −2k</span>라고 한 가지로만 놓으면
<span class="m">k &gt; 0</span> 갈래만 보게 되는데 그쪽은 불가능하다.
<b>두 근의 크기 비교에 문자가 끼어 있으면 반드시 경우를 나눈다.</b><br><br>
그리고 <span class="m">−1 &lt; −2k &lt; 1</span>처럼
<b>음수로 나눌 때 부등호를 뒤집는 것</b>을 잊기 쉽다.
헷갈리면 <span class="m">−2k</span>를 통째로 한 덩어리로 보고
마지막에 <span class="m">k</span>로 옮기는 편이 안전하다.

## 노하우

<b>&lsquo;구간에서 증가·감소&rsquo; 조건은 <span class="m">f′ = 0</span>의 근을 묻는 것이다.</b>
최고차항의 계수가 양수인 삼차함수는 증가 → 감소 → 증가이므로,
감소 구간의 양 끝이 곧 <span class="m">f′</span>의 두 근이다.<br><br>
<b>근을 문자로 표현했을 때 대소가 정해지지 않으면 경우를 나눈다.</b>
<span class="m">2k/3</span>과 <span class="m">−2k</span>처럼 부호가 갈리는 두 식이 나오면
<span class="m">k &gt; 0</span>, <span class="m">k &lt; 0</span>을 각각 확인하는 것이 정석이다.
한쪽이 모순으로 죽는 경우가 대부분이다.
