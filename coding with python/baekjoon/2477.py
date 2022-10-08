# my code

from collections import deque

k= int(input())
distance_ew = []
distance_ns = []
distance_total = deque()
e, w, s, n, small = 0, 0, 0, 0, 0

for _ in range(6):
    way, distance = map(int, input().split())
    distance_total.append([way, distance])
    
    if way == 1:
        distance_ew.append(distance)
        e += 1
            
    elif way == 2:
        distance_ew.append(distance)
        w += 1
            
    elif way == 3: 
        distance_ns.append(distance)
        s += 1
            
    elif way == 4: 
        distance_ns.append(distance)
        n += 1
        
if n == 2 and w == 2:
    while distance_total[0][0] != 3:
        distance_total.rotate(-1)
        
    small = distance_total[-2][1] * distance_total[-3][1]
    
elif e == 2 and s == 2:
    while distance_total[0][0] != 4:
        distance_total.rotate(-1)
        
    small = distance_total[-2][1] * distance_total[-3][1]
    
elif w == 2 and s == 2:
    while distance_total[0][0] != 1:
        distance_total.rotate(-1)
        
    small = distance_total[-2][1] * distance_total[-3][1]
    
elif e == 2 and n == 2:
    while distance_total[0][0] != 2:
        distance_total.rotate(-1)
        
    small = distance_total[-2][1] * distance_total[-3][1]

big = max(distance_ew) * max(distance_ns)
sol = (big - small) * k

print(sol)
