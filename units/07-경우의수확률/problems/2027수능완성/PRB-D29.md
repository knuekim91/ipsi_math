---
id: PRB-D29
unit: 07-경우의수확률
topic: 중복조합과 같은 종류의 접시
level: 4점
difficulty: 최상
source: 2027 수능완성 실전 모의고사 2회 29번
exam: 2027-수능완성
origin: 기출
core: "빵의 배분이 두 가지뿐이고 두 경우 모두 세 접시의 빵 개수가 서로 달라, 접시가 서로 구별되는 것으로 바뀐다"
tags: [중복조합,같은종류,포함배제,여사건]
status: seed
added: 2026-09-07
answer: 481
---

## 문제

<p>같은 종류의 사과 <span class="m">4</span>개와 같은 종류의 배
<span class="m">6</span>개가 있다.
이 <span class="m">10</span>개의 과일과 같은 종류의 빵
<span class="m">6</span>개를 다음 조건을 만족시키도록
같은 종류의 접시 <span class="m">3</span>개에 남김없이 나누어 담는
경우의 수를 구하시오.</p>

<div class="cond">
<span class="cond m">(가) 빵을 1개만 담는 접시의 개수는 1이다.</span>
<span class="cond m">(나) 각 접시에는 과일을 1개 이상 담는다.</span>
<span class="cond m">(다) 사과를 빵보다 많이 담는 접시가 있다.</span>
</div>

## 발상

<b>접시가 같은 종류라는 것이 이 문제의 가장 큰 걸림돌이다.</b>
접시를 구별할 수 없으면 순서를 매길 수 없어 중복조합을 바로 쓸 수 없다.
그런데 <b>빵을 먼저 나누어 보면 이 걸림돌이 저절로 사라진다.</b><br><br>

조건 (가)에서 빵이 정확히 <span class="m">1</span>개인 접시가
<b>딱 하나</b>다. 남은 두 접시에는 빵이 모두
<span class="m">5</span>개 들어가는데,
<b>그 두 접시의 빵은 <span class="m">1</span>개가 되면 안 된다.</b>
합이 <span class="m">5</span>인 두 수 중 <span class="m">1</span>이 없는 것은
<span class="m">{0, 5}</span>와 <span class="m">{2, 3}</span>뿐이다.<br><br>

<b>두 경우 모두 세 접시의 빵 개수가 서로 다르다.</b>
<span class="m">(1, 0, 5)</span>와 <span class="m">(1, 2, 3)</span>이다.
빵의 개수가 다르면 접시를 이름으로 구별할 수 있으므로,
<b>과일을 나누는 단계에서는 접시를 서로 다른 것으로 보아도 된다.</b>
같은 종류라는 조건이 여기서 무력해진다.<br><br>

그 뒤에는 <b>여사건</b>으로 간다.
조건 (나)를 만족시키는 과일 배분을 모두 센 다음,
조건 (다)를 어기는 것을 빼면 된다.
조건 (다)를 어긴다는 것은
<b>모든 접시에서 사과가 빵 이하</b>라는 뜻이라 다루기 쉽다.

## 풀이

<p><span class="step">① 빵을 나눈다.</span>
조건 (가)에서 빵이 <span class="m">1</span>개인 접시는 정확히
<span class="m">1</span>개이다.
그 접시를 뺀 나머지 두 접시의 빵의 합은
<span class="m">6 − 1 = 5</span>이고,
<b>두 접시 모두 빵이 <span class="m">1</span>개여서는 안 된다.</b>
합이 <span class="m">5</span>인 두 개의 음이 아닌 정수의 쌍 중
<span class="m">1</span>을 포함하지 않는 것을 찾는다.</p>
<p class="m">{0, 5}, &nbsp; {2, 3}</p>
<p><span class="m">{1, 4}</span>는 빵이 <span class="m">1</span>개인 접시가
둘이 되어 조건 (가)에 어긋나므로 버린다.
따라서 빵의 배분은 다음 두 가지뿐이다.</p>
<p class="m">(1, 0, 5) 또는 (1, 2, 3)</p>

<p><span class="step">② 접시가 구별됨을 확인한다.</span>
두 경우 모두 <b>세 접시의 빵의 개수가 서로 다르다.</b>
그러므로 각 경우에서 세 접시는 빵의 개수로 구별되고,
<b>과일을 나누는 것은 서로 다른 세 접시에 나누어 담는 문제</b>가 된다.
같은 종류의 접시라는 조건 때문에 중복해서 세는 일이 생기지 않는다.</p>

