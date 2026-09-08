---
id: DIF-C13-V2
parent: DIF-C13
unit: 05-미분
topic: f(x+a)=f(x)+b 와 미분가능
level: 4점
difficulty: 상
source: 자체 개발 (DIF-C13 변형 · 상수항이 있는 경우)
origin: 유사문항
core: "양변을 미분하면 f′이 주기 a인 함수가 되어 f′(0)=f′(a)가 나오고, b는 f(a)−f(0)이므로 상수항이 살아 있다"
tags: [미분가능,주기,도함수,함수방정식]
status: variant
added: 2026-09-08
answer: 112
---

## 문제

<p>두 상수 <span class="m">a (a &gt; 0)</span>, <span class="m">b</span>와
실수 전체의 집합에서 미분가능한 함수 <span class="m">f(x)</span>가
다음 조건을 만족시킨다.</p>

<div class="cond">
<span class="cond m">(가) 0 ≤ x ≤ a일 때, f(x) = x<sup>3</sup> − 6x<sup>2</sup> + 15x + 2이다.</span>
<span class="cond m">(나) 모든 실수 x에 대하여 f(x + a) = f(x) + b이다.</span>
</div>

<p><span class="m">a × b</span>의 값을 구하시오.</p>

## 발상

<b>앞의 문항들과 구조는 같지만 함정이 하나 더 있다.
조건 (가)의 식에 <b>상수항 <span class="m">2</span></b>가 붙어 있다.</b><br><br>

<b>상수항은 <span class="m">a</span>를 구할 때는 아무 영향이 없다.</b>
미분하면 사라지기 때문이다.
그러므로 <span class="m">a</span>는 앞의 문항들과 똑같은 방법으로 구한다.
조건 (나)를 미분하여 <span class="m">f′(a) = f′(0)</span>을 얻고,
조건 (가)로 두 값을 계산해 방정식을 푼다.<br><br>

<b>하지만 <span class="m">b</span>를 구할 때는 상수항이 살아 있다.</b>
<span class="m">b = f(a) − f(0)</span>인데,
<span class="m">f(0)</span>이 <span class="m">0</span>이 아니라
<span class="m">2</span>이기 때문이다.
<b><span class="m">f(0) = 0</span>이라고 넘겨짚으면 여기서 틀린다.</b>
다행히 뺄셈이므로 상수항 <span class="m">2</span>는 서로 지워지지만,
그것을 <b>확인하고 넘어가는 것</b>과 <b>모르고 지나가는 것</b>은 다르다.

## 풀이

<p><span class="step">① 조건 (나)를 미분한다.</span>
등식이 모든 실수 <span class="m">x</span>에서 성립하므로
양변을 <span class="m">x</span>에 대하여 미분한다.
오른쪽의 <span class="m">b</span>는 상수이므로 사라진다.</p>
<p class="m">f′(x + a) = f′(x)</p>
<p>여기에 <span class="m">x = 0</span>을 대입한다.</p>
<p class="m">f′(a) = f′(0)</p>

<p><span class="step">② 도함수를 구한다.</span>
조건 (가)에서 <span class="m">0 ≤ x ≤ a</span>일 때
<span class="m">f(x) = x<sup>3</sup> − 6x<sup>2</sup> + 15x + 2</span>이므로,
상수항 <span class="m">2</span>는 미분하면 <span class="m">0</span>이 된다.</p>
<p class="m">f′(x) = 3x<sup>2</sup> − 12x + 15</p>
<p><span class="m">0</span>과 <span class="m">a</span>는 모두 이 구간의 점이므로
두 값을 이 식으로 구한다.</p>
<p class="m">f′(0) = 15</p>
<p class="m">f′(a) = 3a<sup>2</sup> − 12a + 15</p>

