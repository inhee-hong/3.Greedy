# my code

n = int(input())
m = int(input())

graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
def dfs(v): 
    global cnt
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1


visited = [False] * (n+1)      

dfs(1)
print(cnt)
