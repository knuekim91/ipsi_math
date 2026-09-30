---
id: PRB-W01
unit: 07-경우의수확률
topic: 동전 뒤집기 시행과 홀짝
level: 4점
difficulty: 상
source: 나은이가 가져온 문제 (확률과 통계 28번)
exam: 오답노트
origin: 기출
core: "뒷면의 개수의 홀짝만 본다. 홀수 눈은 2개를 뒤집어 홀짝을 그대로 두고, 짝수 눈은 1개를 뒤집어 홀짝을 바꾼다"
tags: [확률,시행,홀짝,패리티,경우나누기]
status: seed
added: 2026-09-30
answer: ①
---

## 문제

<p>탁자 위에 <span class="m">6</span>개의 동전이 일렬로 놓여 있다.
이 <span class="m">6</span>개의 동전 중 <span class="m">1</span>번째 자리와
<span class="m">2</span>번째 자리와 <span class="m">3</span>번째 자리의 동전은
뒷면이 보이도록 놓여 있고, 나머지 자리의 <span class="m">3</span>개의 동전은
앞면이 보이도록 놓여 있다.
이 <span class="m">6</span>개의 동전과 한 개의 주사위를 사용하여
다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">주사위를 한 번 던져 나온 눈의 수가 k일 때,</span>
<span class="cond m">k가 홀수이면 k번째 자리의 동전과 k+1번째 자리의 동전을 한 번씩 뒤집어 제자리에 놓고,</span>
<span class="cond m">k가 짝수이면 임의로 하나의 동전을 선택하여 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>이 시행을 <span class="m">3</span>번 반복한 후 이
<span class="m">6</span>개의 동전이 모두 같은 면이 보이도록 놓여 있을 확률은?</p>

<div class="fig">
<svg viewBox="0 0 384 116" role="img" aria-label="동전 6개가 일렬로 놓여 있다. 1, 2, 3번째 자리는 뒷면이 보이고 4, 5, 6번째 자리는 앞면이 보인다.">
  <circle class="po" cx="42"  cy="30" r="21"/>
  <circle class="po" cx="110" cy="30" r="21"/>
  <circle class="po" cx="178" cy="30" r="21"/>
  <circle class="po" cx="246" cy="30" r="21"/>
  <circle class="po" cx="314" cy="30" r="21"/>
  <circle class="po" cx="382" cy="30" r="21"/>
  <circle class="rg" cx="42"  cy="30" r="21"/>
  <circle class="rg" cx="110" cy="30" r="21"/>
  <circle class="rg" cx="178" cy="30" r="21"/>
  <text x="42"  y="72" text-anchor="middle">뒷면</text>
  <text x="110" y="72" text-anchor="middle">뒷면</text>
  <text x="178" y="72" text-anchor="middle">뒷면</text>
  <text x="246" y="72" text-anchor="middle">앞면</text>
  <text x="314" y="72" text-anchor="middle">앞면</text>
  <text x="382" y="72" text-anchor="middle">앞면</text>
  <text x="42"  y="98" text-anchor="middle">1</text>
  <text x="110" y="98" text-anchor="middle">2</text>
  <text x="178" y="98" text-anchor="middle">3</text>
  <text x="246" y="98" text-anchor="middle">4</text>
  <text x="314" y="98" text-anchor="middle">5</text>
  <text x="382" y="98" text-anchor="middle">6</text>
  <text x="212" y="114" text-anchor="middle">자리 번호</text>
</svg>
</div>

<div class="choices"><span>① 5/144</span><span>② 1/24</span><span>③ 7/144</span>
<span>④ 1/18</span><span>⑤ 1/16</span></div>

## 발상

<b>동전 여섯 개의 상태를 모두 따라가면 경우가
<span class="m">2<sup>6</sup> = 64</span>가지라 감당할 수 없다.
하나의 수만 보고 따라가야 한다. 그 수가 <b>뒷면의 개수</b>다.</b><br><br>

<b>두 규칙이 뒷면의 개수에 하는 일이 완전히 다르다.</b>
<span class="m">k</span>가 홀수이면 동전 <b>두 개</b>를 뒤집는다.
두 개가 모두 뒷면이었다면 뒷면이 <span class="m">2</span> 줄고,
모두 앞면이었다면 <span class="m">2</span> 늘고,
하나씩이었다면 그대로다.
<b>어느 경우든 뒷면의 개수의 홀짝은 바뀌지 않는다.</b>
반면 <span class="m">k</span>가 짝수이면 동전 <b>한 개</b>를 뒤집으므로
뒷면의 개수가 반드시 <span class="m">1</span> 늘거나 <span class="m">1</span> 줄고,
<b>홀짝이 반드시 바뀐다.</b><br><br>

