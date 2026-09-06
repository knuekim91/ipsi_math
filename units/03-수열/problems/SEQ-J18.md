---
id: SEQ-J18
unit: 03-수열
topic: 등차수열
level: 3점
difficulty: 하
source: 2027-06모평 18번
exam: 2027-06모평
origin: 기출
core: "항 번호의 차이가 곧 공차의 배수다"
tags: [등차수열,공차]
status: seed
added: 2026-09-06
answer: 15
---

## 문제

<p>등차수열 <span class="m">{a<sub>n</sub>}</span>이 <span class="m">a<sub>6</sub> = 5</span>, <span class="m">a<sub>5</sub> = a<sub>2</sub> − 6</span>을 만족시킬 때, <span class="m">a<sub>1</sub></span>의 값을 구하시오.</p>

## 발상

<b><span class='m'>a<sub>5</sub> − a<sub>2</sub></span>는 번호가 3 차이나니 곧 <span class='m'>3d</span></b>다. 첫째항을 세우지 않아도 공차가 바로 나온다.

## 풀이

<p><span class="step">① 공차.</span> <span class="m">a<sub>5</sub> − a<sub>2</sub> = 3d = −6 → d = −2</span></p><p><span class="step">② 첫째항.</span> <span class="m">a<sub>6</sub> = a<sub>1</sub> + 5d = a<sub>1</sub> − 10 = 5</span></p><p class="m">a<sub>1</sub> = 15</p>

## 노하우

<b>등차수열에서 <span class='m'>a<sub>m</sub> − a<sub>n</sub> = (m − n)d</span>.</b> 첫째항과 공차를 미지수 두 개로 세워 연립하는 대신, 번호 차이만 보면 공차가 한 줄에 나온다.
