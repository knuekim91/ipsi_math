# -*- coding: utf-8 -*-
"""사회문화 표 분석 변형문항 9제 검증. 모든 수치를 분수로 다뤄 반올림 오차를 없앤다."""
from fractions import Fraction as F
ok = True
def chk(tag, got, want):
    global ok
    hit = got == want
    ok &= hit
    print("  %-46s %-14s %s" % (tag, got, "" if hit else "★기대 %s★" % want))

print("E1  계층 구조 — A,B,C 추론")
# B->A 상승, B->C 하강  =>  B=중층, A=상층, C=하층
t  = {"A": F(10,100), "B": F(30,100), "C": F(60,100)}
t2 = {"A": F(20,100), "B": F(50,100), "C": F(30,100)}
P, P2 = 1000, 1500                      # 만 명
chk("ㄱ A는 상층", "참", "참")
chk("ㄴ 중층 t+20 / 중층 t", F(int(P2*t2['B']), int(P*t['B'])), F(5,2))
chk("ㄷ 하층 t -> t+20", "%d -> %d (감소)" % (P*t['C'], P2*t2['C']), "600 -> 450 (감소)")
print("   t년 구조: 상%d 중%d 하%d -> 피라미드형" % (P*t['A'], P*t['B'], P*t['C']))
print()

print("E2  상대적 인구 — 전체 인구 동일")
# A->C 상승, A->B 하강 => A=중층, C=상층, B=하층
par = {"A":100, "B":150, "C":50}; chi = {"A":100, "B":60, "C":40}
N = 600
pp = {k: F(v, sum(par.values()))*N for k,v in par.items()}
cc = {k: F(v, sum(chi.values()))*N for k,v in chi.items()}
print("   부모 중%s 하%s 상%s / 자녀 중%s 하%s 상%s"
      % (pp['A'],pp['B'],pp['C'],cc['A'],cc['B'],cc['C']))
chk("ㄱ 중층 자녀/부모 = 2 인가", cc['A']/pp['A'], F(3,2))     # 1.5 이므로 ㄱ 거짓
chk("ㄴ 부모 피라미드(상<중<하)", pp['C']<pp['A']<pp['B'], True)
chk("ㄷ 상층대비하층 비 부모>자녀", pp['B']/pp['C'] > cc['B']/cc['C'], True)
print()

print("E3  갑·을국 비교")
# A->C 하강(A가 위), 을국 피라미드형 => 을 20/30/50 = 상/중/하 => A상 B중 C하
g = {"A":F(30,100),"B":F(50,100),"C":F(20,100)}; Ng = 300
e = {"A":F(20,100),"B":F(30,100),"C":F(50,100)}; Ne = 100
G = {k:v*Ng for k,v in g.items()}; E = {k:v*Ne for k,v in e.items()}
print("   갑 상%s 중%s 하%s / 을 상%s 중%s 하%s" % (G['A'],G['B'],G['C'],E['A'],E['B'],E['C']))
chk("① 둘 다 다이아몬드형", (g['B']==max(g.values())) and (e['B']==max(e.values())), False)
chk("② 상층 갑/을 = 5배", G['A']/E['A'], F(9,2))
chk("③ 중층 갑/을 = 5배", G['B']/E['B'], F(5))
chk("④ 하층 갑 < 을", G['C'] < E['C'], False)
chk("⑤ 갑 상층 > 을 전체", G['A'] > Ne, False)
print()

print("F1  사회보장 기본")
A, B, dup = F(40,100), F(15,100), F(5,100)
non = 1 - (A + B - dup); N = 1000
chk("비수혜자 비율", non, F(50,100))
chk("② 비수혜자 500만", non*N, 500)
chk("③ A만 수혜 400만인가", (A-dup)*N, 350)
chk("⑤ 중복/B = 1/2 인가", dup/B, F(1,3))
print()

print("F2  두 국가 + 빈칸")
# 갑: A50 중복10 비수혜40 -> 수혜60 = 50+x-10 -> x=20
x = 1 - F(40,100) - (F(50,100) - F(10,100))
# 을: A60 B20 비수혜30 -> 수혜70 = 60+20-y -> y=10
y = F(60,100) + F(20,100) - (1 - F(30,100))
chk("㉠ (갑 B수혜자)", x, F(20,100)); chk("㉡ (을 중복)", y, F(10,100))
chk("① ㉠+㉡ = 35", (x+y)*100, F(30))
chk("③ 중복 갑/을 = 2배", (F(10,100)*2000)/(y*1000), F(2))
chk("④ A만 을 < 갑", (F(60,100)-y) < (F(50,100)-F(10,100)), False)
chk("⑤ 비수혜 갑 < 을", F(40,100)*2000 < F(30,100)*1000, False)
print()

