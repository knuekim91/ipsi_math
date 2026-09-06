# -*- coding: utf-8 -*-
"""나은이가 가져온 3문항 검증"""
import io, itertools
from sympy import (symbols, Rational, solve, simplify, expand, Poly, nsolve,
                   S, diff, real_roots, Symbol, factor, nsimplify)

x = Symbol('x')
OUT = []
def say(*a): OUT.append(" ".join(str(t) for t in a))

# ══════════════════════════════════════════════════════════
# A. 2019학년도 6월 평가원 나형 30번
#    사차함수, (가) Σ_{k=1}^n f(k)=f(n)f(n+1) (n=1..5)
#    (나) n=3,4 에서 [n, n+2] 평균변화율 ≤ 0.  128 f(5/2) = ?
# ══════════════════════════════════════════════════════════
say("=" * 60)
say("[A] 2019 6월 나형 30번")
a, b, c, d, e = symbols('a b c d e')
f = a*x**4 + b*x**3 + c*x**2 + d*x + e
F = lambda t: f.subs(x, t)

# n=1 : f(1)(1-f(2))=0  -> f(1)=0  또는 f(2)=1
# n=2..5 : f(n)[f(n+1)-f(n-1)-1]=0
sols = []
for c1 in [0, 1]:                       # 0: f(1)=0 , 1: f(2)=1
    for pick in itertools.product([0, 1], repeat=4):   # n=2,3,4,5
        eqs = [F(1) if c1 == 0 else F(2) - 1]
        for i, n in enumerate([2, 3, 4, 5]):
            eqs.append(F(n) if pick[i] == 0 else F(n+1) - F(n-1) - 1)
        sol = solve(eqs, [a, b, c, d, e], dict=True)
        for s in sol:
            g = f.subs(s)
            free = g.free_symbols - {x}
            if free:                    # 미결정 파라미터가 남으면 건너뜀
                continue
            if g.coeff(x, 4) == 0:      # 사차함수가 아니면 탈락
                continue
            # 원래 조건 (가)를 직접 재확인
            G = lambda t: g.subs(x, t)
            ok = all(simplify(sum(G(k) for k in range(1, n+1)) - G(n)*G(n+1)) == 0
                     for n in range(1, 6))
            if not ok:
                continue
            # (나) 평균변화율 ≤ 0
            na = all(simplify((G(n+2) - G(n))/2) <= 0 for n in [3, 4])
            sols.append((expand(g), na, c1, pick))

seen = set()
for g, na, c1, pick in sols:
    if g in seen:
        continue
    seen.add(g)
    G = lambda t: g.subs(x, t)
    say("  후보 f(x) =", g)
    say("      f(1..6) =", [G(k) for k in range(1, 7)])
    say("      (나) 평균변화율 n=3:", (G(5)-G(3))/2, " n=4:", (G(6)-G(4))/2,
        " -> 조건", "만족" if na else "불만족")
    if na:
        say("      ★ 128 * f(5/2) =", 128*G(Rational(5, 2)))

# ══════════════════════════════════════════════════════════
# B. 2021학년도 수능 나형 30번
# ══════════════════════════════════════════════════════════
say("=" * 60)
say("[B] 2021 수능 나형 30번")
r, m, k = symbols('r m k', real=True)
# h(0)=0 -> |f(0)-g(0)|=0 -> p(0)=0, 그리고 x=0<1 이라 |p| 미분가능 -> 중근
p = x**2*(x - r)                      # p = f - g, 최고차 1
g_ = m*(x - 1) + k                    # g(1)=k, g'=m
# x=1 에서 연속 / 미분  (p(1)<0 인 경우: r>1)
e1 = -p.subs(x, 1) - (p.subs(x, 1) + 2*k)          # |p(1)| = p(1)+2g(1)
e2 = -diff(p, x).subs(x, 1) - (diff(p, x).subs(x, 1) + 2*m)
s = solve([e1, e2], [k, m], dict=True)[0]
say("  g(1) =", s[k], " ,  g'(1) =", s[m])
H = lambda t: (p + 2*g_).subs(s).subs(x, t)        # h = f+g = p+2g  (x>=1)
say("  h(2) =", simplify(H(2)))
rv = solve(simplify(H(2)) - 5, r)
say("  h(2)=5  ->  r =", rv)
R = rv[0]
say("  r > 1 ?", R > 1, " /  g'=2r-3 != 0 ?", (2*R-3) != 0)
say("  ★ h(4) =", simplify(H(4).subs(r, R)))
# 전면 재검증
pp = p.subs(r, R); gg = g_.subs(s).subs(r, R); ff = pp + gg
say("  검산: f(x) =", expand(ff), " , g(x) =", expand(gg))
say("        h(0)=|p(0)| =", abs(pp.subs(x, 0)),
    " h(2)=", (ff+gg).subs(x, 2), " h(4)=", (ff+gg).subs(x, 4))
