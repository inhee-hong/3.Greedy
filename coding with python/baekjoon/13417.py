# my code

from collections import deque

n = int(input())
for i in range(n):
    m = int(input())
    lists = list(map(str, input().split()))
    ans = deque()
    for j in range(m):
        if j == 0:
            ans.append(lists[j])
        else:
            if ans[0] < lists[j]:
                ans.append(lists[j])
            else:
                ans.appendleft(lists[j])
                
    print(''.join(ans))
