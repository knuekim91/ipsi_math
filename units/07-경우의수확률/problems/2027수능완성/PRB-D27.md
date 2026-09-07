---
id: PRB-D27
unit: 07-경우의수확률
topic: 같은 것이 있는 순열과 이웃 조건
level: 3점
difficulty: 중상
source: 2027 수능완성 실전 모의고사 2회 27번
exam: 2027-수능완성
origin: 기출
core: "개수 조건으로 (a,b,c)의 조합을 세 가지로 좁힌 뒤, a를 뺀 나머지를 먼저 배열하고 a를 자리 사이에 끼워 넣는다"
tags: [같은것이있는순열,이웃조건,여사건,끼워넣기]
status: seed
added: 2026-09-07
answer: ①
---

## 문제

<p>문자 <span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span> 중에서 중복을 허락하여 <span class="m">6</span>개를
다음 조건을 만족시키도록 선택해 일렬로 나열하는 경우의 수는?</p>

<div class="cond">
<span class="cond m">(가) a와 b는 홀수 개씩 선택하고, c는 1개 이상 선택한다.</span>
<span class="cond m">(나) 모든 a는 b와 이웃한다.</span>
</div>

<div class="choices"><span>① 58</span><span>② 62</span><span>③ 66</span>
<span>④ 70</span><span>⑤ 74</span></div>

## 발상

<b>먼저 각 문자를 몇 개씩 쓸지부터 정한다.</b>
<span class="m">a</span>의 개수와 <span class="m">b</span>의 개수가
둘 다 홀수이면 그 합은 짝수이다.
전체가 <span class="m">6</span>개이므로
<b><span class="m">c</span>의 개수도 짝수</b>가 되고,
<span class="m">1</span>개 이상이므로
<span class="m">2</span>개 또는 <span class="m">4</span>개뿐이다.
경우가 세 가지로 확 줄어든다.<br><br>

<b>조건 (나)는 <span class="m">a</span>의 개수를 다시 한 번 제한한다.</b>
한 문자가 이웃할 수 있는 자리는 왼쪽과 오른쪽, 최대 두 곳이다.
그러므로 <span class="m">b</span>가 하나뿐인데
<span class="m">a</span>가 셋이면,
<b>세 번째 <span class="m">a</span>는 어떻게 놓아도
<span class="m">b</span>와 이웃할 수 없다.</b>
이 관찰 하나로 경우 하나가 통째로 사라진다.<br><br>

<b>남은 경우는 <span class="m">a</span>가 한 개뿐이므로 세기 쉽다.</b>
<span class="m">a</span>를 뺀 나머지 문자들을 먼저 한 줄로 세운 뒤,
<b>그 사이사이의 자리에 <span class="m">a</span>를 끼워 넣는</b> 방식으로 세면
&lsquo;이웃&rsquo; 조건이 &lsquo;어느 자리에 끼우는가&rsquo;의 문제가 되어 명확해진다.

## 풀이

<p><span class="step">① 문자의 개수를 정한다.</span>
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>의 개수를 각각
<span class="m">p</span>, <span class="m">q</span>,
<span class="m">r</span>라 하자.</p>
<p class="m">p + q + r = 6, &nbsp; p와 q는 홀수, &nbsp; r ≥ 1</p>
<p><span class="m">p</span>와 <span class="m">q</span>가 모두 홀수이므로
<span class="m">p + q</span>는 짝수이고, 따라서
<span class="m">r = 6 − (p + q)</span>도 짝수이다.
<span class="m">r ≥ 1</span>인 짝수는 <span class="m">2</span>와
<span class="m">4</span>뿐이다.</p>
<p class="m">r = 2 : p + q = 4 → (p, q) = (1, 3) 또는 (3, 1)</p>
<p class="m">r = 4 : p + q = 2 → (p, q) = (1, 1)</p>
<p>따라서 세 가지 경우를 따지면 된다.</p>

<p><span class="step">② (p, q, r) = (3, 1, 2)인 경우를 지운다.</span>
<span class="m">b</span>가 <span class="m">1</span>개뿐이다.
이 <span class="m">b</span>와 이웃할 수 있는 자리는
<b>바로 왼쪽과 바로 오른쪽 두 곳뿐</b>이므로,
<span class="m">b</span>와 이웃하는 <span class="m">a</span>는
많아야 <span class="m">2</span>개이다.
그런데 <span class="m">a</span>가 <span class="m">3</span>개이므로
적어도 하나는 <span class="m">b</span>와 이웃하지 못한다.</p>
<p class="m">(경우의 수) = 0</p>

<p><span class="step">③ (p, q, r) = (1, 3, 2)인 경우의 전체 배열을 센다.</span>
<span class="m">a</span>를 잠시 빼고, <span class="m">b</span>
<span class="m">3</span>개와 <span class="m">c</span>
<span class="m">2</span>개를 한 줄로 세운다.
같은 것이 있는 순열이므로</p>
<p class="m">5! / (3! × 2!) = 120/12 = 10 (가지)</p>
<p>이렇게 세운 <span class="m">5</span>개의 문자 사이사이와 양 끝,
곧 <b><span class="m">6</span>개의 자리</b> 중 한 곳에
<span class="m">a</span>를 끼워 넣는다.</p>
<p class="m">10 × 6 = 60 (가지)</p>

