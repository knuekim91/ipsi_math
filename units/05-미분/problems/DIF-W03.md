---
id: DIF-W03
unit: 05-미분
topic: 합성 방정식의 실근 개수
level: 4점
difficulty: 상
source: 2022-06모평 공통 22번
exam: 2022-06모평
origin: 오답노트
core: "g(x)=x−f(x)로 두면 g(α)=α, g(β)=β가 되어 실근 두 개는 공짜로 생긴다"
tags: [삼차함수,합성,실근개수,중근]
status: wrong
added: 2026-09-06
answer: 61
---

## 문제

<p>삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킨다.</p><span class="cond">(가) 방정식 <span class="m">f(x) = 0</span>의 서로 다른 실근의 개수는 <span class="m">2</span>이다.<br>(나) 방정식 <span class="m">f(x − f(x)) = 0</span>의 서로 다른 실근의 개수는 <span class="m">3</span>이다.</span><p><span class="m">f(1) = 4</span>, <span class="m">f′(1) = 1</span>, <span class="m">f′(0) &gt; 1</span>일 때, <span class="m">f(0) = q/p</span>이다. <span class="m">p + q</span>의 값을 구하시오. (단, <span class="m">p</span>와 <span class="m">q</span>는 서로소인 자연수이다.)</p>

## 발상

(가)에서 삼차함수가 실근 2개 → <b>중근 <span class='m'>α</span> + 단순근 <span class='m'>β</span></b>, 곧 <span class='m'>f(x) = a(x−α)<sup>2</sup>(x−β)</span>.<br><br><b><span class='m'>g(x) = x − f(x)</span>로 두는 것이 이 문제의 전부다.</b> 그러면 <span class='m'>f(x−f(x)) = 0 ⟺ g(x) = α</span> 또는 <span class='m'>g(x) = β</span>인데,</p><p class='m'>g(α) = α − f(α) = α, &nbsp; g(β) = β − f(β) = β</p><p><b><span class='m'>α</span>와 <span class='m'>β</span>는 저절로 해가 된다.</b> 실근 2개는 공짜고, <b>딱 하나만 더 나와야</b> 한다. 삼차함수에서 <span class='m'>g(x)=c</span>의 해가 2개인 것은 <b><span class='m'>c</span>가 극값일 때뿐</b>이다.<br><br>여기서 <span class='m'>f′(1)=1</span>이 결정타다. <b><span class='m'>g′(1) = 1 − f′(1) = 0</span>이라 <span class='m'>x=1</span>이 <span class='m'>g</span>의 극점</b>이고, 그 극값이 <span class='m'>g(1) = 1 − f(1) = −3</span>이다.

## 풀이

<p><span class="step">① f의 모양을 정한다.</span>
(가)에서 삼차함수인데 <span class="m">f(x) = 0</span>의 서로 다른 실근이 <span class="m">2</span>개라 했다.
삼차함수의 근은 위수를 합쳐 <span class="m">3</span>개이므로,
<b>하나는 중근이고 하나는 단순근</b>이다.
중근을 <span class="m">α</span>, 단순근을 <span class="m">β</span>라 하고 최고차항의 계수를 <span class="m">a</span>라 하면</p>
<p class="m">f(x) = a(x − α)<sup>2</sup>(x − β), &nbsp; α ≠ β</p>

<p><span class="step">② 안쪽을 치환해 방정식을 풀어 쓴다.</span>
<span class="m">f(x − f(x)) = 0</span>은 <b>안쪽 <span class="m">x − f(x)</span>가 <span class="m">f</span>의 근이 되라</b>는 뜻이다.
안쪽을 <span class="m">g(x)</span>라 두자.</p>
<p class="m">g(x) = x − f(x)</p>
<p class="m">f(x − f(x)) = 0 ⟺ g(x) = α 또는 g(x) = β</p>
<p>즉 <span class="m">y = g(x)</span>의 그래프에 <b>수평선 두 개를 긋고 교점을 세는</b> 문제가 되었다.</p>

<p><span class="step">③ 실근 두 개가 공짜로 생김을 확인한다.</span>
<span class="m">α</span>와 <span class="m">β</span>는 <span class="m">f</span>의 근이라 <span class="m">f(α) = f(β) = 0</span>이다.
이를 <span class="m">g</span>에 넣어 보면</p>
<p class="m">g(α) = α − f(α) = α − 0 = α</p>
<p class="m">g(β) = β − f(β) = β − 0 = β</p>
<p>즉 <b><span class="m">x = α</span>는 <span class="m">g(x) = α</span>의 해이고,
<span class="m">x = β</span>는 <span class="m">g(x) = β</span>의 해</b>다.
계산하지 않아도 이미 <b>서로 다른 실근 두 개</b>가 확보되어 있다.</p>

