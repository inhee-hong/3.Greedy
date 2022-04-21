# my_code

def solution(n, build_frame):
    answer = [[]]
    
    a = []
    b = []
    for i in range(len(build_frame)):
        if build_frame[i][2] == 0 and buile_frame[i][3] == 1:
            if (build_frame[i][1] == 0) or (([build_frame[i][0], build_frame[i][1]]) in b) or (([build_frame[i][0], build_frame[i][1]]) in a):
                a.append([build_frame[i][0], build_frame[i][1]+1])
                set(a)
            else:
                continue
                
        elif build_frame[i][2] == 1 and buile_frame[i][3] == 1:
            if (([build_frame[i][0], build_frame[i][1]] or [build_frame[i][0]+1, build_frame[i][1]]) in a) or (([build_frame[i][0], build_frame[i][1]] and [build_frame[i][0]+1, build_frame[i][1]]) in b):
                b.append([build_frame[i][0], build_frame[i][1]])
                b.append([build_frame[i][0]+1, build_frame[i][1]])
                set(b)
            else:
                continue
            
        elif build_frame[i][2] == 0 and buile_frame[i][3] == 0:
            if a.remove([build_frame[i][0], build_frame[i][1]])
            remove()
            
        elif build_frame[i][2] == 1 and buile_frame[i][3] == 0:
    
    return answer
