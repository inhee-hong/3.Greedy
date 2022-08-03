# my code

import sys
sys.setrecursionlimit(10000)

n, m =  map(int, sys.stdin.readline().split())

graph = [[] * (m+1) for _ in range(n+1)]

for _ in range(m):
    u, v =  map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for k in range(len(graph)):
    graph[k].sort()

cnt = 0 
def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
visited = [False] * (n+1)

for i in range(1, len(graph)):
    if visited[i] == False:
        dfs(i)
        cnt += 1
        
print(cnt)
