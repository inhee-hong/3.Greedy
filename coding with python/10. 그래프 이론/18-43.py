
n, m = map(int, input().split())
road = []
total_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    road.append([z, x, y])
    total_cost += z
    
road.sort()

# 부모 테이블 초기화
parent = [0] * (n+1)
for j in range(1, n+1):
    parent[j] = j

    
# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
mini_cost = 0
for roads in road:
    cost, a, b = roads
    
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        mini_cost += cost
        
print(total_cost - mini_cost)
