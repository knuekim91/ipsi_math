# -*- coding: utf-8 -*-
"""2027학년도 9월 모의평가 30문항을 units/ 아래 문항 파일로 생성한다. (1회성 시드)"""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "2027-09모평"
DATE = "2026-09-04"

P = []
def add(**kw): P.append(kw)

# ============================ 01-지수로그 ============================
add(id="EXP-001", unit="01-지수로그", topic="지수법칙", level="2점", diff="하", num=1,
    core="밑을 소수로 통일한 뒤 지수만 계산", tags="지수법칙,밑통일", answer="④",
    q='<p class="m">2<sup>3/2</sup> × 4<sup>−1/2</sup>의 값은?</p>'
      '<div class="choices"><span>① 2<sup>−1</sup></span><span>② 2<sup>−1/2</sup></span>'
      '<span>③ 1</span><span>④ 2<sup>1/2</sup></span><span>⑤ 2</span></div>',
    idea="4를 2<sup>2</sup>으로 바꾸는 순간 끝난다. 밑이 다른 채로 계산을 시작하지 않는다.",
    sol='<p class="m">4<sup>−1/2</sup> = (2<sup>2</sup>)<sup>−1/2</sup> = 2<sup>−1</sup></p>'
        '<p class="m">2<sup>3/2</sup> × 2<sup>−1</sup> = 2<sup>1/2</sup></p>',
    know="지수 계산은 <b>밑을 소수(素數)로 통일</b>한 뒤 지수만 더하고 뺀다.")

add(id="EXP-002", unit="01-지수로그", topic="로그방정식", level="3점", diff="중", num=16,
    core="밑 통일 → 진수 비교 → 진수>0 검산", tags="로그방정식,진수조건,무연근", answer="6",
    q='<p class="m">방정식 log<sub>3</sub>(x−3) = log<sub>9</sub>(2x−3)을 만족시키는 실수 x의 값을 구하시오.</p>',
    idea="log<sub>9</sub> = ½log<sub>3</sub>로 밑을 맞추고, <b>마지막에 반드시 진수 조건으로 거른다.</b> 무연근이 하나 나오도록 설계된 문제다.",
    sol='<p><span class="step">① 밑 통일.</span> <span class="m">2 log<sub>3</sub>(x−3) = log<sub>3</sub>(2x−3) → (x−3)<sup>2</sup> = 2x−3</span></p>'
        '<p><span class="step">② 정리.</span> <span class="m">x<sup>2</sup> − 8x + 12 = 0 → x = 2, 6</span></p>'
        '<p><span class="step">③ 진수 조건.</span> <span class="m">x − 3 &gt; 0</span>이므로 <span class="m">x = 6</span>.</p>',
    trap="<span class='m'>x=2</span>를 원식에 넣으면 <span class='m'>log<sub>3</sub>(−1)</span>. 제곱하는 순간 정보가 사라지므로 검산은 필수다.",
    know="로그방정식은 <b>① 밑 통일 → ② 진수 비교 → ③ 진수&gt;0 검산</b>의 3단계. 3단계를 빠뜨리면 답이 두 개가 된다.")

add(id="EXP-003", unit="01-지수로그", topic="지수함수와 수평선", level="4점", diff="중상", num=10,
    core="수평선 절단 → 가로 길이 = log_a(진수의 비)", tags="지수함수,로그의차,그래프", answer="③",
    q='<p class="m">상수 a (a&gt;1)에 대하여 직선 y = 7이 두 곡선 y = 16a<sup>x</sup>, y = ¼a<sup>x</sup>과 '
      '만나는 점을 각각 A, B라 하자. AB = 4일 때, a의 값은?</p>'
      '<div class="choices"><span>① √2</span><span>② 2</span><span>③ 2√2</span><span>④ 4</span><span>⑤ 4√2</span></div>',
    idea="두 점의 <span class='m'>y</span>좌표가 같으므로 AB는 순수하게 <span class='m'>x</span>좌표의 차이고, "
         "그 차는 <b>진수의 비의 로그</b>가 된다.",
    sol='<p class="m">16a<sup>x</sup> = 7 → x<sub>A</sub> = log<sub>a</sub>(7/16)</p>'
        '<p class="m">¼a<sup>x</sup> = 7 → x<sub>B</sub> = log<sub>a</sub>28</p>'
        '<p class="m">AB = log<sub>a</sub>(28 ÷ 7/16) = log<sub>a</sub>64 = 4</p>'
        '<p class="m">a<sup>4</sup> = 64 = 2<sup>6</sup> → a = 2<sup>3/2</sup> = 2√2</p>',
    know="지수함수를 수평선으로 자르면 <b>가로 길이 = log<sub>a</sub>(진수의 비)</b>. "
         "두 로그를 따로 계산하지 말고 처음부터 비로 묶는다.")

add(id="EXP-004", unit="01-지수로그", topic="지수·로그의 역함수 대칭", level="4점", diff="상", num=22,
    core="log_a(x+k)+k 는 y=a^x 를 직선 y=x+k 에 대칭시킨 것", tags="역함수,대칭이동,포물선의현", answer="97",
    q='<p>상수 <span class="m">a</span> (<span class="m">a&gt;1</span>)과 직사각형 ABCD가 다음 조건을 만족시킨다.</p>'
      '<span class="cond m">(가) 두 곡선 y = a<sup>x</sup>, y = 2x<sup>2</sup> − (7/2)x + 3은 모두 점 A와 점 B를 지난다.</span>'
      '<span class="cond m">(나) 두 곡선 y = log<sub>a</sub>(x − ¼) − ¼, y = 2x<sup>2</sup> − (15/2)x + 15/2는 모두 점 C와 점 D를 지난다.</span>'
      '<p><span class="m">a<sup>3</sup> = q/p</span>일 때 <span class="m">p+q</span>의 값을 구하시오. '
      '(<span class="m">p, q</span>는 서로소인 자연수)</p>',
    idea="<b>y = log<sub>a</sub>(x−¼) − ¼ 은 y = a<sup>x</sup>을 직선 y = x − ¼ 에 대칭이동한 곡선이다.</b> "
         "직사각형도 이 직선에 대해 대칭이므로 변 AB의 기울기가 1로 고정된다.",
    sol='<p><span class="step">① 대칭축.</span> <span class="m">y = x + k</span>에 대한 대칭은 <span class="m">(x,y) ↦ (y−k, x+k)</span>이고 '
        '<span class="m">y = a<sup>x</sup></span>을 <span class="m">y = log<sub>a</sub>(x+k)+k</span>로 보낸다. 비교하면 <span class="m">k = −¼</span>.</p>'
        '<p><span class="step">② 대칭이 강제하는 것.</span> D↦A, C↦B이므로 AD ⊥ 대칭축, 따라서 <b>AB의 기울기 = 1</b>.</p>'
        '<p><span class="step">③ 기울기 1인 현.</span> 현의 기울기 <span class="m">= 2(x<sub>A</sub>+x<sub>B</sub>) − 7/2 = 1 → x<sub>A</sub>+x<sub>B</sub> = 9/4</span>. '
        '같은 방법으로 <span class="m">x<sub>C</sub>+x<sub>D</sub> = 17/4</span>.</p>'
        '<p><span class="step">④ 두 식 연결.</span> <span class="m">x<sub>D</sub> = y<sub>A</sub>+¼, x<sub>C</sub> = y<sub>B</sub>+¼</span>이므로 '
        '<span class="m">y<sub>A</sub>+y<sub>B</sub> = 17/4 − ½ = 15/4</span>.</p>'
        '<p><span class="step">⑤ 근과 계수.</span> <span class="m">y<sub>A</sub>+y<sub>B</sub> = 33/4 − 4x<sub>A</sub>x<sub>B</sub> = 15/4 → x<sub>A</sub>x<sub>B</sub> = 9/8</span>, '
        '따라서 <span class="m">8t<sup>2</sup>−18t+9 = 0 → x<sub>A</sub> = 3/4, x<sub>B</sub> = 3/2</span>.</p>'
        '<p><span class="step">⑥ 마무리.</span> <span class="m">y<sub>A</sub> = 3/2</span>이므로 '
        '<span class="m">a<sup>3/4</sup> = 3/2 → a<sup>3</sup> = (3/2)<sup>4</sup> = 81/16</span>. '
        '네 점은 <span class="m">A(3/4,3/2), B(3/2,9/4), C(5/2,5/4), D(7/4,1/2)</span>. <span class="m">p+q = 97</span>.</p>',
    know="<b>log<sub>a</sub>(x+k)+k 꼴을 보면 즉시 &lsquo;y=a<sup>x</sup>을 y=x+k에 대칭시킨 것&rsquo;으로 읽는다.</b> "
         "대칭이 만드는 기울기 ±1을 찾으면, 포물선의 현은 <b>두 근의 합</b>으로 즉시 결정된다.")

