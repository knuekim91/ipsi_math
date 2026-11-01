---
id: STA-W02-V2
parent: STA-W02
unit: 08-통계
topic: 확률 하나로 p를 찾아 평균을 거꾸로 구하기
level: 4점
difficulty: 상
source: 자체 개발 (STA-W02 변형 · 역방향)
origin: 유사문항
core: "P(Y=0) = (1−p)ⁿ 은 p를 혼자 결정한다. 평균을 주지 않아도 확률 하나면 분포가 전부 선다"
tags: [이항분포,이산확률변수,절댓값,평균,역추론]
status: variant
added: 2026-11-01
answer: 24
---

## 문제

<p>이산확률변수 <span class="m">X</span>가 가지는 값은 절댓값이
<span class="m">2</span> 이하인 정수이고, 확률변수
<span class="m">Y = |X − 1|</span>은 이항분포를 따른다.</p>

<p class="m">P(X = 1) = 8/27, &nbsp; P(X = 2) = 1/9</p>

<p>일 때, <span class="m">108 × E(X)</span>의 값을 구하시오.</p>

## 발상

<b>모문항은 평균을 주고 확률을 물었다. 이 문항은 확률을 주고 평균을 묻는다.</b>
방향이 거꾸로다.<br><br>

<b>그런데 평균 <span class="m">np</span>를 안 줬다.</b>
그러면 <span class="m">p</span>를 어디서 구하나.
<b><span class="m">P(X = 1)</span>이 그 일을 한다.</b><br><br>

<span class="m">Y = |X − 1|</span>에서
<span class="m">Y = 0</span>이 되는 것은
<span class="m">X = 1</span> 하나뿐이다.
<b>겹치지 않는 칸</b>이므로</p>
<p class="m">P(X = 1) = P(Y = 0) = (1 − p)<sup>n</sup></p>
<p>이고, <span class="m">n</span>을 먼저 세어 두면
<b><span class="m">p</span>가 한 번에 나온다.</b><br><br>

<b>이것이 이 유형에서 가장 쓸모 있는 한 줄이다.</b>
<span class="m">P(Y = 0)</span>이나
<span class="m">P(Y = n)</span>처럼 <b>양 끝</b>의 확률은
조합이 <span class="m">1</span>이라 거듭제곱 하나뿐이고,
<b>그래서 <span class="m">p</span>를 혼자 결정한다.</b>

## 풀이

<p><span class="step">① n을 센다.</span>
<span class="m">X = −2, −1, 0, 1, 2</span>를
<span class="m">Y = |X − 1|</span>에 넣는다.</p>
<p class="m">X = −2 → Y = 3</p>
<p class="m">X = −1 → Y = 2</p>
<p class="m">X = 0 → Y = 1</p>
<p class="m">X = 1 → Y = 0</p>
<p class="m">X = 2 → Y = 1</p>
<p><span class="m">Y</span>가 가지는 값은
<span class="m">0, 1, 2, 3</span>이고 최댓값이
<span class="m">3</span>이므로</p>
<p class="m">n = 3</p>
<p><b>겹치는 칸은 <span class="m">Y = 1</span> 하나</b>이고,
거기로 <span class="m">X = 0</span>과 <span class="m">X = 2</span>가 들어온다.</p>

<p><span class="step">② P(X = 1)로 p를 구한다.</span>
<span class="m">Y = 0</span>은 <span class="m">X = 1</span>에서만 오므로</p>
<p class="m">P(Y = 0) = (1 − p)<sup>3</sup> = 8/27</p>
<p class="m">1 − p = 2/3 → p = 1/3</p>

<p><span class="step">③ Y의 분포를 적는다.</span>
<span class="m">Y</span>는 <span class="m">B(3, 1/3)</span>을 따르므로
분모를 <span class="m">27</span>로 맞추면</p>
<p class="m">P(Y=0) = 8/27, &nbsp; P(Y=1) = 12/27, &nbsp; P(Y=2) = 6/27, &nbsp; P(Y=3) = 1/27</p>

<p><span class="step">④ X의 분포로 되돌린다.</span></p>
<p class="m">P(X = 1) = P(Y=0) = 8/27</p>
<p class="m">P(X = 0) + P(X = 2) = P(Y=1) = 12/27</p>
<p class="m">P(X = −1) = P(Y=2) = 6/27</p>
<p class="m">P(X = −2) = P(Y=3) = 1/27</p>
<p>주어진 <span class="m">P(X = 2) = 1/9 = 3/27</span>이므로
겹친 칸이 갈라진다.</p>
<p class="m">P(X = 0) = 12/27 − 3/27 = 9/27</p>

