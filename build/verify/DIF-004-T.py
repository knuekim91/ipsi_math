# -*- coding: utf-8 -*-
"""DIF-004 '왜' 사다리 T1~T4 검증"""
H = 1e-7
L = lambda F,a: (F(a)-F(a-H))/H
R = lambda F,a: (F(a+H)-F(a))/H
J = lambda F,a: R(F,a)-L(F,a)
cont = lambda F,a: abs(F(a-H)-F(a+H)) < 1e-5

print("T1  f = ax+b (x<1), 4x^2 (x>=1) 이 x=1에서 미분가능")
a, b = 8, -4
f = lambda x: (a*x+b) if x < 1 else 4*x*x
print(f"   a={a}, b={b} | 연속 {cont(f,1)} | 왼쪽 {L(f,1):.4f} 오른쪽 {R(f,1):.4f} 뛰기 {J(f,1):.6f}")
print(f"   a-b = {a-b}")

print("T2  u=5|x-1|, v=-3|x-1|, h=u+v 의 뛰기")
u = lambda x: 5*abs(x-1); v = lambda x: -3*abs(x-1); h = lambda x: u(x)+v(x)
print(f"   뛰기 u={J(u,1):.4f}  v={J(v,1):.4f}  h={J(h,1):.4f}   합 확인 {J(u,1)+J(v,1):.4f}")

print("T3  g: x<1 이면 10(x-1), x>=1 이면 -2(x-1). h=g+t|x-1| 이 미분가능한 양수 t")
g = lambda x: 10*(x-1) if x < 1 else -2*(x-1)
print(f"   g의 뛰기 {J(g,1):.4f}")
t_found = None
for t10 in range(1, 201):
    t = t10/10
    hh = lambda x, t=t: g(x) + t*abs(x-1)
    if abs(J(hh,1)) < 1e-3: t_found = t; break
print(f"   t = {t_found}  (-12 + 2t = 0 -> 6)")

print("T4  f = 2x+a (x<1), 2x+5 (x>=1) 이 x=1에서 미분가능한 a")
for a2 in (0, 3, 5):
    ff = lambda x, a2=a2: (2*x+a2) if x < 1 else (2*x+5)
    print(f"   a={a2}: 연속 {cont(ff,1)} | 왼쪽 {L(ff,1):.2f} 오른쪽 {R(ff,1):.2f}"
          f" -> 기울기는 같지만 연속? {cont(ff,1)}")
print("   => a = 5 일 때만 미분가능")
