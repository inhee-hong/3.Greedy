# my code

n = int(input())
graph = [[]*n for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v): 
    for j in graph[v]:
        if visited[j] == 0:
            visited[j] = v
            dfs(j)

visited = [0] * (n+1)  

dfs(1)

for k in range(2, n+1):
    print(visited[k])
    
# dfs는 항상 부모에서 자식으로 이동하는 점 이용

# 주의할 점!!
# 기본적으로 반복은 1000회로 되어 있기 때문에, sys.setrecursionlimit(10**9)로 늘려주어야 한다.
# (재귀를 사용해서 풀어야하는 문제라면, 이 코드는 거의 필수이다.)