<p><span class="step">④ 나머지 한 개가 어디서 오는지 따진다.</span>
실근이 모두 <span class="m">3</span>개라 했으므로 <b>딱 하나만 더</b> 나와야 한다.
<span class="m">g</span>는 삼차함수이므로 <span class="m">g(x) = c</span>의 해는 <span class="m">1</span>개, <span class="m">2</span>개, <span class="m">3</span>개 중 하나다.
두 방정식의 해를 합쳐 <span class="m">3</span>개이고 각각 적어도 <span class="m">1</span>개씩 있으므로,
<b>하나는 해가 1개, 다른 하나는 해가 2개</b>다.</p>
<p>삼차함수에서 <span class="m">g(x) = c</span>의 해가 정확히 <span class="m">2</span>개인 것은
<b><span class="m">c</span>가 <span class="m">g</span>의 극값일 때뿐</b>이고,
그때 두 해 중 하나는 <b>극값을 갖는 점에서의 중근</b>이다.</p>

<p><span class="step">⑤ f′(1) = 1이 극점을 지목한다.</span>
<span class="m">g(x) = x − f(x)</span>를 미분하면</p>
<p class="m">g′(x) = 1 − f′(x)</p>
<p><span class="m">f′(1) = 1</span>이므로</p>
<p class="m">g′(1) = 1 − 1 = 0</p>
<p>즉 <b><span class="m">x = 1</span>이 <span class="m">g</span>의 극점</b>이다. 그때의 값은</p>
<p class="m">g(1) = 1 − f(1) = 1 − 4 = −3</p>
<p>새로 추가되는 해가 바로 이 극점 <span class="m">x = 1</span>이므로,
<b>그 수평선의 높이가 <span class="m">−3</span></b>이어야 한다. 따라서</p>
<p class="m">α = −3 또는 β = −3</p>

<p><span class="step">⑥ β = −3은 불가능함을 보인다.</span>
<span class="m">f(x) = a(x − α)<sup>2</sup>(x + 3)</span>이라 하고 두 조건을 쓴다.</p>
<p class="m">f(1) = a(1 − α)<sup>2</sup> × 4 = 4 → a(1 − α)<sup>2</sup> = 1</p>
<p>도함수를 구한다. 공통인수 <span class="m">(x − α)</span>로 묶으면</p>
<p class="m">f′(x) = a(x − α)[2(x + 3) + (x − α)] = a(x − α)(3x + 6 − α)</p>
<p class="m">f′(1) = a(1 − α)(9 − α) = 1</p>
<p>두 식의 오른쪽이 모두 <span class="m">1</span>이므로 왼쪽끼리 같다.</p>
<p class="m">a(1 − α)<sup>2</sup> = a(1 − α)(9 − α)</p>
<p>한쪽으로 넘기고 <span class="m">a(1 − α)</span>로 묶는다.</p>
<p class="m">a(1 − α)[(1 − α) − (9 − α)] = 0 → a(1 − α)(−8) = 0</p>
<p>그러면 <span class="m">a(1 − α) = 0</span>이 되어 <span class="m">f(1) = 0</span>이 되는데,
<span class="m">f(1) = 4</span>라 했으므로 <b>모순</b>이다.</p>

<p><span class="step">⑦ α = −3으로 f를 결정한다.</span>
<span class="m">f(x) = a(x + 3)<sup>2</sup>(x − β)</span>로 두고 같은 두 조건을 쓴다.</p>
<p class="m">f(1) = a × 16 × (1 − β) = 4 → a(1 − β) = 1/4 &nbsp;&nbsp; … ㉠</p>
<p class="m">f′(x) = a(x + 3)[2(x − β) + (x + 3)] = a(x + 3)(3x + 3 − 2β)</p>
<p class="m">f′(1) = a × 4 × (6 − 2β) = 8a(3 − β) = 1 &nbsp;&nbsp; … ㉡</p>
<p>㉡을 ㉠으로 나누면 <span class="m">a</span>가 약분된다.</p>
<p class="m">8(3 − β) / (1 − β) = 1 ÷ (1/4) = 4</p>
<p class="m">8(3 − β) = 4(1 − β) → 24 − 8β = 4 − 4β</p>
<p class="m">20 = 4β → β = 5</p>
<p>㉠에 넣어 <span class="m">a</span>를 구한다.</p>
<p class="m">a(1 − 5) = 1/4 → −4a = 1/4 → a = −1/16</p>
<p class="m">f(x) = −(1/16)(x + 3)<sup>2</sup>(x − 5)</p>

