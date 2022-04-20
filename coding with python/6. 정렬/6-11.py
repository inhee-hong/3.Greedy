# my_code

N = int(input())
student = [list(input().split()) for _ in range(N)]

#dict(student)

new_student = sorted(dict(student).items(), key=lambda x: x[1])

for i in range(len(new_student)):
    print(new_student[i][0], end=' ')
    
---------------------------------------------------------------------

# answer

n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))
  
array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')
