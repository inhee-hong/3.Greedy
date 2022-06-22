# my code

n = int(input())

def pibo(i):
    if i < 2:
        return i
    return pibo(i-1) + pibo(i-2)

print(pibo(n))
