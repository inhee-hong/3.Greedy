# my_code

N = int(input())
A = [int(input()) for _ in range(N)]

A.sort(reverse = True)

for i in A:
    print(i, end=' ')
_________________________________________________
# answer

n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
  print(i, end=' ')
