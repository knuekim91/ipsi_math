---
id: DIF-C13-V1
parent: DIF-C13
unit: 05-미분
topic: f(x+a)=f(x)+b 와 미분가능
level: 4점
difficulty: 상
source: 자체 개발 (DIF-C13 변형)
origin: 유사문항
core: "양변을 미분하면 f′이 주기 a인 함수가 되어 f′(0)=f′(a)가 나온다"
tags: [미분가능,주기,도함수,함수방정식]
status: variant
added: 2026-09-08
answer: ③
---

## 문제

<p>두 상수 <span class="m">a (a &gt; 0)</span>, <span class="m">b</span>와
실수 전체의 집합에서 미분가능한 함수 <span class="m">f(x)</span>가
다음 조건을 만족시킬 때, <span class="m">f(2a)</span>의 값은?</p>

<div class="cond">
<span class="cond m">(가) 0 ≤ x ≤ a일 때, f(x) = 2x<sup>3</sup> − 9x<sup>2</sup> + 12x이다.</span>
<span class="cond m">(나) 모든 실수 x에 대하여 f(x + a) = f(x) + b이다.</span>
</div>

<div class="choices"><span>① 12</span><span>② 15</span><span>③ 18</span>
<span>④ 21</span><span>⑤ 24</span></div>

## 발상

<b>모르는 것이 <span class="m">a</span>와 <span class="m">b</span> 두 개이므로
식도 두 개가 필요하다. 두 식은 서로 다른 곳에서 나온다.</b><br><br>

<b>첫 번째 식은 미분에서 나온다.</b>
조건 (나)는 모든 실수에서 성립하는 등식이므로 양변을 미분할 수 있다.
오른쪽의 <span class="m">b</span>는 상수라 사라진다.</p>
<p class="m">f′(x + a) = f′(x)</p>
<p>즉 도함수는 <span class="m">a</span>마다 되풀이된다.
여기에 <span class="m">x = 0</span>을 넣으면
<span class="m">f′(a) = f′(0)</span>이고,
<b><span class="m">0</span>과 <span class="m">a</span>는 모두
조건 (가)의 구간에 들어 있으므로 둘 다 계산된다.</b>
이 식이 <span class="m">a</span>를 정한다.<br><br>

<b>두 번째 식은 대입에서 나온다.</b>
조건 (나)에 <span class="m">x = 0</span>을 넣으면
<span class="m">b = f(a) − f(0)</span>이다.
<span class="m">a</span>를 이미 구했으므로 <span class="m">b</span>도 정해진다.<br><br>

<b>마지막으로 구하는 <span class="m">f(2a)</span>는 두 칸이다.</b>
조건 (나)를 두 번 쓰면
<span class="m">f(2a) = f(0) + 2b</span>가 된다.

## 풀이

<p><span class="step">① 조건 (나)를 미분한다.</span>
등식이 모든 실수 <span class="m">x</span>에서 성립하므로
양변을 <span class="m">x</span>에 대하여 미분한다.
상수 <span class="m">b</span>는 미분하면 <span class="m">0</span>이다.</p>
<p class="m">f′(x + a) = f′(x)</p>
<p>여기에 <span class="m">x = 0</span>을 대입한다.</p>
<p class="m">f′(a) = f′(0)</p>

<p><span class="step">② 도함수를 구한다.</span>
조건 (가)에서 <span class="m">0 ≤ x ≤ a</span>일 때
<span class="m">f(x) = 2x<sup>3</sup> − 9x<sup>2</sup> + 12x</span>이므로</p>
<p class="m">f′(x) = 6x<sup>2</sup> − 18x + 12</p>
<p><span class="m">0</span>과 <span class="m">a</span>는 모두 이 구간의 점이므로
두 값을 이 식으로 구한다.</p>
<p class="m">f′(0) = 12</p>
<p class="m">f′(a) = 6a<sup>2</sup> − 18a + 12</p>

<p><span class="step">③ a를 구한다.</span>
①의 등식에 ②의 값을 넣는다.</p>
<p class="m">6a<sup>2</sup> − 18a + 12 = 12</p>
<p>양변에서 <span class="m">12</span>를 빼면 상수항이 사라진다.</p>
<p class="m">6a<sup>2</sup> − 18a = 0</p>
<p>공통인수 <span class="m">6a</span>로 묶는다.</p>
<p class="m">6a(a − 3) = 0 → a = 0 또는 a = 3</p>
<p><span class="m">a &gt; 0</span>이므로 <span class="m">a = 3</span>이다.</p>

