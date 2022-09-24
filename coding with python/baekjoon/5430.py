# my code

from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    array = input().replace('[','').replace(']','').split(',')
    lists = deque()
    if n != 0:
        for j in array:
            lists.append(int(j))
        
    
    cnt, ans = 0, 0
    for i in range(len(p)):
        if p[i] == 'R':
            cnt += 1
        elif p[i] == 'D':
            if len(lists) == 0:
                ans += 1
                print('error')  
                break
            else:
                if cnt % 2 == 0:
                    lists.popleft()
                else:
                    lists.pop()
    
    if ans == 0:
        if cnt % 2 == 0:
            print(list(lists))
        else:
            lists.reverse()
            print(list(lists))           
