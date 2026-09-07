# -*- coding: utf-8 -*-
"""수능완성 2회 10~22번 검증"""
from sympy import *
from fractions import Fraction as F
OK = []
def chk(n, got, want):
    OK.append((n, got, want, got == want))

# 10번  P: A(5) 출발 v1=t^2-2t / Q: B(0) 출발 v2=-t+2
t, u = symbols('t u', real=True)
xP = 5 + integrate(u**2 - 2*u, (u, 0, t))
xQ = 0 + integrate(-u + 2, (u, 0, t))
h = simplify(xP - xQ)                       # t^3/3 - t^2/2 - 2t + 5
cr = [c for c in solve(diff(h, t), t) if c.is_real and c >= 0]
# h 는 t>=0 에서 부호가 바뀌지 않으므로 |h| 의 최소는 h 의 극소에서 난다
assert all(h.subs(t, v) > 0 for v in [0, 1, 2, 3, 10]), "부호 확인"
a = min(cr, key=lambda v: h.subs(t, v))
# v1 = t(t-2) 는 (0,2) 에서 음, (2,4) 에서 양이므로 부호로 끊어 적분한다
dist = (integrate(2*u - u**2, (u, 0, 2)) + integrate(u**2 - 2*u, (u, 2, 2*a)))
chk("10", dist, Integer(8))

# 11번  f'(x)>=2 (x>1), [-1,1] 에서 f=2x^3-2x^2+5
x = symbols('x', real=True)
f0 = 2*x**3 - 2*x**2 + 5
assert diff(f0, x).subs(x, 1) == 2                 # x=1 에서 매끄럽게 이어진다
assert minimum(f0, x, Interval(-1, 1)) > 0          # [-1,1] 에서 x축 위
area = integrate(f0, (x, -1, 1)) + integrate(2*x + 3, (x, 1, 3))
chk("11", area, Rational(68, 3))

# 12번은 v12.py 에서 좌표로 전수 확인했다 (AB=AC=2, AD=1, AE=2CD, AE//BD, E-B-C 공선)
chk("12", "sqrt(7)/2", "sqrt(7)/2")

# 13번  f(0)=0, f'(0)=0, |f-f(1)| 이 꼭 한 점에서 미분불가
p, q, c, r = symbols('p q c r', real=True)
tot = 0
for g in [(x - 1)*(x - c)**3, (x - r)*(x - 1)**3]:
    fr = list(g.free_symbols - {x})[0]
    for v in solve(Eq(diff(g, x).subs(x, 0), 0), fr):   # g'(0)=0  (f 에 일차항이 없다)
        gg = g.subs(fr, v)
        if simplify(gg.subs(x, 1)) != 0 or gg == 0:
            continue
        f1 = -gg.subs(x, 0)                              # f(0)=0 -> f(1) = -g(0)
        tot += expand(gg.subs(x, -1) + f1)
chk("13", simplify(tot), Rational(56, 3))

# 14번  a_{n+1} = |a_n| - 1, a_m * sum = -55
s14 = 0
for N in range(1, 200):
    seq, cur = [], N
    for _ in range(120):
        seq.append(cur); cur = abs(cur) - 1
    run = 0
    for m in range(1, 101):
        run += seq[m-1]
        if m >= 10 and seq[m-1]*run == -55:
            s14 += m
chk("14", s14, 176)

# 15번  f(x) = ∫0^1 |t^3 - x t^2| dt,  g(x) = f(x+1/2) - f(x)
def fex(z):
    """f 를 조각식으로. 정의와 일치하는지 아래에서 확인한다."""
    if z <= 0:  return Rational(1,4) - z/3
    if z <= 1:  return z**4/6 - z/3 + Rational(1,4)
    return z/3 - Rational(1,4)
tt = symbols('tt', positive=True)
for z in [Rational(-1,2), Rational(0), Rational(3,10), Rational(3,4), Rational(1), Rational(3,2)]:
    assert simplify(integrate(tt**2*Abs(tt - z), (tt, 0, 1)) - fex(z)) == 0, z
G = lambda z: fex(z + Rational(1,2)) - fex(z)
# x <= -1/2 이면 g = -1/6, x >= 1 이면 g = 1/6 (상수) -> 부등식이 '<' 이므로 제외된다
assert G(Rational(-3,4)) == Rational(-1,6) and G(Rational(-1,2)) == Rational(-1,6)
assert G(Rational(5,4))  == Rational(1,6)  and G(Rational(1))    == Rational(1,6)
# (-1/2, 1) 안에서는 |g| < 1/6 인지 촘촘히 확인
worst = max(abs(G(Rational(k, 2000))) for k in range(-999, 2000))
assert worst < Rational(1,6), worst
al, be15 = Rational(-1,2), Rational(1)
chk("15", fex(al) + fex(be15/2), Rational(49, 96))

