from collections import Counter

def solution(k, tangerine):
    answer = 0
    ans = 0
    
    # 귤 크기별로 개수 세어준 후, 큰 순서대로 나열되는 list 추출
    count_targerine = Counter(tangerine).most_common()
    for i in range(k):
        if answer + count_targerine[i][1] >= k:
            answer += count_targerine[i][1]
            ans += 1
            break
        else:
            answer += count_targerine[i][1]
            ans += 1
    
    return ans