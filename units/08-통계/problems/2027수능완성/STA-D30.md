---
id: STA-D30
unit: 08-통계
topic: 두 정규분포의 대칭 관계
level: 4점
difficulty: 최상
source: 2027 수능완성 실전 모의고사 2회 30번
exam: 2027-수능완성
origin: 기출
core: "P(X ≥ x) = P(Y ≤ −x+10)이 모든 x에서 성립하려면 표준편차가 같고 두 평균의 합이 10이다"
tags: [정규분포,표준화,대칭,표준정규분포표]
status: seed
added: 2026-09-07
answer: 818
---

## 문제

<p>정규분포 <span class="m">N(m<sub>1</sub>, σ<sub>1</sub><sup>2</sup>)</span>을 따르는
확률변수 <span class="m">X</span>와 정규분포
<span class="m">N(m<sub>2</sub>, σ<sub>2</sub><sup>2</sup>)</span>을 따르는
확률변수 <span class="m">Y</span>가 다음 조건을 만족시킨다.</p>

<div class="cond">
<span class="cond m">모든 실수 x에 대하여 P(X ≥ x) = P(Y ≤ −x + 10)이다.</span>
</div>

<p><span class="m">P(a ≤ X ≤ a + 8) ≥ P(a ≤ Y ≤ a + 8)</span>이 되도록 하는
실수 <span class="m">a</span>의 최댓값을
<span class="m">a<sub>0</sub></span>이라 하자.</p>
<p class="m">P(a<sub>0</sub> ≤ X ≤ a<sub>0</sub> + 2) = P(a<sub>0</sub> + 2 ≤ X ≤ a<sub>0</sub> + 4)</p>
<p class="m">P(a<sub>0</sub> ≤ X ≤ a<sub>0</sub> + 4) = P(m<sub>2</sub> − σ<sub>2</sub> ≤ Y ≤ m<sub>2</sub> + σ<sub>2</sub>)</p>
<p>일 때, <span class="m">P(a<sub>0</sub> ≤ X ≤ m<sub>2</sub>)</span>의 값을
아래 표준정규분포표를 이용하여 구한 값을 <span class="m">k</span>라 하자.
<span class="m">1000 × k</span>의 값을 구하시오.
(단, <span class="m">m<sub>1</sub> &lt; m<sub>2</sub></span>이고
<span class="m">σ<sub>1</sub></span>과 <span class="m">σ<sub>2</sub></span>는
양수이다.)</p>

<span class="cond"><span class="m">z</span> : 1.0 / 1.5 / 2.0 / 2.5<br>
<span class="m">P(0 ≤ Z ≤ z)</span> : 0.341 / 0.433 / 0.477 / 0.494</span>

## 발상

<b>첫 조건은 두 정규분포가 &lsquo;서로 뒤집힌 같은 모양&rsquo;임을 말한다.</b>
양변을 표준화해 보면 정체가 드러난다.
<span class="m">P(Z ≥ u) = P(Z ≤ −u)</span>라는 표준정규분포의 대칭성을 쓰면
양변이 같은 꼴이 되고, <b>모든 <span class="m">x</span>에 대하여</b>
성립해야 하므로 <span class="m">x</span>의 계수와 상수항을 각각 비교할 수 있다.
그 결과가 <b>표준편차가 같고, 두 평균의 합이 <span class="m">10</span></b>이다.<br><br>

<b>표준편차가 같으면 두 분포는 평행이동 관계다.</b>
그러면 <span class="m">P(a ≤ X ≤ a + 8)</span>과
<span class="m">P(a ≤ Y ≤ a + 8)</span>의 비교는 아주 단순해진다.
<b>같은 폭의 창문을 어느 평균 쪽에 더 가까이 대고 있는가</b>의 문제이기 때문이다.
창문의 한가운데가 <span class="m">m<sub>1</sub></span>에 더 가까우면
<span class="m">X</span>의 확률이 더 크다.<br><br>

나머지 두 등식은 각각 <span class="m">m<sub>1</sub></span>과
<span class="m">σ</span>를 하나씩 정해 준다.
첫 등식은 <b>이웃한 두 구간의 확률이 같다</b>는 뜻이므로
그 경계가 대칭축, 곧 평균이라는 말이고,
둘째 등식은 <b>표준화했을 때 폭이 같다</b>는 뜻이다.

## 풀이

<p><span class="step">① 첫 조건을 표준화한다.</span>
좌변과 우변을 각각 표준정규분포로 바꾼다.</p>
<p class="m">P(X ≥ x) = P(Z ≥ (x − m<sub>1</sub>)/σ<sub>1</sub>)</p>
<p class="m">P(Y ≤ −x + 10) = P(Z ≤ (−x + 10 − m<sub>2</sub>)/σ<sub>2</sub>)</p>
<p>표준정규분포는 <span class="m">0</span>에 대하여 대칭이므로
<span class="m">P(Z ≥ u) = P(Z ≤ −u)</span>이다.
좌변을 이 꼴로 바꾼다.</p>
<p class="m">P(Z ≤ −(x − m<sub>1</sub>)/σ<sub>1</sub>)
= P(Z ≤ (−x + 10 − m<sub>2</sub>)/σ<sub>2</sub>)</p>

