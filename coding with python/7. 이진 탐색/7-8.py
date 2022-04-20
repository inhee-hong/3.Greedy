# my_code

def binary_search2(array, target, start, end):
    if start > end:
        return None
    mid = (end + start) // 2 

    cnt = []
    for i in range(len(array)):
        if array[i] > mid:
            cnt.append(array[i] - mid)
    
    if sum(cnt) == target:
        return mid

    elif sum(cnt) < target:
        return binary_search2(array, target, start-1, end)

    elif sum(cnt) > target:
        return mid

N, M = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

answer = binary_search2(H, M, H[0], H[N-1])
print(answer)

------------------------------------------------------------------

# answer

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