# ============================ 02-삼각함수 ============================
add(id="TRI-001", unit="02-삼각함수", topic="삼각함수의 최대·주기", level="3점", diff="하", num=6,
    core="a sin(bx+c)+d 의 최대·최소·주기 즉답", tags="삼각함수,주기,최댓값", answer="⑤",
    q='<p class="m">두 양수 a, b에 대하여 함수 f(x) = a sin(x/b) + 2의 최댓값이 5이고 주기가 8π일 때, a+b의 값은?</p>'
      '<div class="choices"><span>① 6</span><span>② 25/4</span><span>③ 13/2</span><span>④ 27/4</span><span>⑤ 7</span></div>',
    idea="최댓값 = 진폭 + 평행이동, 주기 = 2π ÷ (x의 계수). 두 조건이 a와 b를 <b>따로</b> 결정한다.",
    sol='<p class="m">a + 2 = 5 → a = 3</p><p class="m">2πb = 8π → b = 4</p><p class="m">a + b = 7</p>',
    know="<b>y = a sin(bx+c)+d 는 최대 |a|+d, 최소 −|a|+d, 주기 2π/|b|</b>를 계산 없이 읽어낸다. "
         "a의 부호가 주어지지 않으면 절댓값을 잊지 않는다.")

add(id="TRI-002", unit="02-삼각함수", topic="외접원과 사인법칙", level="4점", diff="중상", num=12,
    core="같은 원의 현 = 2R sin(원주각)", tags="사인법칙,코사인법칙,외접원,원주각", answer="④ (4√2)",
    q='<p class="m">AB = 4, AC = 5, cos(∠BAC) = 1/8인 삼각형 ABC의 외접원에서 점 A를 포함하지 않는 호 BC 위에 점 D가 있다. '
      'sin(∠BCD) = √14/4일 때, 선분 BD의 길이는?</p>'
      '<div class="choices"><span>① 2√7</span><span>② 12√5/5</span><span>③ 7√10/4</span><span>④ 4√2</span><span>⑤ 9√10/5</span></div>',
    idea="점 D의 위치를 구하려 하지 않는다. <b>D와 A는 같은 원 위에 있으므로 외접원 반지름 R이 공유된다.</b> "
         "그러면 BD = 2R sin(∠BCD)로 한 줄에 끝난다.",
    sol='<p><span class="step">① 코사인법칙.</span> <span class="m">BC<sup>2</sup> = 16+25−2·4·5·(1/8) = 36 → BC = 6</span></p>'
        '<p><span class="step">② 외접원.</span> <span class="m">sin A = 3√7/8</span>, '
        '<span class="m">2R = BC / sin A = 16/√7</span></p>'
        '<p><span class="step">③ 삼각형 BCD에 사인법칙.</span> '
        '<span class="m">BD = 2R sin(∠BCD) = (16/√7)(√14/4) = 4√2</span></p>',
    trap="사각형 ABDC가 원에 내접하므로 <span class='m'>∠BDC = 180° − A</span>, 즉 <span class='m'>sin∠BDC = sin A</span>. "
         "D의 좌표를 잡으려 들면 계산이 폭발한다.",
    know="<b>&lsquo;외접원 위의 점&rsquo;은 2R을 두 번 쓰라는 신호.</b> 같은 원의 현은 언제나 <b>(현) = 2R·sin(원주각)</b>이다.")

add(id="TRI-003", unit="02-삼각함수", topic="삼각함수 그래프의 대칭", level="4점", diff="상", num=20,
    core="수평선과 코사인 곡선의 두 교점은 대칭축에 대해 대칭", tags="그래프대칭,교점,넓이비", answer="17",
    q='<p class="m">0 ≤ x ≤ 2π에서 f(x) = sin x, g(x) = −k cos x (k&gt;1). 두 곡선의 제1사분면 교점을 A, 제4사분면 교점을 B, '
      'A를 지나 x축에 평행한 직선이 y=g(x)와 만나는 A가 아닌 점을 C, B를 지나 x축에 평행한 직선이 y=g(x)와 만나는 B가 아닌 점을 D라 하자. '
      '(삼각형 CDB) : (삼각형 AOD) = 14 : 5일 때, A의 x좌표를 a라 하면 B, D의 x좌표는 각각 p(a), q(a)이고 a = α이다. '
      '3 × p(α)/q(α)의 값을 구하시오. (O는 원점)</p>',
    idea="A의 x좌표를 a라 두면 <b>y = −k cos x 는 x = π에 대해 대칭</b>이므로 같은 높이의 짝점이 "
         "2π−a, π−a로 즉시 나온다. B는 tan x = −k의 다음 해이므로 a+π.",
    sol='<p><span class="step">① 교점.</span> <span class="m">tan x = −k</span>의 첫 해 <span class="m">a ∈ (π/2, π)</span>, 다음 해 <span class="m">a+π</span>. '
        '→ <span class="m">B(a+π, −sin a)</span>, 즉 <span class="m">p(a) = a+π</span></p>'
        '<p><span class="step">② 대칭으로 C, D.</span> <span class="m">C(2π−a, sin a)</span>, <span class="m">D(π−a, −sin a)</span>, 즉 <span class="m">q(a) = π−a</span></p>'
        '<p><span class="step">③ 넓이.</span> <span class="m">DB = 2a</span>이므로 <span class="m">(CDB) = ½·2a·2sin a = 2a sin a</span>, '
        '<span class="m">(AOD) = ½|a(−sin a) − (π−a)(sin a)| = (π/2) sin a</span></p>'
        '<p><span class="step">④ 비.</span> <span class="m">(π/2)sin a = (5/14)(2a sin a)</span>에서 sin a가 약분되어 '
        '<span class="m">a = 7π/10 = α</span> (이때 <span class="m">k = −tan(7π/10) ≈ 1.376 &gt; 1</span> 만족)</p>'
        '<p class="m">3 × (7π/10 + π)/(π − 7π/10) = 3 × (17π/10)/(3π/10) = 17</p>',
    know="<b>수평선이 삼각함수 곡선을 자를 때 두 교점의 x좌표 합은 대칭축의 2배.</b> "
         "cos 계열의 대칭축은 x = 0, π, 2π. 넓이비에서는 sin a가 약분되어 각만 남는다.")

