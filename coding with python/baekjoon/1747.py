# my code

import math

n = int(input())

def palindrome(num):
    for i in range(len(str(num))//2):
        if str(num)[i] == str(num)[-i-1]:
            continue
        else:
            return False
    return True


def prime(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]


for num in prime(1100000):
    if num >= n:
        if palindrome(num) == True:
            print(num)
            break
