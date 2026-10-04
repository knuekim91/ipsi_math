---
id: PRB-W02
unit: 07-경우의수확률
topic: 순서가 정해진 나열과 같은 수가 적힌 공
level: 4점
difficulty: 중상
source: 2016학년도 9월 모의평가 B형 15번
exam: 오답노트
origin: 기출
core: "분모를 공을 구별해 세었으면 분자도 공을 구별해 세야 한다. a≤b≤c≤d는 수의 나열을 하나로 묶지만, 같은 수가 적힌 두 공이 자리를 바꾼 것은 서로 다른 경우다"
tags: [확률,순열,같은것이있는순열,순서가정해진나열]
status: wrong
added: 2026-10-04
answer: ①
---

## 문제

<p>주머니에 <span class="m">1, 1, 2, 3, 4</span>의 숫자가 하나씩 적혀 있는
<span class="m">5</span>개의 공이 들어 있다.
이 주머니에서 임의로 <span class="m">4</span>개의 공을 동시에 꺼내어
임의로 일렬로 나열하고, 나열된 순서대로 공에 적혀 있는 수를
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>라 할 때,
<span class="m">a ≤ b ≤ c ≤ d</span>일 확률은?</p>

<div class="choices"><span>① 1/15</span><span>② 1/12</span><span>③ 1/9</span>
<span>④ 1/6</span><span>⑤ 1/3</span></div>

## 발상

<b><span class="m">a ≤ b ≤ c ≤ d</span>라는 조건은 나열의 자유를 거의 다 없앤다.</b>
어떤 공 <span class="m">4</span>개를 꺼냈는지가 정해지면,
그 네 수를 작은 것부터 늘어놓는 방법은 <b>하나뿐</b>이다.
그러니 &lsquo;나열하는 문제&rsquo;가 사실상 &lsquo;무엇을 꺼낼 것인가&rsquo;의 문제로 바뀐다.<br><br>

<b>그런데 여기에 이 문제의 진짜 함정이 숨어 있다.</b>
<span class="m">1</span>이 적힌 공이 <b>두 개</b>다.
이 두 공은 적힌 수는 같지만 <b>서로 다른 공</b>이다.
전체 경우의 수를 셀 때 우리는 다섯 개의 공을 모두 구별해서 세게 된다.
그렇다면 <b>분자도 똑같이 구별해서 세야 한다.</b><br><br>

<span class="m">1</span>이 적힌 두 공이 모두 뽑힌 경우,
수의 나열은 <span class="m">1, 1, x, y</span> 하나뿐이지만
<b>앞의 두 자리에 어느 공이 가느냐가 두 가지</b>다.
분모와 분자의 세는 기준을 맞추는 것, 그것이 이 문제의 전부다.<br><br>

<b>경우를 나누는 기준은 &lsquo;꺼내지 않은 공 하나&rsquo;</b>로 잡는다.
다섯 개 중 넷을 꺼내므로, 남기는 공 하나를 정하면 꺼낸 공이 정해진다.
가짓수가 다섯 개뿐이라 손으로 전부 적을 수 있다.

## 풀이

<p><span class="step">① 공에 이름을 붙인다.</span>
수가 같아도 공은 서로 다르므로 구별해 적는다.</p>
<p class="m">1<sub>①</sub>, 1<sub>②</sub>, 2, 3, 4</p>

<p><span class="step">② 전체 경우의 수를 센다.</span>
<span class="m">5</span>개의 공 중에서 <span class="m">4</span>개를 꺼내어
일렬로 나열하므로, 서로 다른 <span class="m">5</span>개에서
<span class="m">4</span>개를 택하는 순열이다.</p>
<p class="m">(전체) = <sub>5</sub>P<sub>4</sub> = 5 × 4 × 3 × 2 = 120</p>
<p>꺼내는 방법 <span class="m"><sub>5</sub>C<sub>4</sub> = 5</span>가지에
나열하는 방법 <span class="m">4! = 24</span>가지를 곱해도 같다.</p>
<p class="m">5 × 24 = 120</p>

<p><span class="step">③ 조건의 뜻을 새긴다.</span>
<span class="m">a ≤ b ≤ c ≤ d</span>는 꺼낸 네 수가
<b>작은 것부터 차례로 놓였다</b>는 뜻이다.
그러므로 <b>수의 나열 순서는 꺼낸 공들이 정해지는 순간 결정된다.</b>
남은 자유는 <b>같은 수가 적힌 공끼리 자리를 바꾸는 것</b>뿐이다.</p>

