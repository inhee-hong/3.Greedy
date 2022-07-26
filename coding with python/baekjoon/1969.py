# my code

from collections import Counter

n, m = map(int, input().split())
ans = [[] for i in range(m)]
answer = ''
cnt = 0

for i in range(n):
    word = input()
    
    for j in range(m):
        ans[j].append(word[j])


for k in range(m):
    num = Counter(sorted(ans[k]))
    answer += (num.most_common()[0][0])
    if len(num) != 1:
        cnt += (n - num.most_common()[0][1])

print(answer)
print(cnt)
