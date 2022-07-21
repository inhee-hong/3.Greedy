# my code

n = int(input())
fight = list(map(int, input().split()))

fight = fight[::-1]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if fight[j] < fight[i]:
            dp[i] = max(dp[i], dp[j]+1)
           
print(n - max(dp))
