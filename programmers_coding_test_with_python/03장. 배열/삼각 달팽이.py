# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    # 입력 받을 삼각형 형태 만들어주기
    triangle = [[0 for _ in range(i+1)] for i in range(n)]
    
    # now : 현재 상태(아래로 갈지, 오른쪽으로 갈지, 위로 갈지 방향 정하는 기준)
    # num : 달팽이에 채워 넣을 수
    # x, y : 현재 좌표
    now, num = 1, 1
    x, y = 0, 0
    # n부터 시작해서 한 방향으로 달팽이를 채우면, 다음 방향은 1번 덜 채워도 된다.
    for i in range(n, 0, -1):
        for j in range(i):
            # 아래로 갈 때
            if now % 3 == 1:   
                triangle[x][y] = num
                x += 1
            
            # 오른쪽으로 갈 때
            elif now % 3 == 2:
                triangle[x-1][y+1] = num
                y += 1
            
            # 위로 갈 때
            elif now % 3 == 0:
                triangle[x-2][y-1] = num
                x -= 1
                y -= 1
            # 채워 넣을 수 업데이트
            num += 1
        # 방향 업데이트
        now += 1
    
    # 달팽이를 채운 값들을 answer에 넣어주기
    for lst in triangle:
        answer += lst
        
    return answer