<b>처음에 뒷면은 <span class="m">3</span>개로 홀수이고,
목표인 &lsquo;모두 같은 면&rsquo;은 뒷면이 <span class="m">0</span>개이거나
<span class="m">6</span>개로 둘 다 짝수다.</b>
홀수에서 짝수로 가려면 홀짝이 <b>홀수 번</b> 바뀌어야 하므로,
<b><span class="m">3</span>번의 시행에서 짝수 눈이 홀수 번 나와야 한다.</b>
곧 짝수 눈이 <span class="m">1</span>번 또는 <span class="m">3</span>번이다.
이 한 줄이 경우를 둘로 줄여 준다.<br><br>

<b>홀수 눈이 만드는 세 쌍이 서로 겹치지 않는다는 것도 중요하다.</b>
<span class="m">k = 1, 3, 5</span>는 각각
<span class="m">(1, 2)</span>, <span class="m">(3, 4)</span>,
<span class="m">(5, 6)</span>번째 자리를 뒤집는다.
<b>같은 쌍을 두 번 뒤집으면 원래대로 돌아온다.</b>

## 풀이

<p><span class="step">① 자리와 기호를 정한다.</span>
<span class="m">n</span>번째 자리의 동전을 <span class="m">c<sub>n</sub></span>이라 하자.
처음 상태는 다음과 같다.</p>
<p class="m">c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub> : 뒷면 &nbsp;/&nbsp;
c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub> : 앞면</p>
<p>홀수 눈이 뒤집는 세 쌍을 이름 붙인다.</p>
<p class="m">P<sub>1</sub> = {c<sub>1</sub>, c<sub>2</sub>}, &nbsp;
P<sub>2</sub> = {c<sub>3</sub>, c<sub>4</sub>}, &nbsp;
P<sub>3</sub> = {c<sub>5</sub>, c<sub>6</sub>}</p>

<p><span class="step">② 홀짝으로 경우를 가른다.</span>
발상에서 본 대로, 짝수 눈이 나온 횟수가 홀수여야 한다.
<span class="m">3</span>번 던지므로 다음 두 경우뿐이다.</p>
<p class="m">(경우 1) 짝수 눈 3번 &nbsp;/&nbsp; (경우 2) 짝수 눈 1번, 홀수 눈 2번</p>

<p><span class="step">③ 경우 1을 센다.</span>
세 번 모두 짝수 눈이므로, 매번 <b>임의의 동전 한 개</b>를 뒤집는다.
<span class="m">3</span>번의 시행에서 동전은 모두
<span class="m">3</span>번 뒤집힌다.<br>
모두 앞면이 되려면 처음 뒷면인
<span class="m">c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub></span>을
<b>각각 한 번씩</b> 뒤집어야 한다. 그 순서는
<span class="m">3! = 6</span>가지다.
모두 뒷면이 되려면 <span class="m">c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub></span>을
각각 한 번씩 뒤집어야 하므로 역시 <span class="m">6</span>가지다.</p>
<p>한 번의 시행에서 <b>짝수 눈이 나오고 특정한 동전 하나를 고를</b> 확률은</p>
<p class="m">(3/6) × (1/6) = 1/12</p>
<p>이므로, 경우 1의 확률은 다음과 같다.</p>
<p class="m">(6 + 6) × (1/12)<sup>3</sup> = 12 × 1/1728 = 1/144</p>

<p><span class="step">④ 경우 2에서 무엇이 가능한지 따진다.</span>
홀수 눈 두 번은 쌍 두 개를 뒤집고, 짝수 눈 한 번은 동전 한 개를 뒤집는다.
<b>같은 쌍이 두 번 나오면 서로 지워져 아무 일도 일어나지 않는다.</b>
그러면 동전 한 개만 바뀌는데, 처음 상태에서 한 개만 바꾸어
모두 같은 면이 될 수는 없다. 그러므로 <b>서로 다른 두 쌍</b>이어야 한다.<br>
서로 다른 두 쌍을 고르는 방법은
<span class="m">P<sub>1</sub>P<sub>2</sub></span>,
<span class="m">P<sub>1</sub>P<sub>3</sub></span>,
<span class="m">P<sub>2</sub>P<sub>3</sub></span>의 세 가지다. 하나씩 확인한다.</p>
<p class="m">P<sub>1</sub>, P<sub>2</sub> → c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>, c<sub>4</sub>가 뒤집혀 앞 앞 앞 뒤 앞 앞</p>
<p class="m">P<sub>1</sub>, P<sub>3</sub> → c<sub>1</sub>, c<sub>2</sub>, c<sub>5</sub>, c<sub>6</sub>가 뒤집혀 앞 앞 뒤 앞 뒤 뒤</p>
<p class="m">P<sub>2</sub>, P<sub>3</sub> → c<sub>3</sub>, c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub>가 뒤집혀 뒤 뒤 앞 뒤 뒤 뒤</p>
<p>여기에 동전 한 개를 더 뒤집어 모두 같은 면이 되어야 한다.
<b>어긋난 동전이 정확히 하나인 경우만 살아남는다.</b></p>
<p class="m">P<sub>1</sub>, P<sub>2</sub> 이고 c<sub>4</sub>를 뒤집으면 → 모두 앞면</p>
<p class="m">P<sub>2</sub>, P<sub>3</sub> 이고 c<sub>3</sub>을 뒤집으면 → 모두 뒷면</p>
<p><span class="m">P<sub>1</sub>, P<sub>3</sub></span>인 경우는 어긋난 동전이
<span class="m">3</span>개여서 한 번으로는 맞출 수 없다.</p>

