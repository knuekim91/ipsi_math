---
id: PRB-W05-V3
parent: PRB-W05
unit: 07-경우의수확률
topic: 경우의 수가 주어질 때 보라 카드 장수 구하기 (역추론)
level: 4점
difficulty: 중상
source: 자체 개발 (PRB-W05 변형 · 경우의 수로부터 미지수 찾기)
origin: 유사문항
core: "경우의 수가 보라 장수 m 의 함수로 정리되면 m 을 미지수로 한 식이 된다. 단색 배분별 가짓수에서 보라 분배 C(m−1, |S|−1) 를 묶어 두면 역추론이 쉽다"
tags: [중복조합,분배,홀짝,경우나누기,역추론,색의가짓수]
status: variant
added: 2026-11-04
answer: 8
---

## 문제

<p>빨간색, 주황색, 노란색, 파란색 카드가 각각 1장씩 있고, 보라색 카드가 <span class="m">m</span>장 있다.
이 <span class="m">m + 4</span>장의 카드를 세 학생 A, B, C에게 남김없이 나누어 주는 경우의 수를
<span class="m">N(m)</span>이라 하자. (단, 같은 색 카드끼리는 서로 구별하지 않는다.)</p>

<div class="cond">
<span class="cond m">세 학생 A, B, C가 받는 카드의 색의 가짓수는 모두 홀수이다.</span>
<span class="cond m">N(m) = 501 일 때, 자연수 m 의 값을 구하시오.</span>
</div>

## 발상

<b>경우의 수를 보라 장수 m의 식으로 먼저 쓴다.</b>
그러면 주어진 값 501이 m에 대한 방정식이 된다.<br><br>

<b>단색 카드 네 장의 배분 종류는 몇 개뿐이다.</b>
종류마다 보라를 받는 학생 수 <span class="m">s</span>가 정해지고,
보라 <span class="m">m</span>장을 <span class="m">s</span>명에게 1장 이상씩 나누는 방법은 <span class="m">C(m − 1, s − 1)</span>이다.
종류마다 이 값을 곱해 더하면 <span class="m">N(m)</span>이 된다.

## 풀이

<p><span class="step">① 단색 배분의 종류를 나열한다.</span>
네 장을 세 학생에게 나누는 종류 가운데 보라를 받을 학생이 있는 것은 다음과 같다.</p>
<p class="m">(4, 0, 0), &nbsp; (3, 1, 0), &nbsp; (2, 2, 0), &nbsp; (2, 1, 1)</p>
<p>각 종류에는 짝수인 k가 적어도 하나 있으므로 모두 보라를 받을 학생이 있다.
세 수가 모두 홀수인 경우는 합이 4일 수 없으므로 애초에 없다.</p>

<p><span class="step">② 종류별 가짓수를 m의 식으로 쓴다.</span>
보라를 받는 학생 수 <span class="m">s</span>는 짝수 <span class="m">k</span>의 개수다.</p>
<p class="m">(4, 0, 0) : s = 3, 배분 1, 순서 3 → 3 · C(m−1, 2)</p>
<p class="m">(2, 2, 0) : s = 3, 배분 6, 순서 3 → 18 · C(m−1, 2)</p>
<p class="m">(3, 1, 0) : s = 1, 배분 4, 순서 6 → 24 · C(m−1, 0) = 24</p>
<p class="m">(2, 1, 1) : s = 1, 배분 12, 순서 3 → 36 · C(m−1, 0) = 36</p>

<p><span class="step">③ N(m)을 정리한다.</span></p>
<p class="m">N(m) = 21 · C(m−1, 2) + 60</p>

<p><span class="step">④ 501을 대입한다.</span></p>
<p class="m">21 · C(m−1, 2) + 60 = 501 → C(m−1, 2) = 21</p>
<p class="m">C(7, 2) = 21 이므로 m − 1 = 7 → m = 8</p>
<p class="m">답 8</p>

<p><span class="step">⑤ 확인한다.</span>
<span class="m">m = 8</span>이면 <span class="m">C(7, 2) = 21</span>이므로
<span class="m">N(8) = 21 · 21 + 60 = 441 + 60 = 501</span>이다. ✓</p>

## 함정

<b>보라를 받는 학생이 한 명인 경우를 빼먹는다.</b>
<span class="m">(3, 1, 0)</span>과 <span class="m">(2, 1, 1)</span>은 보라를 받는 학생이 한 명뿐이라
<span class="m">C(m − 1, 0) = 1</span>이다. 이 두 항은 <span class="m">m</span>과 무관한 상수 <span class="m">60</span>이 된다.
이 상수를 빼먹으면 <span class="m">21 · C(m−1, 2) = 441</span>이 되어 답이 틀린다.<br><br>

<b>C(m−1, 2)를 C(m, 2)로 쓰면 m이 하나 어긋난다.</b>
보라 <span class="m">m</span>장을 <span class="m">s</span>명에게 1장 이상씩 나누면
칸막이는 <span class="m">m − 1</span>개 자리에 <span class="m">s − 1</span>개를 꽂는 것이다.

## 노하우

<b>경우의 수를 미지수 m의 식으로 쓰면 역추론이 방정식 하나가 된다.</b>
먼저 종류별 가짓수를 m에 대해 정리하고, 주어진 값과 맞춘다.
이 문항에서는 <span class="m">21 · C(m−1, 2) + 60 = 501</span>이 되어 <span class="m">C(m−1, 2) = 21</span>로 줄어든다.
