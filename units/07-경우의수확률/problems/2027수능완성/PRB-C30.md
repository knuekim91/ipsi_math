---
id: PRB-C30
unit: 07-경우의수확률
topic: 시행 횟수로 상태를 추적하는 확률
level: 4점
difficulty: 상
source: 2027 수능완성 실전 모의고사 1회 30번
exam: 2027-수능완성
origin: 기출
core: "두 시행의 횟수 차이만으로 조건이 결정되어 i−j=3 이라는 한 줄로 줄어든다"
tags: [확률,시행,경우의수,조건]
status: seed
added: 2026-09-07
answer: 256
---

## 문제

<p>상자 <span class="m">A</span>와 상자 <span class="m">B</span>에 각각
<span class="m">9</span>개씩 공이 들어 있고, 상자에 들어 있지 않은 공
<span class="m">21</span>개가 있다.
두 상자 <span class="m">A, B</span>와 한 개의 주사위를 사용하여 다음 시행을 한다.</p>
<span class="cond">주사위를 한 번 던져<br>
나온 눈의 수가 <span class="m">4</span>보다 작거나 같으면<br>
상자 <span class="m">A</span>에서 공 <span class="m">1</span>개를 꺼내어
상자 <span class="m">B</span>에 넣고,<br>
나온 눈의 수가 <span class="m">4</span>보다 크면<br>
상자에 들어 있지 않은 공 중에서 <span class="m">2</span>개를 상자
<span class="m">A</span>에, <span class="m">1</span>개를 상자
<span class="m">B</span>에 각각 넣는다.</span>
<p>이 시행을 <span class="m">7</span>번 반복할 때,
<span class="m">6</span>번째 시행까지 상자 <span class="m">B</span>에 들어 있는 공의 개수가
상자 <span class="m">A</span>에 들어 있는 공의 개수의 <span class="m">2</span>배가 되는
경우가 <span class="m">1</span>번만 일어나고,
<span class="m">7</span>번째 시행에서 다시 상자 <span class="m">B</span>에 들어 있는 공의 개수가
상자 <span class="m">A</span>에 들어 있는 공의 개수의 <span class="m">2</span>배가 될 확률은
<span class="m">p</span>이다. <span class="m">3<sup>7</sup> × p</span>의 값을 구하시오.
(단, 공끼리는 서로 구별하지 않는다.)</p>

## 발상

<b>공의 개수를 매번 따라가지 않는다.</b>
두 종류의 시행을 각각 몇 번 했는지만 세면 개수가 바로 나온다.<br><br>
㉠(눈이 <span class="m">4</span> 이하)을 <span class="m">i</span>번,
㉡(눈이 <span class="m">4</span> 초과)을 <span class="m">j</span>번 했다면</p>
<p class="m">A = 9 − i + 2j, &nbsp; B = 9 + i + j</p>
<p><span class="m">B = 2A</span>를 정리하면 놀랍게도
<b><span class="m">i − j = 3</span>이라는 한 줄</b>로 줄어든다.
그러면 이 조건은 <b><span class="m">n</span>번째까지의 횟수 차이</b>만 보면 되는 문제가 된다.

## 풀이

<p><span class="step">① 두 시행이 개수를 어떻게 바꾸는지 적는다.</span>
주사위 눈이 <span class="m">1, 2, 3, 4</span>면 ㉠, <span class="m">5, 6</span>이면 ㉡이다.</p>
<p class="m">㉠ (확률 4/6 = 2/3) : A는 1 감소, B는 1 증가</p>
<p class="m">㉡ (확률 2/6 = 1/3) : A는 2 증가, B는 1 증가</p>

<p><span class="step">② n번 시행한 뒤의 개수를 식으로 쓴다.</span>
㉠을 <span class="m">i</span>번, ㉡을 <span class="m">j</span>번 했다고 하자
(<span class="m">i + j = n</span>).</p>
<p class="m">A = 9 − i + 2j, &nbsp; B = 9 + i + j</p>

<p><span class="step">③ 조건 B = 2A 를 정리한다.</span></p>
<p class="m">9 + i + j = 2(9 − i + 2j)</p>
<p>오른쪽을 전개한다.</p>
<p class="m">9 + i + j = 18 − 2i + 4j</p>
<p><span class="m">i</span>와 <span class="m">j</span>를 왼쪽으로, 상수를 오른쪽으로 모은다.</p>
<p class="m">3i − 3j = 9 → i − j = 3</p>
<p><b>조건이 &lsquo;㉠을 ㉡보다 <span class="m">3</span>번 더 했다&rsquo;로 바뀌었다.</b></p>

<p><span class="step">④ 조건이 성립할 수 있는 시각을 찾는다.</span>
<span class="m">i + j = n</span>과 <span class="m">i − j = 3</span>을 연립하면</p>
<p class="m">i = (n+3)/2, &nbsp; j = (n−3)/2</p>
<p>둘 다 <span class="m">0</span> 이상의 정수여야 하므로
<b><span class="m">n</span>은 <span class="m">3</span> 이상의 홀수</b>다.
<span class="m">7</span>번까지 중에서는</p>
<p class="m">n = 3 (i=3, j=0), &nbsp; n = 5 (i=4, j=1), &nbsp; n = 7 (i=5, j=2)</p>
<p>이 세 시각에서만 조건이 성립할 수 있다.</p>

