# my code

n, x = map(int, input().split())
h = list(map(int, input().split()))

# x와 같은 값의 인덱스 찾기
def find_mids(n, x, h):
    first = 0
    end = n - 1
    mid = (first + end) // 2
    
    while h[mid] != x:

        if h[mid] < x:
            first = mid + 1
            mid = (first + end) // 2

        elif h[mid] > x:
            end = mid - 1
            mid = (first + end) // 2
    
    return mid

# mid_left 찾기
def find_lefts(n, x, h):
    first_left = 0
    end_left = mid
    mid_left = (first_left + end_left) // 2

    before = mid_left
    now = mid_left

    while first_left <= end_left:

        if h[mid_left] == x:
            end_left = mid_left - 1
            mid_left = (first_left + end_left) // 2
            now = mid_left

            if abs(now - before) == 1 and h[now] != h[before]:
                if h[now] == x:
                    mid_left = now
                else:
                    mid_left = before
                break

            else:
                before = mid_left

        elif h[mid_left] != x:
            first_left = mid_left + 1
            mid_left = (first_left + end_left) // 2
            now = mid_left

            if now - before == 1 and h[now] != h[before]:
                if h[now] == x:
                    mid_left = now
                else:
                    mid_left = before
                break

            else:
                before = mid_left
    
    return mid_left
        

# mid_right 찾기        
def find_rights(n, x, h):       
    first_right = mid
    end_right = n - 1
    mid_right = (first_right + end_right) // 2

    before = mid_right
    now = mid_right

    while first_right <= end_right:

        if h[mid_right] != x:
            end_right = mid_right - 1
            mid_right = (first_right + end_right) // 2
            now = mid_right

            if abs(now - before) == 1 and h[now] != h[before]:
                if h[now] == x:
                    mid_right = now
                else:
                    mid_right = before
                break

            else:
                before = mid_right

        elif h[mid_right] == x:
            first_right = mid_right + 1
            mid_right = (first_right + end_right) // 2
            now = mid_right

            if now - before == 1 and h[now] != h[before]:
                if h[now] == x:
                    mid_right = now
                else:
                    mid_right = before
                break

            else:
                before = mid_right
                
    return mid_right


if x in h:
    print(mid_right - mid_left + 1)
else:
    print(-1)
