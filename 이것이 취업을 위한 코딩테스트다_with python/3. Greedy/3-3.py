# my_code

N, M = map(int, input().split())

sum = []
for i in range(N):
  n = list(map(int, input().split()))
  sum.append(min(n))

print(max(sum))
