# my answer
## 풀이
## 시간이 가장 적게 걸리는 순서대로 나열한 후, 문제와 같이 걸리는 시간을 구한다면 성공!

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
ans = 0
for i in range(n):
    ans += lst[i]*(n-i)
print(ans)