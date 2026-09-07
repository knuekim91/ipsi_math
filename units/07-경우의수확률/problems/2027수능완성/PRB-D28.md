---
id: PRB-D28
unit: 07-경우의수확률
topic: 함수의 개수와 조건부확률
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 2회 28번
exam: 2027-수능완성
origin: 기출
core: "3의 배수는 3 하나뿐이므로 (나)는 f(2)=3 또는 f(4)=3 이고, 값이 1씩만 움직이므로 한 칸씩 세어 나간다"
tags: [함수의개수,조건부확률,여사건,합집합]
status: seed
added: 2026-09-07
answer: ⑤
---

## 문제

<p>집합 <span class="m">X = {1, 2, 3, 4, 5}</span>에 대하여
<span class="m">X</span>에서 <span class="m">X</span>로의 모든 함수
<span class="m">f</span> 중에서 임의로 하나를 선택하는 시행을 한다.
이 시행에서 선택한 함수 <span class="m">f</span>가 다음 조건을 만족시킬 때,
<span class="m">f(4)</span>가 홀수일 확률은?</p>

<div class="cond">
<span class="cond m">(가) n = 1, 2, 3, 4일 때, |f(n+1) − f(n)| ≤ 1이다.</span>
<span class="cond m">(나) f(2) × f(4)는 3의 배수이다.</span>
</div>

<div class="choices"><span>① 25/41</span><span>② 26/41</span><span>③ 27/41</span>
<span>④ 28/41</span><span>⑤ 29/41</span></div>

## 발상

<b>조건 (나)를 먼저 간단한 말로 바꾼다.</b>
<span class="m">f</span>의 값은 <span class="m">1</span>부터
<span class="m">5</span>까지이고, 그중 <span class="m">3</span>의 배수는
<span class="m">3</span> 하나뿐이다.
곱이 <span class="m">3</span>의 배수이려면 두 수 중 적어도 하나가
<span class="m">3</span>의 배수여야 하므로</p>
<p class="m">(나) ⟺ f(2) = 3 또는 f(4) = 3</p>
<p>&lsquo;또는&rsquo;이 나왔으므로 <b>합집합의 개수 공식</b>을 쓴다.<br><br>

<b>조건 (가)는 값이 한 칸씩만 움직인다는 뜻이다.</b>
<span class="m">f(1), f(2), f(3), f(4), f(5)</span>를 차례로 적으면,
<b>이웃한 값의 차가 <span class="m">1</span> 이하</b>이므로
제자리이거나 위아래로 한 칸씩만 옮겨 간다.
그러므로 어떤 값 <span class="m">v</span>에서 다음에 올 수 있는 값의 개수는
<span class="m">v</span>가 가운데 값
<span class="m">(2, 3, 4)</span>이면 <span class="m">3</span>가지,
끝값 <span class="m">(1</span> 또는 <span class="m">5)</span>이면
<span class="m">2</span>가지이다.
<b>이 개수만 알면 전부 곱셈으로 셀 수 있다.</b><br><br>

문제가 묻는 것은 <b>조건부확률</b>이다.
조건 (가), (나)를 만족시키는 함수 전체를 분모로,
그중 <span class="m">f(4)</span>가 홀수인 것을 분자로 놓는다.

## 풀이

<p><span class="step">① 한 칸 이동의 가짓수를 정리한다.</span>
값 <span class="m">v</span> 다음에 올 수 있는 값은
<span class="m">v − 1</span>, <span class="m">v</span>,
<span class="m">v + 1</span> 중 <span class="m">1</span>부터
<span class="m">5</span> 사이에 있는 것이다.
그 개수를 <span class="m">d(v)</span>라 하자.</p>
<p class="m">d(1) = 2, &nbsp; d(2) = d(3) = d(4) = 3, &nbsp; d(5) = 2</p>
<p>두 칸 뒤까지 가는 경우의 수도 미리 세어 둔다.
값 <span class="m">v</span>에서 두 칸 진행하는 경우의 수는
<span class="m">v</span>의 이웃들의 <span class="m">d</span>값을 더한 것이다.</p>
<p class="m">v = 2 : d(1) + d(2) + d(3) = 2 + 3 + 3 = 8</p>
<p class="m">v = 3 : d(2) + d(3) + d(4) = 3 + 3 + 3 = 9</p>
<p class="m">v = 4 : d(3) + d(4) + d(5) = 3 + 3 + 2 = 8</p>