<p><span class="step">⑤ 평균을 구한다.</span>
분모가 모두 <span class="m">27</span>이므로 분자만 모아서 계산한다.</p>
<p class="m">E(X) = {(−2)(1) + (−1)(6) + (0)(9) + (1)(8) + (2)(3)} / 27</p>
<p class="m">= (−2 − 6 + 0 + 8 + 6) / 27 = 6/27 = 2/9</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">108 × 2/9 = 24</p>
<p class="m">답 24</p>

<p><span class="step">⑦ 확인한다.</span>
확률의 합을 본다.</p>
<p class="m">(1 + 6 + 9 + 8 + 3) / 27 = 27/27 = 1 ✓</p>

## 함정

<b><span class="m">P(X = 1)</span>을 겹친 칸으로 착각하면 막힌다.</b>
<span class="m">Y = |X − 1|</span>에서 겹치는 것은
<span class="m">Y = 1</span>이다
(<span class="m">X = 0</span>과 <span class="m">X = 2</span>).
<span class="m">Y = 0</span>은 <span class="m">X = 1</span>뿐이라
<b>확률이 그대로 건너온다.</b>
<b>어느 칸이 겹치는지는 대응표를 적어야만 보인다.</b><br><br>

<b>모문항의 <span class="m">Y = |X + 1|</span>과 겹치는 칸이 다르다.</b>
모문항은 <span class="m">X = −2</span>와 <span class="m">X = 0</span>이 겹쳤고,
여기서는 <span class="m">X = 0</span>과 <span class="m">X = 2</span>가 겹친다.
<b>외워 둔 대응을 그대로 쓰면 틀린다.</b> 매번 다시 적는다.<br><br>

<b><span class="m">(1 − p)<sup>3</sup> = 8/27</span>에서
<span class="m">p = 2/3</span>이라고 쓰지 않는다.</b>
<span class="m">1 − p = 2/3</span>이므로
<span class="m">p = 1/3</span>이다.
<b>한 번 더 빼야 한다.</b>
<span class="m">p = 2/3</span>으로 가면 평균이
<span class="m">2</span>가 되어 모문항과 같아지고,
<span class="m">P(X = 1)</span>이 <span class="m">12/27</span>이 되어
주어진 값과 어긋난다. <b>어긋나면 거기서 알아챌 수 있다.</b><br><br>

<b>평균을 구할 때 <span class="m">X = 0</span>인 항을 빼먹어도 답은 같다.</b>
<span class="m">0</span>을 곱하니 사라지기 때문이다.
하지만 <b><span class="m">P(X = 0)</span>은 확률의 합을 확인할 때 필요</b>하므로
적어 두고 넘어간다.

## 노하우

<b>양 끝의 확률은 <span class="m">p</span>를 혼자 결정한다.</b></p>
<p class="m">P(Y = 0) = (1 − p)<sup>n</sup>, &nbsp; P(Y = n) = p<sup>n</sup></p>
<p>조합이 <span class="m">1</span>이라 거듭제곱 하나만 남는다.
<b>평균을 안 줘도 이 확률 하나면 <span class="m">p</span>가 나온다.</b>
<span class="m">8/27</span>, <span class="m">1/27</span>,
<span class="m">16/81</span>처럼 <b>세제곱·네제곱 꼴의 분수</b>가 주어지면
양 끝 확률을 준 것이라고 보면 거의 맞는다.<br><br>

<b>순서는 언제나 같다.</b></p>
<p class="m">값을 적는다 → n → p → Y 의 분포 → X 의 분포 → 묻는 것</p>
<p>어느 방향으로 묻든 이 순서는 바뀌지 않는다.
<b><span class="m">n</span>을 먼저 세지 않으면 어느 것도 시작되지 않는다.</b><br><br>

<b>분모를 하나로 맞춰 두면 평균 계산이 암산이 된다.</b>
전부 <span class="m">27</span>분의 꼴로 적어 두면
분자에 <span class="m">X</span>값을 곱해 더하기만 하면 된다.
<b>분수를 그때그때 통분하면 거기서 실수가 난다.</b>
