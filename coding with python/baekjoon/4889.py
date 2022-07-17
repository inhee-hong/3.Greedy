# my code

from collections import deque 

number = 0

while True:
    n = input()
    answer = 0
    
    if '-' in n:
        break
        
    else:
        queue = deque(n)
        answer = 0
        puts = []
        number += 1
        for i in range(len(queue)):
            if len(queue) == 0:
                break
            else:
                if len(puts) == 0:
                    if queue[0] == '{':
                        puts.append(queue[0])
                        queue.popleft()
                    else:
                        answer += 1
                        puts.append('{')
                        queue.popleft()
                else:
                    if queue[0] == '{':
                        puts.append(queue[0])
                        queue.popleft()
                    else:
                        if puts[-1] == '{':
                            puts.pop()
                            queue.popleft()
        answer += len(puts) // 2
        print(number , '. ' , answer, sep = '')     
