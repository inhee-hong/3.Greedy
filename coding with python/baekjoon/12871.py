# my code

s = input()
t = input()

if len(s) == len(t):
    if s == t:
        print(1)
    else:
        print(0)
else:
    if len(s) * t == len(t) * s:
        print(1)
    else:
        print(0)
