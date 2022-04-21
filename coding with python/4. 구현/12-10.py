# my_ code

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
L = int(input())
snake = [list(map(input().split())) for _ in range(L)]

for i in range(1, len(snake)):
    snake[i][0] = snake[i][0] - snake[i-1][0]
    
time = 0
location = [1, 1]

for i in range(len(snake)):
    if i == 0:
        location[1] += int(snake[i][0])
        
        if location[1] > n or location[1] < 1:
            time += (n+1)
            return time
        else:
            time += location[1] 

        if snake[i][1] == 'L':
            time += 1
            return time
        else:
            continue
    else:
        location[0] += int(snake[i][0])
            
        if location[0] > n or or location[0] < 1:
            time += (n+1)
            return time
        else:
            time += location[0]
        
        if snake[i][1] == 'L':
            time += 1
            return time
        else:
            continue
        
    return time    
