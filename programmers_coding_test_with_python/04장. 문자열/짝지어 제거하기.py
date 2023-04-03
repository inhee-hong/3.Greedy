# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for i in range(len(s)):
        # stack이 비었으면 채워주기
        if len(stack) == 0:
            stack.append(s[i])
        # stack의 마지막 값과 현재 비교할 값이 같으면(같은 알파벳이 2개 붙어 있으면) 제거해주기
        elif s[i] == stack[-1]:
            stack.pop()
        # 나머지 경우 stack에 값을 넣어주기
        else:
            stack.append(s[i])
            
    if not stack:
        return 1
    else:
        return 0