# my code

from itertools import permutations

n = list(input())

new = list(permutations(n, len(n)))

a = sorted(set(new))

if a.index(tuple(n)) == (len(n) - 1):
    print(0)
else:
    print(''.join(a[a.index(tuple(n)) + 1]))
