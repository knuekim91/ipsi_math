---
id: EXP-W01-V1
parent: EXP-W01
unit: 01-지수로그
topic: 역함수인 두 곡선의 교점을 중점과 거리로 찾기
level: 4점
difficulty: 상
source: 자체 개발 (EXP-W01 변형 · 교점을 도형으로 다루기)
origin: 유사문항
core: "교점이 y=x 위에 있으므로 두 점은 (p,p), (q,q)다. 중점과 거리가 주어지면 p와 q가 연립방정식 없이 바로 나온다"
tags: [지수함수,로그함수,역함수,교점,중점,두점사이의거리]
status: variant
added: 2026-10-17
answer: ③
---

## 문제

<p><span class="m">a &gt; 1</span>인 상수 <span class="m">a</span>와 상수
<span class="m">b</span>에 대하여 두 함수</p>

<p class="m">y = a<sup>x</sup> + b, &nbsp; y = log<sub>a</sub>(x − b)</p>

<p>의 그래프가 서로 다른 두 점 <span class="m">P</span>,
<span class="m">Q</span>에서 만난다.
선분 <span class="m">PQ</span>의 중점이 <span class="m">(2, 2)</span>이고
<span class="m">PQ = 4√2</span>일 때,
<span class="m">a<sup>8</sup></span>의 값은?</p>

<div class="choices"><span>① 21</span><span>② 23</span><span>③ 25</span>
<span>④ 27</span><span>⑤ 29</span></div>

## 발상

<b>모문항에서 가장 중요한 한 줄만 떼어 낸 문제다.</b>
직선도 부등식도 없다. 오직 <b>교점이 어디 있는가</b>만 묻는다.<br><br>

<b>두 함수는 서로 역함수이므로 그래프는
<span class="m">y = x</span>에 대하여 대칭</b>이고,
<span class="m">a &gt; 1</span>이라 둘 다 증가함수이므로
<b>교점은 반드시 직선 <span class="m">y = x</span> 위에 있다.</b>
곧 두 점은</p>
<p class="m">P(p, p), &nbsp; Q(q, q)</p>
<p>꼴이다. <b>미지수가 두 개로 줄었다.</b><br><br>

그러면 중점과 거리가 그대로 <span class="m">p</span>,
<span class="m">q</span>를 준다.
<b>중점은 합을, 거리는 차를 알려 준다.</b>
합과 차를 알면 두 수가 나온다.<br><br>

<b>이 성질을 모르면 손도 못 댄다.</b>
<span class="m">a<sup>x</sup> + b = log<sub>a</sub>(x − b)</span>를
연립해 봐야 풀리지 않는다.

## 풀이

<p><span class="step">① 교점이 y = x 위에 있음을 쓴다.</span></p>
<p class="m">y = a<sup>x</sup> + b → x = log<sub>a</sub>(y − b)</p>
<p>이므로 두 함수는 서로 역함수이고, 두 그래프는 직선
<span class="m">y = x</span>에 대하여 대칭이다.
<span class="m">a &gt; 1</span>이므로 두 함수는 모두 증가함수이고,
<b>증가함수와 그 역함수의 교점은 직선
<span class="m">y = x</span> 위에 있다.</b></p>
<p class="m">P(p, p), &nbsp; Q(q, q) &nbsp; (p &lt; q)</p>

<p><span class="step">② 중점에서 합을 얻는다.</span></p>
<p class="m">((p + q)/2, (p + q)/2) = (2, 2)</p>
<p class="m">p + q = 4</p>

<p><span class="step">③ 거리에서 차를 얻는다.</span></p>
<p class="m">PQ = √{(q − p)<sup>2</sup> + (q − p)<sup>2</sup>} = √2 (q − p)</p>
<p><span class="m">√2 (q − p) = 4√2</span>이므로</p>
<p class="m">q − p = 4</p>

<p><span class="step">④ 두 교점을 구한다.</span>
<span class="m">p + q = 4</span>, <span class="m">q − p = 4</span>이므로</p>
<p class="m">p = 0, &nbsp; q = 4</p>