<p><span class="step">③ 조건 (나)를 만족시키는 과일 배분을 센다.</span>
먼저 조건 (나)를 무시하고 센다.
같은 종류의 사과 <span class="m">4</span>개를 서로 다른
<span class="m">3</span>개의 접시에 나누는 경우의 수는 중복조합이다.</p>
<p class="m"><sub>3</sub>H<sub>4</sub> = <sub>6</sub>C<sub>4</sub> = <sub>6</sub>C<sub>2</sub> = 15</p>
<p>같은 종류의 배 <span class="m">6</span>개도 마찬가지이다.</p>
<p class="m"><sub>3</sub>H<sub>6</sub> = <sub>8</sub>C<sub>6</sub> = <sub>8</sub>C<sub>2</sub> = 28</p>
<p class="m">(전체) = 15 × 28 = 420</p>
<p>여기서 <b>과일이 하나도 없는 접시가 생기는 경우</b>를 뺀다.
특정한 한 접시가 비는 경우는, 과일을 나머지 두 접시에만 담는 것이다.</p>
<p class="m"><sub>2</sub>H<sub>4</sub> × <sub>2</sub>H<sub>6</sub>
= <sub>5</sub>C<sub>4</sub> × <sub>7</sub>C<sub>6</sub> = 5 × 7 = 35</p>
<p>특정한 두 접시가 동시에 비는 경우는 모든 과일을 한 접시에 담는
<span class="m">1</span>가지이다.
세 접시가 모두 비는 일은 없다. 포함배제로 정리한다.</p>
<p class="m">(빈 접시가 있는 경우) = 3 × 35 − 3 × 1 = 105 − 3 = 102</p>
<p class="m">(조건 (나)를 만족) = 420 − 102 = 318</p>
<p>이 값은 빵의 배분과 관계없이 두 경우 모두 같다.</p>

<p><span class="step">④ 빵이 (1, 0, 5)일 때 조건 (다)를 어기는 경우를 센다.</span>
조건 (다)를 어긴다는 것은
<b>모든 접시에서 사과의 개수가 빵의 개수 이하</b>라는 뜻이다.
사과의 개수를 <span class="m">a<sub>1</sub></span>,
<span class="m">a<sub>2</sub></span>,
<span class="m">a<sub>3</sub></span>이라 하면</p>
<p class="m">a<sub>1</sub> ≤ 1, &nbsp; a<sub>2</sub> ≤ 0, &nbsp; a<sub>3</sub> ≤ 5</p>
<p>이고 <span class="m">a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub> = 4</span>이다.
<span class="m">a<sub>2</sub> = 0</span>이므로
<span class="m">a<sub>1</sub></span>이
<span class="m">0</span> 또는 <span class="m">1</span>이다.</p>
<p class="m">(a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>) = (0, 0, 4) 또는 (1, 0, 3)</p>
<p>각각에 대하여 조건 (나)를 지키도록 배를 나눈다.
<b>사과가 <span class="m">0</span>개인 접시에는 배가
<span class="m">1</span>개 이상 들어가야 한다.</b><br>
<span class="m">(0, 0, 4)</span>이면 첫째와 둘째 접시에 배가 필요하므로,
두 접시에 배를 하나씩 미리 준 뒤 남은
<span class="m">4</span>개를 자유롭게 나눈다.</p>
<p class="m"><sub>3</sub>H<sub>4</sub> = <sub>6</sub>C<sub>2</sub> = 15</p>
<p><span class="m">(1, 0, 3)</span>이면 둘째 접시에만 배가 필요하므로,
배 하나를 미리 주고 남은 <span class="m">5</span>개를 나눈다.</p>
<p class="m"><sub>3</sub>H<sub>5</sub> = <sub>7</sub>C<sub>2</sub> = 21</p>
<p class="m">(조건 (다)를 어기는 경우) = 15 + 21 = 36</p>
<p class="m">(빵이 (1, 0, 5)인 경우의 수) = 318 − 36 = 282</p>

