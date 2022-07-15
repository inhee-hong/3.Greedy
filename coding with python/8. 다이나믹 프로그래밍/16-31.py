# my code

#1 3 3 2 2 1 4 1 0 6 4 7
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))
    print(gold)
    dp = []
    index = 0
    max_value = 0
    first = 0
    for j in range(n):
        a = []
        a.append(gold[index])
        if j == 0:
            max_value = gold[index]
            first = j
        else:
            if max_value < gold[index]:
                max_value = gold[index]
                first = j
        index += 1
        a.append(gold[index])
        index += 1
        a.append(gold[index])
        index += 1
        a.append(gold[index])
        index += 1
        dp.append(a)
    #print(dp)
    #print(max_value)
    #print(first)
    

    now = max_value
    ans = now
    max_index = first
    
    for p in range(1, m):
        max_values = 0
    
        if now_left == 0:
            for q in range(2):
                if max_values < dp[now_left + q][p]:
                    max_values = dp[now_left + q][p]
                    max_index = (now_left + q)
                    
        elif now_left == (n - 1):
            for q in range(2):
                if max_values < dp[now_left - 1 + q][p]:
                    max_values = dp[now_left - 1 + q][p]
                    max_index = (now_left - 1 + q)
                    
        else:
            for q in range(3):
                if max_values < dp[now_left - 1 + q][p]:
                    max_values = dp[now_left - 1 + q][p]
                    max_index = (now_left - 1 + q)
        
        ans += max_values
        #print(ans)
        #print('max_values : ', max_values)
        #print('max_index : ', max_index)
        #print('p : ', p)
        #print('---------------')
    print(ans)
