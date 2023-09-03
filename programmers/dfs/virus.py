import sys
from collections import deque

def bfs(graph,start):
    queue = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    print(cnt)


inputs = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]

for i in range(m):
    vertex1, vertex2 = map(int,inputs().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

bfs(graph,1)
    