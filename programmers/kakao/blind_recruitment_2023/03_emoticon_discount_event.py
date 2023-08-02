from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    lst = [10,20,30,40]
    
    combList = product(lst,repeat = len(emoticons))
    temp = list(combList)
    
    for comb in temp:
        flag = 0
        cList = list(comb)
        uList = [0 for i in range(len(users))]
        
        for u in range(len(users)):
            for e in range(len(emoticons)): 
                if cList[e] >= users[u][0]:
                    
                    uList[u] += emoticons[e]*(100-cList[e])//100

        pCnt = 0
        mCnt = 0
        
        for i in range(len(uList)):
            if uList[i] >= users[i][1]:
                pCnt += 1
                uList[i] = 0
            else:
                mCnt += uList[i]
        
        if pCnt > answer[0]:
            answer[0] = pCnt
            answer[1] = mCnt
        elif pCnt == answer[0]:
            if mCnt > answer[1]:
                answer[0] = pCnt
                answer[1] = mCnt   

     
    return answer
