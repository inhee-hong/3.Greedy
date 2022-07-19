# my code

a, b = map(str, input().split())

ans = []

if len(a) == len(b):
    num = 0
    for k in range(len(a)):
        if a[k] != b[k]:
            num += 1
    print(num)
else:
    for i in range(len(b) - len(a)+1):
        num = 0
        c = b[i:i+len(a)]

        for j in range(len(a)):
            if a[j] != c[j]:
                num += 1
        ans.append(num)
    print(min(ans))
