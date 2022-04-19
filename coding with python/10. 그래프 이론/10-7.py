# my_code

n, m = map(int, input().split())
team = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    if team[i][0] == 1:
        if team[i][1] == team[i][2]:
            print('YES')
        else:
            print('NO')
 
