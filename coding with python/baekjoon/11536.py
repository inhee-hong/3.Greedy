# my code

n = int(input())
name_list = []
for i in range(n):
    name = input()
    name_list.append(name)
    
if sorted(name_list) == name_list:
    print('INCREASING')
elif sorted(name_list, reverse = True) == name_list:
    print('DECREASING')
else:
    print('NEITHER')