# ============================ 03-수열 ============================
add(id="SEQ-001", unit="03-수열", topic="등차수열", level="3점", diff="하", num=3,
    core="a_m = a_n + (m−n)d 로 직접 건너뛴다", tags="등차수열,공차", answer="②",
    q='<p class="m">등차수열 {a<sub>n</sub>}에 대하여 a<sub>2</sub> = 2, a<sub>10</sub> − a<sub>7</sub> = 9일 때, a<sub>7</sub>의 값은?</p>'
      '<div class="choices"><span>① 16</span><span>② 17</span><span>③ 18</span><span>④ 19</span><span>⑤ 20</span></div>',
    idea="a<sub>10</sub> − a<sub>7</sub>은 첫째항과 무관하게 3d다. 첨자 차이가 공차의 배수라는 것만 쓴다.",
    sol='<p class="m">3d = 9 → d = 3</p><p class="m">a<sub>7</sub> = a<sub>2</sub> + 5d = 2 + 15 = 17</p>',
    know="등차수열은 <b>a<sub>m</sub> = a<sub>n</sub> + (m−n)d</b>로 직접 건너뛴다. a<sub>1</sub>을 경유하면 계산이 두 배가 된다.")

add(id="SEQ-002", unit="03-수열", topic="등비수열", level="3점", diff="중", num=8,
    core="a₁을 약분해 r만의 방정식으로", tags="등비수열,부분합,근의선별", answer="③",
    q='<p class="m">모든 항이 양수인 등비수열 {a<sub>n</sub>}의 첫째항부터 제n항까지의 합을 S<sub>n</sub>이라 하자. '
      'S<sub>3</sub> / (a<sub>1</sub> + 2a<sub>2</sub>) = 7/3일 때, a<sub>8</sub>/a<sub>6</sub>의 값은?</p>'
      '<div class="choices"><span>① 4</span><span>② 9</span><span>③ 16</span><span>④ 25</span><span>⑤ 36</span></div>',
    idea="분자·분모를 a<sub>1</sub>로 묶으면 <b>a<sub>1</sub>이 약분되어 r만의 이차방정식</b>이 된다. 구하는 값도 r<sup>2</sup>이라 a<sub>1</sub>은 끝까지 불필요.",
    sol='<p class="m">(1 + r + r<sup>2</sup>)/(1 + 2r) = 7/3 → 3r<sup>2</sup> − 11r − 4 = 0 → (3r+1)(r−4) = 0</p>'
        '<p>모든 항이 양수이므로 <span class="m">r = 4</span>, 따라서 <span class="m">a<sub>8</sub>/a<sub>6</sub> = r<sup>2</sup> = 16</span></p>',
    trap="<span class='m'>r = −1/3</span>을 버리는 근거는 &lsquo;모든 항이 양수&rsquo;. 조건 문장 하나가 근을 거르는 장치다.",
    know="등비수열의 비율 조건은 <b>a<sub>1</sub>을 약분해 r만의 방정식</b>으로. 구하는 값이 a<sub>m</sub>/a<sub>n</sub>이면 답은 언제나 r<sup>m−n</sup>.")

add(id="SEQ-003", unit="03-수열", topic="귀납적 정의", level="3점", diff="하", num=18,
    core="항이 10개 이내면 나열이 최속", tags="귀납적정의,홀짝분기", answer="38",
    q='<p class="m">수열 {a<sub>n</sub>}은 a<sub>1</sub> = 28이고 모든 자연수 n에 대하여 '
      'a<sub>n+1</sub> = ½a<sub>n</sub> (a<sub>n</sub>이 짝수), 2a<sub>n</sub>+12 (a<sub>n</sub>이 홀수)를 만족시킬 때, '
      'a<sub>6</sub>의 값을 구하시오.</p>',
    idea="규칙을 분석하지 말고 다섯 번 계산한다.",
    sol='<p class="m">28(짝) → 14(짝) → 7(홀) → 26(짝) → 13(홀) → 38</p>',
    trap="<span class='m'>a<sub>3</sub>=7</span>은 홀수이므로 <span class='m'>2·7+12 = 26</span>. 매 항마다 짝·홀을 다시 판정하지 않으면 어긋난다.",
    know="<b>홀짝 분기 수열은 규칙을 찾는 문제가 아니라 정확히 나열하는 문제.</b> 각 항 옆에 (짝)/(홀)을 적어두면 실수가 사라진다.")

add(id="SEQ-004", unit="03-수열", topic="조건부 정의 함수의 급수", level="4점", diff="상", num=14,
    core="예외 항만 빼고 다시 더해 정수 판정을 분모 하나로 압축", tags="시그마,정수판정,완전세제곱", answer="⑤ (171)",
    q='<p class="m">실수 전체에서 정의된 함수 f(x) = 5 (x가 자연수가 아닌 경우), 1/x (x가 자연수인 경우)에 대하여, '
      'Σ<sub>k=1</sub><sup>n</sup> f(∛k)/(5f(k))의 값이 자연수가 되도록 하는 300 이하의 자연수 n의 개수는?</p>'
      '<div class="choices"><span>① 135</span><span>② 144</span><span>③ 153</span><span>④ 162</span><span>⑤ 171</span></div>',
    idea="k는 항상 자연수이므로 분모는 늘 5/k. 분자만 갈라지는데 <b>∛k가 자연수인 경우는 k가 완전세제곱일 때뿐</b>이다.",
    sol='<p><span class="step">① 항의 두 종류.</span> k가 완전세제곱이 아니면 항 = k, '
        '<span class="m">k = m<sup>3</sup></span>이면 항 <span class="m">= (1/m)÷(5/m<sup>3</sup>) = m<sup>2</sup>/5</span></p>'
        '<p><span class="step">② 합.</span> <span class="m">M = ⌊∛n⌋</span>일 때 '
        '<span class="m">S<sub>n</sub> = Σk − Σm<sup>3</sup> + (1/5)Σm<sup>2</sup></span>. '
        '앞 두 항은 정수이므로 <b>조건은 Σm<sup>2</sup>이 5의 배수인가</b>로 축소된다.</p>'
        '<p><span class="step">③ 판정.</span> <span class="m">Σ<sub>m=1</sub><sup>M</sup>m<sup>2</sup></span> = 1, 5, 14, 30, 55, 91 (M=1~6) → M = 2, 4, 5</p>'
        '<p><span class="step">④ 개수.</span> <span class="m">M=2: 8~26 (19개), M=4: 64~124 (61개), M=5: 125~215 (91개) → 171</span></p>',
    know="<b>&lsquo;자연수일 때만 다르게 정의된 함수&rsquo;는 예외 항을 통째로 빼고 다시 더한다.</b> "
         "그러면 정수 판정이 분모에 남는 항 하나로 압축되고, 남는 일은 구간별 개수 세기뿐이다.")

