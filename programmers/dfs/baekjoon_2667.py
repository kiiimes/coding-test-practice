import sys
from collections import deque

dx = [0,1,0,-1]
dy = [-1,0,1,0]

inputs = sys.stdin.readline
n = int(input())

def bfs(graph,start):
    queue = deque([start])
    graph[start[0]][start[1]] = '-1'
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >=n:
                continue

            if graph[mx][my] == '1':
                queue.append([mx,my])
                graph[mx][my] = '-1'
                cnt += 1

    return cnt

graph = []
for i in range(n):
    temp = list(inputs().rstrip())
    graph.append(temp)

total = 0
cntList = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            cnt = bfs(graph,[i,j])
            cntList.append(cnt)
            total += 1

print(total)
cntList.sort()
for i in cntList:
    print(i)



    

    