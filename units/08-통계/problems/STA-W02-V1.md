---
id: STA-W02-V1
parent: STA-W02
unit: 08-통계
topic: 이항분포를 따를 수 있는 변환 고르기
level: 4점
difficulty: 상
source: 자체 개발 (STA-W02 변형 · 조건의 뜻을 정면으로)
origin: 유사문항
core: "B(n,p)의 값은 0부터 n까지 빠짐없이 나와야 한다. 최댓값만 보면 안 되고 0에서 시작하는지도 봐야 한다"
tags: [이항분포,이산확률변수,절댓값,확률변수의값,판정]
status: variant
added: 2026-11-01
answer: ④
---

## 문제

<p>이산확률변수 <span class="m">X</span>가 가지는 값이 절댓값이
<span class="m">2</span> 이하인 정수일 때,
<span class="m">X</span>의 확률분포를 적당히 정하여
<b>이항분포를 따르게 할 수 있는</b> 확률변수만을
&lt;보기&gt;에서 있는 대로 고른 것은?</p>

<span class="cond m">ㄱ. |X|</span><span class="cond m">ㄴ. |X| + 1</span><span class="cond m">ㄷ. |X + 1|</span>

<div class="choices"><span>① ㄱ</span><span>② ㄷ</span><span>③ ㄱ, ㄴ</span>
<span>④ ㄱ, ㄷ</span><span>⑤ ㄱ, ㄴ, ㄷ</span></div>

## 발상

<b>모문항에서 <span class="m">n = 3</span>을 찾던 그 한 줄만으로 풀린다.</b>
계산이 거의 없다. 대신 <b>그 한 줄을 정확히 알고 있는지</b>를 묻는다.<br><br>

<span class="m">B(n, p)</span>를 따르는 확률변수는
<span class="m">n</span>번 중 성공한 횟수이므로 가질 수 있는 값이</p>
<p class="m">0, 1, 2, …, n</p>
<p>이다. 여기서 <b>두 가지</b>를 읽어야 한다.</p>
<p class="m">① 가장 큰 값이 n 이다</p>
<p class="m">② 0 부터 하나도 빠짐없이 나와야 한다</p>
<p><b>①만 보고 ②를 놓치는 것이 이 문항의 함정이다.</b><br><br>

그러니 할 일은 하나다. <b>각 변환이 가지는 값을 전부 적고,
<span class="m">0</span>부터 연속해서 이어지는지 본다.</b>
확률을 어떻게 나눌지는 그다음 문제다.

## 풀이

<p><span class="step">① X가 가지는 값을 적는다.</span></p>
<p class="m">X = −2, −1, 0, 1, 2</p>

<p><span class="step">② ㄱ. |X| 를 확인한다.</span></p>
<p class="m">|−2| = 2, &nbsp; |−1| = 1, &nbsp; |0| = 0, &nbsp; |1| = 1, &nbsp; |2| = 2</p>
<p>가지는 값은 <span class="m">0, 1, 2</span>로
<span class="m">0</span>부터 빠짐없이 이어진다.
최댓값이 <span class="m">2</span>이므로
<span class="m">B(2, p)</span>가 될 수 있는지 보면 된다.
<span class="m">B(2, p)</span>에서</p>
<p class="m">P(0) = (1−p)<sup>2</sup>, &nbsp; P(1) = 2p(1−p), &nbsp; P(2) = p<sup>2</sup></p>
<p>이고, 예를 들어 <span class="m">p = 1/2</span>이면
<span class="m">1/4, 1/2, 1/4</span>이다.
<span class="m">P(X = 0) = 1/4</span>로 두고,
<span class="m">P(X = −1) + P(X = 1) = 1/2</span>,
<span class="m">P(X = −2) + P(X = 2) = 1/4</span>이 되도록
<b>아무렇게나 나누면</b> 된다.
<b>따를 수 있다.</b></p>

<p><span class="step">③ ㄴ. |X| + 1 을 확인한다.</span></p>
<p class="m">가지는 값 : 1, 2, 3</p>
<p>값이 세 개이고 연속이라 <span class="m">B(2, p)</span>처럼 보이지만,
<b><span class="m">0</span>이 없다.</b>
<span class="m">B(n, p)</span>를 따르는 확률변수는
<span class="m">P(Y = 0) = (1 − p)<sup>n</sup></span>이고,
<span class="m">0 &lt; p &lt; 1</span>이면 이 값은
<span class="m">0</span>이 아니다.
곧 <b><span class="m">Y = 0</span>이 반드시 일어날 수 있어야</b> 하는데
<span class="m">|X| + 1 ≥ 1</span>이라 영영 <span class="m">0</span>이 못 된다.
<b>따를 수 없다.</b></p>

