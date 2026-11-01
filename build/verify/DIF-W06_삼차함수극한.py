# -*- coding: utf-8 -*-
"""DIF-W06 (수학 14번) 검증.

조건 : 모든 실수 t 에 대하여 lim_{x->t} (x+t)(x-f(t)) / (f(x)+x^2) 가 존재하고 0 이 아니다.
핵심 : g = f + x^2 의 근 0 은 중근, -1 은 단근, 그리고 f(t)=t 의 해 t=1/c 가
       0 또는 -1 이어야 한다  ->  c = -1, f(x) = -x^3 - 2x^2, f(-3) = 9.
"""
from sympy import symbols, limit, factor, expand, solve, Rational, simplify

x, c = symbols('x c')
t = symbols('t')

# 1) 구조 : g = c x^2 (x+1), f = g - x^2
f_c = c*x**3 + c*x**2 - x**2
g_c = f_c + x**2
print("g =", factor(g_c), "   f =", expand(f_c))

# 2) f(t)=t 의 근 : t(t+1)(ct-1) -> 1/c 가 0, -1 이어야 한다
print("f(t)-t =", factor(f_c - x))
print("c =", solve(Rational(1) / c + 1, c))

# 3) c = -1 에서 모든 t 의 극한을 계산
f = expand(f_c.subs(c, -1))
g = f + x**2
print("\nf(x) =", f, "   f(-3) =", f.subs(x, -3), "  (9 ?)")
print("t 별 극한 (0 이 아니어야 함)")
for tv in [-3, -2, Rational(-1, 2), -1, 0, Rational(1, 2), 1, 2, 5]:
    L = limit((x + tv) * (x - f.subs(x, tv)) / g, x, tv)
    expect = -2*(tv + 1) if tv not in (0, -1) else (-1 if tv == 0 else 2)
    print("  t = %-5s  극한 = %-4s  (기대 %s)  %s" % (tv, L, expect, "OK" if L == expect else "확인"))
