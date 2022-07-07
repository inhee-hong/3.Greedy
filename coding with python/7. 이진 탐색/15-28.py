# my code

n = int(input())
a = list(map(int, input().split()))

first = 0
end = n-1
mid = (first + end) // 2

ans = -1

while first <= end:
    
    if first == a[first]:
        ans = a[first]
        break
    elif end == a[end]:
        ans = a[end]
        break
    else:
        if a[mid] < mid:
            first = mid + 1
            mid = (first + end) // 2
        elif a[mid] > mid:
            end = mid - 1
            mid = (first + end) // 2
        else:
            ans = a[mid]
            break
print(ans)
