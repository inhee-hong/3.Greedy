# my code

n, m = map(int, input().split())
see = set()
for i in range(n):
    see.add(input())

listen = set()
for j in range(m):
    listen.add(input())
        
answer = sorted(list(see & listen))

print(len(answer))
for k in answer:
    print(k)
    
    
## set을 이용해야 시간초과가 안뜸
