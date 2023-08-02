import math
def solution(n, k):
    answer = -1

    num = ''
    while n > 0:
        n,mod = divmod(n,k)
        num += str(mod)
    numList = num[::-1].split('0')
    print(numList)
    
    answer = 0
    
    for num in numList:
        flag = 0
        if num == '' or num == '1':
            continue
        for j in range(2,int(math.sqrt(int(num)) + 1)):
            if int(num) % j == 0:
                flag = 1
                break
        if flag == 0:
            answer += 1
            
    return answer
