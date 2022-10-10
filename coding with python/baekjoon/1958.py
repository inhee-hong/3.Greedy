one = input()
two = input()
three = input()

arr = [[[0] * (len(three)+1) for _ in range(len(two)+1)] for _ in range(len(one)+1)]

for i in range(1, len(one)+1):
    for j in range(1, len(two)+1):
        for k in range(1, len(three)+1):
            if one[i-1] == two[j-1] and two[j-1] == three[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = -1

for i in range(len(one)+1):
    for j in range(len(two)+1):
        ans = max(max(arr[i][j]), ans)

print(ans)
