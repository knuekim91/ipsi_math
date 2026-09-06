---
id: PRB-J25
unit: 07-경우의수확률
topic: 이항정리
level: 3점
difficulty: 중
source: 2027-06모평 25번
exam: 2027-06모평
origin: 기출
core: "곱해지는 두 항 각각에서 필요한 차수를 나눠 맡긴다"
tags: [이항정리,전개식,계수]
status: seed
added: 2026-09-06
answer: ①
---

## 문제

<p><span class="m">(x + 4)<sup>6</sup>(3x + 2)</span>의 전개식에서 <span class="m">x<sup>6</sup></span>의 계수는?</p><div class="choices"><span>① 74</span><span>② 78</span><span>③ 82</span><span>④ 86</span><span>⑤ 90</span></div>

## 발상

<span class='m'>x<sup>6</sup></span>을 만드는 길은 두 가지다. <b>뒤에서 상수 2를 뽑고 앞에서 <span class='m'>x<sup>6</sup></span>을 뽑거나, 뒤에서 <span class='m'>3x</span>를 뽑고 앞에서 <span class='m'>x<sup>5</sup></span>를 뽑거나.</b>

## 풀이

<p><span class="step">① x<sup>6</sup>을 만드는 길이 몇 개인지 센다.</span>
<span class="m">(x + 4)<sup>6</sup></span>과 <span class="m">(3x + 2)</span>를 곱할 때,
뒤쪽 인수에서 무엇을 뽑느냐에 따라 앞쪽에서 뽑아야 할 차수가 정해진다.
뒤쪽은 <span class="m">3x</span> 아니면 <span class="m">2</span> 둘뿐이므로 <b>길은 두 개</b>다.</p>
<p class="m">뒤에서 2(상수)를 뽑으면 → 앞에서 x<sup>6</sup>을 뽑아야 한다</p>
<p class="m">뒤에서 3x를 뽑으면 → 앞에서 x<sup>5</sup>를 뽑아야 한다</p>

<p><span class="step">② (x+4)<sup>6</sup>의 일반항을 쓴다.</span></p>
<p class="m">일반항 = <sub>6</sub>C<sub>r</sub> x<sup>6−r</sup> 4<sup>r</sup></p>

<p><span class="step">③ 첫 번째 길을 계산한다.</span>
<span class="m">x<sup>6</sup></span>이 되려면 <span class="m">6 − r = 6</span>, 곧 <span class="m">r = 0</span>이다.</p>
<p class="m"><sub>6</sub>C<sub>0</sub> × 4<sup>0</sup> = 1 × 1 = 1</p>
<p>여기에 뒤쪽에서 뽑은 <span class="m">2</span>를 곱한다.</p>
<p class="m">2 × 1 = 2</p>

<p><span class="step">④ 두 번째 길을 계산한다.</span>
<span class="m">x<sup>5</sup></span>이 되려면 <span class="m">6 − r = 5</span>, 곧 <span class="m">r = 1</span>이다.</p>
<p class="m"><sub>6</sub>C<sub>1</sub> × 4<sup>1</sup> = 6 × 4 = 24</p>
<p>여기에 뒤쪽에서 뽑은 <span class="m">3x</span>의 <b>계수 <span class="m">3</span>을 곱하는 것을 잊지 않는다.</b></p>
<p class="m">3 × 24 = 72</p>

<p><span class="step">⑤ 두 길을 더한다.</span></p>
<p class="m">2 + 72 = 74</p>
<p class="m">답 ①</p>

## 함정

<span class='m'>3x</span>를 뽑을 때 계수 <b>3을 곱하는 것을 잊기 쉽다.</b> 24만 더하면 26이 되어 보기에 없는 값이 나오므로 바로 알아챌 수 있다.

## 노하우

<b>두 다항식의 곱에서 특정 차수의 계수는 &lsquo;차수를 나눠 맡는 모든 방법&rsquo;을 더한 것.</b> 뒤 인수의 차수가 낮으면 <b>뒤쪽 항을 기준으로 경우를 나누는 것</b>이 항상 빠르다.
