# my code

n = int(input())

five_num = n // 5
tmp = five_num
ans = 0

if (n - five_num*5) % 3 == 0:
    print(five_num + ((n - five_num*5) // 3))
    ans += 2
else:
    for i in range(five_num):
        tmp -= 1
        if (n - tmp*5) % 3 == 0:
            ans += 1
            break
            
if ans == 0:
    print(-1)
elif ans == 1:
    print(tmp + ((n - tmp*5) // 3))
