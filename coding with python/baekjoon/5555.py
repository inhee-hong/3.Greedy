# my code

s = input()
n = int(input())

ans = 0
for i in range(n):
    strs = input()
    new_str = strs + strs
    if s in new_str:
        ans += 1
print(ans)     
