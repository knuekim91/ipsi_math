# -*- coding: utf-8 -*-
"""12번: 손으로 얻은 cos(각DBC)=3/4 로 원 위에 A,B,C,D 를 놓고 모든 조건을 확인."""
import math
s7, s14, s2 = math.sqrt(7), math.sqrt(14), math.sqrt(2)
eps = math.asin(s7/4)                       # 호 DC 의 절반 = 각DBC
dlt = math.asin(s14/8)                      # 호 AD 의 절반 = 각ABD
R   = 4/s14                                 # AB = 2R sin(각ACB) = 2
zet = math.pi - 2*(dlt + eps)          # AB = AC 이려면 호 CB 는 이렇게 정해진다
eta = math.pi - dlt - eps - zet
assert abs(dlt + eps + zet + eta - math.pi) < 1e-12

def P(cum):                                 # 원 위 점 (누적 중심각)
    return (R*math.sin(cum), R*math.cos(cum))
A = P(0.0)                                  # A 부터 시계방향으로 D, C, B
D = P(2*dlt)
C = P(2*dlt + 2*eps)
B = P(2*dlt + 2*eps + 2*zet)

def dist(p, q): return math.hypot(p[0]-q[0], p[1]-q[1])
def cross(o, p, q): return (p[0]-o[0])*(q[1]-o[1]) - (p[1]-o[1])*(q[0]-o[0])

# A 를 지나 BD 에 평행한 직선과 직선 BC 의 교점 E
dx, dy = D[0]-B[0], D[1]-B[1]
ex, ey = C[0]-B[0], C[1]-B[1]
det = dx*(-ey) - (-ex)*dy
s = ((B[0]-A[0])*(-ey) - (-ex)*(B[1]-A[1])) / det
E = (A[0] + s*dx, A[1] + s*dy)

print("AB      = %.12f   (2)" % dist(A, B))
print("AC      = %.12f   (2)" % dist(A, C))
print("AD      = %.12f   (1)" % dist(A, D))
print("AE      = %.12f" % dist(A, E))
print("CD      = %.12f" % dist(C, D))
print("AE : CD = %.12f   (2)" % (dist(A, E)/dist(C, D)))
print("AE//BD  : 외적 %.2e" % ((E[0]-A[0])*dy - (E[1]-A[1])*dx))
print("E,B,C 공선: 외적 %.2e" % cross(E, B, C))
print("E 는 B 바깥쪽?  (E-B)·(C-B) = %.6f  <0 이면 그림과 같다"
      % ((E[0]-B[0])*(C[0]-B[0]) + (E[1]-B[1])*(C[1]-B[1])))
S = abs(cross(A, E, B))/2
print()
print("삼각형 AEB 넓이 = %.12f" % S)
print("sqrt(7)/2       = %.12f" % (s7/2))
print("일치" if abs(S - s7/2) < 1e-10 else "★불일치★")
