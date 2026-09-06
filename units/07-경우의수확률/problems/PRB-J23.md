---
id: PRB-J23
unit: 07-경우의수확률
topic: 같은 것이 있는 순열
level: 2점
difficulty: 하
source: 2027-06모평 23번
exam: 2027-06모평
origin: 기출
core: "같은 문자가 k개면 k!로 나눈다"
tags: [같은것이있는순열]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>네 개의 문자 <span class="m">x, y, z, z</span>를 일렬로 나열하는 경우의 수는?</p><div class="choices"><span>① 6</span><span>② 9</span><span>③ 12</span><span>④ 15</span><span>⑤ 18</span></div>

## 발상

<span class='m'>z</span>가 두 개이므로 <b>두 <span class='m'>z</span>를 바꿔 놓은 배열이 같은 것으로 세어진다</b>. 전체를 <span class='m'>2!</span>로 나눈다.

## 풀이

<p><span class="step">① 같은 문자가 몇 개인지 센다.</span>
나열할 문자는 <span class="m">x, y, z, z</span>로 모두 <span class="m">4</span>개이고,
그중 <span class="m">z</span>가 <b>두 개</b>로 서로 구별되지 않는다.</p>

<p><span class="step">② 왜 나누는지 생각한다.</span>
네 개가 모두 다르다면 <span class="m">4! = 24</span>가지다.
그런데 두 개의 <span class="m">z</span>는 자리를 서로 바꿔도 <b>보이는 결과가 똑같다.</b>
바꿔 놓는 방법이 <span class="m">2! = 2</span>가지이므로
<span class="m">24</span>가지 안에서 <b>같은 배열이 두 번씩 세어졌다.</b>
그래서 <span class="m">2!</span>로 나눈다.</p>
<p class="m">4! / 2! = 24 / 2 = 12</p>
<p class="m">답 ③</p>

## 노하우

<b>같은 것이 있는 순열: n개 중 같은 것이 각각 p개, q개, … 이면 n!/(p!q!…).</b> &lsquo;구별하지 않는다&rsquo;는 말이 나오면 반드시 나눗셈이 따라온다.