<p><span class="step">④ ㄷ. |X + 1| 을 확인한다.</span></p>
<p class="m">|−1| = 1, &nbsp; |0| = 0, &nbsp; |1| = 1, &nbsp; |2| = 2, &nbsp; |3| = 3</p>
<p>가지는 값은 <span class="m">0, 1, 2, 3</span>으로
<span class="m">0</span>부터 빠짐없이 이어진다.
<span class="m">B(3, p)</span>의 네 확률을
<span class="m">P(X = −1)</span>,
<span class="m">P(X = −2) + P(X = 0)</span>,
<span class="m">P(X = 1)</span>,
<span class="m">P(X = 2)</span>에 그대로 맞추면 되므로
<b>따를 수 있다.</b></p>

<p><span class="step">⑤ 답을 만든다.</span>
따를 수 있는 것은 ㄱ과 ㄷ이다.</p>
<p class="m">답 ④</p>

## 함정

<b>ㄴ이 이 문항의 전부다.</b>
<span class="m">|X| + 1</span>은 값이 <span class="m">1, 2, 3</span>으로
<b>세 개이고 연속</b>이라 <span class="m">B(2, p)</span>와 모양이 같아 보인다.
하지만 <b>이항분포는 반드시 <span class="m">0</span>에서 시작한다.</b>
<span class="m">n</span>번 중 한 번도 성공하지 못하는 경우가 있기 때문이다.
<b>&lsquo;값이 몇 개인가&rsquo;가 아니라 &lsquo;<span class="m">0</span>부터 시작하는가&rsquo;를 본다.</b><br><br>

<b>ㄴ을 고르면 ③이나 ⑤가 나온다.</b>
<span class="m">|X| + 1</span>을 보고 &lsquo;<span class="m">|X|</span>가 되니까
한 칸 민 것뿐&rsquo;이라고 넘기면 걸린다.
<b>평행이동한 이항분포는 이항분포가 아니다.</b><br><br>

<b>ㄷ에서 겹치는 칸을 보고 &lsquo;안 된다&rsquo;고 판단하지 않는다.</b>
<span class="m">|X + 1| = 1</span>이
<span class="m">X = −2</span>와 <span class="m">X = 0</span> 두 군데에서 오는 것은
<b>아무 문제가 되지 않는다.</b>
합이 <span class="m">B(3, p)</span>의 값과 같기만 하면 되고,
어떻게 나눌지는 자유다.
<b>겹침은 &lsquo;값을 못 가진다&rsquo;와 전혀 다른 이야기</b>다.<br><br>

<b>ㄱ에서 <span class="m">n = 2</span>인데 ㄷ에서는
<span class="m">n = 3</span>인 것이 이상하지 않다.</b>
<span class="m">n</span>은 문제가 정해 주는 수가 아니라
<b>변환마다 따로 세는 수</b>다.

## 노하우

<b>이항분포 판정은 두 줄이면 끝난다.</b></p>
<p class="m">① 가지는 값을 전부 적는다</p>
<p class="m">② 0, 1, 2, …, n 으로 빠짐없이 이어지는가</p>
<p>이어지면 <b>따를 수 있고</b>, 하나라도 비거나
<span class="m">0</span>에서 시작하지 않으면 <b>따를 수 없다.</b>
<b>확률을 계산할 필요가 아예 없다.</b><br><br>

<b>자주 나오는 안 되는 꼴을 외워 둔다.</b></p>
<p class="m">|X| + 1 → 1, 2, 3 : 0 이 없다</p>
<p class="m">X<sup>2</sup> → 0, 1, 4 : 2 와 3 이 빈다</p>
<p class="m">2|X| → 0, 2, 4 : 1 과 3 이 빈다</p>
<p><b>상수를 더하거나 배수를 곱하면 이항분포가 깨진다.</b>
절댓값처럼 <b>값을 겹치게 만드는 것</b>은 괜찮지만,
<b>값을 옮기거나 벌리는 것</b>은 안 된다.
이 차이를 잡아 두면 판정이 순식간이다.<br><br>

<b>&lsquo;있는 대로 고르시오&rsquo;는 전부 확인하라는 뜻이다.</b>
하나를 찾았다고 멈추지 않는다.
세 개면 세 개 다 값을 적어 본다.
<b>적어 보는 데 드는 시간이 고민하는 시간보다 짧다.</b>
