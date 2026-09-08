---
id: DIF-C13-T4
parent: DIF-C13
unit: 05-미분
topic: 양변을 미분하면 상수가 사라진다
level: 3점
difficulty: 중상
source: 사다리 4단 (DIF-C13 에서 a 를 정하는 단계)
origin: 사다리
core: "f(x+a) = f(x) + b 의 양변을 미분하면 b가 사라져 f′(x+a) = f′(x) 가 되고, 미분가능이므로 f′(0) = f′(a) 다"
tags: [미분가능,도함수,주기,함수방정식]
status: variant
added: 2026-09-08
answer: 2
---

## 문제

<p>실수 전체의 집합에서 미분가능한 함수
<span class="m">f(x)</span>가 두 상수
<span class="m">a (a &gt; 0)</span>, <span class="m">b</span>에 대하여
다음 조건을 만족시킨다.</p>

<div class="cond">
<span class="cond m">(가) 0 ≤ x ≤ a일 때, f(x) = x<sup>3</sup> − 3x<sup>2</sup> + 5x이다.</span>
<span class="cond m">(나) 모든 실수 x에 대하여 f(x + a) = f(x) + b이다.</span>
</div>

<p>양수 <span class="m">a</span>의 값을 구하시오.</p>

## 발상

<b>지금까지는 조건 (나)를 값을 옮기는 데만 썼다.
이번에는 <b>미분</b>해서 쓴다.</b><br><br>

조건 (나)는 <b>모든 실수 <span class="m">x</span></b>에서 성립하는 등식이다.
양변이 <span class="m">x</span>에 대한 함수로서 같으므로,
<b>양변을 <span class="m">x</span>에 대하여 미분해도 여전히 같다.</b>
이때 오른쪽의 <span class="m">b</span>는 상수이므로
미분하면 <span class="m">0</span>이 되어 <b>사라진다.</b></p>
<p class="m">f′(x + a) = f′(x)</p>
<p><b>이것이 핵심이다.</b> 원래 함수는 한 칸 갈 때마다
<span class="m">b</span>만큼 올라갔지만,
<b>도함수는 한 칸 가도 그대로</b>다.
곧 <span class="m">f′</span>은 <span class="m">a</span>마다
똑같은 값이 되풀이되는 함수다.<br><br>

그러면 특히 <span class="m">x = 0</span>에서
<span class="m">f′(a) = f′(0)</span>이어야 한다.
그런데 <span class="m">f′(0)</span>과 <span class="m">f′(a)</span>는
<b>조건 (가)의 식으로 둘 다 계산할 수 있다.</b>
<span class="m">0</span>과 <span class="m">a</span>가 모두
그 구간의 끝점이기 때문이다.
이 한 줄이 <span class="m">a</span>를 정한다.

## 풀이

<p><span class="step">① 조건 (나)의 양변을 미분한다.</span>
등식이 모든 실수에서 성립하므로 양변을
<span class="m">x</span>에 대하여 미분할 수 있다.
왼쪽은 합성함수이지만 안쪽 <span class="m">x + a</span>를
미분하면 <span class="m">1</span>이므로 그대로 내려온다.
오른쪽의 <span class="m">b</span>는 상수라 <span class="m">0</span>이 된다.</p>
<p class="m">f′(x + a) = f′(x)</p>

<p><span class="step">② x = 0을 대입한다.</span></p>
<p class="m">f′(a) = f′(0)</p>
<p><b>이것이 이 문제에서 쓸 수 있는 유일한 새 정보</b>이고,
동시에 <span class="m">f</span>가 <span class="m">x = a</span>에서
미분가능하다는 조건 그 자체이기도 하다.
<span class="m">x = a</span>의 왼쪽에서는 조건 (가)의 식이 쓰이고
오른쪽에서는 조건 (나)로 넘어온 값이 쓰이는데,
그 두 미분계수가 같아야 꺾이지 않기 때문이다.</p>

