---
id: PRB-W04
unit: 07-경우의수확률
topic: 부호 조건이 걸린 정수 순서쌍의 개수
level: 4점
difficulty: 상
source: 2027학년도 10월 모의고사(대성) 30번
exam: 오답노트
origin: 기출
core: "|x|+x 는 x>0 이면 2x, x<0 이면 0 이다. 그래서 (다)는 '왼쪽이 음수, 오른쪽이 양수'만이 아니라 '둘 다 양수인데 왼쪽이 작다'도 포함한다"
tags: [중복조합,절댓값,부호,순서쌍,경우나누기,대칭]
status: wrong
added: 2026-10-17
answer: 132
---

## 문제

<p>다음 조건을 만족시키는 <span class="m">0</span>이 아닌 네 정수
<span class="m">a</span>, <span class="m">b</span>,
<span class="m">c</span>, <span class="m">d</span>의 모든 순서쌍
<span class="m">(a, b, c, d)</span>의 개수를 구하시오.</p>

<div class="cond">
<span class="cond m">(가) a + b + c + d = 0</span>
<span class="cond m">(나) |a| + |b| + |c| + |d| = 14</span>
<span class="cond m">(다) |a| + a &lt; |b| + b</span>
</div>

## 발상

<b>(가)와 (나)를 같이 보면 양수 쪽과 음수 쪽이 따로 정해진다.</b>
양수인 것들의 합을 <span class="m">A</span>,
음수인 것들의 합을 <span class="m">B</span>라 하면
(가)는 <span class="m">A + B = 0</span>,
(나)는 <span class="m">A − B = 14</span>다.
더하고 빼면 <span class="m">A = 7</span>,
<span class="m">B = −7</span>이다.
<b>양수들은 합이 7, 음수들은 절댓값의 합이 7</b>로 완전히 갈라진다.<br><br>

<b>(다)는 부호를 거르는 장치다.</b>
<span class="m">|x| + x</span>는</p>
<p class="m">x &gt; 0 → 2x, &nbsp; x &lt; 0 → 0</p>
<p>이다. 곧 <b>음수는 모두 <span class="m">0</span>으로 뭉뚱그려지고,
양수만 자기 값의 두 배로 남는다.</b><br><br>

<b>여기가 이 문제의 전부다.</b>
<span class="m">|a| + a &lt; |b| + b</span>를
&lsquo;왼쪽은 음수, 오른쪽은 양수&rsquo;로만 읽으면 안 된다.
<b>둘 다 양수여도 <span class="m">2a &lt; 2b</span>, 곧
<span class="m">a &lt; b</span>면 성립한다.</b>
갈래가 둘이다.

## 풀이

<p><span class="step">① 양수 쪽과 음수 쪽의 합을 구한다.</span>
<span class="m">0</span>이 아닌 정수이므로 넷은 모두 양수 아니면 음수다.
양수인 것들의 합을 <span class="m">A</span>,
음수인 것들의 합을 <span class="m">B</span>라 하면</p>
<p class="m">(가) A + B = 0, &nbsp; (나) A − B = 14</p>
<p class="m">A = 7, &nbsp; B = −7</p>
<p><b>양수들의 합은 7, 음수들의 절댓값의 합은 7</b>이다.
둘 다 <span class="m">0</span>이 아니므로
<b>양수도 적어도 하나, 음수도 적어도 하나</b> 있다.</p>

<p><span class="step">② 합이 7인 양의 정수 순서쌍의 개수를 미리 구해 둔다.</span>
<span class="m">k</span>개의 양의 정수의 합이 <span class="m">7</span>인
순서쌍의 개수는, 각각에서 <span class="m">1</span>씩 떼어 내면
<b>음이 아닌 <span class="m">k</span>개의 정수의 합이
<span class="m">7 − k</span></b>인 문제가 되므로</p>
<p class="m"><sub>k</sub>H<sub>7−k</sub> = <sub>6</sub>C<sub>k−1</sub></p>
<p class="m"><sub>1</sub>H<sub>6</sub> = 1, &nbsp;
<sub>2</sub>H<sub>5</sub> = <sub>6</sub>C<sub>5</sub> = 6, &nbsp;
<sub>3</sub>H<sub>4</sub> = <sub>6</sub>C<sub>4</sub> = 15</p>
<p><b>이 세 수 <span class="m">1, 6, 15</span>만 가지고 끝까지 간다.</b></p>

