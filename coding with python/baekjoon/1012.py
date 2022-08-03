# my code

import sys
sys.setrecursionlimit(10000)


T = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)

for _ in range(T):                
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1


    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[a][b] > 0:
                dfs(a, b)
                cnt += 1

    print(cnt)
    
    
    
## 런타임 에러를 방지하기위해 맨 앞에 두 줄을 써주었다
