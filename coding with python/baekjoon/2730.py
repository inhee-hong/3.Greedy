# my code(error)

n = int(input())

for i in range(n):
    cal, paper = map(str, input().split())
    cals = cal.split('/')
    papers = paper.split('/')
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    cals_day = sum(days[:int(cals[0])-1]) + int(cals[1])
    papers_day = sum(days[:int(papers[0])-1]) + int(papers[1])
    
    if cals[0] == '1' and papers[0] == '12':
        new_cals_day = cals_day + 365
        if 0 < new_cals_day - papers_day <= 7:
            print(f'{cal} IS {new_cals_day - papers_day} DAYS PRIOR')
        elif 0 < papers_day - new_cals_day <= 7:
            print(f'{cal} IS {papers_day - new_cals_day} DAYS AFTER')
        elif abs(new_cals_day - papers_day) > 7:
            print('OUT OF RANGE')
        elif new_cals_day - papers_day == 0:
            print('SAME DAY')
            
    elif cals[0] == '12' and papers[0] == '1':
        new_papers_day = papers_day + 365
        if 0 < cals_day - new_papers_day <= 7:
            print(f'{cal} IS {cals_day - new_papers_day} DAYS PRIOR')
        elif 0 < new_papers_day - cals_day <= 7:
            print(f'{cal} IS {new_papers_day - cals_day} DAYS AFTER')
        elif abs(cals_day - new_papers_day) > 7:
            print('OUT OF RANGE')
        elif cals_day - new_papers_day == 0:
            print('SAME DAY')
            
    elif abs(cals_day - papers_day) > 7:
        print('OUT OF RANGE')
    elif 0 < cals_day - papers_day <= 7:
        print(f'{cal} IS {cals_day - papers_day} DAYS PRIOR')
    elif 0 < papers_day - cals_day <= 7:
        print(f'{cal} IS {papers_day - cals_day} DAY AFTER')
    elif cals_day - papers_day == 0:
        print('SAME DAY')
        