<p><span class="step">③ (다)를 두 갈래로 나눈다.</span>
<span class="m">|x| + x</span>는
<span class="m">x &gt; 0</span>이면 <span class="m">2x</span>,
<span class="m">x &lt; 0</span>이면 <span class="m">0</span>이다.</p>
<p class="m">a &lt; 0 일 때 : |a| + a = 0 &lt; |b| + b → b &gt; 0</p>
<p class="m">a &gt; 0 일 때 : 0 &lt; 2a &lt; |b| + b → b &gt; 0, 2a &lt; 2b</p>
<p>따라서 갈래는 둘이다.</p>
<p class="m">(i) a &lt; 0, b &gt; 0 &nbsp;&nbsp; (ii) 0 &lt; a &lt; b</p>

<p><span class="step">④ (i) a &lt; 0 &lt; b 인 경우를 센다.</span>
<span class="m">a</span>는 음수, <span class="m">b</span>는 양수로 정해졌으므로
<b><span class="m">c</span>, <span class="m">d</span>의 부호만</b> 고르면 된다.<br>

<b>양수 3개, 음수 1개</b> <span class="m">(c &gt; 0, d &gt; 0)</span><br>
음수는 <span class="m">a</span>뿐이므로
<span class="m">a = −7</span>로 <span class="m">1</span>가지,
양수 <span class="m">b</span>, <span class="m">c</span>,
<span class="m">d</span>의 합이 <span class="m">7</span>이므로
<span class="m">15</span>가지</p>
<p class="m">1 × 15 = 15</p>

<p><b>양수 2개, 음수 2개</b>
<span class="m">(c &gt; 0, d &lt; 0</span> 또는
<span class="m">c &lt; 0, d &gt; 0)</span><br>
음수 둘의 절댓값의 합이 <span class="m">7</span>이므로
<span class="m">6</span>가지, 양수 둘의 합이
<span class="m">7</span>이므로 <span class="m">6</span>가지</p>
<p class="m">6 × 6 = 36</p>
<p>두 경우가 있으므로 <span class="m">36 × 2 = 72</span></p>

<p><b>양수 1개, 음수 3개</b> <span class="m">(c &lt; 0, d &lt; 0)</span><br>
양수는 <span class="m">b = 7</span>로 <span class="m">1</span>가지,
음수 <span class="m">a</span>, <span class="m">c</span>,
<span class="m">d</span>의 절댓값의 합이 <span class="m">7</span>이므로
<span class="m">15</span>가지</p>
<p class="m">1 × 15 = 15</p>
<p class="m">15 + 72 + 15 = 102</p>

<p><span class="step">⑤ (ii) 0 &lt; a &lt; b 인 경우를 센다.</span>
<span class="m">a</span>, <span class="m">b</span>가 모두 양수이므로
<b>음수는 <span class="m">c</span>, <span class="m">d</span> 안에만</b> 있다.
둘 다 양수이면 음수가 하나도 없어 불가능하다.<br>

