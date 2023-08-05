def solution(survey, choices):
    answer = ''
    lst = [['R','T'],['C','F'],['J','M'],['A','N']]
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }

    
    for i in range(len(survey)):
        num = choices[i] - 4
        
        if num < 0:
            dic[survey[i][0]] += abs(num)
        else:
            dic[survey[i][1]] += num
    
    for i in range(len(lst)):
        if dic[lst[i][0]] < dic[lst[i][1]]:
            answer += lst[i][1]
        else:
            answer += lst[i][0]
    print(answer)
    return answer                
                
