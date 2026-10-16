import numpy as np

def pairs(a,b,c,N=4000):
    # f(x)=x^3+ax^2+bx+c ; 같은 함숫값을 갖는 (x1,x2), x1<x2
    f=lambda x:x**3+a*x**2+b*x+c
    # 극점
    d=4*a*a-12*b
    out=[]
    if d<=0: return out
    r1=(-2*a-np.sqrt(d))/6; r2=(-2*a+np.sqrt(d))/6   # 극대, 극소
    lo,hi=f(r2),f(r1)
    for y in np.linspace(lo+1e-9,hi-1e-9,N):
        rr=np.roots([1,a,b,c-y]); rr=np.sort(rr[np.abs(rr.imag)<1e-9].real)
        if len(rr)<3: continue
        for i in range(3):
            for j in range(i+1,3):
                out.append((rr[i],rr[j]))
    return out,r1,r2

print("=== 원문항  f=x^3-7x^2+36 ===")
P,r1,r2=pairs(-7,0,36)
print(" 극대 %.6f  극소 %.6f"%(r1,r2))
print(" 관계식 p=s^2+as+b 오차 max = %.2e"%max(abs(x*y-((x+y)**2-7*(x+y))) for x,y in P))
bad=[(x,y) for x,y in P if x*y>1e-9]
print(" x1x2>0 인 쌍의 x2 최솟값 = %.6f  (극소점 %.6f)"%(min(y for x,y in bad),r2))
print(" s 범위 = [%.4f, %.4f]   2*극소 = %.4f"%(min(x+y for x,y in P),max(x+y for x,y in P),2*r2))

print()
print("=== V1  f=x^3-4x^2+10 : x1x2 의 최솟값 ===")
P,r1,r2=pairs(-4,0,10)
print(" 수치 최솟값 = %.6f   이론 -4"%min(x*y for x,y in P))
s=np.array([x+y for x,y in P]); print(" 최소가 되는 s = %.4f  (이론 2)"%s[np.argmin([x*y for x,y in P])])
print(" 상수항 바꿔도? f=x^3-4x^2+999 ->", round(min(x*y for x,y in pairs(-4,0,999)[0]),6))

print()
print("=== V2  f=x^3-6x^2+11 : x1+x2 의 범위 ===")
P,r1,r2=pairs(-6,0,11)
print(" 극대 %.4f 극소 %.4f"%(r1,r2))
print(" s 범위 = (%.5f, %.5f)   이론 (0, 8)"%(min(x+y for x,y in P),max(x+y for x,y in P)))
print(" 중점 범위 = (%.5f, %.5f)  = (극대, 극소)"%(min((x+y)/2 for x,y in P),max((x+y)/2 for x,y in P)))
print(" alpha+beta = 8 ,  -4a/3 =", -4*(-6)/3)

print()
print("=== V3  M=6, f(0)=10  ->  f=x^3-9x^2+10 ===")
P,r1,r2=pairs(-9,0,10)
print(" 극대 %.4f 극소 %.4f  (M=극소=6)"%(r1,r2))
bad=[(x,y) for x,y in P if x*y>1e-9]
print(" x1x2>0 쌍의 x2 최솟값 = %.6f"%min(y for x,y in bad))
f=lambda x:x**3-9*x**2+10
print(" f(6) =",f(6)," f(0) =",f(0))