<p><span class="step">② 계수를 비교한다.</span>
<span class="m">Z</span>의 분포함수는 증가함수이므로 양쪽의 값이 같다.</p>
<p class="m">(−x + m<sub>1</sub>)/σ<sub>1</sub> = (−x + 10 − m<sub>2</sub>)/σ<sub>2</sub></p>
<p>이 등식이 <b>모든 실수 <span class="m">x</span></b>에 대하여 성립해야 하므로,
<span class="m">x</span>의 계수끼리, 상수항끼리 각각 같아야 한다.</p>
<p class="m">(x의 계수) : −1/σ<sub>1</sub> = −1/σ<sub>2</sub> → σ<sub>1</sub> = σ<sub>2</sub></p>
<p>이 공통값을 <span class="m">σ</span>라 하자. 이제 상수항을 비교한다.</p>
<p class="m">m<sub>1</sub>/σ = (10 − m<sub>2</sub>)/σ → m<sub>1</sub> + m<sub>2</sub> = 10</p>

<p><span class="step">③ a의 최댓값을 구한다.</span>
두 분포는 표준편차가 <span class="m">σ</span>로 같으므로 모양이 같고,
평균만 다른 평행이동 관계이다.
따라서 폭이 <span class="m">8</span>로 같은 구간
<span class="m">[a, a + 8]</span>의 확률은
<b>그 구간의 한가운데가 평균에 가까울수록 크다.</b>
구간의 한가운데는 <span class="m">a + 4</span>이므로</p>
<p class="m">P(a ≤ X ≤ a + 8) ≥ P(a ≤ Y ≤ a + 8)
⟺ |a + 4 − m<sub>1</sub>| ≤ |a + 4 − m<sub>2</sub>|</p>
<p><span class="m">m<sub>1</sub> &lt; m<sub>2</sub></span>이므로, 이는
<span class="m">a + 4</span>가 두 평균의 한가운데보다
왼쪽에 있다는 뜻이다.</p>
<p class="m">a + 4 ≤ (m<sub>1</sub> + m<sub>2</sub>)/2 = 10/2 = 5</p>
<p class="m">a ≤ 1 → a<sub>0</sub> = 1</p>

<p><span class="step">④ 첫 번째 등식으로 m₁을 구한다.</span>
<span class="m">a<sub>0</sub> = 1</span>을 넣으면 주어진 등식은 다음과 같다.</p>
<p class="m">P(1 ≤ X ≤ 3) = P(3 ≤ X ≤ 5)</p>
<p>서로 맞닿아 있고 폭이 <span class="m">2</span>로 같은 두 구간의 확률이 같다.
정규분포의 그래프는 평균에 대하여 대칭이므로,
<b>두 구간이 경계 <span class="m">x = 3</span>에 대하여 대칭</b>이어야 한다.
곧 <span class="m">x = 3</span>이 대칭축이다.</p>
<p class="m">m<sub>1</sub> = 3</p>
<p>②에서 <span class="m">m<sub>1</sub> + m<sub>2</sub> = 10</span>이므로</p>
<p class="m">m<sub>2</sub> = 10 − 3 = 7</p>
<p><span class="m">m<sub>1</sub> = 3 &lt; 7 = m<sub>2</sub></span>이므로
주어진 조건에 맞는다.</p>

<p><span class="step">⑤ 두 번째 등식으로 σ를 구한다.</span>
좌변은 <span class="m">P(1 ≤ X ≤ 5)</span>이다.
<span class="m">m<sub>1</sub> = 3</span>이 이 구간의 한가운데이므로
표준화하면 <span class="m">0</span>을 중심으로 대칭인 구간이 된다.</p>
<p class="m">P(1 ≤ X ≤ 5) = P(−2/σ ≤ Z ≤ 2/σ) = 2 P(0 ≤ Z ≤ 2/σ)</p>
<p>우변은 평균에서 표준편차만큼 좌우로 벌린 구간이다.</p>
<p class="m">P(m<sub>2</sub> − σ ≤ Y ≤ m<sub>2</sub> + σ) = P(−1 ≤ Z ≤ 1) = 2 P(0 ≤ Z ≤ 1)</p>
<p>두 값이 같으므로 표준화한 폭이 같아야 한다.</p>
<p class="m">2/σ = 1 → σ = 2</p>

<p><span class="step">⑥ 구하는 확률을 표준화한다.</span>
<span class="m">a<sub>0</sub> = 1</span>,
<span class="m">m<sub>2</sub> = 7</span>이고
<span class="m">X</span>는 평균이 <span class="m">3</span>,
표준편차가 <span class="m">2</span>인 정규분포를 따른다.</p>
<p class="m">k = P(1 ≤ X ≤ 7) = P((1 − 3)/2 ≤ Z ≤ (7 − 3)/2)</p>
<p class="m">= P(−1 ≤ Z ≤ 2)</p>

