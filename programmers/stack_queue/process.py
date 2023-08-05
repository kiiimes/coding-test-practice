from collections import deque
def solution(priorities, location):
    answer = 0 
    dic = {}
    lst = []
    
    for i in range(len(priorities)):
        dic[chr(ord('A')+i)] = priorities[i]
        
    keyList = deque(dic.keys())
    alpha = keyList[location]
    priorities.sort() 
        
    length = len(priorities)
    
    while keyList:
        temp = keyList.popleft()
        if dic[temp] == priorities[len(priorities)-1]:
            lst.append(temp)
            priorities.pop()
        else:
            keyList.append(temp)
    
    for i in range(len(lst)):
        if lst[i] == alpha:
            return i+1

    
    return answer
