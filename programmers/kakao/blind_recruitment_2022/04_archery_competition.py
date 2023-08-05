from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    comb = combinations_with_replacement(range(11),n)
    max_score = -1
    
    for c in comb:        
        lionInfo = [0]*11
        
        for i in c:
                      
            lionInfo[10-i] += 1
        appeach = 0
        lion = 0
        for i in range(11):
            if lionInfo[i] == info[i] == 0:
                continue
            elif lionInfo[i] <= info[i]:
                appeach += (10-i)
            else:
                lion += (10-i)
        if appeach < lion:
            score = lion - appeach
            if max_score < score:
                max_score = score
                answer = lionInfo
    if answer == []:
        return [-1]
    print(max_score)
  
    return answer
