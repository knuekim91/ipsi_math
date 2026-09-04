from fractions import Fraction as F

def poly_roots_quad(A,B,C):
    """정확 유리수 판별. (disc, roots) 반환. roots는 유리수일 때만."""
    d = B*B - 4*A*C
    return d

def limit_exists(b, c, t, Nroots):
    """f=x^2+bx+c, 분모 D=f(x)+f(x-t), 분자의 근집합 Nroots(중복도 dict).
       모든 a에서 극한 존재 여부."""
    A = F(2); B = 2*(b - t); C = t*t - b*t + 2*c
    disc = B*B - 4*A*C
    if disc < 0:
        return True
    if disc == 0:
        r = -B / (2*A)
        return Nroots.get(r, 0) >= 2
    # 서로 다른 두 실근: 유리근이 아니면 분자(유리계수)의 근일 수 없음
    # r = (-B ± sqrt(disc))/(2A)
    num = disc.numerator; den = disc.denominator
    def isq(n):
        if n < 0: return None
        r = int(n**0.5)
        for k in (r-2,r-1,r,r+1,r+2):
            if k>=0 and k*k==n: return k
        return None
    sn, sd = isq(num), isq(den)
    if sn is None or sd is None:
        return False
    s = F(sn, sd)
    for r in ((-B+s)/(2*A), (-B-s)/(2*A)):
        if Nroots.get(r,0) < 1:
            return False
    return True

def check(name, b, c, Nroots, t0, target_label, target_val):
    b, c, t0 = F(b), F(c), F(t0)
    bad = []
    t = F(1,20)
    while t <= 8:
        ok = limit_exists(b, c, t, Nroots)
        want = (t >= t0)
        if ok != want: bad.append((t, ok, want))
        t += F(1,20)
    f = lambda x: x*x + b*x + c
    print(f"[{name}] f(x)=x^2+({b})x+({c})  경계 t0={t0}  "
          f"{target_label}={target_val}  검증={'통과' if not bad else '실패 '+str(bad[:4])}")
    return not bad

# V1: 분자 (x-3)f(x), 집합 {t>=2}, f(x)=(x-3)(x-1)
ok1 = check("LIM-003-V1", -4, 3, {F(3):2, F(1):1}, 2, "f(5)", (5*5-4*5+3))

# V2-a: 분자 (x^2-4)f(x), {t>=5/2}, f=(x-2)(x+1/2)
ok2a = check("LIM-003-V2 (i)", F(-3,2), -1, {F(2):2, F(-2):1, F(-1,2):1}, F(5,2), "f(0)", F(-1))
# V2-b: f=(x+2)(x+9/2)
ok2b = check("LIM-003-V2 (ii)", F(13,2), 9, {F(-2):2, F(2):1, F(-9,2):1}, F(5,2), "f(0)", 9)
print("   -> 가능한 f(0)의 합 =", F(-1)+9)

# V3: 분자 (x-k)f(x), {t>=3}, f=(x-k)(x-k+3), f(0)=4, k>0 -> k=4
for k in (4, -1):
    b = -(2*k-3); c = k*(k-3)
    print(f"   k={k}: f(0)={c}, f(6)={36+6*b+c}")
ok3 = check("LIM-003-V3 (k=4)", -5, 4, {F(4):2, F(1):1}, 3, "f(6)", 36-30+4)

print("\n전체:", "모두 통과" if all([ok1,ok2a,ok2b,ok3]) else "실패 있음")
