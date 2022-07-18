# my code

n = int(input())
input_list = [input() for _ in range(n)]
output_list = [input() for _ in range(n)]

ans = 0
for i in range(n):
    if input_list.index(output_list[i]) > i:
        ans += 1
        
print(ans)