# ============================ 04-극한연속 ============================
add(id="LIM-001", unit="04-극한연속", topic="미분계수의 정의", level="2점", diff="하", num=2,
    core="(f(x)−f(a))/(x−a) 는 계산하지 말고 f′(a)로 읽는다", tags="미분계수,극한", answer="③",
    q='<p class="m">함수 f(x) = 2x<sup>3</sup> − x − 4에 대하여 lim<sub>x→2</sub> (f(x) − f(2))/(x − 2)의 값은?</p>'
      '<div class="choices"><span>① 19</span><span>② 21</span><span>③ 23</span><span>④ 25</span><span>⑤ 27</span></div>',
    idea="계산하는 극한이 아니라 <b>기호를 바꿔 읽는 극한</b>이다.",
    sol='<p class="m">f′(x) = 6x<sup>2</sup> − 1 → f′(2) = 23</p>',
    know="<b>(f(x)−f(a))/(x−a) 형태는 즉시 f′(a).</b> 변형형 (f(a+h)−f(a))/h 도 같다.")

add(id="LIM-002", unit="04-극한연속", topic="함수의 연속", level="3점", diff="하", num=4,
    core="구간별 정의 함수의 연속은 경계점만 본다", tags="연속,좌우극한", answer="②",
    q='<p class="m">함수 f(x) = 7x + a (x ≤ 2), x<sup>2</sup> + ax (x &gt; 2)가 실수 전체의 집합에서 연속일 때, 상수 a의 값은?</p>'
      '<div class="choices"><span>① 9</span><span>② 10</span><span>③ 11</span><span>④ 12</span><span>⑤ 13</span></div>',
    idea="다항식은 어디서나 연속이므로 확인할 점은 경계 x=2 하나뿐이다.",
    sol='<p class="m">14 + a = 4 + 2a → a = 10</p>',
    know="<b>구간별 정의 함수의 연속은 경계점만.</b> 등호가 붙은 쪽의 함숫값은 이미 정해져 있으니 맞출 것은 반대쪽 극한 하나다.")

add(id="LIM-003", unit="04-극한연속", topic="극한 존재 조건", level="4점", diff="상", num=15,
    core="분모의 근에서 분자도 같은 위수 이상으로 0 / 범위의 경계는 판별식=0", tags="극한존재,판별식,중근", answer="④ (10)",
    q='<p>최고차항의 계수가 1인 이차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킬 때 <span class="m">f(2)</span>의 값은?</p>'
      '<span class="cond m">모든 실수 a에 대하여 lim<sub>x→a</sub> (2x+1)f(x) / (f(x) + f(x−t))의 값이 존재하도록 하는 '
      '양수 t의 집합은 {t | t ≥ 3/2}이다.</span>'
      '<div class="choices"><span>① 5/2</span><span>② 5</span><span>③ 15/2</span><span>④ 10</span><span>⑤ 25/2</span></div>',
    idea="분모 D(x) = f(x)+f(x−t)는 이차식이다. <b>t가 커지면 판별식이 음수가 되어 극한이 자동으로 존재</b>하므로, "
         "t = 3/2 는 정확히 <b>판별식 = 0(중근)</b>인 경계다.",
    sol='<p><span class="step">① 분모.</span> <span class="m">f(x) = x<sup>2</sup>+bx+c</span>라 하면 '
        '<span class="m">D(x) = 2x<sup>2</sup> + 2(b−t)x + (t<sup>2</sup>−bt+2c)</span>, '
        '<span class="m">Δ = 4(b<sup>2</sup>−4c−t<sup>2</sup>)</span></p>'
        '<p><span class="step">② 경계.</span> <span class="m">b<sup>2</sup>−4c = (3/2)<sup>2</sup> = 9/4</span></p>'
        '<p><span class="step">③ 중근 처리.</span> 중근 <span class="m">r = (t−b)/2</span>에서 분자 <span class="m">(2x+1)f(x)</span>가 '
        '<span class="m">(x−r)<sup>2</sup></span>으로 나누어져야 한다. <span class="m">f = (x−r)<sup>2</sup></span>이면 '
        '<span class="m">b<sup>2</sup>−4c = 0</span>이라 모순이므로 <span class="m">2r+1 = 0</span>, 즉 <span class="m">r = −1/2</span>.</p>'
        '<p><span class="step">④ 상수.</span> <span class="m">(3/2−b)/2 = −1/2 → b = 5/2</span>, '
        '<span class="m">25/4 − 4c = 9/4 → c = 1</span></p>'
        '<p class="m">f(x) = x<sup>2</sup> + (5/2)x + 1 → f(2) = 10</p>'
        '<p><span class="step">⑤ 확인.</span> t &lt; 3/2 이면 서로 다른 두 실근이 모두 분자의 근 {−1/2, −2}여야 하는데 '
        '근의 합을 비교하면 t = 0 이 나와 불가능하다.</p>',
    know="<b>분수 극한의 존재 조건 = 분모의 근에서 분자도 같은 위수 이상으로 0.</b> "
         "그리고 <b>매개변수 범위가 부등식으로 주어지면 경계는 거의 항상 판별식 = 0</b>이다.")

# ============================ 05-미분 ============================
add(id="DIF-001", unit="05-미분", topic="극대·극소", level="3점", diff="하", num=7,
    core="f′(α)=0으로 미지수를 먼저 없애고 f′을 인수분해", tags="극값,삼차함수", answer="②",
    q='<p class="m">함수 f(x) = 2x<sup>3</sup> + ax<sup>2</sup> − 4ax가 x = 1에서 극소일 때, f(x)의 극댓값은? (단, a는 상수)</p>'
      '<div class="choices"><span>① 19</span><span>② 20</span><span>③ 21</span><span>④ 22</span><span>⑤ 23</span></div>',
    idea="극값 조건 f′(1)=0 하나로 a가 결정된다. 그 다음 f′을 인수분해하면 극대점이 바로 보인다.",
    sol='<p class="m">f′(x) = 6x<sup>2</sup>+2ax−4a, f′(1) = 6−2a = 0 → a = 3</p>'
        '<p class="m">f′(x) = 6(x+2)(x−1) → x = −2에서 극대</p>'
        '<p class="m">f(−2) = −16 + 12 + 24 = 20</p>',
    know="<b>삼차함수는 최고차 계수가 양수면 작은 근에서 극대, 큰 근에서 극소.</b>")

add(id="DIF-002", unit="05-미분", topic="속도와 가속도", level="4점", diff="중", num=9,
    core="위치·속도·가속도 세 줄을 먼저 다 쓴다", tags="속도,가속도,근의선별", answer="①",
    q='<p class="m">수직선 위를 움직이는 두 점 P, Q가 있다. 시각 t (t ≥ 0)일 때 두 점의 위치가 각각 '
      'x<sub>1</sub> = 4t<sup>3</sup> − t<sup>2</sup> − 11t, x<sub>2</sub> = 2t<sup>2</sup> + 7t + 3이다. '
      '두 점의 속도가 같아지는 순간 두 점의 가속도를 각각 p, q라 할 때, p − q의 값은?</p>'
      '<div class="choices"><span>① 30</span><span>② 33</span><span>③ 36</span><span>④ 39</span><span>⑤ 42</span></div>',
    idea="&lsquo;속도가 같아지는 순간&rsquo;은 v<sub>1</sub> = v<sub>2</sub>라는 방정식이고, t ≥ 0이 근을 걸러준다.",
    sol='<p class="m">v<sub>1</sub> = 12t<sup>2</sup>−2t−11, v<sub>2</sub> = 4t+7</p>'
        '<p class="m">2t<sup>2</sup>−t−3 = 0 → (2t−3)(t+1) = 0 → t = 3/2</p>'
        '<p class="m">p = 24t−2 = 34, q = 4 → p−q = 30</p>',
    know="운동 문제는 <b>위치·속도·가속도 세 줄을 먼저 다 써놓고</b> 시작한다. t ≥ 0은 근을 하나 버리라는 지시다.")

