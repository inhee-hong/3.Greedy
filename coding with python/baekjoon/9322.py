# my code

T = int(input())
for _ in range(T):
    n = int(input())
    key_1 = list(map(str, input().split()))
    key_2 = list(map(str, input().split()))
    password = list(map(str, input().split()))
    
    lists = [0 for _ in range(n)]
    
    for i in range(n):
        index = key_1.index(key_2[i])
        lists[index] = password[i]
        
    print(' '.join(lists))
