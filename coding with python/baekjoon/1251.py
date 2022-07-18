# my code

s = input()
ans = []

for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        first = s[:i][::-1]
        second = s[i:j][::-1]
        third = s[j:][::-1]
        
        ans.append(first + second + third)

ans = sorted(ans)
print(ans[0])