add(id="DIF-003", unit="05-미분", topic="접선의 방정식", level="3점", diff="중", num=19,
    core="접점 후보가 둘이면 반드시 추가 조건으로 거른다", tags="접선,후보선별", answer="15",
    q='<p class="m">기울기가 8이고 y절편이 양수인 직선이 곡선 y = x<sup>3</sup> − 3x<sup>2</sup> − x + 2에 접할 때, '
      '이 직선은 점 (1, k)를 지난다. k의 값을 구하시오.</p>',
    idea="f′(x) = 8 에서 접점 후보가 <b>두 개</b> 나온다. &lsquo;y절편이 양수&rsquo;가 하나를 버리라는 지시다.",
    sol='<p class="m">3x<sup>2</sup>−6x−1 = 8 → x<sup>2</sup>−2x−3 = 0 → x = 3, −1</p>'
        '<p><span class="m">x=3</span>: <span class="m">y = 8x − 25</span> (y절편 −25, 탈락)</p>'
        '<p><span class="m">x=−1</span>: <span class="m">y = 8x + 7</span> (y절편 7, 채택)</p>'
        '<p class="m">k = 8 + 7 = 15</p>',
    know="<b>접점 후보가 둘 이상이면 반드시 거른다.</b> 문제에 붙은 부호 조건(y절편이 양수, a&gt;1, 모든 항이 양수)은 예외 없이 그 필터다.")

add(id="DIF-004", unit="05-미분", topic="미분가능성과 절댓값", level="4점", diff="상", num=21,
    core="꺾이는 점 목록을 먼저 적고, 꺾임을 좌우 도함수의 차(뛰기) 하나로 관리", tags="미분가능성,절댓값,중근", answer="12",
    q='<p>최고차항의 계수가 1인 삼차함수 <span class="m">f(x)</span>가 다음 조건을 만족시킬 때, '
      '<span class="m">f(0)</span>의 최댓값과 최솟값의 곱을 구하시오.</p>'
      '<span class="cond m">(가) 방정식 f(x) = 0의 서로 다른 실근의 개수는 2이다.</span>'
      '<span class="cond m">(나) g(x) = −f(x) (f(x) ≥ 0), 7f(x) (f(x) &lt; 0)일 때, 어떤 실수 a에 대하여 '
      'h(x) = g(x) + |(x−1)(x−a)(x−4+a)| 가 실수 전체의 집합에서 미분가능하다.</span>',
    idea="<b>두 함수 모두 부호가 바뀌는 점에서만 꺾인다.</b> g는 f의 단순근 한 곳에서만 꺾이므로 |P|도 꺾이는 곳이 "
         "정확히 그 한 점이어야 하고(→ P는 중근을 가져야 함), 두 꺾임이 상쇄되어야 한다.",
    sol='<p><span class="step">① f의 모양.</span> 실근이 정확히 2개 → <span class="m">f(x) = (x−p)<sup>2</sup>(x−q)</span>, <span class="m">p ≠ q</span></p>'
        '<p><span class="step">② g의 꺾임.</span> 중근 p에서는 <span class="m">f′(p)=0</span>이라 미분가능. 단순근 q에서만 꺾이고 '
        '<span class="m">g′(q<sup>−</sup>) = 7f′(q), g′(q<sup>+</sup>) = −f′(q)</span> → 뛰기 <span class="m">= −8f′(q)</span></p>'
        '<p><span class="step">③ |P|의 꺾임.</span> 단순근에서만 꺾이므로 세 근 1, a, 4−a 중 둘이 겹쳐야 한다. '
        '<span class="m">a=2</span> → 단순근 <span class="m">x=1</span>; <span class="m">a=1 또는 3</span> → 단순근 <span class="m">x=3</span></p>'
        '<p><span class="step">④ 상쇄.</span> <span class="m">−8f′(q) + 2|P′(q)| = 0 → |P′(q)| = 4(q−p)<sup>2</sup></span></p>'
        '<p><span class="step">⑤ 계산.</span> <span class="m">q=1, |P′(1)|=1 → p = ½, 3/2 → f(0) = −¼, −9/4</span><br>'
        '<span class="m">q=3, |P′(3)|=4 → p = 2, 4 → f(0) = −12, −48</span></p>'
        '<p class="m">최댓값 −¼, 최솟값 −48 → 곱 = 12</p>',
    know="<b>절댓값·구간별 정의 함수의 미분가능성은 &lsquo;꺾이는 점의 목록&rsquo;에서 시작한다.</b> "
         "꺾임을 <b>좌우 도함수의 차이(뛰기)</b>라는 하나의 수로 관리하면 킬러가 일차방정식으로 줄어든다. "
         "부호가 바뀌지 않는 중근에서는 애초에 꺾이지 않는다.")

# ============================ 06-적분 ============================
add(id="INT-001", unit="06-적분", topic="정적분 계산", level="3점", diff="하", num=5,
    core="아래끝이 0이면 대입은 위끝 한 번", tags="정적분", answer="①",
    q='<p class="m">∫<sub>0</sub><sup>2</sup> (2x<sup>3</sup> + 6x<sup>2</sup> − x) dx의 값은?</p>'
      '<div class="choices"><span>① 22</span><span>② 24</span><span>③ 26</span><span>④ 28</span><span>⑤ 30</span></div>',
    idea="그대로 계산한다. 30초 안에 끝내고 시간을 뒤로 넘긴다.",
    sol='<p class="m">[x<sup>4</sup>/2 + 2x<sup>3</sup> − x<sup>2</sup>/2]<sub>0</sub><sup>2</sup> = 8 + 16 − 2 = 22</p>',
    know="아래끝이 0이면 <b>대입은 위끝 한 번뿐</b>이다.")

add(id="INT-002", unit="06-적분", topic="부정적분과 초기조건", level="3점", diff="하", num=17,
    core="적분상수를 먼저 확정한 뒤 값을 대입", tags="부정적분,적분상수", answer="11",
    q='<p class="m">다항함수 f(x)에 대하여 f′(x) = 6x<sup>2</sup> − 2x이고 f(0) = 10일 때, f(1)의 값을 구하시오.</p>',
    idea="적분 → 상수 확정 → 대입의 순서를 지킨다.",
    sol='<p class="m">f(x) = 2x<sup>3</sup> − x<sup>2</sup> + C, f(0) = C = 10</p><p class="m">f(1) = 2 − 1 + 10 = 11</p>',
    know="<b>적분상수는 반드시 먼저 확정한 뒤 값을 대입한다.</b> 순서를 바꾸면 C를 빠뜨린다.")

