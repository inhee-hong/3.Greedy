# my code

n = int(input())

number_list = []
for _ in range(n):
    word = list(input())
    num = ''
    
    for i in range(len(word)-1):
        if word[i].isdigit() == True:
                num += word[i]
        else:
            if len(num) != 0:
                number_list.append(int(num))
                num = ''

    if word[-1].isdigit() == True:
        num += word[-1]
        number_list.append(int(num))
    else:
        if len(num) != 0:
            number_list.append(int(num))
    
number_list.sort()

for j in range(len(number_list)):
    print(number_list[j])
