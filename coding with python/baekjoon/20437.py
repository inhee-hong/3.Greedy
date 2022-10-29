from collections import defaultdict

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    
    len_text = len(W)
    
    W_alpha = defaultdict(list)
    
    for i in range(len_text):
        if W.count(W[i]) >= K:
            W_alpha[W[i]].append(i)
    
    if not W_alpha:
        print(-1)
    else:
        min_str = 10000
        max_str = 0
        
        for p in W_alpha.values():
            for q in range(len(p)-K+1):
                temp = p[q+K-1] - p[q] + 1
                
                if temp < min_str:
                    min_str = temp
                
                if temp > max_str:
                    max_str = temp
                    
        print(min_str, max_str)
