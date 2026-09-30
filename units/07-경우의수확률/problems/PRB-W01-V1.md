---
id: PRB-W01-V1
parent: PRB-W01
unit: 07-경우의수확률
topic: 동전 뒤집기 시행과 홀짝
level: 3점
difficulty: 중
source: 자체 개발 (PRB-W01 변형 · 시행 2번)
origin: 유사문항
core: "시행이 2번이면 짝수 눈은 정확히 1번이어야 하고, 남은 경우가 몇 개 안 되어 손으로 다 셀 수 있다"
tags: [확률,시행,홀짝,패리티]
status: variant
added: 2026-09-30
answer: ③
---

## 문제

<p>탁자 위에 <span class="m">6</span>개의 동전이 일렬로 놓여 있다.
<span class="m">1</span>번째, <span class="m">2</span>번째,
<span class="m">3</span>번째 자리의 동전은 뒷면이 보이도록 놓여 있고,
나머지 <span class="m">3</span>개의 동전은 앞면이 보이도록 놓여 있다.
이 <span class="m">6</span>개의 동전과 한 개의 주사위를 사용하여
다음 시행을 한다.</p>

<div class="cond">
<span class="cond m">주사위를 한 번 던져 나온 눈의 수가 k일 때,</span>
<span class="cond m">k가 홀수이면 k번째 자리의 동전과 k+1번째 자리의 동전을 한 번씩 뒤집어 제자리에 놓고,</span>
<span class="cond m">k가 짝수이면 임의로 하나의 동전을 선택하여 한 번 뒤집어 제자리에 놓는다.</span>
</div>

<p>이 시행을 <span class="m">2</span>번 반복한 후 이
<span class="m">6</span>개의 동전이 모두 같은 면이 보이도록 놓여 있을 확률은?</p>

<div class="choices"><span>① 1/36</span><span>② 1/24</span><span>③ 1/18</span>
<span>④ 5/72</span><span>⑤ 1/12</span></div>

## 발상

<b>규칙은 그대로이고 시행 횟수만 <span class="m">3</span>번에서
<span class="m">2</span>번으로 줄었다.
그런데 이 한 글자가 경우를 크게 줄인다.</b><br><br>

뒷면의 개수는 처음에 <span class="m">3</span>개로 홀수이고,
모두 같은 면이면 <span class="m">0</span>개이거나 <span class="m">6</span>개로 짝수다.
홀짝을 바꾸는 것은 <b>짝수 눈뿐</b>이므로 짝수 눈이 홀수 번 나와야 한다.
<span class="m">2</span>번만 던지므로 <b>짝수 눈이 정확히 한 번</b>이고,
나머지 한 번은 홀수 눈이다.<br><br>

<b>그러면 일어나는 일이 아주 단순해진다.</b>
홀수 눈 한 번이 쌍 하나를 뒤집고, 짝수 눈 한 번이 동전 하나를 뒤집는다.
<b>뒤집는 순서는 결과에 영향을 주지 않으므로</b>
어떤 쌍과 어떤 동전을 골랐는지만 따지면 된다.

## 풀이

<p><span class="step">① 경우를 하나로 좁힌다.</span>
<span class="m">n</span>번째 자리의 동전을 <span class="m">c<sub>n</sub></span>이라 하자.
뒷면의 개수가 홀수인 <span class="m">3</span>에서 짝수인
<span class="m">0</span> 또는 <span class="m">6</span>으로 가야 하므로,
홀짝이 홀수 번 바뀌어야 한다.
<span class="m">2</span>번의 시행에서 짝수 눈은 정확히 한 번 나온다.</p>

<p><span class="step">② 홀수 눈이 뒤집는 쌍을 적는다.</span></p>
<p class="m">k = 1 → {c<sub>1</sub>, c<sub>2</sub>}, &nbsp;
k = 3 → {c<sub>3</sub>, c<sub>4</sub>}, &nbsp;
k = 5 → {c<sub>5</sub>, c<sub>6</sub>}</p>
<p>짝수 눈은 여섯 개 중 임의의 한 개를 뒤집는다.
그러므로 <b>모두 세 개의 동전이 뒤집힌다.</b>
다만 고른 동전이 그 쌍 안에 들어 있으면 두 번 뒤집혀 제자리로 돌아오고,
실제로는 한 개만 바뀐다.</p>