add(id="INT-003", unit="06-적분", topic="적분방정식", level="4점", diff="중상", num=11,
    core="∫ₐˣ 꼴은 ① x=a 대입 ② 양변 미분, 이 두 개가 전부", tags="적분방정식,곱미분", answer="③",
    q='<p class="m">다항함수 f(x)가 모든 실수 x에 대하여 '
      '∫<sub>−1</sub><sup>x</sup> f(t) dt = x f(x) − 2x<sup>3</sup> − 3x<sup>2</sup> + 6을 만족시킬 때, f(0)의 값은?</p>'
      '<div class="choices"><span>① 6</span><span>② 7</span><span>③ 8</span><span>④ 9</span><span>⑤ 10</span></div>',
    idea="적분방정식에 쓸 수 있는 동작은 두 개뿐이다 — <b>아래끝 대입</b>과 <b>양변 미분</b>. 이 문제는 둘 다 쓴다.",
    sol='<p><span class="step">① 양변 미분.</span> <span class="m">f(x) = f(x) + xf′(x) − 6x<sup>2</sup> − 6x → f′(x) = 6x + 6</span></p>'
        '<p class="m">f(x) = 3x<sup>2</sup> + 6x + C</p>'
        '<p><span class="step">② x = −1 대입.</span> 좌변이 0이므로 '
        '<span class="m">0 = −f(−1) + 2 − 3 + 6 → f(−1) = 5</span></p>'
        '<p class="m">3 − 6 + C = 5 → C = 8 → f(0) = 8</p>',
    know="<b>∫<sub>a</sub><sup>x</sup> 꼴이 보이면 반사적으로 두 줄을 쓴다: &lsquo;x = a 대입&rsquo;과 &lsquo;양변 미분&rsquo;.</b> "
         "미분은 함수의 형태를, 대입은 상수를 준다.")

add(id="INT-004", unit="06-적분", topic="절댓값 정적분과 존재성", level="4점", diff="중상", num=13,
    core="부호가 안 바뀌는 경우가 최솟값 / 존재성은 연속성+중간값", tags="절댓값적분,대칭,중간값정리,보기", answer="⑤ (ㄱ,ㄴ,ㄷ)",
    q='<p>최고차항의 계수가 6인 이차함수 <span class="m">f(x)</span>가 <span class="m">f(0) = 0</span>, '
      '<span class="m">∫<sub>0</sub><sup>2</sup> f(x) dx = 4</span>를 만족시킨다. &lt;보기&gt;에서 옳은 것만을 있는 대로 고른 것은?</p>'
      '<span class="cond m">ㄱ. ∫<sub>0</sub><sup>2</sup> |f(x)| dx = 6</span>'
      '<span class="cond m">ㄴ. g(1) = 0인 일차함수 g(x)에 대하여 ∫<sub>0</sub><sup>2</sup> (f(x)+g(x)) dx = 4이다.</span>'
      '<span class="cond m">ㄷ. k &gt; 6인 각각의 실수 k에 대하여, ∫<sub>0</sub><sup>2</sup>(f(x)+h(x))dx = 4와 '
      '∫<sub>0</sub><sup>2</sup>|f(x)+h(x)|dx = k를 동시에 만족시키는 일차함수 h(x)가 존재한다.</span>'
      '<div class="choices"><span>① ㄱ</span><span>② ㄱ, ㄴ</span><span>③ ㄱ, ㄷ</span><span>④ ㄴ, ㄷ</span><span>⑤ ㄱ, ㄴ, ㄷ</span></div>',
    idea="f를 먼저 확정하고, ㄴ은 <b>x=1에 대한 대칭으로 적분이 0</b>임을 보고, ㄷ은 값을 만들지 말고 <b>연속성 + 중간값</b>으로 처리한다.",
    sol='<p><span class="step">① f 결정.</span> <span class="m">f(x) = 6x<sup>2</sup>+bx</span>, <span class="m">16+2b = 4 → b = −6</span>, '
        '<span class="m">f(x) = 6x(x−1)</span></p>'
        '<p><span class="step">② ㄱ.</span> <span class="m">−∫<sub>0</sub><sup>1</sup>f = 1, ∫<sub>1</sub><sup>2</sup>f = 5 → 6</span> (참)</p>'
        '<p><span class="step">③ ㄴ.</span> <span class="m">g(x) = m(x−1)</span>이고 구간 [0,2]는 x=1에 대칭이므로 '
        '<span class="m">∫<sub>0</sub><sup>2</sup>g = 0</span> (참)</p>'
        '<p><span class="step">④ ㄷ.</span> 같은 이유로 <span class="m">h(x) = p(x−1)</span>, '
        '<span class="m">f+h = (x−1)(6x+p)</span>. '
        '<span class="m">F(p) = ∫<sub>0</sub><sup>2</sup>|(x−1)(6x+p)|dx</span>는 '
        '<span class="m">F(−6) = 4, F(0) = 6, F(10) = 16</span>이고 p → ∞이면 F → ∞. '
        'F가 연속이므로 중간값 정리에 의해 6보다 큰 모든 k가 실현된다 (참)</p>',
    trap="<span class='m'>p = −6</span>이면 <span class='m'>f+h = 6(x−1)<sup>2</sup></span>로 부호가 바뀌지 않아 F = 4가 최소. "
         "&lsquo;부호가 안 바뀌는 순간&rsquo;이 절댓값 적분의 극단값이다.",
    know="<b>① 절댓값 적분은 부호가 안 바뀌는 경우를 먼저 찾는다(= 최솟값). "
         "② 대칭 구간에서 대칭점을 지나는 일차함수의 적분은 0. "
         "③ &lsquo;모든 k에 대해 존재하는가&rsquo;는 연속성 + 중간값으로 답한다.</b>")

# ============================ 07-경우의수확률 ============================
add(id="PRB-001", unit="07-경우의수확률", topic="같은 것이 있는 순열", level="2점", diff="하", num=23,
    core="n!/(p!q!)", tags="순열,중복", answer="①",
    q='<p class="m">다섯 개의 숫자 1, 2, 3, 3, 3을 모두 일렬로 나열하는 경우의 수는?</p>'
      '<div class="choices"><span>① 20</span><span>② 24</span><span>③ 28</span><span>④ 32</span><span>⑤ 36</span></div>',
    idea="같은 것의 중복도로 나눈다.", sol='<p class="m">5!/3! = 20</p>',
    know="같은 것이 p개, q개면 <b>n!/(p!q!)</b>. 중복도를 세는 것을 잊지 않는다.")

add(id="PRB-002", unit="07-경우의수확률", topic="조건부확률", level="3점", diff="하", num=24,
    core="P(A∩B) = P(A)P(B|A) 를 곱셈 공식으로", tags="조건부확률,여사건", answer="④",
    q='<p class="m">두 사건 A, B에 대하여 P(B|A) = 2/3, P(A<sup>C</sup>) = 2/5일 때, P(A∩B)의 값은?</p>'
      '<div class="choices"><span>① 1/10</span><span>② 1/5</span><span>③ 3/10</span><span>④ 2/5</span><span>⑤ 1/2</span></div>',
    idea="조건부확률의 정의를 곱셈 형태로 뒤집는다.",
    sol='<p class="m">P(A) = 3/5, P(A∩B) = (3/5)(2/3) = 2/5</p>',
    know="<b>P(A∩B) = P(A)P(B|A)</b>는 분수식이 아니라 곱셈 공식으로 외운다. 여사건이 주어지면 먼저 P(A)로 되돌린다.")

