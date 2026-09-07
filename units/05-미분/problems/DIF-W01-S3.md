---
id: DIF-W01-S3
unit: 05-미분
parent: DIF-W01
topic: 근과 값 두 개로 사차함수 결정
level: 4점
difficulty: 중상
source: 사다리 3단 (DIF-W01 풀이 ⑤⑥)
origin: 사다리
core: "두 식을 나누면 최고차 계수가 약분되어 남은 근만의 방정식이 된다"
tags: [사차함수,인수분해,미정계수]
status: variant
added: 2026-09-07
answer: 65
---

## 문제

<p>사차함수 <span class="m">f(x)</span>가 다음을 만족시킨다.</p>
<span class="cond m">f(3) = f(4) = f(5) = 0, &nbsp; f(1) = −1, &nbsp; f(2) = 1</span>

<p><b>(1)</b> <span class="m">f(x)</span>를 두 상수
<span class="m">a</span>, <span class="m">s</span>를 써서 나타내시오.</p>
<p><b>(2)</b> <span class="m">f(2) = 1</span>과 <span class="m">f(1) = −1</span>을
<span class="m">a</span>, <span class="m">s</span>에 대한 식으로 쓰시오.</p>
<p><b>(3)</b> 두 식을 나누어 <span class="m">s</span>를 구하시오.</p>
<p><b>(4)</b> <span class="m">a</span>를 구하고
<span class="m">128 × f(5/2)</span>의 값을 구하시오.</p>

## 발상

근을 셋 아는데 사차함수이므로 <b>근이 하나 더 있다.</b>
그것을 <span class="m">s</span>라 두면 미지수는 <span class="m">a</span>와 <span class="m">s</span> 둘이고,
값도 두 개 주어졌으니 딱 맞는다.<br><br>
<b>두 식을 나누는 것이 핵심이다.</b> 양쪽 모두 <span class="m">a</span>를 인수로 갖고 있어서
나누면 <span class="m">a</span>가 약분되고 <span class="m">s</span>만의 방정식이 남는다.

## 풀이

<p><span class="step">(1) 인수정리로 꼴을 세운다.</span>
<span class="m">f(3) = f(4) = f(5) = 0</span>이므로
<span class="m">f(x)</span>는 <span class="m">(x−3), (x−4), (x−5)</span>를 인수로 갖는다.
사차함수라 인수가 하나 더 필요하고, 그 근을 <span class="m">s</span>라 하자.
최고차항의 계수를 <span class="m">a</span>라 하면</p>
<p class="m">f(x) = a(x − 3)(x − 4)(x − 5)(x − s)</p>

<p><span class="step">(2) 값 두 개를 식으로 옮긴다.</span>
<b>부호에 주의해서</b> 하나씩 대입한다.</p>
<p class="m">f(2) = a(2−3)(2−4)(2−5)(2−s) = a(−1)(−2)(−3)(2−s)</p>
<p>음수가 <b>세 개</b>이므로 곱은 음수다.</p>
<p class="m">f(2) = −6a(2 − s) = 1 &nbsp;&nbsp; … ㉠</p>
<p class="m">f(1) = a(1−3)(1−4)(1−5)(1−s) = a(−2)(−3)(−4)(1−s)</p>
<p class="m">f(1) = −24a(1 − s) = −1 &nbsp;&nbsp; … ㉡</p>

<p><span class="step">(3) 나누어 a를 없앤다.</span>
㉡을 ㉠으로 나눈다. 오른쪽은 <span class="m">−1 ÷ 1 = −1</span>이고,
왼쪽에서는 <b><span class="m">a</span>와 <span class="m">−6</span>이 약분된다.</b></p>
<p class="m">(−24a(1 − s)) / (−6a(2 − s)) = 4(1 − s) / (2 − s) = −1</p>
<p>양변에 <span class="m">(2 − s)</span>를 곱한다.</p>
<p class="m">4(1 − s) = −(2 − s)</p>
<p>양쪽을 전개한다.</p>
<p class="m">4 − 4s = −2 + s</p>
<p><span class="m">s</span>를 오른쪽으로, 상수를 왼쪽으로 모은다.</p>
<p class="m">4 + 2 = s + 4s → 6 = 5s → s = 6/5</p>

<p><span class="step">(4) a를 구한다.</span>
㉠에 <span class="m">s = 6/5</span>를 넣는다.</p>
<p class="m">−6a(2 − 6/5) = −6a(10/5 − 6/5) = −6a(4/5) = −24a/5</p>
<p>이것이 <span class="m">1</span>이므로</p>
<p class="m">−24a/5 = 1 → a = −5/24</p>
<p>따라서</p>
<p class="m">f(x) = −(5/24)(x−3)(x−4)(x−5)(x − 6/5)</p>
<p><span class="m">−(5/24)(x − 6/5) = −(1/24)(5x − 6)</span>이므로 더 깔끔하게 쓰면</p>
<p class="m">f(x) = −(1/24)(x − 3)(x − 4)(x − 5)(5x − 6)</p>

<p><span class="step">(5) 값을 계산한다.</span>
<span class="m">x = 5/2</span>를 넣는다. 괄호를 하나씩 계산한다.</p>
<p class="m">5/2 − 3 = −1/2, &nbsp; 5/2 − 4 = −3/2, &nbsp; 5/2 − 5 = −5/2</p>
<p class="m">5 × 5/2 − 6 = 25/2 − 12/2 = 13/2</p>
<p>음수가 <b>세 개</b>이므로 네 괄호의 곱은 음수다.</p>
<p class="m">(−1/2)(−3/2)(−5/2)(13/2) = −195/16</p>
<p class="m">f(5/2) = −(1/24) × (−195/16) = 195/384 = 65/128</p>

<p><span class="step">(6) 답.</span>
<span class="m">128</span>을 곱하면 분모가 정확히 지워진다.
<b>문제가 <span class="m">128</span>을 곱하라고 한 이유가 이것이다.</b></p>
<p class="m">128 × 65/128 = 65</p>
<p class="m">답 65</p>

## 노하우

<b>미지수가 둘인데 식도 둘이면 &lsquo;나누기&rsquo;를 먼저 생각한다.</b>
두 식이 같은 인수(여기서는 <span class="m">a</span>)를 공유하면
나누는 순간 그것이 사라지고 미지수가 하나로 줄어든다.
연립방정식을 정직하게 푸는 것보다 훨씬 짧다.<br><br>
그리고 <b>답이 <span class="m">65/128</span>처럼 나오고 문제가 <span class="m">128</span>을 곱하라고 하면
계산이 맞았다는 신호</b>다. 이런 숫자는 출제자가 답을 정수로 만들려고 붙인 것이라,
곱했을 때 딱 떨어지지 않으면 어딘가 틀린 것이다.
