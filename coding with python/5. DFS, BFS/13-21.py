from collections import deque

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 인접한 국가 찾을 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def process(x, y, union_id):
    # 연합 국가 좌표 담을 리스트와 큐 정의
    united_x_y = []
    united_q = deque([])
    # 현재 x,y 좌표 append
    united_x_y.append((x, y))
    united_q.append((x, y))
    # 연합 인구 계산할 변수들
    union[x][y] = union_id
    summary = graph[x][y]
    count = 1
    # 큐가 빌 때까지 반복
    while united_q:
        x, y = united_q.popleft()
        # 인접 국가 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(graph[x][y]-graph[nx][ny]) <= R:
                    union[nx][ny] = union_id
                    united_x_y.append((nx, ny))
                    united_q.append((nx, ny))
                    summary += graph[nx][ny]
                    count += 1
    # 연합된 국가들 인구 갱신
    for i, j in united_q:
        graph[i][j] = summary // count


total_count = 0  # 인구 이동 횟수
while True:
    union = [[-1] * N for _ in range(N)]  # 연합처리되었는지 확인할 2d 리스트
    union_id = 0  # 연합 ID
    # 주어진 graph 정보에서 원소 하나씩 연합 처리 시작
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1: # 연합이 되지 않은 국가들만 처리
                process(i, j, union_id)
                union_id += 1

    if union_id == (N*N):
        break
    total_count += 1

print(total_count)
