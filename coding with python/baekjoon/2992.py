# my code

from itertools import permutations

n = input()
a = sorted(set(permutations(n, len(n))))

if a.index(tuple(n)) == (len(a) - 1):
    print(0)
else:
    print(''.join(a[a.index(tuple(n)) + 1]))
