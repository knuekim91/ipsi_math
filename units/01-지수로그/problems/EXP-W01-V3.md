---
id: EXP-W01-V3
parent: EXP-W01
unit: 01-지수로그
topic: 부등식의 해와 교점으로 두 상수를 거꾸로 찾기
level: 4점
difficulty: 상
source: 자체 개발 (EXP-W01 변형 · 역방향 추론)
origin: 유사문항
core: "m = −1/b 로 b를 먼저 잡고, 교점이 y=x 위에 있다는 것으로 a를 잡는다. 모문항에서 챙겨 둔 두 줄이면 끝난다"
tags: [지수함수,로그함수,역함수,부등식,역추론,함수결정]
status: variant
added: 2026-10-17
answer: 64
---

## 문제

<p>두 상수 <span class="m">a (a &gt; 1)</span>, <span class="m">b</span>에 대하여
<span class="m">x &gt; b</span>에서 <span class="m">a<sup>x</sup> + b</span>와
<span class="m">log<sub>a</sub>(x − b)</span> 중 크지 않은 값을
<span class="m">f(x)</span>라 하자.
모든 양수 <span class="m">t</span>에 대하여 <span class="m">x</span>에 대한 방정식</p>

<p class="m">f(x) = t(x − 1) + 1</p>

<p>이 서로 다른 두 실근 <span class="m">α(t)</span>,
<span class="m">β(t)</span> <span class="m">(α(t) &lt; β(t))</span>를 갖는다.
다음 조건을 만족시킬 때,
<span class="m">16 × a<sup>3</sup></span>의 값을 구하시오.</p>

<div class="cond">
<span class="cond m">(가) 부등식 f(α(t)) × f(β(t)) &gt; 0의 해는 0 &lt; t &lt; 1이다.</span>
<span class="cond m">(나) β(1) = 3</span>
</div>

## 발상

<b>모문항은 조건에서 <span class="m">a</span>를 구했다.
이 문항도 같지만, 길이 훨씬 짧다.</b>
모문항을 풀면서 <b>두 줄을 결론으로 챙겨 두었는지</b>가 갈림길이다.</p>
<p class="m">① 부등식의 해가 0 &lt; t &lt; m 이면 m = −1/b</p>
<p class="m">② 교점은 y = x 위에 있다 → a<sup>x</sup> + b = x</p>
<p><b>(가)는 ①로, (나)는 ②로 한 줄씩 넘긴다.</b><br><br>

<b>①이 왜 성립하는지는 다시 떠올릴 수 있어야 한다.</b>
<span class="m">f</span>의 <span class="m">x</span>절편은
<span class="m">(b + 1, 0)</span>이고,
직선 <span class="m">y = t(x − 1) + 1</span>의
<span class="m">x</span>절편은 <span class="m">1 − 1/t</span>다.
<b>둘이 같아지는 순간이 부호가 갈리는 경계</b>다.<br><br>

<b>(나)는 더 짧다.</b>
<span class="m">t = 1</span>이면 직선이 <span class="m">y = x</span>가 되므로
<span class="m">β(1)</span>은 <b>두 곡선의 교점의
<span class="m">x</span>좌표</b>다.
그 점을 <span class="m">a<sup>x</sup> + b = x</span>에 넣으면 끝이다.

## 풀이

<p><span class="step">① 조건 (가)로 b를 구한다.</span>
<span class="m">f</span>의 그래프가 <span class="m">x</span>축과 만나는 점은
두 교점의 바깥, 곧 로그 쪽이므로</p>
<p class="m">log<sub>a</sub>(x − b) = 0 → x = b + 1</p>
<p>직선 <span class="m">y = t(x − 1) + 1</span>의
<span class="m">x</span>절편은</p>
<p class="m">t(x − 1) + 1 = 0 → x = 1 − 1/t</p>
<p>두 절편이 같아질 때의 <span class="m">t</span>가 부호가 갈리는 경계
<span class="m">m</span>이고, (가)에서
<span class="m">m = 1</span>이므로</p>
<p class="m">1 − 1/1 = b + 1</p>
<p class="m">0 = b + 1 → b = −1</p>

