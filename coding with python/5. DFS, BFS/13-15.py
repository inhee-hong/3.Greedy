from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
print(graph)

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
print(graph)

# 모든 도시에 대한 최단 거리 초기화    
distance = [-1] * (n + 1)
print(distance)
distance[x] = 0
print(x)
print(distance)

# BFS 수행
q = deque([x])
print(q)
while q:
    now = q.popleft()
    print(now)
    
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            print(q)
            print(distance)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)
