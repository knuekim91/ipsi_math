---
id: PRB-W04-V2
parent: PRB-W04
unit: 07-경우의수확률
topic: 양수 쪽과 음수 쪽의 합이 다를 때
level: 4점
difficulty: 상
source: 자체 개발 (PRB-W04 변형 · 합이 0이 아닌 경우)
origin: 유사문항
core: "합이 S, 절댓값의 합이 T면 양수 쪽은 (S+T)/2, 음수 쪽은 (T−S)/2다. 둘이 다르면 양쪽의 가짓수도 달라져 대칭에 기댈 수 없다"
tags: [중복조합,절댓값,부호,순서쌍,경우나누기]
status: variant
added: 2026-10-17
answer: 58
---

## 문제

<p>다음 조건을 만족시키는 <span class="m">0</span>이 아닌 네 정수
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>의 모든 순서쌍
<span class="m">(a, b, c, d)</span>의 개수를 구하시오.</p>

<div class="cond">
<span class="cond m">(가) a + b + c + d = 4</span>
<span class="cond m">(나) |a| + |b| + |c| + |d| = 10</span>
<span class="cond m">(다) |a| + a &lt; |b| + b</span>
</div>

## 발상

<b>모문항은 합이 <span class="m">0</span>이라 양수 쪽과 음수 쪽이
똑같이 <span class="m">7</span>이었다.</b>
그래서 <span class="m">1, 6, 15</span>라는 세 수를 양쪽에 그대로 썼다.<br><br>

<b>여기서는 합이 <span class="m">4</span>라 양쪽이 어긋난다.</b></p>
<p class="m">A + B = 4, &nbsp; A − B = 10 → A = 7, B = −3</p>
<p><b>양수들의 합은 7, 음수들의 절댓값의 합은 3</b>이다.
<span class="m">7</span>은 넉넉하고 <span class="m">3</span>은 빠듯하다.<br><br>

<b>그래서 음수 쪽 가짓수가 확 줄어든다.</b>
합이 <span class="m">3</span>인 양의 정수가
<span class="m">3</span>개라면 <b>모두 <span class="m">1</span></b>일 수밖에 없다.
<b>양쪽 표를 따로 만들어 놓고 시작해야 헷갈리지 않는다.</b><br><br>

<b>(다)를 읽는 법은 그대로다.</b>
<span class="m">a &lt; 0 &lt; b</span>이거나
<span class="m">0 &lt; a &lt; b</span>, 두 갈래다.

## 풀이

<p><span class="step">① 양수 쪽과 음수 쪽의 합을 구한다.</span>
양수들의 합을 <span class="m">A</span>,
음수들의 합을 <span class="m">B</span>라 하면</p>
<p class="m">A + B = 4, &nbsp; A − B = 10</p>
<p class="m">A = 7, &nbsp; B = −3</p>

<p><span class="step">② 양쪽 표를 만든다.</span>
<span class="m">k</span>개의 양의 정수의 합이
<span class="m">n</span>인 순서쌍의 개수는
<span class="m"><sub>k</sub>H<sub>n−k</sub> = <sub>n−1</sub>C<sub>k−1</sub></span>이다.</p>
<p class="m">합이 7 : &nbsp; 1개 → 1, &nbsp; 2개 → <sub>6</sub>C<sub>1</sub> = 6, &nbsp; 3개 → <sub>6</sub>C<sub>2</sub> = 15</p>
<p class="m">합이 3 : &nbsp; 1개 → 1, &nbsp; 2개 → <sub>2</sub>C<sub>1</sub> = 2, &nbsp; 3개 → <sub>2</sub>C<sub>2</sub> = 1</p>
<p><b>왼쪽은 양수 쪽, 오른쪽은 음수 쪽에 쓴다. 섞으면 끝이다.</b></p>

<p><span class="step">③ (i) a &lt; 0 &lt; b 인 경우를 센다.</span>
<span class="m">a</span>가 음수, <span class="m">b</span>가 양수로 정해졌으므로
<span class="m">c</span>, <span class="m">d</span>의 부호만 고른다.<br>

<b>음수 1개</b> <span class="m">(c &gt; 0, d &gt; 0)</span> :
음수는 <span class="m">a = −3</span>으로 <span class="m">1</span>가지,
양수 셋의 합이 <span class="m">7</span>이므로
<span class="m">15</span>가지</p>
<p class="m">1 × 15 = 15</p>

<p><b>음수 2개</b>
<span class="m">(c &gt; 0, d &lt; 0</span> 또는
<span class="m">c &lt; 0, d &gt; 0)</span> :
음수 둘의 절댓값의 합이 <span class="m">3</span>이므로
<span class="m">2</span>가지, 양수 둘의 합이
<span class="m">7</span>이므로 <span class="m">6</span>가지</p>
<p class="m">2 × 6 = 12</p>
<p>두 경우가 있으므로 <span class="m">12 × 2 = 24</span></p>

<p><b>음수 3개</b> <span class="m">(c &lt; 0, d &lt; 0)</span> :
음수 셋의 절댓값의 합이 <span class="m">3</span>이므로
<b>모두 <span class="m">−1</span></b>로 <span class="m">1</span>가지,
양수는 <span class="m">b = 7</span>로 <span class="m">1</span>가지</p>
<p class="m">1 × 1 = 1</p>
<p class="m">15 + 24 + 1 = 40</p>

