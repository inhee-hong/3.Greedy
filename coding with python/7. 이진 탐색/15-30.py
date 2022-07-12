# my code

def solution(words, queries):
    answer = []
    
    for i in range(len(queries)):
        cnt = queries[i].count('?')
        
        if cnt == 5:
            new = 0
            for j in words:
                if len(j) == len(queries[i]):
                    new += 1
            answer.append(new)
        else:
            if queries[i][0] == '?':
                new = 0
                word = queries[i][cnt:]
                #print(word)
                for j in words:
                    if j.endswith(word) == True and len(j) == len(queries[i]):
                        new += 1
                answer.append(new)
            else:
                new = 0
                word = queries[i][:len(queries[i]) - cnt]
                #print(word)
                for j in words:
                    if j.startswith(word) == True and len(j) == len(queries[i]):
                        new += 1
                answer.append(new)
                
    return answer
    
  # 45점
