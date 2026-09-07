---
id: PRB-D25
unit: 07-경우의수확률
topic: 중복순열과 여사건 세기
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 2회 25번
exam: 2027-수능완성
origin: 기출
core: "12100보다 큰 것을 직접 세지 말고, 전체에서 12100 이하인 것을 빼는 여사건으로 센다"
tags: [중복순열,여사건,자리수비교]
status: seed
added: 2026-09-07
answer: ④
---

## 문제

<p>숫자 <span class="m">1</span>, <span class="m">2</span>,
<span class="m">3</span> 중에서 중복을 허락하여 <span class="m">5</span>개를
택해 일렬로 나열하여 만들 수 있는 다섯 자리의 자연수 중
<span class="m">12100</span>보다 큰 자연수의 개수는?</p>

<div class="choices"><span>① 162</span><span>② 180</span><span>③ 198</span>
<span>④ 216</span><span>⑤ 234</span></div>

## 발상

<b>&lsquo;보다 큰 것&rsquo;을 세는 것보다 &lsquo;이하인 것&rsquo;을 세는 편이 훨씬 짧다.</b>
만들 수 있는 수는 모두 다섯 자리이고 각 자리에
<span class="m">1</span>, <span class="m">2</span>,
<span class="m">3</span> 중 하나가 오므로 전체 개수는
<span class="m">3<sup>5</sup></span>이다.
여기서 <span class="m">12100</span> 이하인 것의 개수를 빼면 된다.<br><br>

<b><span class="m">12100</span> 이하인 것이 몇 개 안 된다는 점이 핵심이다.</b>
만드는 수는 모두 <span class="m">11111</span> 이상이다.
만 자리가 <span class="m">2</span>나 <span class="m">3</span>이면
그 수는 <span class="m">20000</span> 이상이므로
<span class="m">12100</span>보다 크다.
그러므로 만 자리가 <span class="m">1</span>인 경우만 살펴보면 되고,
그 다음 천 자리까지만 비교하면 결론이 난다.

## 풀이

<p><span class="step">① 전체 개수를 구한다.</span>
다섯 개의 자리 각각에 <span class="m">1</span>,
<span class="m">2</span>, <span class="m">3</span> 중
하나가 중복을 허락하여 들어가므로, 중복순열의 수이다.</p>
<p class="m">(전체) = <sub>3</sub>Π<sub>5</sub> = 3<sup>5</sup> = 243</p>
<p>모든 자리가 <span class="m">1</span> 이상이므로
만들어지는 수는 모두 다섯 자리 자연수이다.</p>

<p><span class="step">② 12100 이하인 경우를 만 자리로 나눈다.</span>
만들어지는 수를
<span class="m">abcde</span>라 하자.
각 자리는 <span class="m">1</span>, <span class="m">2</span>,
<span class="m">3</span> 중 하나이다.<br>
만 자리 <span class="m">a</span>가 <span class="m">2</span> 또는
<span class="m">3</span>이면 그 수는 <span class="m">20000</span> 이상이므로
<span class="m">12100</span>보다 크다.
따라서 <span class="m">12100</span> 이하가 되려면
<span class="m">a = 1</span>이어야 한다.</p>

<p><span class="step">③ 천 자리로 다시 나눈다.</span>
<span class="m">a = 1</span>이므로 그 수는
<span class="m">1bcde</span> 꼴이고,
<span class="m">12100</span>과 비교하려면 천 자리
<span class="m">b</span>를 <span class="m">2</span>와 견주면 된다.<br>
<span class="m">b = 1</span>이면 그 수는 최대
<span class="m">13333</span>이 아니라
<span class="m">11333</span>이므로
<span class="m">12100</span>보다 작다.
곧 <span class="m">b = 1</span>인 경우는 <b>모두</b>
<span class="m">12100</span> 이하이다.
남은 세 자리 <span class="m">c</span>, <span class="m">d</span>,
<span class="m">e</span>가 각각 <span class="m">3</span>가지이므로</p>
<p class="m">3<sup>3</sup> = 27 (개)</p>
<p><span class="m">b = 2</span>이면 그 수는
<span class="m">12cde</span> 꼴이고, 백 자리
<span class="m">c</span>가 <span class="m">1</span> 이상이므로
가장 작은 수가 <span class="m">12111</span>이다.</p>
<p class="m">12111 &gt; 12100</p>
<p>따라서 <span class="m">b = 2</span>인 경우는 <b>하나도</b>
<span class="m">12100</span> 이하가 아니다.<br>
<span class="m">b = 3</span>이면 그 수는 <span class="m">13000</span> 이상이므로
역시 <span class="m">12100</span>보다 크다.</p>

<p><span class="step">④ 12100 이하인 개수를 정리한다.</span></p>
<p class="m">(12100 이하) = 27</p>

<p><span class="step">⑤ 답을 만든다.</span>
전체에서 뺀다.</p>
<p class="m">(12100보다 큰 것) = 243 − 27 = 216</p>
<p class="m">답 ④</p>

## 함정

<b><span class="m">12100</span> 자체는 만들 수 없다는 점에 주의한다.</b>
<span class="m">0</span>은 쓸 수 있는 숫자가 아니므로
<span class="m">12100</span>은 애초에 만들어지지 않는다.
그래서 &lsquo;<span class="m">12100</span> 이하&rsquo;와
&lsquo;<span class="m">12100</span> 미만&rsquo;이 같은 개수가 되어
경계에서 헷갈릴 일이 없다.<br><br>

<b><span class="m">b = 2</span>일 때를 대충 넘기면 안 된다.</b>
<span class="m">12cde</span>에서 <span class="m">c</span>가
<span class="m">0</span>일 수 있다면
<span class="m">12011</span>처럼 <span class="m">12100</span>보다
작은 수가 생긴다.
<b>쓸 수 있는 숫자가 <span class="m">1</span>, <span class="m">2</span>,
<span class="m">3</span>뿐이라 최솟값이 <span class="m">12111</span></b>이라는
확인이 이 문제의 실제 관문이다.<br><br>

<b>전체를 <span class="m">3 × 3 × 3 × 3 × 3</span>이 아니라
<span class="m">5!</span> 같은 것으로 세면 안 된다.</b>
중복을 허락하므로 각 자리가 서로 독립이다.
<span class="m">3<sup>5</sup> = 243</span>이다.

## 노하우

<b>&lsquo;<span class="m">N</span>보다 큰 것&rsquo;은 여사건으로 센다.</b>
큰 쪽을 직접 세면 만 자리마다 경우가 갈려 복잡하지만,
작은 쪽은 대개 몇 개 안 된다.
<b>어느 쪽이 적은지 먼저 가늠하고 시작하는 것</b>이
경우의 수 문제의 기본 요령이다.<br><br>

<b>크기 비교는 앞자리부터 차례로 끊는다.</b>
만 자리를 비교해 결판이 나면 그 아래는 볼 필요가 없고,
같으면 천 자리로 내려간다.
<b>결판이 나는 자리에서 멈추는 것</b>이 요령이다.
이 문제는 천 자리에서 모두 끝난다.<br><br>

<b>중복순열의 수는 <span class="m">n<sup>r</sup></span>이다.</b>
서로 다른 <span class="m">n</span>개에서 중복을 허락하여
<span class="m">r</span>개를 택해 일렬로 나열하는 경우의 수는
<span class="m"><sub>n</sub>Π<sub>r</sub> = n<sup>r</sup></span>이다.
<b>&lsquo;중복을 허락하여&rsquo;와 &lsquo;일렬로 나열&rsquo;이 함께 나오면</b>
바로 이 공식이다.
