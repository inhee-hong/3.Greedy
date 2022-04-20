# my_code

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

ans = coin[0]
for i in range(1, len(coin)):
    if coin[i] > ans:
        break
    ans += coin[i] 

print(ans+1)   