<p><span class="step">④ (ii) 0 &lt; a &lt; b 인 경우를 센다.</span>
<span class="m">a</span>, <span class="m">b</span>가 모두 양수이므로
음수는 <span class="m">c</span>, <span class="m">d</span> 안에만 있다.<br>

<b><span class="m">c &gt; 0, d &lt; 0</span></b> :
음수는 <span class="m">d = −3</span>으로 <span class="m">1</span>가지.
양수 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>의 합이 <span class="m">7</span>인 순서쌍은
<span class="m">15</span>개이고, 그중
<span class="m">a = b</span>인 것은
<span class="m">2a + c = 7</span>에서
<span class="m">a = 1, 2, 3</span>으로 <span class="m">3</span>가지다.</p>
<p class="m">(15 − 3) ÷ 2 = 6</p>

<p><b><span class="m">c &lt; 0, d &gt; 0</span></b> : 같은 방법으로
<span class="m">6</span>가지</p>

<p><b><span class="m">c &lt; 0, d &lt; 0</span></b> :
음수 둘의 절댓값의 합이 <span class="m">3</span>이므로
<span class="m">2</span>가지.
양수는 <span class="m">a + b = 7</span>,
<span class="m">a &lt; b</span>이므로
<span class="m">(1, 6), (2, 5), (3, 4)</span>로
<span class="m">3</span>가지</p>
<p class="m">3 × 2 = 6</p>
<p class="m">6 + 6 + 6 = 18</p>

<p><span class="step">⑤ 답을 만든다.</span></p>
<p class="m">40 + 18 = 58</p>
<p class="m">답 58</p>

## 함정

<b><span class="m">7</span>과 <span class="m">3</span>을 바꿔 쓰면 전부 틀린다.</b>
<span class="m">A = (S + T)/2 = 7</span>이 <b>양수</b> 쪽이고,
<span class="m">(T − S)/2 = 3</span>이 <b>음수</b> 쪽이다.
합이 양수이면 <b>양수 쪽이 더 크다</b>는 것을 그림으로 떠올려 확인한다.<br><br>

<b>음수가 3개일 때 &lsquo;<span class="m">1</span>가지&rsquo;를 그냥 넘기지 않는다.</b>
합이 <span class="m">3</span>인 양의 정수 셋은
<span class="m">(1, 1, 1)</span>뿐이다.
<span class="m"><sub>3</sub>H<sub>0</sub> = <sub>2</sub>C<sub>2</sub> = 1</span>로도 나오지만,
<b>직접 떠올려 확인하는 편이 빠르고 안전하다.</b><br><br>

<b>음수가 <span class="m">4</span>개인 경우는 없다.</b>
양수들의 합이 <span class="m">7</span>이므로
<b>양수가 적어도 하나는 있어야</b> 한다.
마찬가지로 음수도 적어도 하나 있어야 한다.
<span class="m">0</span>이 아니라는 조건이 이것을 보장한다.<br><br>

<b>모문항의 답을 그대로 쓰지 않는다.</b>
모문항에서는 (i)이 <span class="m">102</span>, (ii)가
<span class="m">30</span>이었다.
<b>여기서는 <span class="m">40</span>과 <span class="m">18</span>이다.</b>
음수 쪽 가짓수가 <span class="m">15, 6, 1</span>에서
<span class="m">1, 2, 1</span>로 바뀌었기 때문이다.

## 노하우

<b>합과 절댓값의 합에서 양쪽을 분리하는 공식</b></p>
<p class="m">합 = S, 절댓값의 합 = T 일 때</p>
<p class="m">양수들의 합 = (S + T)/2, &nbsp; 음수들의 절댓값의 합 = (T − S)/2</p>
<p><b><span class="m">S</span>와 <span class="m">T</span>의 홀짝이 같아야
정수가 나온다.</b>
다르면 그런 순서쌍이 아예 없다는 뜻이므로,
<b>문제를 풀기 전에 한 번 확인하면 헛걸음을 막는다.</b><br><br>

<b>양쪽 표를 따로 적어 두고 시작한다.</b>
합이 <span class="m">n</span>인 양의 정수
<span class="m">k</span>개의 순서쌍은
<span class="m"><sub>n−1</sub>C<sub>k−1</sub></span>,
곧 <b><span class="m">n − 1</span>개의 자리에
<span class="m">k − 1</span>개의 칸막이를 꽂는 것</b>이다.
<span class="m">n = 3</span>이면 칸막이 자리가
<span class="m">2</span>개뿐이라 <span class="m">1, 2, 1</span>로 금방 끝난다.
<b>작은 쪽부터 세면 실수가 준다.</b><br><br>

<b>합이 <span class="m">0</span>이 아니면 대칭이 깨진다.</b>
모문항에서는 부호를 모두 뒤집어도 조건이 그대로여서
&lsquo;양수 <span class="m">3</span>개&rsquo;와
&lsquo;음수 <span class="m">3</span>개&rsquo;의 개수가 같았다
<span class="m">(15와 15)</span>.
<b>여기서는 그 대칭이 없으므로 한쪽을 세고 다른 쪽을 베끼면 안 된다.</b>
<span class="m">15</span>와 <span class="m">1</span>로 열다섯 배 차이가 난다.
