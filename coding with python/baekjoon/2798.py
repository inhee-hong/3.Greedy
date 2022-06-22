# my code

from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

lists = list(combinations(card, 3))
ans = []
for i in range(len(lists)):
    if sum(lists[i]) <= m:
        ans.append(sum(lists[i]))

print(max(ans))
