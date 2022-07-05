# my code

from collections import deque

n = int(input())

lists = deque(i for i in range(1, n+1))


while len(lists) != 1:
    lists.popleft()
    lists.rotate(-1)
print(lists[0])