<b>양수 3개, 음수 1개</b>
<span class="m">(c &gt; 0, d &lt; 0</span> 또는
<span class="m">c &lt; 0, d &gt; 0)</span><br>
음수는 <span class="m">−7</span> 하나로 <span class="m">1</span>가지.
양수 셋의 합이 <span class="m">7</span>인 순서쌍은
<span class="m">15</span>개인데, 그중
<span class="m">a &lt; b</span>인 것만 센다.<br>
<span class="m">a = b</span>인 경우는 나머지 하나를
<span class="m">e</span>라 할 때
<span class="m">2a + e = 7</span>에서
<span class="m">a = 1, 2, 3</span>으로 <span class="m">3</span>가지다.
남은 <span class="m">12</span>개는
<span class="m">a &lt; b</span>와 <span class="m">a &gt; b</span>가
<b>맞바꾸기로 짝</b>을 이루므로 반씩이다.</p>
<p class="m">(15 − 3) ÷ 2 = 6</p>
<p>두 경우가 있으므로 <span class="m">6 × 2 = 12</span></p>

<p><b>양수 2개, 음수 2개</b> <span class="m">(c &lt; 0, d &lt; 0)</span><br>
음수 둘의 절댓값의 합이 <span class="m">7</span>이므로
<span class="m">6</span>가지.
양수는 <span class="m">a + b = 7</span>이고
<span class="m">a &lt; b</span>이므로</p>
<p class="m">(1, 6), (2, 5), (3, 4) → 3가지</p>
<p class="m">3 × 6 = 18</p>
<p class="m">12 + 18 = 30</p>

<p><span class="step">⑥ 답을 만든다.</span></p>
<p class="m">102 + 30 = 132</p>
<p class="m">답 132</p>

## 다른 풀이

<b>(다)는 한 줄로 줄일 수 있다.</b>
<span class="m">|b| + b</span>가
<span class="m">|a| + a ≥ 0</span>보다 커야 하므로
<span class="m">|b| + b &gt; 0</span>, 곧
<span class="m">b &gt; 0</span>이다.
그러면 <span class="m">a</span>가 음수이면
<span class="m">a &lt; 0 &lt; b</span>이고,
<span class="m">a</span>가 양수이면
<span class="m">2a &lt; 2b</span>에서
<span class="m">a &lt; b</span>다.
거꾸로 <span class="m">b &gt; 0</span>이고
<span class="m">a &lt; b</span>이면 (다)가 성립한다.</p>
<p class="m">(다) ⟺ b &gt; 0 이고 a &lt; b</p>
<p><b>두 갈래로 나누는 대신 이 한 줄을 들고 가면 실수가 줄어든다.</b>
&lsquo;<span class="m">b</span>가 양수&rsquo;만 확인하고 나면
남는 것은 <span class="m">a &lt; b</span>라는 평범한 대소뿐이다.<br><br>

<b>맞바꾸기 대칭으로 검산한다.</b>
<span class="m">a</span>와 <span class="m">b</span>를 맞바꾸어도
(가)와 (나)는 그대로이므로,</p>
<p class="m">(|a|+a &lt; |b|+b 인 개수) = (|a|+a &gt; |b|+b 인 개수)</p>
<p>이다. 한편 <span class="m">|a| + a = |b| + b</span>인 것은
<b><span class="m">a</span>, <span class="m">b</span>가 모두 음수</b>이거나
<b><span class="m">a = b &gt; 0</span></b>인 경우로
<span class="m">66 + 6 = 72</span>개다.
(다)를 뺀 전체는 <span class="m">60 + 216 + 60 = 336</span>개이므로</p>
<p class="m">132 + 132 + 72 = 336 ✓</p>
<p><b>답을 내고 나면 이 한 줄로 확인할 수 있다.</b></p>

## 함정

<b>(다)를 &lsquo;음수 &lt; 양수&rsquo;로만 읽으면 102에서 멈춘다.</b>
실제로 그렇게 풀어 <span class="m">102</span>를 적었다.
<b><span class="m">102</span>는 (i)만 센 값이고 그 부분은 완벽하다.</b>
빠진 것은 <b>둘 다 양수인데 <span class="m">a</span>가 더 작은</b>
<span class="m">30</span>가지다.<br>
<span class="m">|x| + x</span>는 음수를 <span class="m">0</span>으로 뭉개지만,
<b>양수끼리는 크기를 그대로 남긴다.</b>
<span class="m">x &gt; 0</span>일 때 <span class="m">2x</span>라는 것을
표로 적어 두면 놓치지 않는다.<br><br>