<p><span class="step">③ a를 구한다.</span>
①의 등식에 ②의 값을 넣는다.</p>
<p class="m">3a<sup>2</sup> − 12a + 15 = 15</p>
<p>양변에서 <span class="m">15</span>를 빼면 상수항이 사라진다.</p>
<p class="m">3a<sup>2</sup> − 12a = 0</p>
<p>공통인수 <span class="m">3a</span>로 묶는다.</p>
<p class="m">3a(a − 4) = 0 → a = 0 또는 a = 4</p>
<p><span class="m">a &gt; 0</span>이므로 <span class="m">a = 4</span>이다.</p>

<p><span class="step">④ 구간의 양 끝값을 구한다.</span>
<span class="m">a = 4</span>이므로 조건 (가)의 구간은
<span class="m">0 ≤ x ≤ 4</span>이다.
양 끝에서의 값을 구한다.
<b>이때 상수항 <span class="m">2</span>를 빠뜨리지 않는다.</b></p>
<p class="m">f(0) = 0 − 0 + 0 + 2 = 2</p>
<p class="m">f(4) = 64 − 6 × 16 + 15 × 4 + 2</p>
<p class="m">= 64 − 96 + 60 + 2 = 30</p>

<p><span class="step">⑤ b를 구한다.</span>
조건 (나)에 <span class="m">x = 0</span>을 대입한다.</p>
<p class="m">f(0 + a) = f(0) + b → f(4) = f(0) + b</p>
<p>④의 값을 넣는다.</p>
<p class="m">30 = 2 + b → b = 28</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">a × b = 4 × 28 = 112</p>
<p class="m">답 112</p>

## 함정

<b><span class="m">f(0) = 0</span>이라고 넘겨짚으면 안 된다.</b>
조건 (가)의 식에 상수항 <span class="m">2</span>가 있으므로
<span class="m">f(0) = 2</span>이다.
<span class="m">f(0) = 0</span>으로 보면
<span class="m">b = 30</span>이 되어 답이 <span class="m">120</span>이 된다.
<b>대입은 언제나 식 전체에 한다.</b><br><br>

<b>거꾸로, <span class="m">a</span>를 구할 때는 상수항을 신경 쓸 필요가 없다.</b>
미분하면 사라지기 때문이다.
<b>어느 단계에서 상수항이 살아 있고 어느 단계에서 사라지는지</b>를
구분하는 것이 이 문제의 요점이다.<br><br>

<b>구하는 것이 <span class="m">f(2a)</span>가 아니라
<span class="m">a × b</span>임을 확인한다.</b>
문제마다 묻는 대상이 다르다.
<span class="m">a</span>와 <span class="m">b</span>를 다 구해 놓고
엉뚱한 것을 답으로 적는 일이 잦다.

## 노하우

<b>상수항은 &lsquo;미분에서는 죽고 대입에서는 산다&rsquo;.</b>
<span class="m">a</span>를 구하는 단계는 미분이므로 상수항이 사라지고,
<span class="m">b</span>를 구하는 단계는 대입이므로 상수항이 살아난다.
<b>같은 상수항이 단계마다 다르게 작용한다</b>는 것을 알아 두면
비슷한 문제에서 흔들리지 않는다.<br><br>

<b><span class="m">b = f(a) − f(0)</span>에서는 결국 상수항이 지워진다.</b>
뺄셈이기 때문이다. 그래서 <span class="m">f(0)</span>을 잘못 보아도
<b>운 좋게 맞는 경우</b>가 있는데, 그것은 우연이다.
<span class="m">f(0)</span>을 정확히 적고 빼는 습관을 들인다.<br><br>

<b>도함수를 완전제곱 꼴로 보면 그림이 보인다.</b>
<span class="m">f′(x) = 3x<sup>2</sup> − 12x + 15 = 3(x − 2)<sup>2</sup> + 3</span>이므로
<span class="m">f′(x) ≥ 3 &gt; 0</span>이다.
곧 <span class="m">f</span>는 <b>계속 증가하는 함수</b>이고,
<span class="m">x = 2</span>에서 가장 완만해진다.
한 칸 <span class="m">0 ≤ x ≤ 4</span>가 <span class="m">x = 2</span>에 대하여
좌우 대칭인 모양이라는 것도 확인할 수 있다.