<p><span class="step">② 조건 (나)로 a를 구한다.</span>
<span class="m">t = 1</span>이면 직선은</p>
<p class="m">y = 1 × (x − 1) + 1 = x</p>
<p>이므로 <span class="m">β(1)</span>은 두 곡선의 교점의
<span class="m">x</span>좌표다.
교점은 <span class="m">y = x</span> 위에 있으므로
<span class="m">a<sup>x</sup> + b = x</span>를 만족시킨다.
<span class="m">x = 3</span>, <span class="m">b = −1</span>을 넣으면</p>
<p class="m">a<sup>3</sup> − 1 = 3 → a<sup>3</sup> = 4</p>

<p><span class="step">③ 답을 만든다.</span></p>
<p class="m">16 × a<sup>3</sup> = 16 × 4 = 64</p>
<p class="m">답 64</p>

<p><span class="step">④ 확인한다.</span>
<span class="m">a = <sup>3</sup>√4 ≈ 1.587 &gt; 1</span>,
<span class="m">b = −1</span>이다.
<span class="m">a<sup>x</sup> − 1 = x</span>에
<span class="m">x = 0</span>을 넣으면
<span class="m">1 − 1 = 0</span>이므로
<b>작은 쪽 교점은 <span class="m">α(1) = 0</span></b>이다.</p>
<p class="m">α(1) = 0 &lt; 1 &lt; 3 = β(1)</p>
<p>회전축 <span class="m">(1, 1)</span>이 두 교점 사이에 있으므로
<b>모든 양수 <span class="m">t</span>에서 근이 두 개</b>라는 전제도 맞는다.
<span class="m">a + b = <sup>3</sup>√4 − 1 ≈ 0.59 &lt; 1</span>로도 같은 확인이 된다.</p>

## 함정

<b><span class="m">β(1) = 3</span>을 직선에 대입하지 않는다.</b>
<span class="m">β(1)</span>은 <b>직선과
<span class="m">y = f(x)</span>의 교점</b>이지만,
<span class="m">t = 1</span>일 때 그 직선이 하필
<span class="m">y = x</span>라서 <b>두 곡선의 교점</b>이기도 하다.
<span class="m">y = x</span>임을 알아채지 못하면
<span class="m">a</span>를 구할 식이 나오지 않는다.<br><br>

<b><span class="m">m = 1</span>이라고 해서 <span class="m">b = 0</span>이 아니다.</b>
<span class="m">m = −1/b</span>에서
<span class="m">1 = −1/b</span>, 곧
<span class="m">b = −1</span>이다.
<b>부호를 흘리면 <span class="m">b = 1</span>이 되고
정의역부터 틀어진다.</b><br><br>

<b><span class="m">a<sup>3</sup> = 4</span>에서 <span class="m">a</span>를 구하려 들지 않는다.</b>
묻는 것은 <span class="m">16 × a<sup>3</sup></span>이므로
<span class="m">a<sup>3</sup></span>만 있으면 된다.
<span class="m">a = <sup>3</sup>√4</span>를 꺼내는 순간 계산이 지저분해진다.
<b>묻는 꼴 그대로 두고 필요한 덩어리만 구한다.</b>

## 노하우

<b>역방향 문제는 &lsquo;조건 하나 = 미지수 하나&rsquo;로 번역한다.</b>
미지수가 <span class="m">a</span>, <span class="m">b</span> 둘이면
조건도 둘이어야 한다. 이 문항에서는</p>
<p class="m">(가) 부등식의 해 → b</p>
<p class="m">(나) 교점 하나 → a</p>
<p><b>어느 조건이 어느 미지수를 담당하는지 먼저 정하면
풀이가 두 줄로 끝난다.</b><br><br>

<b>모문항을 풀고 나면 반드시 결론을 한 줄로 적어 둔다.</b>
이 문항은 모문항에서</p>
<p class="m">m = −1/b, &nbsp; 교점은 y = x 위</p>
<p>를 챙겨 두었다면 <b>30초 문제</b>다.
챙겨 두지 않았다면 그림부터 다시 그려야 한다.
<b>답을 맞혔는지보다 무엇을 들고 나왔는지가 중요하다.</b><br><br>

<b>전제가 맞는지 끝에 확인한다.</b>
문제는 &lsquo;모든 양수 <span class="m">t</span>에 대하여 두 실근&rsquo;을
<b>이미 주어진 사실</b>로 깔아 두었다.
구한 <span class="m">a</span>, <span class="m">b</span>가
그 전제를 만족시키는지
<span class="m">a + b &lt; 1</span>로 확인하면
<b>계산 실수를 거의 다 잡아낸다.</b>
