# my code

from math import gcd

n, m = map(int, input().split(':'))

num = gcd(n ,m)

print(int(n/num), ':', int(m/num), sep = '')
