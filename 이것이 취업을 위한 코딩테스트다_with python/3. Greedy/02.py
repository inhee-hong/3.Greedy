# my code

s = input()

ans = 0

for i in range(len(s)):
    if ans == 0 or ans == 1:
        ans += int(s[i])
    elif s[i] == 0 or s[i] == 1:
        ans += int(s[i])
    else:
        ans *= int(s[i])

print(ans)