<p><span class="step">② f(2) = 3인 함수의 개수를 센다.</span>
<span class="m">f(2) = 3</span>으로 고정한다.
<span class="m">f(1)</span>은 <span class="m">3</span>의 이웃이므로
<span class="m">2, 3, 4</span>의 <span class="m">3</span>가지이다.
<span class="m">f(3)</span>도 <span class="m">2, 3, 4</span> 중 하나이고,
그 각각에서 <span class="m">f(4)</span>, <span class="m">f(5)</span>까지
두 칸을 더 가야 하므로 ①에서 구한 값을 쓴다.</p>
<p class="m">(f(3) 이후) = 8 + 9 + 8 = 25</p>
<p class="m">(f(2) = 3인 개수) = 3 × 25 = 75</p>

<p><span class="step">③ f(4) = 3인 함수의 개수를 센다.</span>
수열을 거꾸로 읽어도 조건 (가)는 그대로이므로,
②와 완전히 같은 구조이다.
<span class="m">f(5)</span>가 <span class="m">3</span>가지,
<span class="m">f(3)</span>에서 거꾸로 두 칸 가는 경우가
<span class="m">25</span>가지이다.</p>
<p class="m">(f(4) = 3인 개수) = 3 × 25 = 75</p>

<p><span class="step">④ 둘 다 3인 경우를 센다.</span>
<span class="m">f(2) = 3</span>이고
<span class="m">f(4) = 3</span>이라 하자.
<span class="m">f(1)</span>은 <span class="m">3</span>의 이웃이므로
<span class="m">3</span>가지,
<span class="m">f(5)</span>도 <span class="m">3</span>가지이다.
<span class="m">f(3)</span>은 <span class="m">f(2) = 3</span>의 이웃이면서
<span class="m">f(4) = 3</span>의 이웃이어야 하므로
<span class="m">2, 3, 4</span>의 <span class="m">3</span>가지이다.</p>
<p class="m">(둘 다 3인 개수) = 3 × 3 × 3 = 27</p>

<p><span class="step">⑤ 조건을 만족시키는 전체 개수를 구한다.</span>
합집합의 개수 공식을 쓴다.</p>
<p class="m">75 + 75 − 27 = 123</p>

<p><span class="step">⑥ f(4)가 홀수인 경우를 센다.</span>
<span class="m">f(4)</span>가 홀수이면
<span class="m">f(4) ∈ {1, 3, 5}</span>이다. 값별로 나누어 센다.<br>
<b><span class="m">f(4) = 3</span>인 경우</b>는 그 자체로 조건 (나)를 만족시키므로
③에서 센 <span class="m">75</span>가지가 모두 해당된다.</p>
<p class="m">(f(4) = 3) : 75</p>
<p><b><span class="m">f(4) = 1</span>인 경우</b>에는
<span class="m">1</span>이 <span class="m">3</span>의 배수가 아니므로,
조건 (나)를 만족시키려면 <span class="m">f(2) = 3</span>이어야 한다.
<span class="m">f(3)</span>은 <span class="m">3</span>의 이웃
<span class="m">(2, 3, 4)</span>이면서 <span class="m">1</span>의 이웃
<span class="m">(1, 2)</span>이어야 하므로
<span class="m">f(3) = 2</span> 하나뿐이다.
<span class="m">f(1)</span>은 <span class="m">3</span>가지,
<span class="m">f(5)</span>는 <span class="m">1</span>의 이웃이므로
<span class="m">1, 2</span>의 <span class="m">2</span>가지이다.</p>
<p class="m">(f(4) = 1) : 3 × 1 × 2 = 6</p>
<p><b><span class="m">f(4) = 5</span>인 경우</b>도 대칭이므로 같은 방법으로 센다.
<span class="m">f(2) = 3</span>이어야 하고
<span class="m">f(3) = 4</span>, <span class="m">f(1)</span>이
<span class="m">3</span>가지, <span class="m">f(5)</span>가
<span class="m">4, 5</span>의 <span class="m">2</span>가지이다.</p>
<p class="m">(f(4) = 5) : 3 × 1 × 2 = 6</p>
<p class="m">(f(4)가 홀수) = 75 + 6 + 6 = 87</p>

