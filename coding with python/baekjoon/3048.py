# my code

n1, n2 = map(int, input().split())
n1_list = list(input())
n2_list = list(input())
T = int(input())

lists = n1_list[::-1] + n2_list

for _ in range(T):
    for i in range(len(lists) - 1):
        if lists[i] in n1_list and lists[i+1] in n2_list:
            lists[i], lists[i+1] = lists[i+1], lists[i]
            
            if lists[i+1] == n1_list[0]:
                break
                
print(''.join(lists))
