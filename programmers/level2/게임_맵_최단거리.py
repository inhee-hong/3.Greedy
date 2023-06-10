from collections import deque

def bfs(x, y, maps):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])):
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = (maps[x][y] + 1)
                    
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = 0
    
    num = bfs(0, 0, maps)
    
    if num == 1:
        return -1
    else:
        return num