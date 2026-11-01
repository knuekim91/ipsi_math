---
id: STA-W02-V3
parent: STA-W02
unit: 08-통계
topic: 절댓값으로 접힌 이항분포에서 두 조건으로 분포 결정하기
level: 4점
difficulty: 상
source: 자체 개발 (STA-W02 변형 · 겹침이 두 군데)
origin: 유사문항
core: "Y=|X|처럼 양쪽이 같은 값으로 접히면 겹치는 칸이 여럿 생긴다. 칸마다 미지수가 하나씩 늘어나므로 조건도 그만큼 필요하다"
tags: [이항분포,이산확률변수,절댓값,분산,확률분포표,연립]
status: variant
added: 2026-11-01
answer: 16
---

## 문제

<p>이산확률변수 <span class="m">X</span>가 가지는 값은 절댓값이
<span class="m">2</span> 이하인 정수이고, 확률변수
<span class="m">Y = |X|</span>는 이항분포 <span class="m">B(2, p)</span>를 따른다.</p>

<p>다음 두 조건이 주어졌을 때, <span class="m">9 × V(X)</span>의 값을 구하시오.</p>

<div class="cond">
<span class="cond m">(가) E(Y) = 4/3 &nbsp; 이고 &nbsp; E(X) = 2/3 이다.</span>
<span class="cond m">(나) P(X = −1) = 1/9 이다.</span>
</div>

## 발상

<b>이항분포의 평균을 주었으니 <span class="m">p</span>는 바로 나온다.
문제는 <span class="m">X</span>의 분포를 정하는 일이다.</b><br><br>

<span class="m">Y = |X|</span>는 양쪽을 <b>같은 값으로 접는다.</b>
<span class="m">Y = 1</span>은 <span class="m">X = −1</span>과
<span class="m">X = 1</span> 두 군데에서 오고,
<span class="m">Y = 2</span>는 <span class="m">X = −2</span>와
<span class="m">X = 2</span> 두 군데에서 온다.
<b>겹치는 칸이 두 개</b>다.<br><br>

<b>겹치는 칸마다 미지수가 하나씩 생긴다.</b>
그러니 조건도 두 개가 필요하고, 그것이 바로 (가)와 (나)다.
(나)는 <span class="m">Y = 1</span> 칸을 가르고,
(가)의 <span class="m">E(X)</span>는 <span class="m">Y = 2</span> 칸을 가른다.

## 풀이

<p><span class="step">① p를 구한다.</span>
<span class="m">Y ~ B(2, p)</span>이므로 평균은 <span class="m">2p</span>이고</p>
<p class="m">2p = 4/3 → p = 2/3</p>
<p>따라서</p>
<p class="m">P(Y = 0) = (1/3)<sup>2</sup> = 1/9, &nbsp; P(Y = 1) = 2 · (2/3) · (1/3) = 4/9, &nbsp; P(Y = 2) = (2/3)<sup>2</sup> = 4/9</p>

<p><span class="step">② 대응표를 적고 미지수를 놓는다.</span></p>
<p class="m">X = −2, −1, 0, 1, 2 &nbsp;→&nbsp; Y = 2, 1, 0, 1, 2</p>
<p>네 미지수를 놓는다.</p>
<p class="m">P(X = −2) = u, &nbsp; P(X = 2) = s, &nbsp; P(X = 1) = v, &nbsp; P(X = 0) = w</p>
<p><span class="m">P(X = −1) = 1/9</span>은 (나)에서 이미 주어졌다.</p>

<p><span class="step">③ Y = 0 과 Y = 1 칸으로 미지수를 줄인다.</span>
<span class="m">Y = 0</span>은 <span class="m">X = 0</span> 하나뿐이므로
<span class="m">w = P(Y = 0) = 1/9</span>이다.
<span class="m">Y = 1</span>은 <span class="m">X = −1</span>과 <span class="m">X = 1</span>에서 오므로</p>
<p class="m">1/9 + v = 4/9 → v = 1/3</p>
<p><span class="m">Y = 2</span>는 <span class="m">X = −2</span>와 <span class="m">X = 2</span>에서 오므로</p>
<p class="m">u + s = 4/9</p>

<p><span class="step">④ E(X)로 u와 s를 가른다.</span></p>
<p class="m">E(X) = (−2)u + (−1)(1/9) + 0 + (1)(1/3) + (2)s = 2/3</p>
<p class="m">−2u + 2s = 2/3 + 1/9 − 1/3 = 4/9</p>
<p class="m">s − u = 2/9</p>
<p>이것과 <span class="m">u + s = 4/9</span>를 더하면</p>
<p class="m">2s = 6/9 → s = 1/3, &nbsp; u = 1/9</p>

