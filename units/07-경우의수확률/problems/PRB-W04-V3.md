---
id: PRB-W04-V3
parent: PRB-W04
unit: 07-경우의수확률
topic: 부호 조건이 두 번 걸린 정수 순서쌍
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W04 변형 · 조건을 한 줄로 줄인 보람)
origin: 유사문항
core: "(다)를 'b>0 이고 a<b' 로 줄여 두면 조건이 두 번 걸려도 b>0, d>0 만 확인하면 된다. 갈래로 나누면 경우가 네 배로 불어난다"
tags: [중복조합,절댓값,부호,순서쌍,조건의정리]
status: variant
added: 2026-10-17
answer: 48
---

## 문제

<p>다음 조건을 만족시키는 <span class="m">0</span>이 아닌 네 정수
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>의 모든 순서쌍
<span class="m">(a, b, c, d)</span>의 개수를 구하시오.</p>

<div class="cond">
<span class="cond m">(가) a + b + c + d = 0</span>
<span class="cond m">(나) |a| + |b| + |c| + |d| = 14</span>
<span class="cond m">(다) |a| + a &lt; |b| + b</span>
<span class="cond m">(라) |c| + c &lt; |d| + d</span>
</div>

## 발상

<b>모문항의 (다)를 두 번 걸었다.</b>
갈래로 나누어 풀면 <span class="m">2 × 2 = 4</span>가지 조합을
각각 또 부호별로 나누어야 해서 손을 못 댄다.<br><br>

<b>그래서 모문항에서 정리해 둔 한 줄이 여기서 값을 한다.</b></p>
<p class="m">|a| + a &lt; |b| + b &nbsp; ⟺ &nbsp; b &gt; 0 이고 a &lt; b</p>
<p>이 꼴로 바꾸면 (다)와 (라)는</p>
<p class="m">b &gt; 0, &nbsp; a &lt; b, &nbsp; d &gt; 0, &nbsp; c &lt; d</p>
<p>이 된다. <b><span class="m">b</span>와 <span class="m">d</span>가
양수로 못박힌다.</b><br><br>

<b>그러면 음수는 <span class="m">a</span>와
<span class="m">c</span> 안에만 있을 수 있다.</b>
음수들의 절댓값의 합이 <span class="m">7</span>이므로
<b>적어도 하나는 음수</b>여야 한다.
<span class="m">a</span>, <span class="m">c</span>의 부호만 보면 되므로
<b>경우가 셋으로 줄어든다.</b>

## 풀이

<p><span class="step">① 조건을 한 줄로 정리한다.</span>
<span class="m">|x| + x</span>는
<span class="m">x &gt; 0</span>이면 <span class="m">2x</span>,
<span class="m">x &lt; 0</span>이면 <span class="m">0</span>이다.
<span class="m">|a| + a ≥ 0</span>이므로 (다)에서
<span class="m">|b| + b &gt; 0</span>, 곧
<span class="m">b &gt; 0</span>이다.
그 뒤 <span class="m">a</span>가 음수면
<span class="m">a &lt; 0 &lt; b</span>, 양수면
<span class="m">2a &lt; 2b</span>이므로 어느 쪽이든
<span class="m">a &lt; b</span>다.</p>
<p class="m">(다) ⟺ b &gt; 0 이고 a &lt; b</p>
<p class="m">(라) ⟺ d &gt; 0 이고 c &lt; d</p>

<p><span class="step">② 양수 쪽과 음수 쪽의 합을 구한다.</span>
(가), (나)에서 양수들의 합은 <span class="m">7</span>,
음수들의 절댓값의 합은 <span class="m">7</span>이다.
<span class="m">k</span>개의 양의 정수의 합이
<span class="m">7</span>인 순서쌍의 개수는</p>
<p class="m">1개 → 1, &nbsp; 2개 → 6, &nbsp; 3개 → 15</p>

<p><span class="step">③ a와 c의 부호로 나눈다.</span>
<span class="m">b &gt; 0</span>, <span class="m">d &gt; 0</span>이므로
음수는 <span class="m">a</span>, <span class="m">c</span> 안에만 있다.
<b>둘 다 양수이면 음수가 하나도 없어 (나)를 만족시킬 수 없다.</b>
남는 경우는 셋이다.</p>

<p><span class="step">④ a &lt; 0, c &gt; 0 인 경우</span>
음수는 <span class="m">a</span>뿐이므로
<span class="m">a = −7</span>로 <span class="m">1</span>가지.
<span class="m">a &lt; 0 &lt; b</span>이므로
<span class="m">a &lt; b</span>는 저절로 성립한다.<br>
양수 <span class="m">b</span>, <span class="m">c</span>,
<span class="m">d</span>의 합이 <span class="m">7</span>인 순서쌍은
<span class="m">15</span>개이고, 여기서
<span class="m">c &lt; d</span>인 것만 센다.
<span class="m">c = d</span>인 경우는
<span class="m">b + 2c = 7</span>에서
<span class="m">c = 1, 2, 3</span>으로 <span class="m">3</span>가지이므로</p>
<p class="m">(15 − 3) ÷ 2 = 6</p>