say("        x<1 에서 p =", factor(pp), " (x<1 이면 부호 일정 -> |p| 미분가능)")
say("        x=1 연속: 좌", -pp.subs(x, 1), " 우", (ff+gg).subs(x, 1))
say("        x=1 미분: 좌", -diff(pp, x).subs(x, 1),
    " 우", diff(ff+gg, x).subs(x, 1))

# ══════════════════════════════════════════════════════════
# C. 2022학년도 6월 평가원 공통 22번
# ══════════════════════════════════════════════════════════
say("=" * 60)
say("[C] 2022 6월 공통 22번")
A, B, al, be = symbols('A B al be', real=True)     # f = A(x-al)^2 (x-be)
fc = A*(x - al)**2*(x - be)
fp = diff(fc, x)
base = [fc.subs(x, 1) - 4, fp.subs(x, 1) - 1]      # f(1)=4, f'(1)=1
phi = x - fc                                        # x - f(x)
php = diff(phi, x)

cands = []
# phi(x)=al 또는 phi(x)=be 의 해가 모두 3개.
# al, be 는 각각 자기 방정식의 해이므로 (1,2) 조합.
# 해가 2개 = 그 값이 phi 의 극값. phi'(1)=0 이 이미 성립하므로 phi(1)=-3 이 극값.
extra = [al + 3, be + 3]        # phi(1) = 1 - f(1) = -3 이 al 또는 be
for i, ex in enumerate(extra):
    for s in solve(base + [ex], [A, al, be], dict=True):
        if any(v.free_symbols for v in s.values()):
            continue
        cands.append((("al=-3" if i == 0 else "be=-3"), s))

# 다른 임계점 u 에서의 극값이 al 또는 be 인 경우도 확인
u = Symbol('u', real=True)
for i, tgt in enumerate([al, be]):
    for s in solve(base + [php.subs(x, u), phi.subs(x, u) - tgt], [A, al, be, u], dict=True):
        if any(v.free_symbols - {u} for v in s.values()):
            continue
        cands.append((("phi(u)=al" if i == 0 else "phi(u)=be"), s))

def check(s):
    """조건 전체를 수치로 재확인하고 (실근개수, f'(0), f(0)) 반환"""
    try:
        AA, aa, bb = [S(s[v]) for v in (A, al, be)]
    except Exception:
        return None
    if AA == 0 or aa == bb:
        return None
    ff = AA*(x - aa)**2*(x - bb)
    # (가) f(x)=0 의 서로 다른 실근 = {aa, bb} -> 2개  (aa != bb 이므로 자동)
    inner = expand(ff.subs(x, x - ff))
    try:
        rts = real_roots(Poly(inner, x))
    except Exception:
        return None
    n = len(set(rts))
    fp0 = diff(ff, x).subs(x, 0)
    return n, fp0, ff.subs(x, 0), ff

say("  후보 검사:")
best = []
for tag, s in cands:
    r_ = check(s)
    if not r_:
        continue
    n, fp0, f0, ff = r_
    okn, okd = (n == 3), (fp0 > 1)
    say("   [%-10s] a=%s al=%s be=%s | f(x-f(x))=0 실근 %d개 %s | f'(0)=%s %s | f(0)=%s"
        % (tag, s[A], s[al], s[be], n, "OK" if okn else "X",
           fp0, "OK" if okd else "X", f0))
    if okn and okd:
        best.append((f0, ff, s))

for f0, ff, s in best:
    fr = nsimplify(f0, rational=True)
    say("  ★ f(x) =", expand(ff))
    say("    f(0) = %s  ->  q=%d, p=%d,  p+q = %d"
        % (fr, fr.p, fr.q, fr.p + fr.q))
    # 최종 전수 재검증
    say("    재검증: f(1)=%s  f'(1)=%s  f'(0)=%s(>1)  f(x)=0 실근 %s"
        % (ff.subs(x, 1), diff(ff, x).subs(x, 1), diff(ff, x).subs(x, 0),
           sorted(set(real_roots(Poly(expand(ff), x))))))
    say("            f(x-f(x))=0 실근 %s"
        % sorted(set(real_roots(Poly(expand(ff.subs(x, x - ff)), x)))))

io.open("res.txt", "w", encoding="utf-8").write("\n".join(OUT))
print("done")