<b>&lsquo;<span class="m">0</span>이 아닌&rsquo;을 흘리지 않는다.</b>
이 조건 때문에 <b>양수도 하나 이상, 음수도 하나 이상</b>이 보장되고,
&lsquo;<span class="m">k</span>개의 <b>양의</b> 정수의 합&rsquo;으로
중복조합을 쓸 수 있다.
<span class="m">0</span>을 허용하면 식이 완전히 달라진다.<br><br>

<b><span class="m">a &lt; b</span>를 셀 때 <span class="m">15 ÷ 2</span>를 하지 않는다.</b>
<span class="m">a = b</span>인 <span class="m">3</span>가지를
<b>먼저 빼고</b> 나눠야 한다.
홀수를 반으로 나누려는 순간 무언가 빠뜨린 것이다.<br><br>

<b>&lsquo;양수 2개, 음수 2개&rsquo;에서 자리를 두 번 세지 않는다.</b>
(i)에서는 <span class="m">a</span>가 음수,
<span class="m">b</span>가 양수로 <b>이미 정해져 있으므로</b>
<span class="m">c</span>, <span class="m">d</span>의 부호만 고른다.
<span class="m"><sub>4</sub>C<sub>2</sub> = 6</span>을 곱하면 중복이다.

## 노하우

<b><span class="m">|x| ± x</span>는 부호를 거르는 장치다. 표로 외운다.</b></p>
<p class="m">x &gt; 0 : |x| + x = 2x, &nbsp; |x| − x = 0</p>
<p class="m">x &lt; 0 : |x| + x = 0, &nbsp; |x| − x = −2x</p>
<p><b>한쪽은 <span class="m">0</span>으로 뭉개고 다른 쪽은 두 배로 남긴다.</b>
이 꼴이 보이면 <b>곧바로 부호로 경우를 나눈다.</b><br><br>

<b>&lsquo;합&rsquo;과 &lsquo;절댓값의 합&rsquo;이 같이 주어지면 양쪽이 분리된다.</b>
합이 <span class="m">S</span>, 절댓값의 합이
<span class="m">T</span>이면</p>
<p class="m">양수들의 합 = (S + T)/2, &nbsp; 음수들의 절댓값의 합 = (T − S)/2</p>
<p>이 문제는 <span class="m">S = 0</span>이라 양쪽이 똑같이
<span class="m">7</span>이었다.
<b><span class="m">S ≠ 0</span>이면 양쪽 수가 달라지므로 더 조심해야 한다.</b><br><br>

<b><span class="m">k</span>개의 양의 정수의 합이
<span class="m">n</span>인 순서쌍의 개수</b></p>
<p class="m"><sub>k</sub>H<sub>n−k</sub> = <sub>n−1</sub>C<sub>k−1</sub></p>
<p><span class="m">1</span>씩 떼어 내 음이 아닌 수로 바꾸는 것이
<b>중복조합으로 가는 표준 치환</b>이다.
<span class="m">n = 7</span>이면
<span class="m">1, 6, 15, 20</span>이 차례로 나온다.<br><br>

<b>두 자리의 대소가 걸리면 맞바꾸기로 반을 센다.</b></p>
<p class="m">(a &lt; b 인 개수) = (전체 − a = b 인 개수) ÷ 2</p>
<p><span class="m">a</span>와 <span class="m">b</span>를 맞바꾸는 것이
<b>조건을 보존하는 짝짓기</b>이기 때문이다.
<b>세기 어려울 때뿐 아니라 검산에도 쓴다.</b>
이 문제에서는 <span class="m">132 + 132 + 72 = 336</span>이 맞는지만 보면
<span class="m">30</span>을 빠뜨렸는지 바로 드러난다.
