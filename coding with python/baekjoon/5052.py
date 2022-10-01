# my code

def solution(stack):
    for i in range(n-1):
        if stack[i] == stack[i+1][:len(stack[i])]:
            return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    stack = []
    for _ in range(n):
        stack.append(input())
        
    stack.sort()
    
    print(solution(stack))
