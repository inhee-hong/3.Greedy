# my answer
## 풀이 : B가 홀수일 때, 짝수일 때를 구분하여 생각해보자. 또한, 연산과정을 거꾸로 생각하여 B에서 A를 만들어보자.
## B가 짝수일 때는 2를 나누어주고, 홀수일 때는 가장 오른쪽에 있는 1을 빼준다. 그 외에는 간단한 조건들만 더 추가해서 풀어보자.

a, b = map(int, input().split())
cnt = 0
while b > a:
    if b % 2 != 0:
        if str(b)[-1] == '1':
            b = int(str(b)[:-1])
            cnt += 1
        else:
            break
    else:
        b = b // 2
        cnt += 1
if a == b:
    print(cnt+1)
else:
    print(-1)