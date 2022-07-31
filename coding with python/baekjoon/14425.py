# my code

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

cnt = 0
for j in range(m):
    k = input()
    if k in s:
        cnt += 1
print(cnt)
