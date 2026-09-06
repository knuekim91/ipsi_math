---
id: TRI-J08
unit: 02-삼각함수
topic: 코사인법칙
level: 3점
difficulty: 중
source: 2027-06모평 8번
exam: 2027-06모평
origin: 기출
core: "구하는 변을 미지수로 두고 코사인법칙을 이차방정식으로 만든다"
tags: [코사인법칙,이차방정식]
status: seed
added: 2026-09-06
answer: ④
---

## 문제

<p>삼각형 ABC에서</p><span class="cond m">AB = 4, &nbsp; BC = 8, &nbsp; cos A = −1/4</span><p>일 때, 선분 AC의 길이는?</p><div class="choices"><span>① 9/2</span><span>② 5</span><span>③ 11/2</span><span>④ 6</span><span>⑤ 13/2</span></div>

## 발상

<b>각 A를 낀 두 변이 AB와 AC</b>이고 마주 보는 변이 BC다. 구하는 AC를 미지수로 두면 이차방정식이 된다.

## 풀이

<p><span class="step">① 어느 각과 어느 변이 짝인지 확인한다.</span>
코사인법칙은 <b>한 각과 그 각이 마주 보는 변</b>을 잇는다.
여기서 주어진 각은 A이고, <b>각 A가 마주 보는 변은 BC</b>다.
각 A를 낀 두 변은 AB와 AC이므로, 구하는 AC를 <span class="m">b</span>라 두면 식을 세울 수 있다.</p>

<p><span class="step">② 코사인법칙을 쓴다.</span></p>
<p class="m">BC<sup>2</sup> = AB<sup>2</sup> + AC<sup>2</sup> − 2 × AB × AC × cos A</p>
<p>값을 넣는다. <span class="m">AB = 4</span>, <span class="m">BC = 8</span>, <span class="m">cos A = −1/4</span>이다.</p>
<p class="m">8<sup>2</sup> = 4<sup>2</sup> + b<sup>2</sup> − 2 × 4 × b × (−1/4)</p>

<p><span class="step">③ 부호에 주의하며 정리한다.</span>
<b><span class="m">cos A</span>가 음수</b>이므로 마지막 항에서 음수끼리 곱해져 <b>더하기</b>가 된다.</p>
<p class="m">−2 × 4 × b × (−1/4) = +2b</p>
<p class="m">64 = 16 + b<sup>2</sup> + 2b</p>

<p><span class="step">④ 이차방정식을 만든다.</span>
왼쪽의 <span class="m">64</span>를 오른쪽으로 넘긴다.</p>
<p class="m">0 = b<sup>2</sup> + 2b + 16 − 64</p>
<p class="m">b<sup>2</sup> + 2b − 48 = 0</p>

<p><span class="step">⑤ 인수분해하고 길이 조건으로 거른다.</span>
곱이 <span class="m">−48</span>, 합이 <span class="m">2</span>인 두 수는 <span class="m">8</span>과 <span class="m">−6</span>이다.</p>
<p class="m">(b + 8)(b − 6) = 0 → b = −8 또는 b = 6</p>
<p><b>길이는 양수여야 하므로</b> <span class="m">b = −8</span>은 버린다.</p>
<p class="m">AC = 6</p>
<p class="m">답 ④</p>

## 함정

<span class='m'>cos A</span>가 <b>음수</b>라 <span class='m'>−2bc·cos A</span>가 <b>더하기</b>로 바뀐다. 부호를 그대로 대입하지 않고 눈으로만 처리하면 <span class='m'>b<sup>2</sup>−2b−48=0</span>으로 틀린다.

## 노하우

<b>코사인법칙에서 각과 마주 보는 변이 어느 것인지부터 확인한다.</b> 각 A의 맞은편은 BC. 미지수를 세워 이차방정식으로 만들고, 마지막에 <b>양수 조건</b>으로 거른다.
