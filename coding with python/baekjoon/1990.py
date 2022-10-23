# my code

a, b = map(int, input().split())

def prime_list(num, n):
    if n >= 10000000:
        n = 10000000
        
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n+1, i): 
                sieve[j] = False

    return [i for i in range(num, n+1) if sieve[i] == True]

def palindrome(N):
    for k in range(len(str(N))//2):
        if str(N)[k] == str(N)[-k-1]:
            continue
        else:
            return False
    return True

lists = prime_list(a, b)
for ans in lists:
    if palindrome(ans):
        print(ans)
print(-1)
