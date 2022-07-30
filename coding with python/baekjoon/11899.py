# my code

s = input()

ans1 = 0
ans2 = []

if s[0] == '(':
    ans2.append(s[0])
else:
    ans1 += 1
        
for i in range(1, len(s)):
    if s[i] == '(':
        ans2.append(s[i])

    else:
        if len(ans2) != 0:
            ans2 = ans2[:-1]
        else:
            ans1 += 1
            
print(len(ans2) + ans1)  