<p><span class="step">⑤ 문제가 요구하는 것을 정리한다.</span>
<span class="m">7</span>번째에 조건이 성립해야 하므로
<b>전체 <span class="m">7</span>번 중 ㉠이 <span class="m">5</span>번, ㉡이 <span class="m">2</span>번</b>이다.
그리고 <span class="m">n = 3</span>과 <span class="m">n = 5</span> 중
<b>정확히 하나에서만</b> 조건이 성립해야 한다.</p>
<p class="m">n = 3에서 성립 ⟺ 처음 세 번이 모두 ㉠</p>
<p class="m">n = 5에서 성립 ⟺ 처음 다섯 번 중 ㉡이 정확히 1번</p>

<p><span class="step">⑥ ㉡이 놓인 자리로 세어 본다.</span>
㉡ 두 번이 <span class="m">7</span>자리 중 어디에 놓이는지를
<span class="m">(p, q)</span> (<span class="m">p &lt; q</span>)로 나타내면 모두
<span class="m"><sub>7</sub>C<sub>2</sub> = 21</span>가지다.</p>
<p class="m">n = 3 성립 ⟺ p ≥ 4 &nbsp; (처음 3자리에 ㉡이 없음)</p>
<p class="m">n = 5 성립 ⟺ p ≤ 5 이고 q ≥ 6 &nbsp; (처음 5자리에 ㉡이 정확히 1개)</p>
<p><b>둘 중 정확히 하나만</b> 성립하는 것을 고른다.</p>
<p class="m">n=5만 : (1,6) (1,7) (2,6) (2,7) (3,6) (3,7) → 6가지</p>
<p class="m">n=3만 : (4,5) (6,7) → 2가지</p>
<p class="m">둘 다 성립 : (4,6) (4,7) (5,6) (5,7) → 제외</p>
<p class="m">둘 다 안 됨 : 나머지 → 제외</p>
<p>따라서 <span class="m">6 + 2 = 8</span>가지다.</p>
<p>(<span class="m">(6,7)</span>은 처음 다섯 번이 모두 ㉠이라
<span class="m">i−j = 5 ≠ 3</span>이므로 <span class="m">n=5</span>에서는 성립하지 않는다.)</p>

<p><span class="step">⑦ 확률을 계산한다.</span>
각 배열은 ㉠ <span class="m">5</span>번, ㉡ <span class="m">2</span>번이므로 확률이 같다.</p>
<p class="m">(2/3)<sup>5</sup> × (1/3)<sup>2</sup> = 2<sup>5</sup>/3<sup>7</sup> = 32/3<sup>7</sup></p>
<p class="m">p = 8 × 32/3<sup>7</sup> = 256/3<sup>7</sup></p>

<p><span class="step">⑧ 답을 만든다.</span></p>
<p class="m">3<sup>7</sup> × p = 256</p>
<p class="m">답 256</p>

## 함정

<b><span class="m">(4,6)</span>처럼 두 시각 모두에서 성립하는 것을 빼야 한다.</b>
문제가 &lsquo;<span class="m">1</span>번만 일어나고&rsquo;라고 했으므로
<span class="m">n=3</span>과 <span class="m">n=5</span>에서 <b>둘 다 성립하면 탈락</b>이다.
&lsquo;적어도 한 번&rsquo;으로 읽으면 <span class="m">12</span>가지가 되어 답이 <span class="m">384</span>가 된다.<br><br>
그리고 <b><span class="m">(6,7)</span>을 빠뜨리기 쉽다.</b>
처음 세 번이 모두 ㉠이라 <span class="m">n=3</span>에서 성립하고,
<span class="m">n=5</span>에서는 ㉡이 <span class="m">0</span>개라 성립하지 않으므로
&lsquo;정확히 한 번&rsquo;에 해당한다.

## 노하우

<b>상태가 두 종류의 시행으로만 바뀌면 &lsquo;각각 몇 번 했는가&rsquo;로 환원한다.</b>
순서를 따라가며 개수를 세면 <span class="m">2<sup>7</sup> = 128</span>가지를 봐야 하지만,
<span class="m">i</span>와 <span class="m">j</span>로 쓰면 조건이 <span class="m">i − j = 3</span> 한 줄이 된다.<br><br>
<b>그다음은 &lsquo;㉡이 어느 자리에 놓이는가&rsquo;만 센다.</b>
㉡이 <span class="m">2</span>개뿐이라 <span class="m"><sub>7</sub>C<sub>2</sub> = 21</span>가지밖에 없어
손으로 전부 확인할 수 있다.
<b>경우의 수가 <span class="m">20</span>가지 안쪽이면 표를 만들어 세는 것이 가장 안전하다.</b>
