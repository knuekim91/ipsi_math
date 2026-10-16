# -*- coding: utf-8 -*-
"""EXP-W01 (2027-10 모평 22번) 과 유사문항 3제의 수치 검증.

핵심 세 줄
  ① a^x+b 와 log_a(x-b) 는 서로 역함수 -> 교점은 y=x 위 : a^x+b = x
  ② (1,1) 이 두 곡선 사이  <=>  a + b < 1
  ③ f(α(t))·f(β(t)) > 0 의 해가 0<t<m  <=>  m = -1/b
"""
from math import log

def mk(a, b):
    g = lambda x: a**x + b
    h = lambda x: log(x - b) / log(a)
    return g, h, (lambda x: min(g(x), h(x)))

def bis(fn, lo, hi, n=300):
    for _ in range(n):
        m = (lo + hi) / 2
        if fn(lo) * fn(m) <= 0: hi = m
        else: lo = m
    return (lo + hi) / 2

def cross(a, b):
    """두 곡선의 교점 = a^x + b = x 의 근"""
    g, _, _ = mk(a, b)
    d = lambda x: g(x) - x
    xs = [b + 1e-12 + i * 0.0005 for i in range(120000)]
    return [bis(d, xs[i], xs[i+1]) for i in range(len(xs)-1)
            if d(xs[i]) * d(xs[i+1]) < 0]

def roots(a, b, t, far=60.0):
    g, h, f = mk(a, b)
    L = lambda x: t * (x - 1) + 1
    d = lambda x: f(x) - L(x)
    xs = [b + 1e-9 + (i / 6000.0) ** 2 * far for i in range(6001)]
    return [bis(d, xs[i], xs[i+1]) for i in range(len(xs)-1)
            if d(xs[i]) * d(xs[i+1]) < 0]

print("=== 원문항 EXP-W01 : m=4/3 -> b=-3/4 ; β(1)=2α(1) -> a^(3/4)=3/2 ===")
b = -0.75; a = 1.5 ** (4.0/3.0)
c = cross(a, b)
print("  교점 %s   β/α = %.10f (=2?)" % ([round(x, 8) for x in c], c[1]/c[0]))
print("  α<1<β : %s    a+b = %.4f (<1?)" % (c[0] < 1 < c[1], a + b))
print("  m = -1/b = %.6f (=4/3?)   16a^3 = %.6f (=81?)" % (-1/b, 16*a**3))
_, _, f = mk(a, b)
for t in (1.30, 4.0/3 - 1e-6, 4.0/3 + 1e-6, 1.50):
    r = roots(a, b, t)
    s = f(r[0]) * f(r[1])
    print("    t=%.6f  f(α)f(β) = %+0.6f  %s" % (t, s, "양" if s > 0 else "음"))

print()
print("=== V1 : 중점(2,2), PQ=4√2 -> 교점 0,4 -> b=-1, a^4=5 ===")
a = 5 ** 0.25; b = -1.0
c = cross(a, b)
print("  교점 %s   중점 %.6f   PQ = %.6f (=4√2=%.6f?)"
      % ([round(x, 8) for x in c], (c[0]+c[1])/2, 2**0.5*(c[1]-c[0]), 4*2**0.5))
print("  a^8 = %.8f (=25?)" % (a**8))

print()
print("=== V2 : b=-6, 모든 양수 t 에서 두 실근 <=> a+b<1 <=> a<7 ===")
b = -6.0
for a in (2, 3, 4, 5, 6, 6.99, 7, 7.01, 8):
    c = cross(a, b)
    print("  a=%-5s 교점 %-26s a+b=%-6.2f  α<1<β : %s"
          % (a, [round(x, 4) for x in c], a + b, c[0] < 1 < c[1]))
print("  자연수 a 의 합 = %d (=20?)" % sum(range(2, 7)))

print()
print("=== V3 : 해가 0<t<1 -> b=-1 ; β(1)=3 -> a^3=4 ===")
b = -1.0; a = 4 ** (1.0/3.0)
c = cross(a, b)
print("  교점 %s   m = -1/b = %.4f   16a^3 = %.8f (=64?)"
      % ([round(x, 8) for x in c], -1/b, 16*a**3))
_, _, f = mk(a, b)
for t in (0.99, 1.01):
    r = roots(a, b, t); s = f(r[0]) * f(r[1])
    print("    t=%.2f  %s" % (t, "양" if s > 0 else "음"))
