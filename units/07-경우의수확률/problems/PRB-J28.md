---
id: PRB-J28
unit: 07-경우의수확률
topic: 반복 시행과 상태의 뒤집힘
level: 4점
difficulty: 상
source: 2027-06모평 28번
exam: 2027-06모평
origin: 기출
core: "각 카드가 어떤 눈에서 뒤집히는지 표로 만들면 카드 1은 홀수 눈, 카드 6은 짝수 눈에만 반응한다"
tags: [반복시행,확률,패리티,경우의수]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>앞면에 숫자 <span class="m">1, 2, 3, 4, 5, 6</span>이 하나씩 적혀 있는 카드 6장이 있다. 각 카드의 뒷면에는 앞면에 적힌 숫자와 같은 숫자가 적혀 있다. 이 6장의 카드가 다음과 같이 놓여 있다.</p><span class="cond">숫자 <span class="m">1, 6</span>이 적힌 카드는 뒷면이 보이도록 놓여 있고,<br>숫자 <span class="m">2, 3, 4, 5</span>가 적힌 카드는 앞면이 보이도록 놓여 있다.</span><p>이 6장의 카드와 한 개의 주사위를 사용하여 다음 시행을 한다.</p><span class="cond">주사위를 한 번 던져 나온 눈의 수가 <span class="m">k</span>일 때,<br><span class="m">k</span>가 홀수이면 <span class="m">k</span> 이하의 수가 적힌 카드를 모두 한 번씩 뒤집고,<br><span class="m">k</span>가 짝수이면 <span class="m">k</span> 이상의 수가 적힌 카드를 모두 한 번씩 뒤집는다.</span><p>이 시행을 4번 반복한 후 6장의 카드가 모두 앞면이 보이도록 놓여 있을 확률은?</p><div class="choices"><span>① 19/162</span><span>② 13/108</span><span>③ 10/81</span><span>④ 41/324</span><span>⑤ 7/54</span></div>

## 발상

<b>카드가 앞면으로 돌아오려면 뒤집힌 횟수의 &lsquo;홀짝&rsquo;만 맞으면 된다.</b> 순서는 상관없다. 그러니 각 카드가 <b>어떤 눈에서 뒤집히는지</b>를 표로 만들고 홀짝만 따진다. 표를 만들어 보면 <b>카드 1은 홀수 눈에서만, 카드 6은 짝수 눈에서만</b> 뒤집힌다 — 여기서 문제가 풀린다.

## 풀이

<p><span class="step">① 어떤 눈이 어떤 카드를 뒤집는가.</span></p><p class="m">k=1 → {1} &nbsp;&nbsp; k=2 → {2,3,4,5,6}</p><p class="m">k=3 → {1,2,3} &nbsp;&nbsp; k=4 → {4,5,6}</p><p class="m">k=5 → {1,2,3,4,5} &nbsp;&nbsp; k=6 → {6}</p><p><span class="step">② 카드별로 뒤집는 눈을 모은다.</span></p><p class="m">카드 1 : {1, 3, 5} &nbsp; = 홀수 눈 전부</p><p class="m">카드 2, 3 : {2, 3, 5}</p><p class="m">카드 4, 5 : {2, 4, 5}</p><p class="m">카드 6 : {2, 4, 6} &nbsp; = 짝수 눈 전부</p><p>카드 2와 3, 카드 4와 5는 <b>항상 함께 움직이므로 한 덩어리</b>로 본다.</p><p><span class="step">③ 필요한 홀짝.</span> 처음에 뒷면인 카드 1, 6은 <b>홀수 번</b>, 앞면인 나머지는 <b>짝수 번</b> 뒤집혀야 한다.</p><p>4번의 시행 중 홀수 눈이 <span class="m">o</span>번 나왔다 하면 카드 1은 <span class="m">o</span>번, 카드 6은 <span class="m">4 − o</span>번 뒤집힌다. 둘 다 홀수여야 하므로</p><p class="m">o = 1 또는 o = 3</p><p><span class="step">④ o = 1 (홀수 1번, 짝수 3번).</span> 짝수 눈 <span class="m">2, 4, 6</span>이 각각 <span class="m">a, b, c</span>번 (<span class="m">a+b+c=3</span>). 카드 2·3 그룹은 <span class="m">{2,3,5}</span>에, 카드 4·5 그룹은 <span class="m">{2,4,5}</span>에 반응하므로</p><p class="m">홀수 눈이 1 : a 짝수, a+b 짝수 → (a,b,c) = (0,0,3),(0,2,1),(2,0,1) → 1+3+3 = 7</p><p class="m">홀수 눈이 3 : a 홀수, a+b 짝수 → (1,1,1) → 6</p><p class="m">홀수 눈이 5 : a 홀수, a+b 홀수 → (1,0,2),(1,2,0),(3,0,0) → 3+3+1 = 7</p><p>홀수 눈이 나온 <b>자리를 고르는 4가지</b>를 곱하면</p><p class="m">4 × (7 + 6 + 7) = 4 × 20 = 80</p><p><span class="step">⑤ o = 3 (홀수 3번, 짝수 1번).</span> 같은 방식으로 세면</p><p class="m">짝수 눈이 2 : 7 &nbsp;/&nbsp; 4 : 6 &nbsp;/&nbsp; 6 : 7 &nbsp; → 20</p><p class="m">4 × 20 = 80</p><p><span class="step">⑥ 확률.</span></p><p class="m">(80 + 80) / 6<sup>4</sup> = 160 / 1296 = 10/81</p>

## 함정

<b>순서를 따지려 들면 경우의 수가 폭발한다.</b> 뒤집기는 &lsquo;몇 번&rsquo;만 중요하고 &lsquo;언제&rsquo;는 중요하지 않다. 이 점을 먼저 못 박아야 홀짝 문제로 내려온다.

## 노하우

<b>&lsquo;뒤집기를 반복한 뒤의 상태&rsquo; 문제는 전부 홀짝(패리티) 문제다.</b> ① 각 대상이 <b>어떤 시행에서 반응하는지</b> 표를 만들고, ② <b>똑같이 움직이는 것끼리 묶어</b> 상태의 개수를 줄이고, ③ 처음 상태와 목표 상태를 비교해 <b>각 덩어리에 필요한 홀짝</b>을 적는다. 여기서는 카드 1과 6이 각각 홀수 눈·짝수 눈에 정확히 대응해 <b>홀수 눈의 개수가 홀수</b>라는 강한 조건이 먼저 튀어나온다.
