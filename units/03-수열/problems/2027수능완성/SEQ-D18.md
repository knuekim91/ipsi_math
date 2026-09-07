---
id: SEQ-D18
unit: 03-수열
topic: 시그마의 첨자 이동
level: 3점
difficulty: 중
source: 2027 수능완성 실전 모의고사 2회 18번
exam: 2027-수능완성
origin: 기출
core: "관계식 전체에 시그마를 씌우면 좌변이 a2부터 a11까지의 합이 되고, 주어진 합에서 a1을 빼고 a11을 더해 만든다"
tags: [시그마,첨자이동,귀납적정의]
status: seed
added: 2026-09-07
answer: 6
---

## 문제

<p>두 수열 <span class="m">{a<sub>n</sub>}</span>,
<span class="m">{b<sub>n</sub>}</span>이 모든 자연수
<span class="m">n</span>에 대하여</p>
<p class="m">a<sub>n+1</sub> = 2b<sub>n</sub> + 1</p>
<p>을 만족시킨다. <span class="m">a<sub>1</sub> = 1</span>,
<span class="m">a<sub>11</sub> = 3</span>,
<span class="m">Σ<sub>k=1</sub><sup>10</sup> a<sub>k</sub> = 20</span>일 때,
<span class="m">Σ<sub>k=1</sub><sup>10</sup> b<sub>k</sub></span>의 값을 구하시오.</p>

## 발상

<b>구하려는 것은 <span class="m">b</span>의 합인데, 주어진 것은
<span class="m">a</span>의 합이다.</b>
두 수열을 잇는 것은 관계식
<span class="m">a<sub>n+1</sub> = 2b<sub>n</sub> + 1</span> 하나뿐이므로,
<b>이 관계식 양변에 통째로 시그마를 씌우는 것</b>이 유일한 길이다.<br><br>

<span class="m">n = 1</span>부터 <span class="m">n = 10</span>까지 더하면
좌변은 <span class="m">a<sub>2</sub> + a<sub>3</sub> + … + a<sub>11</sub></span>이 된다.
<b>여기서 첨자가 <span class="m">1</span>씩 밀려 있다는 것이 이 문제의 전부다.</b>
주어진 합은 <span class="m">a<sub>1</sub></span>부터
<span class="m">a<sub>10</sub></span>까지이므로,
<b>앞의 <span class="m">a<sub>1</sub></span>을 빼고 뒤의
<span class="m">a<sub>11</sub></span>을 더하면</b> 원하는 합이 된다.
<span class="m">a<sub>1</sub></span>과 <span class="m">a<sub>11</sub></span>의 값이
따로 주어진 이유가 바로 이것이다.

## 풀이

<p><span class="step">① 관계식 양변에 시그마를 씌운다.</span>
<span class="m">n = 1</span>부터 <span class="m">n = 10</span>까지 더한다.</p>
<p class="m">Σ<sub>n=1</sub><sup>10</sup> a<sub>n+1</sub>
= Σ<sub>n=1</sub><sup>10</sup> (2b<sub>n</sub> + 1)</p>
<p>우변을 시그마의 성질로 나눈다.
상수 <span class="m">1</span>을 <span class="m">10</span>번 더하면
<span class="m">10</span>이다.</p>
<p class="m">(우변) = 2 Σ<sub>n=1</sub><sup>10</sup> b<sub>n</sub> + 10</p>

<p><span class="step">② 좌변의 첨자를 옮긴다.</span>
<span class="m">n</span>이 <span class="m">1</span>부터
<span class="m">10</span>까지 갈 때 <span class="m">n + 1</span>은
<span class="m">2</span>부터 <span class="m">11</span>까지 간다.</p>
<p class="m">Σ<sub>n=1</sub><sup>10</sup> a<sub>n+1</sub>
= a<sub>2</sub> + a<sub>3</sub> + … + a<sub>11</sub>
= Σ<sub>k=2</sub><sup>11</sup> a<sub>k</sub></p>

