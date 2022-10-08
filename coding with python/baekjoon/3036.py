# my code

from fractions import Fraction

n = int(input())
r = list(map(int, input().split()))

for i in range(1 , n):
    sol = Fraction(r[0] , r[i])
    print(f"{sol.numerator}/{sol.denominator}")