<p><span class="step">⑦ 표의 값으로 계산한다.</span>
구간이 <span class="m">0</span>을 걸치고 있으므로
<span class="m">0</span>을 경계로 둘로 나눈다.
음수 쪽은 대칭성으로 양수 쪽으로 옮긴다.</p>
<p class="m">P(−1 ≤ Z ≤ 2) = P(−1 ≤ Z ≤ 0) + P(0 ≤ Z ≤ 2)</p>
<p class="m">= P(0 ≤ Z ≤ 1) + P(0 ≤ Z ≤ 2)</p>
<p class="m">= 0.341 + 0.477 = 0.818</p>

<p><span class="step">⑧ 답을 만든다.</span></p>
<p class="m">1000 × k = 1000 × 0.818 = 818</p>
<p class="m">답 818</p>

## 함정

<b>&lsquo;모든 실수 <span class="m">x</span>에 대하여&rsquo;를 흘려 읽으면 안 된다.</b>
이 말이 있기 때문에 <span class="m">x</span>에 대한 항등식이 되고,
<b>계수 비교</b>가 가능해진다.
특정한 <span class="m">x</span> 하나에서만 성립하는 것이라면
<span class="m">σ<sub>1</sub> = σ<sub>2</sub></span>를 끌어낼 수 없다.<br><br>

<b><span class="m">P(X ≥ x)</span>를 그대로 두면 비교가 안 된다.</b>
좌변은 &lsquo;이상&rsquo;이고 우변은 &lsquo;이하&rsquo;이다.
<span class="m">P(Z ≥ u) = P(Z ≤ −u)</span>로 <b>방향을 맞춘 뒤</b>
비교해야 한다. 이 대칭 변환이 없으면 부호를 반대로 잡게 된다.<br><br>

<b>구간의 확률 비교를 &lsquo;<span class="m">a</span>가 평균에 가까울수록&rsquo;으로
읽으면 틀린다.</b>
비교의 기준은 구간의 <b>왼쪽 끝</b>이 아니라 <b>한가운데</b>인
<span class="m">a + 4</span>이다.
폭이 같은 창문이므로 <b>중심이 어디에 있는가</b>가 확률을 정한다.<br><br>

<b><span class="m">P(−1 ≤ Z ≤ 2)</span>를
<span class="m">P(0 ≤ Z ≤ 2) − P(0 ≤ Z ≤ 1)</span>로 쓰면 안 된다.</b>
<span class="m">−1</span>과 <span class="m">2</span>는
<span class="m">0</span>을 사이에 두고 <b>반대쪽</b>에 있으므로
빼는 것이 아니라 <b>더해야</b> 한다.
<span class="m">0.477 − 0.341 = 0.136</span>으로 쓰면 답이 <span class="m">136</span>이 된다.

## 노하우

<b>모든 <span class="m">x</span>에 대한 등식은 항등식으로 푼다.</b>
표준화한 두 식을 놓고 <b><span class="m">x</span>의 계수끼리,
상수항끼리</b> 비교하면 미지수 관계가 한 번에 나온다.
정규분포 문제에서 &lsquo;모든 실수에 대하여&rsquo;가 보이면
<b>반드시 계수 비교</b>다.<br><br>

<b>표준편차가 같은 두 정규분포는 창문의 중심으로 비교한다.</b>
폭이 같은 구간의 확률은 <b>구간의 중심이 평균에 가까울수록 크다.</b>
그래서 <span class="m">P(a ≤ X ≤ a + w) ≥ P(a ≤ Y ≤ a + w)</span>는
<span class="m">|중심 − m<sub>1</sub>| ≤ |중심 − m<sub>2</sub>|</span>,
곧 <b>중심이 두 평균의 중점보다
<span class="m">m<sub>1</sub></span> 쪽에 있다</b>는 조건이 된다.<br><br>

<b>맞닿은 두 구간의 확률이 같으면 경계가 평균이다.</b>
<span class="m">P(p ≤ X ≤ q) = P(q ≤ X ≤ r)</span>이고
두 구간의 폭이 같으면, <span class="m">x = q</span>가 대칭축이므로
<span class="m">q</span>가 곧 평균이다.
이 관찰 하나가 <span class="m">m<sub>1</sub></span>을 즉시 준다.<br><br>

<b>표준정규분포표는 <span class="m">0</span>부터 잰 값이다.</b>
표의 값은 <span class="m">P(0 ≤ Z ≤ z)</span>이므로,
구간이 <span class="m">0</span>을 걸치면 <b>더하고</b>,
같은 쪽에 있으면 <b>뺀다.</b>
<b>수직선에 <span class="m">0</span>을 찍고 구간을 그려 보는 것</b>이
가장 확실한 확인 방법이다.
