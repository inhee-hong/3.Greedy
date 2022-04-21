# my_code

A = input()

count = 0
A_new = []

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8 }

A_new.append(dict[A[0]])
A_new.append(int(A[1]))

move = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, -2],[-1, 2], [1, -2],[1, 2]]

for i in range(8):
  A_new2 = []
  A_new2.append(A_new[0] + move[i][0])
  A_new2.append(A_new[1] + move[i][1])
  if A_new2[0] > 0 and A_new2[1] > 0 and A_new2[0] < 9 and A_new2[1] < 9:
    count += 1

print(count)
