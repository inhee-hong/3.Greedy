# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def ans(num, cnt):
    # 작업이 500번 이상 반복되면 -1을 return
    if cnt >= 501:
        return -1
    # 주어진 수가 1이 되는 경우, 작업 반복 횟수 return
    if num == 1:
        return cnt
    # 주어진 수가 짝수라면, 2로 나누기
    if num % 2 == 0:
        return ans(num / 2, cnt+1)
    # 주어진 수가 홀수라면, 3을 곱하고 1을 더하기
    if num % 2 == 1:
        return ans(3 * num + 1, cnt+1)

def solution(num):
    return ans(num, 0)