<p><span class="step">⑦ 답을 만든다.</span>
조건을 만족시키는 함수 중에서 고르는 것이므로 조건부확률이다.</p>
<p class="m">(확률) = 87/123</p>
<p>분자와 분모를 <span class="m">3</span>으로 약분한다.</p>
<p class="m">87/123 = 29/41</p>
<p class="m">답 ⑤</p>

## 함정

<b><span class="m">3</span>의 배수 조건을 &lsquo;둘 다&rsquo;로 읽으면 안 된다.</b>
<span class="m">f(2) × f(4)</span>가 <span class="m">3</span>의 배수이려면
<b>둘 중 적어도 하나</b>가 <span class="m">3</span>이면 된다.
&lsquo;또는&rsquo;이므로 합집합이고,
<b>겹치는 <span class="m">27</span>가지를 한 번 빼야 한다.</b>
빼지 않으면 분모가 <span class="m">150</span>이 되어 답이 달라진다.<br><br>

<b>전체 함수의 개수 <span class="m">5<sup>5</sup></span>를 분모로 쓰면 안 된다.</b>
문제는 &lsquo;조건을 만족시킬 때&rsquo;의 확률을 묻고 있으므로,
<b>분모는 조건을 만족시키는 함수의 개수</b>인
<span class="m">123</span>이다.
선택지의 분모가 모두 <span class="m">41</span>인 것이
이를 알려 주는 힌트이다.<br><br>

<b><span class="m">f(4) = 1</span>일 때 <span class="m">f(3)</span>이
하나뿐이라는 것을 놓치기 쉽다.</b>
<span class="m">f(3)</span>은 <b>양쪽 모두와</b> 한 칸 이내여야 한다.
<span class="m">f(2) = 3</span>과 <span class="m">f(4) = 1</span>은
<span class="m">2</span>만큼 떨어져 있으므로,
그 사이를 잇는 값은 정확히 가운데인
<span class="m">2</span>뿐이다.

## 노하우

<b>작은 집합에서 &lsquo;<span class="m">k</span>의 배수&rsquo;는 원소를 직접 확인한다.</b>
<span class="m">X = {1, 2, 3, 4, 5}</span>에서
<span class="m">3</span>의 배수는 <span class="m">3</span> 하나뿐이다.
<b>추상적인 조건을 구체적인 값으로 바꾸는 것</b>이 첫 단계다.<br><br>

<b><span class="m">|f(n+1) − f(n)| ≤ 1</span>은 &lsquo;한 칸 걷기&rsquo;로 본다.</b>
값이 <span class="m">1</span>부터 <span class="m">5</span>까지 놓인 길 위에서
제자리 또는 좌우 한 칸씩 움직이는 것이다.
<b>각 위치에서 갈 수 있는 곳의 개수를 먼저 표로 만들어 두면</b>
어떤 조건이 붙어도 곱셈만으로 셀 수 있다.<br><br>

<b>양 끝이 고정되면 가운데는 &lsquo;둘 다의 이웃&rsquo;이다.</b>
<span class="m">f(2)</span>와 <span class="m">f(4)</span>가 정해지면
<span class="m">f(3)</span>의 후보는 두 이웃 집합의 교집합이다.
두 값의 차가 <span class="m">2</span>이면 후보가 하나,
<span class="m">1</span>이면 둘, <span class="m">0</span>이면 셋이고,
<span class="m">3</span> 이상이면 아예 없다.
이 관계를 알면 경우를 빠르게 걸러 낼 수 있다.
