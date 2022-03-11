# my_code

def solution(food_times, k):
    ans = 0    
    i = 0
    
    all_time = 0
    for j in range(len(food_times)):
        all_time += food_times[j]
        
    while True:
        if ans == k:
            break
        else:
            if food_times[i] > 0:
                food_times[i] -= 1
                ans += 1
                if i+1 == len(food_times):
                    i = 0
                else:    
                    i += 1
            else:
                if ans == all_time:
                    break
                else:
                    if i+1 == len(food_times):
                        i = 0
                    else:    
                        i += 1
    return i + 1