add(id="PRB-003", unit="07-경우의수확률", topic="이항정리", level="3점", diff="하", num=25,
    core="지수 방정식으로 r 결정 후 계수 한 번만 계산", tags="이항정리,일반항", answer="⑤",
    q='<p class="m">(2x<sup>3</sup> + 1/x<sup>2</sup>)<sup>4</sup>의 전개식에서 x<sup>2</sup>의 계수는?</p>'
      '<div class="choices"><span>① 8</span><span>② 12</span><span>③ 16</span><span>④ 20</span><span>⑤ 24</span></div>',
    idea="일반항을 쓰고 <b>지수만 방정식으로</b> 놓는다.",
    sol='<p class="m">일반항 = <sub>4</sub>C<sub>r</sub> 2<sup>4−r</sup> x<sup>12−5r</sup></p>'
        '<p class="m">12 − 5r = 2 → r = 2 → <sub>4</sub>C<sub>2</sub>·2<sup>2</sup> = 24</p>',
    know="이항정리는 <b>지수 방정식 → r 결정 → 계수 계산</b>의 세 단계. 전개를 시작하는 순간 지는 문제다.")

add(id="PRB-004", unit="07-경우의수확률", topic="합사건의 확률", level="3점", diff="중", num=26,
    core="포함배제, 배수 조건은 소인수로 쪼개 본다", tags="합사건,포함배제,배수", answer="②",
    q='<p class="m">한 개의 주사위를 두 번 던져 나오는 눈의 수를 차례로 a, b라 하자. '
      'a가 3 이하이거나 a×b가 8의 배수일 확률은?</p>'
      '<div class="choices"><span>① 5/9</span><span>② 11/18</span><span>③ 2/3</span><span>④ 13/18</span><span>⑤ 7/9</span></div>',
    idea="&lsquo;또는&rsquo;은 포함배제. 두 번째 사건은 개수가 적으니 a별로 b를 센다.",
    sol='<p><span class="step">① a ≤ 3:</span> <span class="m">3 × 6 = 18</span></p>'
        '<p><span class="step">② 8 | ab:</span> <span class="m">a=2(b=4), a=4(b=2,4,6), a=6(b=4)</span> → 5</p>'
        '<p><span class="step">③ 교집합:</span> <span class="m">(2,4)</span> 하나</p>'
        '<p class="m">(18 + 5 − 1)/36 = 11/18</p>',
    trap="a=6일 때 6b가 8의 배수이려면 4|3b, 즉 4|b → b=4만. b=2는 12라서 안 된다.",
    know="<b>P(A∪B) = P(A)+P(B)−P(A∩B)의 실수는 언제나 마지막 항에서 난다.</b> "
         "배수 조건은 소인수로 쪼개 <span class='m'>2<sup>3</sup>|ab</span>처럼 보면 누락이 사라진다.")

add(id="PRB-005", unit="07-경우의수확률", topic="조건부확률과 상태 추적", level="4점", diff="상", num=28,
    core="시행 3~4회는 상태 전이표로 압축 / 같은 문자끼리의 교환은 아무 일도 아님", tags="조건부확률,상태전이,시행", answer="⑤ (69/371)",
    q='<p>문자 A가 적힌 3장의 카드와 문자 B가 적힌 3장의 카드가 1번째 자리에서부터 차례로 A, A, A, B, B, B가 보이도록 놓여 있다. '
      '이 6장의 카드와 한 개의 주사위를 사용하여 다음 시행을 한다.</p>'
      '<span class="cond">주사위를 한 번 던져 나온 눈의 수가 <span class="m">k</span>일 때, '
      '<span class="m">k ≤ 5</span>이면 <span class="m">k</span>번째 자리의 카드와 <span class="m">(k+1)</span>번째 자리의 카드를 서로 바꾸어 놓고, '
      '<span class="m">k = 6</span>이면 6장의 카드를 그대로 둔다.</span>'
      '<p>이 시행을 4번 반복한 후 6장의 카드가 1번째 자리에서부터 차례로 A, A, A, B, B, B가 보이도록 놓여 있을 때, '
      '3번째 시행에서 나온 눈의 수가 6일 확률은?</p>'
      '<div class="choices"><span>① 71/373</span><span>② 69/373</span><span>③ 73/371</span><span>④ 71/371</span><span>⑤ 69/371</span></div>',
    idea="나열하지 말고 <b>도달 가능한 배열이 몇 개인지</b> 본다. 4번의 시행으로는 거리 2 이내의 상태에만 갈 수 있어 "
         "관리할 상태는 <b>네 개</b>뿐이다.",
    sol='<p><span class="step">① 전이.</span> <span class="m">S<sub>0</sub></span> = AAABBB에서 k=1,2(A,A), k=4,5(B,B), k=6은 <b>변화 없음</b>. '
        'k=3만 배열을 바꾼다. → <span class="m">S<sub>0</sub>→S<sub>0</sub>: 5, S<sub>0</sub>→S<sub>1</sub>: 1</span></p>'
        '<p><span class="step">②</span> <span class="m">S<sub>1</sub></span> = AABABB에서 '
        '<span class="m">S<sub>1</sub>→S<sub>1</sub>: 3, →S<sub>0</sub>: 1, →S<sub>2</sub>: 1, →S<sub>3</sub>: 1</span></p>'
        '<p><span class="step">③ 2회 후.</span> <span class="m">S<sub>0</sub>: 26, S<sub>1</sub>: 8, S<sub>2</sub>: 1, S<sub>3</sub>: 1</span></p>'
        '<p><span class="step">④ 남은 2회로 복귀.</span> <span class="m">S<sub>0</sub>: 26, S<sub>1</sub>: 8, S<sub>2</sub>: 1, S<sub>3</sub>: 1</span></p>'
        '<p><span class="step">⑤ 분모.</span> <span class="m">26·26 + 8·8 + 1 + 1 = 742</span></p>'
        '<p><span class="step">⑥ 분자.</span> 3번째가 6이면 상태 유지 → 4번째 한 번에 복귀해야 한다. '
        '<span class="m">26×5 + 8×1 = 138</span></p>'
        '<p class="m">138/742 = 69/371</p>',
    know="<b>시행 횟수가 3~4회인 확률 문제는 상태 전이표로 끝난다.</b> "
         "특히 <b>같은 문자끼리의 교환은 아무 일도 일어나지 않는다</b>는 관찰이 6가지 분기를 2가지로 줄인다. "
         "조건부확률은 같은 표를 <b>분모 → 분자</b> 순으로 두 번 읽는다.")