<p><span class="step">⑤ 경우 2의 확률을 구한다.</span>
살아남은 두 가지는 구조가 같으므로 하나만 세고 <span class="m">2</span>를 곱한다.
<span class="m">3</span>번의 시행 중 <b>짝수 눈이 몇 번째에 나오는지</b>가
<span class="m">3</span>가지,
그 시행에서 특정한 동전을 고를 확률이 <span class="m">1/12</span>,
나머지 두 번이 정해진 두 홀수 눈이 되는 순서가
<span class="m">2</span>가지이고 각각의 확률이
<span class="m">(1/6)<sup>2</sup></span>이다.</p>
<p class="m">3 × (1/12) × 2 × (1/6)<sup>2</sup> = 3 × (1/12) × (1/18) = 1/72</p>
<p>두 가지를 합한다.</p>
<p class="m">2 × (1/72) = 1/36</p>

<p><span class="step">⑥ 답을 만든다.</span>
두 경우는 짝수 눈의 횟수가 달라 서로 겹치지 않으므로 그대로 더한다.</p>
<p class="m">1/144 + 1/36 = 1/144 + 4/144 = 5/144</p>
<p class="m">답 ①</p>

## 함정

<b>홀짝을 따지지 않고 경우를 다 세려 하면 시간 안에 끝나지 않는다.</b>
<span class="m">3</span>번의 시행에서 나올 수 있는 결과는
<span class="m">(6 × 6)<sup>3</sup></span>에 이른다.
<b>뒷면의 개수의 홀짝</b>이라는 한 줄이 경우를 둘로 줄인다.
이 관문을 못 넘으면 문제가 열리지 않는다.<br><br>

<b>&lsquo;모두 같은 면&rsquo;은 모두 앞면과 모두 뒷면 <b>둘 다</b>이다.</b>
한쪽만 세면 답이 절반이 된다.
이 문제에서는 두 확률이 각각
<span class="m">5/288</span>로 같아서 더하면 <span class="m">5/144</span>가 된다.<br><br>

<b>같은 홀수 눈이 두 번 나오면 아무 일도 없다는 것을 놓치기 쉽다.</b>
<span class="m">k = 3</span>이 두 번 나오면
<span class="m">c<sub>3</sub>, c<sub>4</sub></span>가 두 번씩 뒤집혀 제자리로 돌아온다.
<b>뒤집기는 두 번 하면 원래대로</b>라는 성질을 늘 염두에 둔다.<br><br>

<b>짝수 눈일 때 &lsquo;임의로 하나&rsquo;는 여섯 개 중 하나다.</b>
앞면 중에서 고르는 것도, 뒷면 중에서 고르는 것도 아니다.
확률이 <span class="m">1/6</span>이지 <span class="m">1/3</span>이 아니다.

## 노하우

<b>뒤집기 문제는 개수의 홀짝부터 본다.</b>
한 번에 <b>짝수 개</b>를 뒤집는 규칙은 홀짝을 보존하고,
<b>홀수 개</b>를 뒤집는 규칙은 홀짝을 바꾼다.
목표 상태의 홀짝과 처음 상태의 홀짝을 비교하면
<b>어떤 규칙이 몇 번 나와야 하는지</b>가 먼저 정해진다.
이것만으로 경우의 대부분이 걸러진다.<br><br>

<b>서로 겹치지 않는 묶음으로 나누어 본다.</b>
<span class="m">k = 1, 3, 5</span>가 만드는 세 쌍
<span class="m">(1,2)</span>, <span class="m">(3,4)</span>,
<span class="m">(5,6)</span>은 서로 겹치지 않는다.
겹치지 않으면 <b>순서를 따질 필요가 없고</b>, 어떤 쌍이 몇 번 나왔는지만 세면 된다.
같은 쌍이 짝수 번이면 없던 일이 된다.<br><br>

<b>대칭이 보이면 절반만 계산한다.</b>
이 문제는 &lsquo;앞뒤를 모두 바꾸고 자리 순서를 거꾸로 하는&rsquo; 뒤바꿈에 대하여
처음 상태와 규칙이 모두 그대로다.
그래서 <b>모두 앞면일 확률과 모두 뒷면일 확률이 반드시 같다.</b>
한쪽만 구하고 <span class="m">2</span>를 곱해도 된다.