<p><span class="step">④ 꺼내지 않은 공으로 경우를 나눈다.</span>
남기는 공이 <span class="m">1</span>이 적힌 공인지 아닌지로 갈린다.<br>
<b>(ㄱ) <span class="m">1<sub>①</sub></span> 또는
<span class="m">1<sub>②</sub></span>를 남기는 경우</b> &mdash; 남기는 방법이
<span class="m">2</span>가지다.
꺼낸 공에 적힌 수는 <span class="m">1, 2, 3, 4</span>로 <b>모두 다르다.</b>
작은 것부터 놓는 방법은 하나뿐이다.</p>
<p class="m">2 × 1 = 2</p>
<p><b>(ㄴ) <span class="m">2, 3, 4</span> 중 하나를 남기는 경우</b> &mdash;
남기는 방법이 <span class="m">3</span>가지다.
이때 <span class="m">1</span>이 적힌 공이 <b>둘 다</b> 꺼내진다.
꺼낸 수를 작은 것부터 놓으면 <span class="m">1, 1, x, y</span> 꼴이고,
<b>앞의 두 자리에 두 공이 들어가는 순서가 <span class="m">2</span>가지</b>다.</p>
<p class="m">3 × 2 = 6</p>

<p><span class="step">⑤ 조건을 만족시키는 경우의 수를 구한다.</span></p>
<p class="m">(조건을 만족) = 2 + 6 = 8</p>

<p><span class="step">⑥ 확률을 구한다.</span></p>
<p class="m">8/120 = 1/15</p>
<p class="m">답 ①</p>

## 함정

<b>이 문제를 틀리는 거의 모든 이유는 분모와 분자의 기준이 다른 것이다.</b>
분모 <span class="m">120</span>은 다섯 개의 공을 <b>모두 구별해서</b> 센 값이다.
그런데 분자를 셀 때 &lsquo;꺼낸 수의 모임&rsquo;만 보고
<span class="m">\{1,2,3,4\}</span>, <span class="m">\{1,1,2,3\}</span>,
<span class="m">\{1,1,2,4\}</span>, <span class="m">\{1,1,3,4\}</span>의
<span class="m">4</span>가지라고 세면 <span class="m">4/120</span>이 되어 틀린다.
<b>한쪽에서 구별했으면 다른 쪽에서도 구별한다.</b><br><br>

<b><span class="m">1</span>이 적힌 두 공을 같은 공으로 보면 안 된다.</b>
눈으로는 구별이 안 되지만, 확률에서는 <b>각각 똑같은 확률로 뽑히는 다른 공</b>이다.
두 공을 하나로 묶으면 뽑힐 확률이 두 배인 공이 되어 버린다.<br><br>

<b>네 수가 모두 다르다면 확률이 <span class="m">1/24</span>이다.</b>
<span class="m">4!</span>가지 나열 중 오름차순이 하나뿐이기 때문이다.
이 문제의 답 <span class="m">1/15</span>가
<span class="m">1/24</span>보다 <b>큰</b> 것은
같은 수가 있어 조건을 만족하는 나열이 늘어났기 때문이다.
답이 나왔을 때 이 크기 비교로 검산할 수 있다.

## 노하우

<b>&lsquo;크기 순서가 정해진 나열&rsquo;은 나열 문제가 아니라 뽑기 문제다.</b>
<span class="m">a ≤ b ≤ c ≤ d</span>, <span class="m">a &lt; b &lt; c &lt; d</span>처럼
순서가 못 박히면 <b>무엇을 뽑느냐만 정하면 배열은 따라온다.</b>
이것이 중복조합의 본질이기도 하다.
같은 발상을 쓰는 문항으로 <span class="m">PRB-C28</span>(크기 순서가 정해진 함수의 개수)이 있다.<br><br>

<b>같은 것이 섞여 있으면 &lsquo;구별하는 세계&rsquo;와 &lsquo;구별 안 하는 세계&rsquo; 중
하나를 골라 끝까지 밀고 간다.</b>
확률 문제에서는 <b>구별하는 쪽</b>이 안전하다.
각 공이 뽑힐 확률이 같다는 전제가 그대로 지켜지기 때문이다.
<span class="m">PRB-J23</span>처럼 <b>경우의 수</b>를 묻는 문제에서는
<span class="m">k!</span>로 나누어 구별하지 않는 쪽으로 세기도 한다.
<b>무엇을 묻는지에 따라 세계를 고른다.</b><br><br>

<b>다섯 개 중 넷을 꺼내면 &lsquo;남기는 하나&rsquo;로 경우를 나눈다.</b>
<span class="m"><sub>5</sub>C<sub>4</sub></span>를 따지는 것보다
<b>버리는 공 하나</b>를 기준으로 삼는 편이 훨씬 짧다.
가짓수가 다섯 개뿐이라 손으로 전부 적어 확인할 수 있다.
