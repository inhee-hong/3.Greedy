# my code

n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

a.sort(reverse = True)

cnt = 0
for j in range(n):
    if a[j] <= k:
        cnt += (k // a[j])
        k -= ((k // a[j]) * a[j])
print(cnt)
