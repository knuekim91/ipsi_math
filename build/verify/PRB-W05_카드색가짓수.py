# -*- coding: utf-8 -*-
"""PRB-W05 (확률과 통계 30번 홀수형) 와 유사문항 검증.

문제 : 빨강·주황·노랑·파랑 카드 1장씩(서로 다른 색), 보라 7장(같은 색)을
       학생 A, B, C 에게 남김없이 나눈다. 각 학생이 받은 색의 가짓수가 모두 홀수.

핵심 : 학생 i 의 색 가짓수 = (받은 단색 카드 수 k_i) + [보라를 1장 이상 받았다] e_i.
       보라는 '받았는가'만 중요하므로 양수인 학생 집합 S 를 정하고,
       보라 m장을 |S| 명에게 1장 이상씩 나누는 방법은 C(m-1, |S|-1).
"""
from itertools import product
from math import comb, factorial


def brute(s, m, n, odd=True):
    """전수 : 단색 s장을 n명에게 배분 x 보라 m장의 분배."""
    tot = 0
    for assign in product(range(n), repeat=s):
        k = [assign.count(i) for i in range(n)]
        for p in product(range(m + 1), repeat=n):
            if sum(p) != m:
                continue
            col = [k[i] + (1 if p[i] > 0 else 0) for i in range(n)]
            if all((c % 2 == 1) == odd for c in col):
                tot += 1
    return tot


def formula(s, m, n):
    """식 : 단색 배분 (multinomial) x 보라 양수집합 S 의 C(m-1,|S|-1)."""
    tot = 0
    for ks in product(range(s + 1), repeat=n):
        if sum(ks) != s:
            continue
        ways = factorial(s)
        for k in ks:
            ways //= factorial(k)
        for e in product(range(2), repeat=n):
            S = sum(e)
            if S == 0 or S > m:
                continue
            if any((ks[i] + e[i]) % 2 == 0 for i in range(n)):
                continue
            tot += ways * comb(m - 1, S - 1)
    return tot


print("원문항 : s=4, m=7, n=3")
print("  전수 %d  식 %d   (375 ?)" % (brute(4, 7, 3), formula(4, 7, 3)))
print("  색 가짓수 조합별 : (1,1,3)=60, (1,1,5)=45, (1,3,3)=270 ?")

print("\nV1 (하) : s=2, m=4, n=2")
print("  전수 %d  식 %d   (6 ?)" % (brute(2, 4, 2), formula(2, 4, 2)))

print("\nV2 (상) : s=5, m=6, n=3")
print("  전수 %d  식 %d   (915 ?)" % (brute(5, 6, 3), formula(5, 6, 3)))

print("\nV3 (역추론) : s=4, n=3 에서 경우의 수가 501 이 되는 보라 장수 m")
for m in range(1, 11):
    v = formula(4, m, 3)
    print("  m=%-2d -> %d%s" % (m, v, "   <- 501" if v == 501 else ""))
