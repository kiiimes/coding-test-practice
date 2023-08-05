from collections import deque
def solution(queue1, queue2):
    # 1 pop, 1 insert

    answer = 0
    total = (sum(queue1) + sum(queue2)) // 2
    
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    qSum1 = sum(deque1)
    qSum2 = sum(deque2)
    
    for i in range(len(queue1)*3):

        if qSum1 > qSum2:
            num = deque1.popleft()
            deque2.append(num)
            qSum1 -= num
            qSum2 += num
        elif qSum1 < qSum2:
            num = deque2.popleft()
            deque1.append(num)
            qSum2 -= num
            qSum1 += num
        else:
            break
        answer += 1

    if sum(deque1) != sum(deque2):
        return -1
    
    return answer