<p><span class="step">③ 도함수를 구한다.</span>
조건 (가)에서 <span class="m">0 ≤ x ≤ a</span>일 때
<span class="m">f(x) = x<sup>3</sup> − 3x<sup>2</sup> + 5x</span>이므로,
이 구간에서의 도함수는 다음과 같다.</p>
<p class="m">f′(x) = 3x<sup>2</sup> − 6x + 5</p>
<p><span class="m">0</span>과 <span class="m">a</span>는 모두 이 구간에 속하므로
두 값을 모두 이 식으로 구할 수 있다.</p>
<p class="m">f′(0) = 5</p>
<p class="m">f′(a) = 3a<sup>2</sup> − 6a + 5</p>

<p><span class="step">④ 방정식을 푼다.</span>
②의 등식에 ③의 값을 넣는다.</p>
<p class="m">3a<sup>2</sup> − 6a + 5 = 5</p>
<p>양변에서 <span class="m">5</span>를 빼면 상수항이 사라진다.</p>
<p class="m">3a<sup>2</sup> − 6a = 0</p>
<p>공통인수 <span class="m">3a</span>로 묶는다.</p>
<p class="m">3a(a − 2) = 0 → a = 0 또는 a = 2</p>
<p>문제에서 <span class="m">a &gt; 0</span>이라 했으므로
<span class="m">a = 0</span>은 버린다.</p>
<p class="m">a = 2</p>
<p class="m">답 2</p>

## 함정

<b><span class="m">f′(x + a) = f′(x) + b</span>라고 쓰면 안 된다.</b>
<span class="m">b</span>는 <b>상수</b>이므로 미분하면 사라진다.
<span class="m">b</span>를 남겨 두면 방정식이 달라져 답이 나오지 않는다.
<b>이 문제에서 미분의 역할이 바로 &lsquo;<span class="m">b</span>를 지우는 것&rsquo;</b>이다.
그래서 <span class="m">b</span>의 값을 몰라도 <span class="m">a</span>를 구할 수 있다.<br><br>

<b><span class="m">a = 0</span>을 버리는 것을 잊지 않는다.</b>
<span class="m">a</span>는 한 칸의 너비이므로
<span class="m">0</span>이면 조건 자체가 뜻을 잃는다.
문제에도 <span class="m">a &gt; 0</span>이라고 적혀 있다.<br><br>

<b><span class="m">f′(a)</span>를 조건 (가)의 식으로 구해도 되는 이유를 짚어 둔다.</b>
<span class="m">a</span>는 구간 <span class="m">0 ≤ x ≤ a</span>의 <b>오른쪽 끝</b>이다.
여기서 구한 <span class="m">f′(a)</span>는 정확히는
<b>왼쪽에서 다가갈 때의 미분계수</b>이고,
<span class="m">f′(0)</span>은 <b>오른쪽에서 다가갈 때의 미분계수</b>다.
<span class="m">f</span>가 미분가능하다는 조건이 그 둘을 이어 준다.

## 노하우

<b>&lsquo;모든 실수에서 성립하는 등식&rsquo;은 미분해도 된다.</b>
함수방정식을 만나면 <b>대입해 보기</b>와 <b>미분해 보기</b>를 모두 시도한다.
특히 <b>한쪽에 상수가 더해져 있으면 미분이 그 상수를 지워</b> 준다.<br><br>

<b><span class="m">f(x + a) = f(x) + b</span>이면
<span class="m">f′</span>은 주기가 <span class="m">a</span>인 함수다.</b>
이 사실은 그림으로도 당연하다.
그래프가 계단처럼 같은 모양을 되풀이하므로,
<b>각 칸에서의 기울기 변화도 똑같이 되풀이</b>되기 때문이다.<br><br>

<b>구간의 양 끝에서 미분계수를 맞추는 것이 이런 문제의 정해진 수순이다.</b>
조건 (가)가 <span class="m">0 ≤ x ≤ a</span>처럼 <b>한 칸만</b> 주어지면,
그 칸의 <b>왼쪽 끝과 오른쪽 끝의 미분계수를 같다고 놓는 것</b>이
거의 언제나 첫 방정식이 된다.
