# my code

n = int(input())

dp = [1, 2, 3, 5]

two = 2
three = 3
five = 5

dp
for i in range(2, n):
    two_ = two *  i
    three_ = three *  i
    five_ = five * i
    dp.append(two_)
    dp.append(three_)
    dp.append(five_)
    dp = list(set(dp))

print(dp[n-1])
