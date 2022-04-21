# my_code

N = int(input())
A_list = list(input().split())

start = [1, 1]

for i in A_list:
  if i == 'L':
    if start[1] == 1:
      continue
    else:
      start[1] -= 1
  if i == 'R':
    if start[1] == 5:
      continue
    else:
      start[1] += 1
  if i == 'U':
    if start[0] == 1:
      continue
    else:
      start[0] -= 1
  if i == 'D':
    if start[0] == 5:
      continue
    else:
      start[0] += 1

print(start[0], start[1])
