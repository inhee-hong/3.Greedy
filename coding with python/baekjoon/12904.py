# my code

S = input()
T = list(input())

while len(T) != len(S):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == (''.join(T)):
    print(1)
else:
    print(0)