<p><span class="step">⑤ X의 분포를 적는다.</span></p>
<p class="m">P(X = −2) = 1/9, &nbsp; P(X = −1) = 1/9, &nbsp; P(X = 0) = 1/9, &nbsp; P(X = 1) = 1/3, &nbsp; P(X = 2) = 1/3</p>
<p>확률의 합은 <span class="m">1/9 · 3 + 1/3 · 2 = 1</span>이다.</p>

<p><span class="step">⑥ 분산을 구한다.</span>
먼저 <span class="m">E(X<sup>2</sup>)</span>를 구한다.</p>
<p class="m">E(X<sup>2</sup>) = 4 · (1/9) + 1 · (1/9) + 0 + 1 · (1/3) + 4 · (1/3)</p>
<p class="m">= 4/9 + 1/9 + 3/9 + 12/9 = 20/9</p>
<p>그러므로</p>
<p class="m">V(X) = E(X<sup>2</sup>) − {E(X)}<sup>2</sup> = 20/9 − 4/9 = 16/9</p>
<p class="m">9 × V(X) = 9 × 16/9 = 16</p>
<p class="m">답 16</p>

<p><span class="step">⑦ 확인한다.</span>
<span class="m">Y = |X|</span>의 분포를 다시 만들어 본다.</p>
<p class="m">P(Y = 0) = P(X = 0) = 1/9 ✓</p>
<p class="m">P(Y = 1) = P(X = −1) + P(X = 1) = 1/9 + 1/3 = 4/9 ✓</p>
<p class="m">P(Y = 2) = P(X = −2) + P(X = 2) = 1/9 + 1/3 = 4/9 ✓</p>

## 함정

<b>(가)만 주어졌다고 착각하면 막힌다.</b>
<span class="m">E(X) = 2/3</span>과 <span class="m">E(Y) = 4/3</span> 둘 다 주어졌지만,
<span class="m">E(Y)</span>는 <span class="m">p</span>를 구하는 데만 쓰였다.
<b>분포를 정하는 데 실제로 쓰이는 정보는 <span class="m">E(X)</span>와 (나)다.</b>
평균만으로는 두 칸이 한꺼번에 흐려져 풀리지 않는다.<br><br>

<b><span class="m">Y = 1</span>의 확률 <span class="m">4/9</span>를
그대로 <span class="m">X = 1</span>에 넣으면 안 된다.</b>
<span class="m">X = −1</span>과 <span class="m">X = 1</span>이 나눠 가지므로
<span class="m">X = −1</span>의 몫 <span class="m">1/9</span>을 먼저 빼야 한다.
<b>겹치는 칸에서는 한쪽을 먼저 확정하고 나머지를 준다.</b><br><br>

<b>분산을 구할 때 <span class="m">{E(X)}<sup>2</sup></span>를 빼먹는다.</b>
<span class="m">E(X<sup>2</sup>) = 20/9</span>만 적고 끝내면 답이 <span class="m">180/9 = 20</span>이 된다.
<b>마지막에 <span class="m">{E(X)}<sup>2</sup> = 4/9</span>를 빼야 한다.</b><br><br>

<b>(나)를 빼고 (가)만으로 풀면 <span class="m">u</span>와 <span class="m">s</span>가 구분되지 않는다.</b>
<span class="m">s − u = 2/9</span>와 <span class="m">u + s = 4/9</span>는 연립해야 풀린다.
하나만 쓰면 답이 여러 개로 갈라진다.

## 노하우

<b>접히는 변환은 겹치는 칸의 개수만큼 조건이 필요하다.</b>
<span class="m">|X|</span>처럼 양쪽이 대칭으로 접히면 칸이 여럿 겹친다.
세어 보면 된다.</p>
<p class="m">겹치는 칸의 개수 = 미지수의 개수 = 필요한 조건의 개수</p>
<p><b>이 문항은 칸이 둘이라 조건도 둘이었다.</b><br><br>

<b>조건을 어느 칸에 쓸지 먼저 정한다.</b>
<span class="m">P(Y = 0)</span>처럼 칸이 하나인 것은 바로 확정된다.
<span class="m">P(X = −1)</span>처럼 한쪽을 직접 주면 다른 쪽이 따라 나온다.
<b>&lsquo;어느 칸이 확정되는가&rsquo;를 먼저 보면 조건을 어떻게 쓸지가 보인다.</b><br><br>

<b>분산은 언제나 두 단계다.</b></p>
<p class="m">E(X<sup>2</sup>) 를 구한다 → 여기서 {E(X)}<sup>2</sup> 를 뺀다</p>
<p><b>마지막 빼기를 잊는 것이 이 유형의 가장 흔한 실수다.</b>
묻는 것이 분산인지 표준편차인지도 확인한다.
