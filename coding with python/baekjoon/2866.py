# my code

from collections import Counter

r, c = map(int, input().split())
ans = r
cnt = 0

alpha = ['' for _ in range(c)]
for i in range(r):
    text = input()
    for j in range(c):
        alpha[j] += (text[j])

for k in range(ans):
    over = Counter(alpha).most_common()[0][1]
    if over > 1:
        break
    else:
        cnt += 1
        if len(alpha[0]) == 1:
            break
        else:
            for q in range(len(alpha)):
                alpha[q] = alpha[q][1:]
            
print(cnt-1)