<p><span class="step">④ b를 구한다.</span>
조건 (나)에 <span class="m">x = 0</span>을 대입한다.</p>
<p class="m">f(a) = f(0) + b → b = f(a) − f(0)</p>
<p><span class="m">a = 3</span>이고 <span class="m">0</span>과
<span class="m">3</span>이 모두 조건 (가)의 구간에 있으므로
그 식으로 계산한다.</p>
<p class="m">f(0) = 0</p>
<p class="m">f(3) = 2 × 27 − 9 × 9 + 12 × 3 = 54 − 81 + 36 = 9</p>
<p class="m">b = 9 − 0 = 9</p>

<p><span class="step">⑤ f(2a)를 구한다.</span>
조건 (나)를 두 번 쓴다. 먼저
<span class="m">x = a</span>를 넣는다.</p>
<p class="m">f(2a) = f(a) + b</p>
<p>다음으로 <span class="m">x = 0</span>을 넣은 결과를 대입한다.</p>
<p class="m">f(a) = f(0) + b</p>
<p>두 식을 합치면 다음과 같다.</p>
<p class="m">f(2a) = f(0) + 2b</p>

<p><span class="step">⑥ 답을 만든다.</span>
<span class="m">f(0) = 0</span>, <span class="m">b = 9</span>를 넣는다.</p>
<p class="m">f(2a) = 0 + 2 × 9 = 18</p>
<p class="m">답 ③</p>

## 함정

<b><span class="m">f(2a)</span>를 조건 (가)의 식에 바로 넣으면 안 된다.</b>
<span class="m">a = 3</span>이므로 <span class="m">2a = 6</span>인데,
조건 (가)는 <span class="m">0 ≤ x ≤ 3</span>에서만 쓸 수 있다.
<span class="m">f(6) = 2 × 216 − 9 × 36 + 72 = 180</span>처럼 계산하면
완전히 틀린 값이 나온다.
<b>구간 밖에서는 조건 (나)로 옮겨 와야 한다.</b><br><br>

<b>미분할 때 <span class="m">b</span>를 남기면 안 된다.</b>
<span class="m">b</span>는 상수이므로 미분하면 사라진다.
<span class="m">b</span>가 사라지는 덕분에
<span class="m">b</span>를 모르는 채로 <span class="m">a</span>를 먼저 구할 수 있다.
<b>순서가 &lsquo;<span class="m">a</span> 먼저, <span class="m">b</span> 나중&rsquo;인 이유</b>가 여기에 있다.<br><br>

<b><span class="m">a = 0</span>을 버린다.</b>
<span class="m">a</span>는 한 칸의 너비이므로 양수여야 하고,
문제에도 <span class="m">a &gt; 0</span>이라고 적혀 있다.

## 노하우

<b>미지수가 둘이면 식도 둘을 찾는다. 나오는 곳이 정해져 있다.</b>
<span class="m">f(x + a) = f(x) + b</span> 꼴에서는
<b>미분하면 <span class="m">a</span>가, 대입하면 <span class="m">b</span>가</b> 나온다.
이 짝을 기억해 두면 문제를 보자마자 순서를 정할 수 있다.<br><br>

<b>구하는 값이 몇 칸 떨어져 있는지 먼저 센다.</b>
<span class="m">f(2a)</span>는 <span class="m">f(0)</span>에서 두 칸,
<span class="m">f(3a)</span>는 세 칸이다. 일반적으로 다음과 같다.</p>
<p class="m">f(na) = f(0) + nb</p>
<p><b>칸의 개수만 세면 계산은 곱셈 한 번</b>으로 끝난다.<br><br>

<b>도함수를 인수분해해 두면 검산이 쉽다.</b>
<span class="m">f′(x) = 6x<sup>2</sup> − 18x + 12 = 6(x − 1)(x − 2)</span>이므로
<span class="m">f</span>는 <span class="m">x = 1</span>에서 극대,
<span class="m">x = 2</span>에서 극소다.
한 칸 <span class="m">0 ≤ x ≤ 3</span> 안에 봉우리와 골이 하나씩 있고
<b>양 끝의 기울기가 <span class="m">12</span>로 같다</b>는 것을
그림으로 확인하면 답에 확신이 선다.
