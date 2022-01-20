# my_code
N = int(input())

N_500 = N // 500
N = N % 500
N_100 = N // 100
N = N % 100
N_50 = N // 50
N = N % 50
N_10 = N // 10
N = N % 10

sum = N_500 + N_100 + N_50 + N_10
print(sum)



# answer
count = 0
n = 1260

coin_types = [500,100,50,10] #큰 단위의 화폐부터 차례대로 확인

for coin in coin_types:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
