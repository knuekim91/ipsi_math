# -*- coding: utf-8 -*-
"""DIF-C13 사다리·유사문항 검증.

f(x+a)=f(x)+b 로 확장한 함수를 실제로 만들어 값을 구하고,
미분가능 조건이 f'(0)=f'(a) 인지 수치로 확인한다.
"""
from sympy import *
x = symbols('x', real=True)

def extend(poly, a, b):
    """[0,a] 에서 poly 인 함수를 f(x+a)=f(x)+b 로 실수 전체에 늘린다."""
    f0 = lambdify(x, poly, "math")
    def f(t):
        n = 0
        t = float(t)
        while t < 0:      t += a; n -= 1
        while t >= a:     t -= a; n += 1
        return f0(t) + n * b
    return f

def check(name, poly, want_a, ask, want):
    d = diff(poly, x)
    # 미분가능 조건: 이음매에서 좌·우 미분계수가 같아야 한다
    sols = [s for s in solve(Eq(d.subs(x, Symbol('A')), d.subs(x, 0)), Symbol('A')) if s.is_real and s > 0]
    a = sols[0]
    b = poly.subs(x, a) - poly.subs(x, 0)
    f = extend(poly, float(a), float(b))
    got = ask(f, float(a), float(b))
    # 이음매에서 실제로 매끄러운지 수치로 확인
    h = 1e-6
    L = (f(float(a)) - f(float(a) - h)) / h
    R = (f(float(a) + h) - f(float(a))) / h
    smooth = abs(L - R) < 1e-3
    print("%-9s a=%-4s b=%-5s  %s = %-8s (기대 %-8s) %s  이음매 매끄러움:%s"
          % (name, a, b, ask.__doc__, round(got, 6), want,
             "일치" if abs(got - want) < 1e-6 else "★불일치★",
             "예" if smooth else "★아니오★"))
    assert a == want_a, (name, a, want_a)

# 원문항
check("DIF-C13", x**3 - 3*x**2 + 5*x, 2,
      (lambda f, a, b: f(2*a)), 12)
DIF = lambda f, a, b: f(2*a); DIF.__doc__ = "f(2a)"
check("DIF-C13", x**3 - 3*x**2 + 5*x, 2, DIF, 12)

V1 = lambda f, a, b: f(2*a); V1.__doc__ = "f(2a)"
check("V1", 2*x**3 - 9*x**2 + 12*x, 3, V1, 18)

V2 = lambda f, a, b: a*b; V2.__doc__ = "a×b "
check("V2", x**3 - 6*x**2 + 15*x + 2, 4, V2, 112)

print()
# 사다리 — 미분가능을 요구하지 않는 단계는 따로 확인한다
def step(name, poly, a, ask_t, want):
    b = poly.subs(x, a) - poly.subs(x, 0)          # b 는 늘 이렇게 정해진다
    f = extend(poly, float(a), float(b))
    got = f(ask_t)
    print("%-4s  a=%s  b=%s  f(%s) = %s  (기대 %s) %s"
          % (name, a, b, ask_t, round(got, 6), want,
             "일치" if abs(got - want) < 1e-9 else "★불일치★"))
step("T1", 3*x**2,      2, 5, 27)
step("T3", x**2 + 1,    3, 8, 23)
print()
print("T4: 원문항과 같은 f 에서 a =", 2, "  (위 DIF-C13 줄에서 확인됨)")
