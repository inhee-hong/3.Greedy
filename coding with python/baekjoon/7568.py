# my code

n = int(input())
lists = []
for i in range(n):
    new = []
    a, b = map(int, input().split())
    new.append(a)
    new.append(b)
    lists.append(new)


for j in range(n):
    cnt = 1
    for k in range(n):
        if lists[j][0] < lists[k][0] and lists[j][1] < lists[k][1]:
            cnt += 1
    print(cnt, end=' ')
