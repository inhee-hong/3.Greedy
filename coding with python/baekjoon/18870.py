# my code

n = int(input())
lists = list(map(int, input().split()))

arr = list(sorted(set(lists)))
dictionary = {arr[i]: i for i in range(len(arr))}

for j in lists:
    print(dictionary[j], end = ' ')
