# answer

N, M = map(int, input().split())
money = [int(input()) for i in range(N)]

d = [10001] * (M + 1)

d[0] = 0
for i in range(N):
    for j in range(money[i], M + 1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j - money[i]] + 1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