<p><span class="step">⑤ a와 b를 구한다.</span>
두 점이 <span class="m">y = a<sup>x</sup> + b</span> 위에 있으므로</p>
<p class="m">a<sup>0</sup> + b = 0 → 1 + b = 0 → b = −1</p>
<p class="m">a<sup>4</sup> + b = 4 → a<sup>4</sup> − 1 = 4 → a<sup>4</sup> = 5</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">a<sup>8</sup> = (a<sup>4</sup>)<sup>2</sup> = 5<sup>2</sup> = 25</p>
<p class="m">답 ③</p>

<p><span class="step">⑦ 확인한다.</span>
<span class="m">a = <sup>4</sup>√5 ≈ 1.495 &gt; 1</span>이고,
<span class="m">b = −1</span>이므로 정의역은
<span class="m">x &gt; −1</span>이다.
<span class="m">P(0, 0)</span>, <span class="m">Q(4, 4)</span>가
<span class="m">y = log<sub>a</sub>(x + 1)</span> 위에도 있는지 보면</p>
<p class="m">log<sub>a</sub>1 = 0 ✓, &nbsp; log<sub>a</sub>5 = log<sub>a</sub>a<sup>4</sup> = 4 ✓</p>

## 함정

<b>중점이 <span class="m">(2, 2)</span>라는 것은 단서가 아니라 확인이다.</b>
교점이 <span class="m">y = x</span> 위에 있으면 중점도 당연히 그 위에 있다.
<b>중점의 좌표가 같은 수 두 개로 주어진 것은
&lsquo;제대로 가고 있다&rsquo;는 신호</b>다.
만약 중점이 <span class="m">(2, 3)</span>처럼 주어지면
그런 <span class="m">a</span>, <span class="m">b</span>는 없다.<br><br>

<b><span class="m">PQ = 4√2</span>에서 <span class="m">√2</span>를 빠뜨리지 않는다.</b>
<span class="m">y = x</span> 위의 두 점은 가로로
<span class="m">q − p</span>, 세로로도 <span class="m">q − p</span>만큼 떨어져 있으므로
<b>실제 거리는 그 <span class="m">√2</span>배</b>다.
<span class="m">q − p = 4√2</span>로 쓰면 교점이
<span class="m">2 ± 2√2</span>가 되어 뒤가 전부 무너진다.<br><br>

<b><span class="m">a<sup>4</sup> = 5</span>에서 멈추지 않는다.</b>
묻는 것은 <span class="m">a<sup>8</sup></span>이다.
<span class="m">a</span>를 <span class="m"><sup>4</sup>√5</span>로 구한 뒤
<span class="m">8</span>제곱하려 들면 계산이 지저분해진다.
<b><span class="m">a<sup>8</sup> = (a<sup>4</sup>)<sup>2</sup></span>으로 묶는다.</b>

## 노하우

<b>&lsquo;서로 역함수인 두 그래프의 교점&rsquo;은 언제나
<span class="m">y = x</span> 위에서 찾는다.</b>
단, <b>두 함수가 모두 증가함수일 때</b>만 그렇다.
감소함수면 <span class="m">y = x</span> 밖에도 교점이 생길 수 있다.
<span class="m">a &gt; 1</span>이라는 조건이 바로 그것을 보장한다.
<b>문제가 <span class="m">a &gt; 1</span>을 괜히 써 준 것이 아니다.</b><br><br>

<b>교점을 <span class="m">(p, p)</span>로 놓으면 미지수가 반으로 준다.</b>
그 뒤로는 <b>중점 = 합, 거리 = 차</b>다.</p>
<p class="m">중점의 x좌표 = (p + q)/2 → 합</p>
<p class="m">PQ = √2 |q − p| → 차</p>
<p><b>합과 차를 얻으면 두 수는 더하고 빼서 나온다.</b><br><br>

<b>구한 값을 다른 식에 넣어 확인하는 습관을 들인다.</b>
<span class="m">a</span>, <span class="m">b</span>를
지수 쪽 식으로만 구했으면 <b>로그 쪽 식에 넣어 본다.</b>
두 번 맞으면 거의 틀리지 않는다.
이 문제에서는 <span class="m">log<sub>a</sub>5 = 4</span>가
<span class="m">a<sup>4</sup> = 5</span>와 같은 말이라
한눈에 확인된다.
