from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque()
    que.append([numbers[0],0])
    que.append([(-1)*numbers[0],0])
    
    print(que)
    while que:
        num,idx = que.popleft()
        if (idx+1) < len(numbers):
            que.append([num + numbers[idx+1],idx+1])
            que.append([num - numbers[idx+1],idx+1])
        else:
            if target == num:
                answer += 1
        
    return answer