add(id="PRB-006", unit="07-경우의수확률", topic="중복조합과 여사건", level="4점", diff="중상", num=29,
    core="부등식 조건은 전체 − 위반 / 하한은 치환으로 표준형 복귀", tags="중복조합,여사건,치환", answer="190",
    q='<p>다음 조건을 만족시키는 자연수 <span class="m">a, b, c, d</span>의 모든 순서쌍 '
      '<span class="m">(a, b, c, d)</span>의 개수를 구하시오.</p>'
      '<span class="cond m">(가) a + b + c + d = 14</span>'
      '<span class="cond m">(나) 10a ≥ d 이고 c &lt; d<sup>2</sup>이다.</span>',
    idea="두 부등식을 직접 만족시키려 하지 말고 <b>위반하는 경우를 센다.</b> "
         "10a &lt; d 는 d ≥ 11이 필요하고, c ≥ d<sup>2</sup>은 d ≤ 3에서만 가능하다.",
    sol='<p><span class="step">① 전체.</span> <span class="m"><sub>13</sub>C<sub>3</sub> = 286</span></p>'
        '<p><span class="step">② 위반 1 (10a &lt; d).</span> <span class="m">d ≥ 11</span> → <span class="m">(1,1,1,11)</span> 하나</p>'
        '<p><span class="step">③ 위반 2 (c ≥ d<sup>2</sup>).</span> '
        '<span class="m">d=1: <sub>12</sub>C<sub>2</sub> = 66, d=2(c≥4): <sub>8</sub>C<sub>2</sub> = 28, '
        'd=3(c≥9): <sub>2</sub>C<sub>2</sub> = 1</span> → 95</p>'
        '<p><span class="step">④ 겹침.</span> <span class="m">(1,1,1,11)</span>은 <span class="m">c=1 &lt; 121</span>이라 겹치지 않음 → 0</p>'
        '<p class="m">286 − 1 − 95 = 190</p>',
    know="<b>부등식이 붙은 방정식의 해 개수는 &lsquo;전체 − 위반&rsquo;이 거의 항상 빠르다.</b> "
         "c ≥ 4 같은 하한은 <span class='m'>c′ = c−3</span> 치환으로 표준 중복조합으로 되돌린다. "
         "마지막에 <b>두 위반이 겹치는지</b> 반드시 확인한다.")

# ============================ 08-통계 ============================
add(id="STA-001", unit="08-통계", topic="정규분포 표준화", level="3점", diff="중상", num=27,
    core="구간 길이가 고정이면 표에서 차를 맞추고, 부호는 1/σ>0이 결정", tags="정규분포,표준화,표읽기", answer="③ (0.0668)",
    q='<p class="m">정규분포 N(1, σ<sup>2</sup>)을 따르는 확률변수 X에 대하여 P((3/2)σ ≤ X ≤ 2σ) = 0.044일 때, '
      'P(X ≥ 10/7)의 값을 표준정규분포표를 이용하여 구한 것은? (단, σ는 양수)</p>'
      '<p class="m">[표] P(0≤Z≤0.5)=0.1915, P(0≤Z≤1.0)=0.3413, P(0≤Z≤1.5)=0.4332, '
      'P(0≤Z≤2.0)=0.4772, P(0≤Z≤2.5)=0.4938</p>'
      '<div class="choices"><span>① 0.0062</span><span>② 0.0228</span><span>③ 0.0668</span>'
      '<span>④ 0.1587</span><span>⑤ 0.3085</span></div>',
    idea="표준화하면 구간이 <span class='m'>[1.5 − 1/σ, 2 − 1/σ]</span>로 <b>길이가 항상 0.5</b>다. "
         "그러니 <b>표에서 차가 0.044인 이웃 두 값</b>을 먼저 찾는다.",
    sol='<p><span class="step">① 표준화.</span> <span class="m">P(1.5 − 1/σ ≤ Z ≤ 2 − 1/σ) = 0.044</span></p>'
        '<p><span class="step">② 표에서 거꾸로.</span> <span class="m">0.4772 − 0.4332 = 0.0440</span> → z가 1.5에서 2.0까지</p>'
        '<p><span class="step">③ 부호 결정.</span> <span class="m">1/σ &gt; 0</span>이므로 구간은 음의 쪽 '
        '<span class="m">[−2, −1.5]</span>. → <span class="m">1.5 − 1/σ = −2 → σ = 2/7</span></p>'
        '<p class="m">P(X ≥ 10/7) = P(Z ≥ 1.5) = 0.5 − 0.4332 = 0.0668</p>',
    trap="<span class='m'>1/σ = 0</span>도 수치상 0.044를 만들지만 σ가 존재하지 않는다. "
         "정규분포에서 <b>표 값이 같은 구간은 항상 좌우 두 개</b>다.",
    know="<b>미지수가 σ에 들어 있으면 표준화 후 &lsquo;구간의 길이&rsquo;를 먼저 본다.</b> "
         "길이가 고정이면 표에서 차를 맞추는 문제로 바뀌고, 남는 일은 부호를 정하는 것뿐이다.")

add(id="STA-002", unit="08-통계", topic="표본평균과 이차모멘트", level="4점", diff="중상", num=30,
    core="Σk²P(X=k) = E(X²) = V(X) + {E(X)}²", tags="표본평균,분산,이차모멘트", answer="170",
    q='<p class="m">숫자 0, 1, 2가 각각 하나씩 적혀 있는 세 개의 공이 들어 있는 주머니가 있다. 이 주머니에서 임의로 한 개의 공을 '
      '꺼내어 공에 적혀 있는 수를 확인한 후 다시 넣는 시행을 한다. 이 시행을 5번 반복하여 확인한 5개의 수의 평균을 X̄라 할 때, '
      'Σ<sub>k=1</sub><sup>10</sup> (k<sup>2</sup> × P(X̄ = k/5)) = a이다. 6 × a의 값을 구하시오.</p>',
    idea="<span class='m'>X̄ = k/5</span>는 <b>합이 k</b>라는 뜻. 구하는 합은 <b>E(S<sup>2</sup>)</b> 그 자체이고 "
         "<span class='m'>E(S<sup>2</sup>) = V(S) + E(S)<sup>2</sup></span>로 한 줄에 끝난다.",
    sol='<p><span class="step">① 기호 바꾸기.</span> 5개의 합을 S라 하면 <span class="m">a = Σk<sup>2</sup>P(S=k) = E(S<sup>2</sup>)</span> '
        '(k=0 항은 0)</p>'
        '<p><span class="step">② 한 번 뽑을 때.</span> <span class="m">m = 1, E(X<sup>2</sup>) = 5/3, V(X) = 2/3</span></p>'
        '<p><span class="step">③ 합.</span> <span class="m">E(S) = 5, V(S) = 5 × 2/3 = 10/3</span></p>'
        '<p class="m">a = 10/3 + 25 = 85/3 → 6a = 170</p>',
    know="<b>Σk<sup>2</sup>P(X=k)가 보이면 확률을 하나씩 구하지 않는다 — 정의상 E(X<sup>2</sup>)이고 "
         "E(X<sup>2</sup>) = V(X) + {E(X)}<sup>2</sup>.</b> "
         "표본평균 문제는 대부분 E(X̄)=m, V(X̄)=σ<sup>2</sup>/n 두 줄과 이 항등식으로 끝난다.")

# ============================ 파일 쓰기 ============================
TPL = """---
id: {id}
unit: {unit}
topic: {topic}
level: {level}
difficulty: {diff}
source: {src} {num}번
core: "{core}"
tags: [{tags}]
status: seed
added: {date}
answer: {answer}
---

## 문제

{q}

## 발상

{idea}

## 풀이

{sol}
{trap_block}
## 노하우

{know}
"""

n = 0
for p in P:
    trap = p.get("trap", "")
    trap_block = f"\n## 함정\n\n{trap}\n" if trap else ""
    out = TPL.format(src=SRC, date=DATE, trap_block=trap_block, **{
        k: p.get(k, "") for k in
        ("id", "unit", "topic", "level", "diff", "num", "core", "tags", "answer", "q", "idea", "sol", "know")
    })
    d = os.path.join(ROOT, "units", p["unit"], "problems")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, p["id"] + ".md"), "w", encoding="utf-8") as f:
        f.write(out)
    n += 1

print(f"{n}개 문항 생성 완료")
