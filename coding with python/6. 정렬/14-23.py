# my_code
n = int(input())
lists = []
for i in range(n):
    a = tuple(map(str, input().split()))
    lists.append(a) 

lists = sorted(lists, key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in lists:
    print(j[0])