<p><span class="step">④ 이웃하지 못하는 경우를 뺀다.</span>
<span class="m">a</span>를 끼운 자리가 <b>나쁜 자리</b>가 되는 것은,
그 자리의 양옆에 있는 문자가 모두 <span class="m">b</span>가 아닐 때이다.
<span class="m">6</span>개의 자리를 왼쪽부터
<span class="m">0</span>번부터 <span class="m">5</span>번이라 하자.<br>
<span class="m">0</span>번 자리는 오른쪽 이웃만 있으므로,
<b>첫 번째 문자가 <span class="m">c</span></b>이면 나쁘다.
<span class="m">5</span>개 중 <span class="m">c</span>가
<span class="m">2</span>개이고 그중 하나가 맨 앞에 오는 배열은
나머지 <span class="m">4</span>자리에서 <span class="m">c</span>의
자리를 고르는 <span class="m">4</span>가지이다.<br>
<span class="m">5</span>번 자리도 같은 이유로 <span class="m">4</span>가지이다.<br>
가운데 <span class="m">1</span>번부터 <span class="m">4</span>번 자리는
<b>양옆이 모두 <span class="m">c</span></b>여야 나쁜데,
<span class="m">c</span>가 <span class="m">2</span>개뿐이므로
두 <span class="m">c</span>가 그 두 자리에 붙어 있어야 한다.
각 자리마다 배열이 <span class="m">1</span>가지씩이므로
<span class="m">4</span>가지이다.</p>
<p class="m">(나쁜 경우) = 4 + 4 + 4 = 12</p>
<p class="m">(이 경우의 수) = 60 − 12 = 48</p>

<p><span class="step">⑤ (p, q, r) = (1, 1, 4)인 경우를 센다.</span>
<span class="m">a</span>가 하나, <span class="m">b</span>가 하나이므로
조건 (나)는 <b><span class="m">a</span>와 <span class="m">b</span>가
서로 이웃한다</b>는 말과 같다.
이웃한 두 문자를 <b>한 덩어리</b>로 묶는다.
덩어리 안의 순서는 <span class="m">ab</span>와
<span class="m">ba</span>의 <span class="m">2</span>가지이다.</p>
<p>이제 이 덩어리 하나와 <span class="m">c</span>
<span class="m">4</span>개, 모두 <span class="m">5</span>개를 한 줄로 세운다.
<span class="m">c</span>는 서로 같으므로
<b>덩어리가 놓일 자리를 고르는 것</b>과 같아
<span class="m">5</span>가지이다.</p>
<p class="m">2 × 5 = 10 (가지)</p>

<p><span class="step">⑥ 답을 만든다.</span>
세 경우는 문자의 개수가 서로 다르므로 겹치지 않는다.
합의 법칙으로 더한다.</p>
<p class="m">0 + 48 + 10 = 58</p>
<p class="m">답 ①</p>

## 함정

<b><span class="m">c</span>의 개수가 짝수라는 것을 놓치면 경우가 늘어난다.</b>
<span class="m">a</span>와 <span class="m">b</span>가 모두 홀수라는 조건에서
<span class="m">c</span>가 짝수임이 따라 나온다.
이를 놓치고 <span class="m">c</span>가
<span class="m">1</span>, <span class="m">3</span>개인 경우까지 따지면
헛수고를 하게 된다.<br><br>

<b><span class="m">(3, 1, 2)</span>를 <span class="m">0</span>이라고 판단하는 것이
이 문제의 관문이다.</b>
&lsquo;모든 <span class="m">a</span>&rsquo;가 <span class="m">b</span>와
이웃해야 하므로, <span class="m">a</span> 하나라도 조건을 어기면 안 된다.
<b><span class="m">b</span> 하나가 감당할 수 있는
<span class="m">a</span>는 최대 <span class="m">2</span>개</b>라는
자리 개수의 한계가 바로 답을 준다.
직접 세려 하면 시간을 크게 잃는다.<br><br>

<b>양 끝 자리를 가운데 자리와 똑같이 다루면 안 된다.</b>
<span class="m">0</span>번과 <span class="m">5</span>번 자리는
이웃이 <b>한 쪽뿐</b>이다.
그래서 &lsquo;그 한 쪽이 <span class="m">c</span>&rsquo;이기만 하면 나쁜 자리가 된다.
양옆을 모두 따지면 개수가 어긋난다.

## 노하우

<b>개수 조건이 있으면 개수부터 확정하고 시작한다.</b>
&lsquo;홀수 개&rsquo;, &lsquo;<span class="m">1</span>개 이상&rsquo; 같은 조건은
<b>따져야 할 경우를 두세 가지로 줄여 주는 선물</b>이다.
홀수 <span class="m">+</span> 홀수 <span class="m">=</span> 짝수라는
간단한 사실이 큰 몫을 한다.<br><br>

<b>이웃 조건은 &lsquo;끼워 넣기&rsquo;로 처리한다.</b>
조건이 걸린 문자를 <b>빼놓고 나머지를 먼저 배열</b>한 뒤,
생긴 자리 중 조건을 만족하는 곳에 끼워 넣는다.
<span class="m">n</span>개를 배열하면 자리는
<span class="m">n + 1</span>개가 생긴다.<br><br>

<b>&lsquo;반드시 이웃&rsquo;은 덩어리로 묶고, &lsquo;이웃하지 않음&rsquo;은 끼워 넣는다.</b>
<span class="m">(1, 1, 4)</span>처럼 이웃해야 할 문자가 하나씩이면
<b>묶어서 하나로 보는 것</b>이 가장 빠르다.
덩어리 안의 순서를 곱하는 것을 잊지 않는다.
