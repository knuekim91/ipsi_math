---
id: DIF-C13
unit: 05-미분
topic: f(x+a)=f(x)+b 와 미분가능
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 13번
exam: 2027-수능완성
origin: 기출
core: "양변을 미분하면 f′이 주기 a인 함수가 되어 f′(0)=f′(a)가 나온다"
tags: [미분가능,주기,도함수]
status: seed
added: 2026-09-07
answer: ②
---

## 문제

<p>두 상수 <span class="m">a (a &gt; 0)</span>, <span class="m">b</span>와
실수 전체의 집합에서 미분가능한 함수 <span class="m">f(x)</span>가
다음 조건을 만족시킬 때, <span class="m">f(2a)</span>의 값은?</p>
<span class="cond">(가) <span class="m">0 ≤ x ≤ a</span>일 때,
<span class="m">f(x) = x<sup>3</sup> − 3x<sup>2</sup> + 5x</span>이다.<br>
(나) 모든 실수 <span class="m">x</span>에 대하여
<span class="m">f(x+a) = f(x) + b</span>이다.</span>
<div class="choices"><span>① 10</span><span>② 12</span><span>③ 14</span>
<span>④ 16</span><span>⑤ 18</span></div>

## 발상

조건 (나)는 <b>그래프를 오른쪽으로 <span class="m">a</span>, 위로 <span class="m">b</span>만큼
옮기면 자기 자신과 겹친다</b>는 뜻이다. 계단처럼 같은 모양이 반복된다.<br><br>
<b>여기서 양변을 미분하는 것이 열쇠다.</b> 상수 <span class="m">b</span>는 미분하면 사라지므로</p>
<p class="eqx m">f′(x+a) = f′(x)</p>
<p>가 되어 <b>도함수가 주기 <span class="m">a</span>인 함수</b>가 된다.
그러면 <span class="m">f′(0)</span>과 <span class="m">f′(a)</span>가 같아야 하고,
이 한 줄이 <span class="m">a</span>를 결정한다.

## 풀이

<p><span class="step">① 조건 (나)의 양변을 미분한다.</span>
<span class="m">f</span>가 실수 전체에서 미분가능하므로 양변을 <span class="m">x</span>로 미분할 수 있다.
오른쪽의 <span class="m">b</span>는 상수라서 미분하면 <span class="m">0</span>이다.</p>
<p class="eqx m">f′(x+a) = f′(x)</p>
<p>즉 <b><span class="m">f′</span>은 주기가 <span class="m">a</span>인 함수</b>다.
따라서 <span class="m">x = 0</span>을 넣으면</p>
<p class="eqx m">f′(a) = f′(0)</p>

<p><span class="step">② 조건 (가)로 도함수를 구해 a를 정한다.</span>
<span class="m">0 ≤ x ≤ a</span>에서
<span class="m">f(x) = x<sup>3</sup> − 3x<sup>2</sup> + 5x</span>이므로</p>
<p class="eqx m">f′(x) = 3x<sup>2</sup> − 6x + 5</p>
<p>양 끝의 값을 각각 계산한다.</p>
<p class="eqx m">f′(0) = 5, &nbsp; f′(a) = 3a<sup>2</sup> − 6a + 5</p>
<p>①에서 두 값이 같아야 하므로</p>
<p class="eqx m">3a<sup>2</sup> − 6a + 5 = 5 → 3a<sup>2</sup> − 6a = 0 → 3a(a − 2) = 0</p>
<p><span class="m">a &gt; 0</span>이므로 <span class="m">a = 0</span>은 버린다.</p>
<p class="eqx m">a = 2</p>

<p><span class="step">③ b를 구한다.</span>
조건 (나)에 <span class="m">x = 0</span>을 넣는다.</p>
<p class="eqx m">f(a) = f(0) + b → f(2) = f(0) + b</p>
<p>(가)의 식으로 두 값을 계산한다.
<span class="m">0</span>과 <span class="m">2</span> 모두
<span class="m">0 ≤ x ≤ 2</span> 안에 있으므로 그 식을 쓸 수 있다.</p>
<p class="eqx m">f(2) = 8 − 12 + 10 = 6, &nbsp; f(0) = 0</p>
<p class="eqx m">b = 6 − 0 = 6</p>

<p><span class="step">④ f(2a)를 구한다.</span>
<span class="m">2a = 4</span>인데 이것은 (가)의 구간
<span class="m">0 ≤ x ≤ 2</span> 밖이므로 <b>(가)의 식을 그대로 쓰면 안 된다.</b>
조건 (나)를 한 번 더 써서 안으로 끌어온다.</p>
<p class="eqx m">f(4) = f(2 + 2) = f(2) + b = 6 + 6 = 12</p>
<p class="m">답 ②</p>

## 함정

<b><span class="m">f(2a) = f(4)</span>에 (가)의 식을 그대로 넣으면 틀린다.</b>
<span class="m">4<sup>3</sup> − 3·4<sup>2</sup> + 5·4 = 64 − 48 + 20 = 36</span>이 나오는데,
(가)는 <span class="m">0 ≤ x ≤ a</span>에서만 쓸 수 있는 식이다.
<b>구간을 벗어나면 반드시 (나)로 되돌려야 한다.</b><br><br>
또 <span class="m">3a(a−2) = 0</span>에서 <span class="m">a = 0</span>도 나오지만
문제가 <span class="m">a &gt; 0</span>이라고 못 박아 두었다.

## 노하우

<b><span class="m">f(x+a) = f(x) + b</span> 를 보면 양변을 미분한다.</b>
상수가 사라지면서 <span class="m">f′(x+a) = f′(x)</span>, 곧
<b>도함수가 주기함수</b>가 된다.
이것이 미지수 <span class="m">a</span>를 잡는 유일한 조건인 경우가 많다.<br><br>
그리고 <b>구간이 정해진 식은 그 구간 안에서만 쓴다.</b>
바깥 값을 물으면 주어진 관계식으로 구간 안으로 옮겨 놓고 계산한다.
이 문제에서는 <span class="m">f(4) → f(2) + b</span>가 그 이동이다.
