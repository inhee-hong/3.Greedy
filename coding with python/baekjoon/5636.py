# my code

import math

def prime(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

prime_list = prime(100001)

for _ in range(1001):
    n = input()
    
    if n == '0':
        break
    else:
        max_ = 0
        for primes in prime_list:
            if str(primes) in n:
                if max_ < primes:
                    max_ = primes

        print(max_)
