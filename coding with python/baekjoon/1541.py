# my code

s = list(input().split('-'))

lists = []
for i in range(len(s)):
    if '+' in s[i]:
        ans = 0
        new = list(s[i].split('+'))
        for j in range(len(new)):
            ans += int(new[j])
        lists.append(ans)
    else:
        lists.append(int(s[i]))
        
answer = 0
for k in range(len(lists)):
    if k == 0:
        answer += int(lists[k])
    else:
        answer -= int(lists[k])
        
print(answer)
