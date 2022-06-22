# my code

n = int(input())
lists = list(map(int, input().split()))

ans = n
for i in lists:
    # 1은 소수가 아니므로 제거
    if i == 1:
        ans -= 1
        continue
    else:
        # 소수 찾기 위한 조건
        for j in range(2, i):
            if i % j == 0:
                ans -= 1
                break
        
print(ans)
