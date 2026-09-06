---
id: DIF-J09
unit: 05-미분
topic: 속도와 위치
level: 4점
difficulty: 중
source: 2027-06모평 9번
exam: 2027-06모평
origin: 기출
core: "속도를 적분해 위치를 만든 뒤 두 위치를 같게 놓는다"
tags: [속도,위치,적분]
status: seed
added: 2026-09-06
answer: ③
---

## 문제

<p>시각 <span class="m">t = 0</span>일 때 동시에 원점을 출발하여 수직선 위를 움직이는 두 점 P, Q가 있다. 시각이 <span class="m">t (t ≥ 0)</span>일 때 두 점 P, Q의 속도가 각각</p><span class="cond m">v<sub>1</sub>(t) = t<sup>2</sup> − t, &nbsp; v<sub>2</sub>(t) = t</span><p>이다. 출발한 후 시각 <span class="m">t = k</span>에서 두 점 P, Q의 위치가 같아질 때, 양수 <span class="m">k</span>의 값은?</p><div class="choices"><span>① 1</span><span>② 2</span><span>③ 3</span><span>④ 4</span><span>⑤ 5</span></div>

## 발상

<b>속도가 주어지면 위치는 적분</b>이다. 둘 다 원점에서 출발하므로 적분상수는 0. 그 다음 두 위치를 같게 놓는다.

## 풀이

<p><span class="step">① 문제가 준 것과 구하는 것을 구분한다.</span>
문제가 준 것은 <b>속도</b>이고 물어보는 것은 <b>위치가 같아지는 순간</b>이다.
위치는 속도를 적분해서 얻는다.
<b>&lsquo;위치가 같다&rsquo;를 &lsquo;속도가 같다&rsquo;로 착각하면 안 된다.</b></p>

<p><span class="step">② 속도를 적분해 위치를 만든다.</span>
적분하면 상수가 하나씩 붙지만,
<b>두 점 모두 <span class="m">t = 0</span>일 때 원점에서 출발</b>하므로
<span class="m">x(0) = 0</span>이 되어 상수는 <span class="m">0</span>이다.</p>
<p class="m">x<sub>1</sub>(t) = ∫(t<sup>2</sup> − t)dt = t<sup>3</sup>/3 − t<sup>2</sup>/2</p>
<p class="m">x<sub>2</sub>(t) = ∫t dt = t<sup>2</sup>/2</p>

<p><span class="step">③ 두 위치를 같게 놓는다.</span></p>
<p class="m">t<sup>3</sup>/3 − t<sup>2</sup>/2 = t<sup>2</sup>/2</p>
<p>오른쪽의 <span class="m">t<sup>2</sup>/2</span>를 왼쪽으로 넘긴다.</p>
<p class="m">t<sup>3</sup>/3 − t<sup>2</sup>/2 − t<sup>2</sup>/2 = 0</p>
<p class="m">t<sup>3</sup>/3 − t<sup>2</sup> = 0</p>

<p><span class="step">④ 공통인수로 묶어 푼다.</span>
양변에 <span class="m">3</span>을 곱해 분수를 없앤다.</p>
<p class="m">t<sup>3</sup> − 3t<sup>2</sup> = 0</p>
<p>두 항 모두 <span class="m">t<sup>2</sup></span>을 가지고 있으므로 묶는다.</p>
<p class="m">t<sup>2</sup>(t − 3) = 0 → t = 0 또는 t = 3</p>

<p><span class="step">⑤ 조건에 맞는 값을 고른다.</span>
<span class="m">t = 0</span>은 <b>출발하는 순간</b>이라 &lsquo;출발한 후&rsquo;가 아니고,
문제도 <span class="m">k</span>가 양수라 했다.</p>
<p class="m">k = 3</p>
<p class="m">답 ③</p>

## 노하우

<b>위치 = ∫속도, 그것도 &lsquo;출발점에서부터&rsquo;.</b> &lsquo;위치가 같다&rsquo;는 <span class='m'>x<sub>1</sub> = x<sub>2</sub></span>이지 <span class='m'>v<sub>1</sub> = v<sub>2</sub></span>가 아니다. 속도가 같은 순간과 헷갈리지 말 것.