<p><span class="step">⑧ f′(0) &gt; 1 인지 확인한다.</span>
<b>이 조건은 장식이 아니다.</b> 다른 갈래를 걸러내기 위해 붙은 것이므로 반드시 확인한다.</p>
<p class="m">f′(0) = −(1/16) × 3 × (0 + 3 − 10) = −(1/16) × 3 × (−7) = 21/16</p>
<p class="m">21/16 = 1.3125 &gt; 1 ✓</p>

<p><span class="step">⑨ 답을 만든다.</span></p>
<p class="m">f(0) = −(1/16) × 9 × (−5) = 45/16</p>
<p><span class="m">45</span>와 <span class="m">16</span>은 서로소이므로
<span class="m">q = 45</span>, <span class="m">p = 16</span>이다.</p>
<p class="m">p + q = 16 + 45 = 61</p>

<p><span class="step">⑩ 검산한다.</span>
<span class="m">g(x) = x + (1/16)(x + 3)<sup>2</sup>(x − 5)</span>에 세 값을 넣어 본다.</p>
<p class="m">g(−3) = −3 = α &nbsp;/&nbsp; g(1) = 1 − 4 = −3 = α &nbsp;/&nbsp; g(5) = 5 − 0 = 5 = β</p>
<p><span class="m">f(x − f(x)) = 0</span>의 실근은 <span class="m">−3, 1, 5</span>로 <b>모두 3개</b>다. ✓</p>
<p class="m">답 61</p>

## 함정

<b><span class='m'>α</span>가 <span class='m'>g</span>의 극점일 수는 없다.</b> <span class='m'>g′(α) = 1 − f′(α)</span>인데 <span class='m'>α</span>는 <span class='m'>f</span>의 중근이라 <span class='m'>f′(α) = 0</span>, 곧 <span class='m'>g′(α) = 1 ≠ 0</span>이다. 그래서 <b>새로 생기는 해가 극점 쪽</b>이라는 것이 확정된다.<br><br>그리고 <b><span class='m'>f′(0) &gt; 1</span>은 장식이 아니다.</b> <span class='m'>x=1</span>이 아닌 <b>다른 극점</b>에서 조건이 맞는 갈래도 계산상 존재하는데, 그것들은 정확히 <span class='m'>f′(0) &gt; 1</span>에서 걸러진다. 이런 부등식 조건이 붙어 있으면 <b>답이 여러 개 나올 수 있다는 출제자의 예고</b>로 읽어야 한다.

## 노하우

<b>안쪽에 함수가 들어간 <span class='m'>f(□) = 0</span> 꼴은 &lsquo;□를 f의 근으로 만드는 문제&rsquo;로 바꾼다.</b> 안쪽을 <span class='m'>g(x)</span>라 두면 <span class='m'>f</span>의 근이 <span class='m'>α, β</span>이므로 <span class='m'>g(x) = α</span> 또는 <span class='m'>g(x) = β</span>, 곧 <b>수평선 두 개를 긋는 그림</b>이 된다.<br><br>이 문제의 특별한 선물은 <b><span class='m'>g(x) = x − f(x)</span>일 때 <span class='m'>f</span>의 근을 그대로 넣으면 <span class='m'>g(α) = α − f(α) = α</span>, <span class='m'>g(β) = β</span>가 되어 그 자리에서 해가 된다</b>는 것이다. 그래서 실근 2개는 세지 않아도 이미 확보되어 있고, <b>남은 한 개가 어디서 오는가</b>만 따지면 된다.<br><br><b>&lsquo;<span class='m'>f(x)=c</span>의 해가 2개&rsquo; = &lsquo;<span class='m'>c</span>가 극값&rsquo; = &lsquo;중근이 하나 있다&rsquo;</b>는 삼차함수 문제의 상비 도구다. 6월 모평 21번(최대근이 불연속이 되는 조건)과 같은 도구를 쓴다.
