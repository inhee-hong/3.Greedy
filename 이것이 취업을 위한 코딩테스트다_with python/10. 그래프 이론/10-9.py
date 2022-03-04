# code_err

n = int(input())
Q = [list(map(int, input().split())) for _ in range(n)]

number = []
for i in range(n):
    number.append(Q[i][0])

for i in range(n):
    sum = 0
    sum += Q[i][0]
    for j in range(1,len(Q[i])+1):
        if Q[i][j] == -1:
            break
        else:
            sum += number[Q[i][j]-1]
    print(sum)