<p><span class="step">⑤ a &gt; 0, c &lt; 0 인 경우</span>
음수는 <span class="m">c = −7</span>로
<span class="m">1</span>가지이고
<span class="m">c &lt; 0 &lt; d</span>이므로
<span class="m">c &lt; d</span>는 저절로 성립한다.<br>
양수 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">d</span>의 합이 <span class="m">7</span>이고
<span class="m">a &lt; b</span>인 것만 세면</p>
<p class="m">(15 − 3) ÷ 2 = 6</p>

<p><span class="step">⑥ a &lt; 0, c &lt; 0 인 경우</span>
음수가 <span class="m">a</span>, <span class="m">c</span> 둘이므로
절댓값의 합이 <span class="m">7</span>인 순서쌍은
<span class="m">6</span>가지.
양수는 <span class="m">b</span>, <span class="m">d</span> 둘이고
합이 <span class="m">7</span>이므로 <span class="m">6</span>가지.
<span class="m">a &lt; 0 &lt; b</span>,
<span class="m">c &lt; 0 &lt; d</span>이므로
<b>두 대소 조건이 모두 저절로 성립</b>한다.</p>
<p class="m">6 × 6 = 36</p>

<p><span class="step">⑦ 답을 만든다.</span></p>
<p class="m">6 + 6 + 36 = 48</p>
<p class="m">답 48</p>

## 함정

<b>&lsquo;저절로 성립&rsquo;하는지 매번 확인한다.</b>
④에서 <span class="m">a &lt; b</span>는 공짜지만
<span class="m">c &lt; d</span>는 공짜가 아니다.
<b>둘 다 양수인 쌍에서만 대소를 따로 세야 한다.</b>
습관적으로 둘 다 세거나 둘 다 빼면 답이
<span class="m">36</span>이나 <span class="m">72</span>로 어긋난다.<br><br>

<b><span class="m">a</span>, <span class="m">c</span>가 둘 다 양수인 경우를
&lsquo;<span class="m">0</span>가지&rsquo;로 적어 둔다.</b>
<span class="m">b</span>, <span class="m">d</span>도 양수이므로
넷이 모두 양수가 되어 음수들의 합
<span class="m">7</span>을 만들 수 없다.
<b>세지 않은 경우가 있는지 표로 확인하는 것이 안전하다.</b><br><br>

<b>(다)와 (라)를 각각 두 갈래로 나누지 않는다.</b>
나누면 <span class="m">4</span>가지 조합에 다시
<span class="m">c</span>, <span class="m">d</span>의 부호까지 얽혀
실수하기 딱 좋다.
<b>한 줄로 줄여 두면 부호를 볼 자리가
<span class="m">a</span>와 <span class="m">c</span> 둘뿐</b>이다.<br><br>

<b>모문항의 답과 견주어 본다.</b>
(라)를 더 걸었으므로 답은 <span class="m">132</span>보다 작아야 한다.</p>
<p class="m">48 &lt; 132 ✓</p>

## 노하우

<b>조건은 세기 전에 가장 간단한 꼴로 바꿔 둔다.</b>
<span class="m">|a| + a &lt; |b| + b</span>를
<b>그대로 들고 다니면 갈래가 계속 불어난다.</b></p>
<p class="m">b &gt; 0 이고 a &lt; b</p>
<p>로 한 번 바꿔 두면 몇 번을 걸어도 똑같이 다룰 수 있다.
<b>모문항에서 답만 맞히고 넘어갔다면 이 문항은 손을 못 댄다.</b><br><br>

<b>조건이 저절로 성립하는 자리를 찾아 둔다.</b>
<span class="m">a &lt; 0 &lt; b</span>이면
<span class="m">a &lt; b</span>는 따질 것도 없다.
<b>부호가 갈리는 순간 대소는 공짜</b>다.
<b>진짜 세야 하는 것은 같은 부호끼리뿐</b>이고,
그때 쓰는 것이 맞바꾸기다.</p>
<p class="m">(a &lt; b 인 개수) = (전체 − a = b 인 개수) ÷ 2</p>
<p><br>

<b>조건을 더 걸면 답이 줄어든다는 것으로 검산한다.</b>
조건이 늘었는데 답이 커졌다면 어딘가에서 중복해 세고 있다.
<b>부등호의 방향만 보고도 답의 크기를 가늠할 수 있다.</b>
