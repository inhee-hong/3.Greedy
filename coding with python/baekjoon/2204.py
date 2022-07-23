# my code

while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        word_list = []
        for i in range(n):
            a = input()
            b = a.lower()
            word_list.append([a, b])
        
        word_list.sort(key =  lambda x : x[1])
    print(word_list[0][0])
