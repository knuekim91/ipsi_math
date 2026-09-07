# -*- coding: utf-8 -*-
"""22번·30번의 '조건'까지 직접 확인한다."""
from sympy import symbols, Poly, Rational, real_roots, nsimplify, maximum, Interval, diff, simplify
x = symbols('x', real=True)

# ---------- 22번 ----------
f = -5*x**4 + 18*x**3 - 13*x**2 + x + 1
h = simplify(f/(x + 1))
print("22번  f(x) = %s" % f)
print("22번  f(-1) = %s  (<0 이어야 x->-1+ 에서 h->-oo)" % f.subs(x, -1))
print("22번  h(0)=%s, h(1)=%s, h(2)=%s" % (h.subs(x,0), h.subs(x,1), h.subs(x,2)))
print("22번  h'(0)=%s, h'(2)=%s  (둘 다 0 이면 x=0, x=2 가 극점)"
      % (diff(h,x).subs(x,0), diff(h,x).subs(x,2)))
print("22번  h 의 최댓값 = %s   (t 의 최댓값 5)" % maximum(h, x, Interval.open(-1, 100)))

def g(t):
    """f(x)=t(x+1) 의 실근 중 x>-1 인 것의 최솟값 (중근도 근으로 센다)"""
    rs = [r for r in real_roots(Poly(f - t*(x + 1), x)) if r > -1]
    return min(rs) if rs else None
print("22번  g(1) = %s   (0)" % g(Rational(1)))
print("22번  g(5) = %s   (2)" % g(Rational(5)))
e = Rational(1, 10**6)
r, l = g(1 + e), g(1 - e)
print("22번  g(1+) ≈ %.6f,  g(1-) ≈ %.6f,  차 ≈ %.6f   (1)"
      % (float(r), float(l), float(r - l)))
print("22번  |f(3)| = %s" % abs(f.subs(x, 3)))

# ---------- 30번 ----------
from statistics import NormalDist
m1, m2, sg = 3.0, 7.0, 2.0
X, Y = NormalDist(m1, sg), NormalDist(m2, sg)
w = lambda D, a, L: D.cdf(a + L) - D.cdf(a)
print()
print("30번  P(X>=x)=P(Y<=-x+10) 최대오차 = %.2e"
      % max(abs((1 - X.cdf(v/10)) - Y.cdf(-v/10 + 10)) for v in range(-200, 300)))
good = [a/1000 for a in range(-4000, 4001) if w(X, a/1000, 8) >= w(Y, a/1000, 8) - 1e-15]
print("30번  P(a<=X<=a+8)>=P(a<=Y<=a+8) 인 a 의 최댓값 a0 = %.3f   (1)" % max(good))
a0 = 1.0
print("30번  P(a0<=X<=a0+2)=%.9f = P(a0+2<=X<=a0+4)=%.9f" % (w(X,a0,2), w(X,a0+2,2)))
print("30번  P(a0<=X<=a0+4)=%.9f = P(m2-s<=Y<=m2+s)=%.9f" % (w(X,a0,4), w(Y,m2-sg,2*sg)))
print("30번  k = P(1<=X<=7) = %.6f   표값 0.341+0.477 = %.3f  ->  1000k = 818"
      % (X.cdf(m2) - X.cdf(a0), 0.341 + 0.477))
