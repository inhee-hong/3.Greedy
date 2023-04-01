# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    answer = []
    # 교점 구하기
    lst = []
    ##### 주의! max, min값을 1e9로 주면 런타임 에러뜬다!! 1e15로 주자... #####
    x_min, y_min = 1e15, 1e15
    x_max, y_max = -1e15, -1e15
    for i in range(len(line)):
        a, b, e = line[i]
        
        for j in range(i+1, len(line)):
            c, d, f = line[j]
            # 평행 또는 일치할 경우 구하지 않고 넘어감
            if a * d == b * c:
                continue
                
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            # 정수인 값들만 저장해주기
            if x == int(x) and y == int(y):
                lst.append((int(x), int(y)))
                # x, y좌표의 최대 최소점 찾기
                if x_min > x:
                    x_min = int(x)
                if x_max < x:
                    x_max = int(x)
                if y_min > y:
                    y_min = int(y)
                if y_max < y:
                    y_max = int(y)     
    # 배열을 생성하자. 문자열은 원하는 위치의 값만 변경할 수 없음 주의! => list로 만들어주기
    ans = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    # 교차점인 곳에는 *을 넣어주자
    for x, y in lst:
        nx = -y + y_max
        ny = x - x_min
        ans[nx][ny] = '*'
    # list 형태니까 str로 만들어주기
    for result in ans:
        answer.append(''.join(result))

    return answer