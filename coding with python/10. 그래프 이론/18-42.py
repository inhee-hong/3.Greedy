# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
g = int(input())
p = int(input())

root = []
parent = [0] * (p + 1) 
for i in range(1, p + 1) :
    parent[i] = i
    root.append(int(input()))

result = 0
for j in range(p) :

    data = find_parent(parent, root[j])
    if data == 0 : # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)
