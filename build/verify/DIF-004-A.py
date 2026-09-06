# -*- coding: utf-8 -*-
"""DIF-004 대수적 풀이 검증: g = 3f - 4|f| 및 A(x)|x-q| 보조정리"""
import random
H=1e-7
L=lambda F,a:(F(a)-F(a-H))/H; R=lambda F,a:(F(a+H)-F(a))/H
J=lambda F,a:R(F,a)-L(F,a)

print("① g(x) = 3f(x) - 4|f(x)| 가 정의와 같은가 (무작위 검사)")
bad=0
for _ in range(20000):
    v=random.uniform(-50,50)
    g_def = -v if v>=0 else 7*v
    g_new = 3*v - 4*abs(v)
    if abs(g_def-g_new)>1e-9: bad+=1
print("   불일치:", bad, "-> p=3, q=-4, p-q =", 3-(-4))

print("\n② 보조정리: A(x)|x-c| 는 A(c)=0 일 때만 c에서 미분가능")
for k in (3,4,5):
    A=lambda x,k=k: x*x-5*x+k
    F=lambda x,k=k: (x*x-5*x+k)*abs(x-1)
    print(f"   k={k}: A(1)={A(1)}, 뛰기={J(F,1):.6f}")

print("\n③ A3 후보: y = (x-5)^2|x-1| - 4(x-p)^2|x-1|")
for p in (-1,0,1,2,3,4):
    F=lambda x,p=p: ((x-5)**2 - 4*(x-p)**2)*abs(x-1)
    print(f"   p={p}: 계수 A(1)={(1-5)**2-4*(1-p)**2}, 뛰기={J(F,1):.6f}")

print("\n④ 원문항을 새 방법으로: |q-r| = 2|q-p| 가 답을 재현하는가")
# P 의 근이 {1,a,4-a}. 중근 r, 단근 q.
cases=[]
for a in (1,2,3):
    roots=[1,a,4-a]
    from collections import Counter
    c=Counter(roots)
    if sorted(c.values())==[1,2]:
        r=[k for k,v in c.items() if v==2][0]
        q=[k for k,v in c.items() if v==1][0]
        cases.append((a,r,q))
print("   (a, 중근 r, 단근 q):", cases)
vals=[]
for a,r,q in cases:
    # |q-r| = 2|q-p|  ->  p = q +- |q-r|/2
    d=abs(q-r)/2
    for p in (q-d, q+d):
        if p==q: continue
        f0 = (0-p)**2*(0-q)
        vals.append(f0)
        # h 가 실제로 미분가능한지 수치 확인
        f=lambda x,p=p,q=q: (x-p)**2*(x-q)
        g=lambda x,f=f: -f(x) if f(x)>=0 else 7*f(x)
        P=lambda x,a=a: (x-1)*(x-a)*(x-4+a)
        h=lambda x,g=g,P=P: g(x)+abs(P(x))
        ok=all(abs(J(h,x0))<1e-2 for x0 in (1,a,4-a,p,q))
        print(f"   a={a} q={q} r={r} -> p={p}, f(0)={f0}, 미분가능 {ok}")
vals=sorted(set(vals))
print("   f(0) 값들:", vals, " 최대x최소 =", max(vals)*min(vals))
