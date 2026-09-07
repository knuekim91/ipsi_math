---
id: DIF-W01-S1
unit: 05-미분
parent: DIF-W01
topic: 이항하고 공통인수로 묶기
level: 3점
difficulty: 하
source: 사다리 1단 (DIF-W01 풀이 ①)
origin: 사다리
core: "넘긴 항이 묶일 때 무엇으로 남는지를 손으로 확인한다"
tags: [이항,공통인수,인수분해]
status: variant
added: 2026-09-07
answer: 풀이 참조
---

## 문제

<p>다음 각 식을 <b>한쪽으로 모은 뒤 공통인수로 묶어</b>
<b>(무엇) × (무엇) = 0</b> 꼴로 만드시오.</p>
<p class="m">(1) &nbsp; a = ab</p>
<p class="m">(2) &nbsp; a = ab − ca</p>
<p class="m">(3) &nbsp; f(n) = f(n)f(n+1) − f(n−1)f(n)</p>

## 발상

<b>왼쪽 항을 오른쪽으로 넘기면 부호가 바뀐 채로 하나 더 생긴다.</b>
그 넘어간 항도 <b>공통인수를 가지고 있다</b>는 것을 놓치지 않는 것이 전부다.
묶을 때 그 항은 괄호 안에 <span class="m">−1</span>을 남긴다.

## 풀이

<p><span class="step">① 가장 단순한 꼴부터.</span>
<span class="m">a = ab</span>에서 왼쪽 <span class="m">a</span>를 오른쪽으로 넘긴다.</p>
<p class="m">0 = ab − a</p>
<p>두 항 모두 <span class="m">a</span>를 가지고 있으므로 묶는다.
<b>뒤의 <span class="m">−a</span>는 <span class="m">a × (−1)</span>이므로 괄호 안에 <span class="m">−1</span>이 남는다.</b></p>
<p class="m">0 = a(b − 1)</p>
<p>따라서 <span class="m">a = 0</span> 또는 <span class="m">b = 1</span>.</p>

<p><span class="step">② 항이 하나 늘어도 같다.</span>
<span class="m">a = ab − ca</span>에서 왼쪽을 넘긴다.</p>
<p class="m">0 = ab − ca − a</p>
<p>세 항 모두 <span class="m">a</span>를 가지고 있다. 각각에서 <span class="m">a</span>를 빼내면
<span class="m">b</span>, <span class="m">−c</span>, <span class="m">−1</span>이 남는다.</p>
<p class="m">0 = a(b − c − 1)</p>

<p><span class="step">③ 이제 진짜 문제와 같은 꼴.</span>
<span class="m">f(n)</span>을 하나의 덩어리로 보면 ②와 <b>글자만 다르고 구조가 똑같다.</b>
<span class="m">a</span> 자리에 <span class="m">f(n)</span>,
<span class="m">b</span> 자리에 <span class="m">f(n+1)</span>,
<span class="m">c</span> 자리에 <span class="m">f(n−1)</span>이 들어간 것이다.</p>
<p>왼쪽 <span class="m">f(n)</span>을 오른쪽으로 넘긴다.</p>
<p class="m">0 = f(n)f(n+1) − f(n−1)f(n) − f(n)</p>
<p>세 항 모두 <span class="m">f(n)</span>을 가지고 있으므로 묶는다.
<b>넘어간 <span class="m">−f(n)</span>이 괄호 안에서 <span class="m">−1</span>이 된다.</b></p>
<p class="m">f(n)[f(n+1) − f(n−1) − 1] = 0</p>
<p>따라서 <span class="m">f(n) = 0</span> 또는
<span class="m">f(n+1) − f(n−1) = 1</span>이다.</p>

## 노하우

<b>등식의 한쪽을 넘길 때 &lsquo;넘긴 항도 공통인수를 가진다&rsquo;는 것을 잊지 않는다.</b>
그 항은 묶고 나면 괄호 안에 <b>계수만 남는다</b> — 대개 <span class="m">−1</span>이다.
<span class="m">−1</span>이 어디서 왔는지 헷갈릴 때는
<span class="m">a = ab</span>처럼 <b>글자 두 개짜리로 줄여</b> 같은 조작을 해 보면 바로 보인다.
