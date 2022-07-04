# my code

from itertools import permutations

n, m = map(int, input().split())

new = list(permutations([i for i in range(1, n+1)], m))

for j in new:
    for k in range(m):
        print(j[k], end = ' ')
    print()
