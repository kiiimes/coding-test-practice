from collections import deque
def bfs(n,computers,start,visited):
    que = deque()
    que.append(start)
    
    while que:
        num = que.popleft()
        visited[num] = True
        
        for i in range(n):
            if computers[num][i] == 1 and not visited[i]:
                que.append(i)
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for start in range(n):
        if visited[start] == False:
            bfs(n,computers,start,visited)
            answer += 1
            
    return answer
    
 
