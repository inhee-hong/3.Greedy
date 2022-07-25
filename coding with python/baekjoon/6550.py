# my code

while True:
    try:
        a, b = map(str, input().split())

        j = 0
        for i in range(len(b)):
            if a[j] == b[j]:
                if len(a) == (j+1):
                    if len(a) != len(b):
                        b = b[:j+1]
                        break
                else:
                    j += 1
                    continue
            else:
                b = b[:j] + b[j+1:]

        if a == b:
            print('Yes')
        else:
            print('No')
            
    except:
        break