print("F3  시기별 + 인구 변화")
# t년: 중복5 비수혜60 -> 수혜40 = A+B-5 -> A+B=45, A=B/2 -> A15 B30
dup1, non1 = F(5,100), F(60,100); s1 = 1-non1
B1 = (s1+dup1)*F(2,3); A1 = B1/2
chk("t년 A,B", (A1*100, B1*100), (F(15), F(30)))
# t+20년: 중복8 비수혜52 -> 수혜48 = A+B-8 -> A+B=56, B=중복*5=40 -> A=16
dup2, non2 = F(8,100), F(52,100); s2 = 1-non2
B2 = dup2*5; A2 = (s2+dup2) - B2
chk("t+20년 A,B", (A2*100, B2*100), (F(16), F(40)))
N1, N2 = 1000, 1500
chk("② A수혜자 t+20/t = 2배", (A2*N2)/(A1*N1), F(8,5))
chk("③ B만 t+20/t = 2배", ((B2-dup2)*N2)/((B1-dup1)*N1), F(48,25))
chk("④ 비수혜 같은가", non1*N1 == non2*N2, False)
chk("⑤ 중복 t+20/t = 2.4배", (dup2*N2)/(dup1*N1), F(12,5))
print()

print("G1  부양비 기본")
def idx(y, w, o): return (F(y,w)*100, F(o,w)*100, F(y,w)*100+F(o,w)*100, F(o,y)*100)
a = idx(200,800,200); b = idx(150,750,300)
print("   t년  유소년%s 노년%s 총%s 노령화%s" % a)
print("   t+20 유소년%s 노년%s 총%s 노령화%s" % b)
chk("ㄱ 총부양비 t+20 > t", b[2] > a[2], True)
chk("ㄴ 노령화 t+20 / t = 2", b[3]/a[3], F(2))
chk("ㄷ 유소년부양비 t+20 > t", b[0] > a[0], False)
print()

print("G2  부양비에서 인구 역산")
def back(tot, aging, work):
    dep = F(tot,100)*work                 # 유소년 + 노년
    young = dep / (1 + F(aging,100)); old = dep - young
    return young, old, work, young+old+work
y1,o1,w1,T1 = back(50,100,1000); y2,o2,w2,T2 = back(60,300,800)
print("   t년  유소년%s 노년%s 부양%s 전체%s" % (y1,o1,w1,T1))
print("   t+30 유소년%s 노년%s 부양%s 전체%s" % (y2,o2,w2,T2))
chk("① 유소년 t+30 <= t 의 절반", y2 <= y1/2, True)
chk("② 노년 t+30 / t = 2", o2/o1, F(36,25))
chk("③ 전체 t+30 > t", T2 > T1, False)
chk("④ 노년부양비 t > t+30", F(o1,w1) > F(o2,w2), False)
chk("⑤ 유소년부양비 t+30 = t 의 절반", (F(y2,w2))/(F(y1,w1)), F(3,5))
print()

print("G3  예측 시나리오")
# t년: 총부양비 60, 노년부양비 = 유소년부양비의 2배 -> 유20 노40
# 부양인구 P -> 유소년 .2P, 노년 .4P, 전체 1.6P, 노년비율 25%
# [예측1] 전체 1.2배, 총부양비 불변(60) -> 부양인구 1.2P, 유소년+노년 .72P
#         노년비율 증가(>25%) -> 노년 > .48P -> 노년부양비 > 40 (증가), 유소년부양비 < 20 (감소)
# [예측2] 전체 0.8배=1.28P, 총부양비 증가(>60) -> 부양인구 < .8P, 노년비율 불변 25% -> 노년 .32P
#         노년부양비 = .32P/부양 > 40 (증가),  유소년부양비 = .96P/부양 - 1 > 20 (증가)
import itertools
def pred1(k):            # k = 노년 비율(%) > 25
    tot = F(192,100); work = F(12,10); old = F(k,100)*tot; young = F(72,100)-old
    return F(old,work)*100, F(young,work)*100, old
def pred2(w):            # w = 부양인구 < 0.8
    tot = F(128,100); old = F(25,100)*tot; young = tot-old-w
    return F(old,w)*100, F(young,w)*100, old
s1 = [pred1(k) for k in (26, 30, 35)]
s2 = [pred2(F(w,100)) for w in (79, 70, 60)]
chk("① 예측1 노년부양비 > 40 (t년값)", all(x[0] > 40 for x in s1), True)
chk("② 예측1 유소년부양비 > 20", all(x[1] > 20 for x in s1), False)
chk("③ 예측2 노년부양비 < 40", all(x[0] < 40 for x in s2), False)
chk("④ 예측1·2 모두 유소년부양비 > 20", all(x[1] > 20 for x in s1+s2), False)
chk("⑤ 예측2 노년 인구 > t년(0.4)", all(x[2] > F(4,10) for x in s2), False)
print()
print("전체", "통과" if ok else "★검토 필요★")
