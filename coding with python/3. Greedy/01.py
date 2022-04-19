# my_code

n = int(input())
scary = list(map(int, input().split()))
scary.sort(reverse = True)

num = n
cnt = 0
i = 0
while True:
    if num >= scary[i]:
        if i == len(scary) - 1:
            if scary[i] == 1:
                cnt += 1
                break
            else:
                break
        else:
            cnt += 1
            num -= scary[i]
            if num == 0:
                break
            else:
                i += scary[i]

    else:
        break
        
print(cnt)
 