# 16, 17, 18
chk("16", [v for v in solve(Eq(log(x-2,3), log(-2*x+7,9)), x) if v > 2], [Integer(3)])
F17 = integrate(8*x**3 + 2*x + 5, x); C = solve(Eq(F17.subs(x,1) + Symbol('C'), 10), Symbol('C'))[0]
chk("17", F17.subs(x, 2) + C, Integer(48))
chk("18", Rational((20 - 1 + 3) - 10, 2), Integer(6))          # sum a_{k+1} = 2*sum b + 10

# 19번  (3/2)*sqrt(-x^2+ax) 의 세제곱근 중 자연수
s19 = 0
for A in range(1, 400):
    cnt = 0
    for n in range(1, 40):
        D = A*A - Rational(16, 9)*n**6                # x^2 - a x + (4/9)n^6 = 0
        if D > 0: cnt += 2
        elif D == 0: cnt += 1
    if cnt == 4: s19 += A
chk("19", s19, 575)

# 20번  f(x)g(x) 가 실수 전체에서 연속
A = symbols('A', real=True)
fL = lambda z: z - A
fR = lambda z: z**2 - 4*A
gL = lambda z: (z - 1)**2
gR = lambda z: -Rational(16,9)*z + A**2
def works(v):
    """a = v 일 때 두 분기점 x=1, x=a 에서 fg 의 좌·우극한이 같은가."""
    f_ = lambda z, side: (fL(z) if (z < 1 or (z == 1 and side < 0)) else fR(z)).subs(A, v)
    g_ = lambda z, side: (gL(z) if (z < v or (z == v and side < 0)) else gR(z)).subs(A, v)
    for b_ in (Integer(1), v):
        if simplify(f_(b_, -1)*g_(b_, -1) - f_(b_, +1)*g_(b_, +1)) != 0:
            return False
    return True
# 후보: 두 분기점 각각을 무해하게 만드는 a (아래 네 식의 근) 전부
cand = set()
for eq in (Eq(gR(1), 0), Eq(fR(A), 0), Eq(gL(1), gR(1)), Eq(fL(1), fR(1))):
    cand |= {v for v in solve(eq, A) if v.is_real}
cand |= {Rational(9,2), Rational(1)}
# 후보 밖에는 해가 없음을 확인 (촘촘한 격자에서 통과하는 값이 더 없는지)
extra = [Rational(k,6) for k in range(-60, 61) if Rational(k,6) not in cand and works(Rational(k,6))]
assert not extra, extra
tot20 = sum(v for v in sorted(cand) if works(v))
chk("20", Rational(tot20).p + Rational(tot20).q, 49)

# 21번  정사각형 PQSR, f(n) = alpha_n - beta_n
def f21(n): return Rational(2)**(n - 2**n) - Rational(2)**(-n - 2**n)
E = Rational(2)**6 * f21(1)/f21(2) * f21(4)/f21(3)
chk("21", Rational(E).p + Rational(E).q, 38)

# 22번  h(x) = f(x)/(x+1),  h(0)=h(1)=1 (0은 극대), h(2)=5 (극대)
A,B,Cc,D,E2 = symbols('A B C D E', real=True)
f22 = A*x**4 + B*x**3 + Cc*x**2 + D*x + E2
h22 = f22/(x + 1)
s = solve([Eq(f22.subs(x,0), 1), Eq(diff(f22,x).subs(x,0), 1),
           Eq(f22.subs(x,1), 2), Eq(f22.subs(x,2), 15),
           Eq(diff(f22,x).subs(x,2), 5)], [A,B,Cc,D,E2], dict=True)[0]
F22 = f22.subs(s)
H = simplify(F22/(x + 1))
assert s[A] < 0
assert simplify(diff(H,x).subs(x,0)) == 0 and simplify(diff(H,x).subs(x,2)) == 0
assert maximum(H, x, Interval.open(-1, 30)) == 5                  # t 의 최댓값 5
chk("22", abs(F22.subs(x, 3)), Integer(32))

for n, got, want, ok in OK:
    print(("%3s  %-14s %-14s %s" % (n, got, want, "일치" if ok else "★불일치★")))
print("맞은 개수", sum(1 for *_, o in OK if o), "/", len(OK))
