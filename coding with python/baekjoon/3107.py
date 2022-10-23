# my code

data = input()
ans = ''

datas = []
data_split = data.split(':')
for k in range(len(data_split)):
    if data_split[k] == '':
        if ' ' not in datas:
            datas.append(' ')
        else:
            continue
    else:
        datas.append(data_split[k])


for i in range(len(datas)):
    
    if i == len(datas)-1:
        if len(datas[i]) == 4:
            ans += datas[i]
            
        elif datas[i] == ' ':
            cnt = (8 - len(datas) + 1)
            for j in range(cnt):
                if j == cnt-1:
                    ans += '0000'
                else:
                    ans += '0000:'
        
        elif 1 <= len(datas[i]) < 4:
            ans += ('0' * (4-len(datas[i])))
            ans += datas[i]


    elif len(datas[i]) == 4:
            ans += datas[i]
            ans += ':'
            
    elif datas[i] == ' ':
        cnt = (8 - len(datas) + 1)
        for j in range(cnt):
            ans += '0000:'    
                
    elif 1 <= len(datas[i]) < 4:
        ans += ('0' * (4-len(datas[i])))
        ans += datas[i]
        ans += ':'
            
print(ans)