<p><span class="step">③ 모두 앞면이 되는 경우를 찾는다.</span>
처음에 뒷면인 것은
<span class="m">c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub></span>이므로
<b>정확히 이 세 개만</b> 뒤집혀야 한다.
쌍 하나와 동전 하나로 <span class="m">{c<sub>1</sub>, c<sub>2</sub>, c<sub>3</sub>}</span>을
만들려면, 쌍이 이 세 개 안에 들어 있어야 한다.</p>
<p class="m">k = 1 로 {c<sub>1</sub>, c<sub>2</sub>}를 뒤집고, 짝수 눈에서 c<sub>3</sub>을 고른다</p>
<p><span class="m">k = 3</span>인 쌍
<span class="m">{c<sub>3</sub>, c<sub>4</sub>}</span>는
<span class="m">c<sub>4</sub></span>가 들어 있어 쓸 수 없다.
따라서 이 한 가지뿐이다.</p>

<p><span class="step">④ 모두 뒷면이 되는 경우를 찾는다.</span>
이번에는 처음에 앞면인
<span class="m">c<sub>4</sub>, c<sub>5</sub>, c<sub>6</sub></span>만 뒤집혀야 한다.</p>
<p class="m">k = 5 로 {c<sub>5</sub>, c<sub>6</sub>}를 뒤집고, 짝수 눈에서 c<sub>4</sub>를 고른다</p>
<p>역시 한 가지뿐이다.</p>

<p><span class="step">⑤ 확률을 구한다.</span>
한 번의 시행에서 특정한 홀수 눈이 나올 확률은
<span class="m">1/6</span>이고,
짝수 눈이 나오면서 특정한 동전을 고를 확률은</p>
<p class="m">(3/6) × (1/6) = 1/12</p>
<p>이다. 두 번의 시행 중 <b>짝수 눈이 첫 번째인지 두 번째인지</b>
<span class="m">2</span>가지가 있으므로, 모두 앞면이 될 확률은</p>
<p class="m">2 × (1/6) × (1/12) = 2/72 = 1/36</p>
<p>모두 뒷면이 될 확률도 같은 모양이므로 <span class="m">1/36</span>이다.</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">1/36 + 1/36 = 2/36 = 1/18</p>
<p class="m">답 ③</p>

## 함정

<b>짝수 눈에서 고른 동전이 쌍 안에 있는 경우를 빼먹으면 안 된다.</b>
예를 들어 <span class="m">k = 1</span>로
<span class="m">c<sub>1</sub>, c<sub>2</sub></span>를 뒤집고
짝수 눈에서 <span class="m">c<sub>1</sub></span>을 골랐다면,
<span class="m">c<sub>1</sub></span>은 두 번 뒤집혀 제자리다.
결국 <span class="m">c<sub>2</sub></span> 하나만 바뀐다.
<b>이런 경우는 모두 같은 면이 될 수 없다는 것을 확인하고 넘어가야</b>
빠뜨린 경우가 없다고 말할 수 있다.<br><br>

<b>순서를 세는 자리를 헷갈리면 안 된다.</b>
곱해야 하는 <span class="m">2</span>는 <b>짝수 눈이 몇 번째 시행인가</b>이지
모두 앞면과 모두 뒷면의 두 가지가 아니다.
그 둘은 마지막에 따로 더한다.

## 노하우

<b>시행 횟수가 줄면 홀짝 조건이 경우를 통째로 정해 준다.</b>
<span class="m">3</span>번이면 짝수 눈이 <span class="m">1</span>번 또는
<span class="m">3</span>번이라 경우가 둘이지만,
<span class="m">2</span>번이면 <b>짝수 눈이 딱 한 번</b>으로 정해진다.
<b>시행 횟수부터 보고 홀짝 조건을 적용하는 것</b>이 언제나 첫 단계다.<br><br>

<b>뒤집는 순서는 결과를 바꾸지 않는다.</b>
같은 동전을 두 번 뒤집으면 제자리이고,
서로 다른 동전은 서로 간섭하지 않는다.
그래서 <b>&lsquo;무엇을 몇 번 뒤집었나&rsquo;만 세면 되고 순서는 확률을 셀 때만 쓴다.</b>