<p><span class="step">⑤ 빵이 (1, 2, 3)일 때 조건 (다)를 어기는 경우를 센다.</span>
같은 방법으로 사과의 조건을 적는다.</p>
<p class="m">a<sub>1</sub> ≤ 1, &nbsp; a<sub>2</sub> ≤ 2, &nbsp; a<sub>3</sub> ≤ 3, &nbsp;
a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub> = 4</p>
<p><span class="m">a<sub>1</sub></span>의 값으로 나누어 모두 적는다.</p>
<p class="m">a<sub>1</sub> = 0 : (0, 1, 3), (0, 2, 2)</p>
<p class="m">a<sub>1</sub> = 1 : (1, 0, 3), (1, 1, 2), (1, 2, 1)</p>
<p>사과가 <span class="m">0</span>개인 접시가 있으면
그 접시에 배를 하나 미리 준다.
앞의 세 가지는 사과가 <span class="m">0</span>개인 접시가 하나씩 있고,
뒤의 두 가지는 모든 접시에 사과가 있다.</p>
<p class="m">(0, 1, 3), (0, 2, 2), (1, 0, 3) : 각각 <sub>3</sub>H<sub>5</sub> = 21</p>
<p class="m">(1, 1, 2), (1, 2, 1) : 각각 <sub>3</sub>H<sub>6</sub> = 28</p>
<p class="m">(조건 (다)를 어기는 경우) = 21 × 3 + 28 × 2 = 63 + 56 = 119</p>
<p class="m">(빵이 (1, 2, 3)인 경우의 수) = 318 − 119 = 199</p>

<p><span class="step">⑥ 답을 만든다.</span>
두 경우는 빵의 배분이 다르므로 겹치지 않는다.</p>
<p class="m">282 + 199 = 481</p>
<p class="m">답 481</p>

## 함정

<b>접시가 같은 종류라고 해서 마지막에 <span class="m">3!</span>로 나누면 안 된다.</b>
이 문제에서는 빵의 개수가 세 접시 모두 다르므로
<b>접시가 이미 구별되어 있다.</b>
나누면 오히려 답이 틀린다.
<b>구별이 되는지 아닌지를 먼저 확인하는 것</b>이 순서다.<br><br>

<b><span class="m">{1, 4}</span>를 남겨 두면 조건 (가)를 어긴다.</b>
빵이 <span class="m">1</span>개인 접시가 <b>정확히 하나</b>여야 하므로,
나머지 두 접시 중 하나가 <span class="m">1</span>개이면 안 된다.
이 배제를 놓치면 경우가 하나 더 늘어난다.<br><br>

<b>조건 (다)의 여사건을 잘못 쓰기 쉽다.</b>
&lsquo;사과를 빵보다 많이 담는 접시가 <b>있다</b>&rsquo;의 부정은
&lsquo;<b>모든</b> 접시에서 사과가 빵 <b>이하</b>&rsquo;이다.
&lsquo;사과가 빵보다 적다&rsquo;가 아니다.
<b>등호가 들어가는 자리</b>를 정확히 잡아야 한다.<br><br>

<b>배를 나눌 때 &lsquo;미리 하나 주기&rsquo;를 빠뜨리면 안 된다.</b>
사과가 없는 접시는 조건 (나) 때문에 배가 반드시 있어야 한다.
배 하나를 먼저 놓고 남은 것을 자유롭게 나누는 것이
<b>&lsquo;<span class="m">1</span>개 이상&rsquo;을 중복조합으로 바꾸는 표준 수법</b>이다.

## 노하우

<b>같은 종류의 그릇 문제는 &lsquo;구별되게 만드는 조건&rsquo;을 찾는다.</b>
조건 (가)처럼 <b>담긴 개수를 서로 다르게 만드는 조건</b>이 있으면
그릇에 이름이 붙은 것과 같아진다.
이 문제에서는 <b>빵을 먼저 나누는 것</b>이 그 열쇠였다.
<b>가장 제약이 센 물건부터 나누는 것</b>이 요령이다.<br><br>

<b>&lsquo;<span class="m">1</span>개 이상&rsquo;은 미리 하나씩 주고 중복조합으로 바꾼다.</b>
서로 다른 <span class="m">n</span>개의 그릇에 같은 물건
<span class="m">r</span>개를 각 그릇에 하나 이상 담는 경우의 수는
<span class="m"><sub>n</sub>H<sub>r−n</sub></span>이다.
필요한 그릇에만 하나씩 미리 주면 나머지는 자유 배분이 된다.<br><br>

<b>&lsquo;∼인 것이 있다&rsquo;는 여사건으로 센다.</b>
&lsquo;있다&rsquo;를 직접 세면 겹치는 경우를 다시 빼야 해서 복잡하다.
반면 그 부정인 &lsquo;모두 ∼가 아니다&rsquo;는
<b>각 접시마다 조건이 하나씩 붙는 형태</b>라 나열하기 쉽다.
<b>부등식이 몇 개 안 되는 유한한 경우로 줄어드는지</b>를 보고
여사건으로 갈지 정한다.
