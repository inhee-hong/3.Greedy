# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):    
    dp = [0 for _ in range(n+1)]
    
    if n == 2:
        return 1
    else:
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567