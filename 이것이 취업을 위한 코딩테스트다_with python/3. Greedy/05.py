# my_code

n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()

ans = 0
cnt = 0
for i in range(n-1):
    if ball[i] != ball[i+1]:
        if cnt == 0:
            ans += (n - (i+1))
        else:
            cnt += 1
            ans += (n - (i+1)) * cnt
            cnt = 0
    else:
        cnt += 1

print(ans)