<p><span class="step">③ 주어진 합으로 바꾼다.</span>
<span class="m">Σ<sub>k=2</sub><sup>11</sup> a<sub>k</sub></span>는
<span class="m">Σ<sub>k=1</sub><sup>10</sup> a<sub>k</sub></span>와
<b>가운데 항들이 모두 같다.</b>
차이는 앞의 <span class="m">a<sub>1</sub></span>이 빠지고
뒤에 <span class="m">a<sub>11</sub></span>이 붙는 것뿐이다.</p>
<p class="m">Σ<sub>k=2</sub><sup>11</sup> a<sub>k</sub>
= Σ<sub>k=1</sub><sup>10</sup> a<sub>k</sub> − a<sub>1</sub> + a<sub>11</sub></p>
<p>주어진 값을 대입한다.</p>
<p class="m">= 20 − 1 + 3 = 22</p>

<p><span class="step">④ 방정식을 푼다.</span>
①의 좌변과 우변을 같다고 놓는다.</p>
<p class="m">22 = 2 Σ<sub>n=1</sub><sup>10</sup> b<sub>n</sub> + 10</p>
<p><span class="m">10</span>을 좌변으로 옮긴다.</p>
<p class="m">2 Σ<sub>n=1</sub><sup>10</sup> b<sub>n</sub> = 22 − 10 = 12</p>
<p class="m">Σ<sub>k=1</sub><sup>10</sup> b<sub>k</sub> = 6</p>
<p class="m">답 6</p>

## 함정

<b><span class="m">Σ<sub>n=1</sub><sup>10</sup> a<sub>n+1</sub></span>을
<span class="m">Σ<sub>k=1</sub><sup>10</sup> a<sub>k</sub></span>와
같다고 놓으면 안 된다.</b>
첨자가 <span class="m">1</span>씩 밀려 있으므로
<span class="m">a<sub>1</sub></span>이 빠지고
<span class="m">a<sub>11</sub></span>이 들어온다.
이 문제에서 <span class="m">a<sub>1</sub></span>과
<span class="m">a<sub>11</sub></span>의 값을 따로 준 것은
<b>바로 이 보정을 하라는 뜻</b>이다.<br><br>

<b>상수항 <span class="m">1</span>의 합을 빠뜨리기 쉽다.</b>
<span class="m">Σ<sub>n=1</sub><sup>10</sup>1 = 10</span>이다.
<span class="m">1</span>로 쓰면 답이 <span class="m">10.5</span>가 되어
자연수가 나오지 않는다.<br><br>

<b>구하는 것이 <span class="m">b</span>의 합인지
<span class="m">a</span>의 합인지 마지막에 확인한다.</b>
계산 도중에 <span class="m">a</span>의 합
<span class="m">22</span>가 나오는데, 이것을 답으로 적으면 안 된다.

## 노하우

<b>두 수열을 잇는 관계식이 하나뿐이면 그 식에 시그마를 씌운다.</b>
<span class="m">a<sub>n+1</sub> = (b<sub>n</sub>에 대한 식)</span> 꼴이 주어지고
한쪽 수열의 합을 알려 주면, <b>관계식을 그대로 더하는 것</b>이 정해진 수순이다.<br><br>

<b>첨자가 밀린 시그마는 &lsquo;빼고 더하기&rsquo;로 맞춘다.</b></p>
<p class="m">Σ<sub>k=2</sub><sup>n+1</sup> a<sub>k</sub>
= Σ<sub>k=1</sub><sup>n</sup> a<sub>k</sub> − a<sub>1</sub> + a<sub>n+1</sub></p>
<p><b>앞에서 하나 빼고 뒤에서 하나 더한다</b>는 이 모양을 기억해 두면,
첨자가 헷갈릴 때마다 항을 직접 나열하지 않아도 된다.
불안하면 <span class="m">a<sub>2</sub> + a<sub>3</sub> + …</span>처럼
<b>세 항만 실제로 적어 보는 것</b>이 가장 확실하다.
