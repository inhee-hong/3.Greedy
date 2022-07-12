# my code

from collections import deque

n, m, v = map(int, input().split())
graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(len(graph)):
    graph[j].sort()
    
    
def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    
    
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

visited = [False] * (n+1)

visited_bfs = [False] * (n+1)
                
dfs(v)
print()
bfs(v)


# 정점 번호가 작은 것을 먼저 방문하므로, graph를 sort해주자
