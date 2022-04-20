# my_code

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(input())
N_store = list(map(int, input().split()))
M = int(input())
M_store = list(map(int, input().split()))

N_store.sort()

for i in range(M):
    answer = binary_search(N_store, M_store[i], 0, N-1)
    
    if answer == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
