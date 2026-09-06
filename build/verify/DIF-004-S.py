# -*- coding: utf-8 -*-
"""DIF-004 도입 사다리 검증 — 좌우 기울기를 수치로 직접 잰다."""
H = 1e-7
def slope_left(F, a):  return (F(a) - F(a - H)) / H
def slope_right(F, a): return (F(a + H) - F(a)) / H
def jump(F, a):        return slope_right(F, a) - slope_left(F, a)
def show(name, F, a, expect):
    L, R, J = slope_left(F, a), slope_right(F, a), jump(F, a)
    ok = abs(J - expect) < 1e-3
    print(f"  {name}: 왼쪽 {L:.4f} / 오른쪽 {R:.4f} / 뛰기 {J:.4f}  기대 {expect}  {'OK' if ok else 'X'}")
    return ok

def G(f):  # g(x) = -f (f>=0), 7f (f<0)
    return lambda x: -f(x) if f(x) >= 0 else 7*f(x)

print("S1  y = |2x| 의 x=0")
ok1 = show("|2x|", lambda x: abs(2*x), 0, 4)

print("S2  f(x)=x 일 때 g 의 x=0")
ok2 = show("g", G(lambda x: x), 0, -8)

print("S3  f(x)=3x 일 때 g 의 x=0   (= -8 x f'(0) = -24)")
ok3 = show("g", G(lambda x: 3*x), 0, -24)

print("S4  P(x)=(x-1)(x-2)^2 에서 |P|")
P = lambda x: (x-1)*(x-2)**2
ok4a = show("|P| at x=1 (단순근)", lambda x: abs(P(x)), 1, 2)
ok4b = show("|P| at x=2 (중근)",  lambda x: abs(P(x)), 2, 0)

print("S5  f(x)=x-3, h = g + |k(x-3)| 가 미분가능한 양수 k")
found = None
for k10 in range(1, 121):
    k = k10 / 10
    h = lambda x, k=k: G(lambda t: t-3)(x) + abs(k*(x-3))
    if abs(jump(h, 3)) < 1e-3:
        found = k; break
print(f"  k = {found}   (뛰기 -8 + 2k = 0 -> k = 4)")
ok5 = (found == 4.0)

print("\n원문항 DIF-004 재확인 (f(0) 후보와 곱)")
import math
def check(p, q, a_):
    f = lambda x: (x-p)**2*(x-q)
    g = lambda x: -f(x) if f(x) >= 0 else 7*f(x)
    P2 = lambda x: (x-1)*(x-a_)*(x-4+a_)
    h = lambda x: g(x) + abs(P2(x))
    return all(abs(jump(h, x0)) < 1e-2 for x0 in (1, a_, 4-a_, p, q))
vals = []
for (p, q, a_) in [(1.5,1,2), (0.5,1,2), (2,3,1), (4,3,1)]:
    if check(p, q, a_): vals.append(-(p**2)*q if q else 0)
vals = sorted(set([(0-p)**2*(0-q) for (p,q,a_) in [(1.5,1,2),(0.5,1,2),(2,3,1),(4,3,1)] if check(p,q,a_)]))
print("  f(0) 값들:", vals, " 최대x최소 =", max(vals)*min(vals))

print("\n전체:", "모두 통과" if all([ok1,ok2,ok3,ok4a,ok4b,ok5]) else "실패 있음")
