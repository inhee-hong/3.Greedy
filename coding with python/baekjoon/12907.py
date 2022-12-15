## 도움 받았습니다
# 솔루션

# 1. 숫자의 갯수를 세는 배열을 하나 생성한다.
# 2. 생성한 배열을 돌며 조건에 어긋나는지 확인
# 3. 확인하는 숫자는 이전에 확인한 숫자의 갯수보다 많아선 안된다.
# 4. 1이 등장하면 조건에 어긋나지 않는 이상 경우의 수에 변화를 줄 수가 없다.
N = int(input())
check = [0] * 41
lst = list(map(int, input().split()))
# 각 숫자의 갯수 세기
for n in lst:
    check[n] += 1
before = 2
result = False
# 숫자를 차례대로 돌며 갯수를 확인
# 이전 숫자보다 갯수가 많으면 안된다
for cnt in check:
    if cnt > before:
        result = True
        break
    before = cnt

if result:
    print(0)
# 처음에 1 하나만 있는 경우에도 갯수는 두 가지
# 갯수가 1이 나온 이후에는 어떤 숫자가 나와도 더 이상 결과 값에 영향을 미치지 않는다.
else:
    print(1 << check.count(2) + (1 in check))