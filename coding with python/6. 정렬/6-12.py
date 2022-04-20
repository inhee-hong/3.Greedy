# my_code

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    A.sort()
    B.sort()
    if A[0] >= B[K+1]:
        break
    else:
        A[0], B[K+1] = B[K+1], A[0]

print(sum(A))

-----------------------------------------------

# answer

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))
