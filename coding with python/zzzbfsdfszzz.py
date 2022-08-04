# 기본 코드

######## DFS ############

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
visited = [False] * (n+1)

#########################


########## BFS ##########

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

########################


# 좌표평면

########### DFS ###############

def dfs(x, y):

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = -1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                dfs(nx, ny)
                
########################

########## BFS ##########

def bfs(x, y):

    queue = deque([(x, y)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:

        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            ans += 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = -1
                    
################################
