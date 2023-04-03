# https://school.programmers.co.kr/learn/courses/30/lessons/60057

################### 예전 풀이 #########################
def solution(s):

    _len = []
    ans = []
    for i in range(1,len(s)+1):
        length = i
        _len = [s[i:i+length] for i in range(0, len(s), length)]

        cnt = 1
        n = ''
        for a in range(len(_len)-1):
            if _len[a] == _len[a+1] and a == len(_len) - 2:
                cnt += 1
                if cnt != 1:
                    n += str(cnt)
                    n += _len[a]
            elif _len[a] != _len[a+1] and a == len(_len) - 2:
                if cnt != 1:
                    n += str(cnt)
                    n += _len[a]
                    n += _len[a+1]
                else:
                    n += _len[a]
                    n += _len[a+1]
            elif _len[a] == _len[a+1]:
                cnt += 1
            elif _len[a] != _len[a+1]:
                if cnt != 1:
                    n += str(cnt)
                    n += _len[a]
                    cnt = 1
                else:
                    n += _len[a]    

        ans.append(len(n))
    ans.append(len(s)) 
    ans.remove(0)
        
    return min(ans)
#################################################################

################# 새로운 풀이 ###################################
def solution(s):
    answer = len(s)
    
    # 문자열 길이의 절반 이상은 반복될 수 없다.
    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        cnt = 1
        # 1부터 반복되는 횟수를 넓혀서 찾아보기
        for i in range(0, len(s)+1, x):
            temp = s[i:i+x]
            if comp == temp:
                cnt += 1
            else:
                comp_len += len(temp)
                if cnt > 1:
                    comp_len += len(str(cnt))
                cnt = 1
                comp = temp
        answer = min(answer, comp_len)
    
    return answer
###############################################################