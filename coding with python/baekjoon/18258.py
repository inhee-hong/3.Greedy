## my code __ pypy로 채점해야 함

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n):
    word = input()
    
    if word[:4] == 'push':
        word = word.split()
        queue.append(word[1])
        
    elif word[:3] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif word[:4] == 'size':
        print(len(queue))
        
    elif word[:5] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif word[:5] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    elif word[:4] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
