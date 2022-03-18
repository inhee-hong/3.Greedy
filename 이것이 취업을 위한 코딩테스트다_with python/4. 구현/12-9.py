# my code

s = input()

# 약수 구하기
num = []
for i in range(1, len(s) + 1):
    if len(s) % i == 0:
        num.append(i)

_len = []
ans = []
for j in num:
    length = j
    _len = [s[k:k+length] for k in range(0, len(s), length)]
    
    cnt = 1
    n = ''
    for a in range(len(_len)-1):
        if _len[a] == _len[a+1] and a == len(_len) - 2:
            cnt += 1
            if cnt != 1:
                n += str(cnt)
                n += _len[a]
        elif _len[a] != _len[a+1] and a == len(_len) - 2:
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
        
print(min(ans))
