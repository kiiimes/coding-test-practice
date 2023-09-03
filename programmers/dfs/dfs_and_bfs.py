# import sys
# from collections import deque

# def dfs_iteration(graph,root):
#   visited=[]
#   stack=[root]

#   while stack:
#     node=stack.pop()

#     if node not in visited:
#       visited.append(node)
#       stack.extend(graph[node])
#   return visited


# def dfs(graph,visited,V):
#   print(V, end=" ")
#   visited[V]=True

#   for i in graph[V]:
#     if not visited[i]:
#       dfs(graph,visited,i)

# def bfs(graph,visited,V):
#   queue=deque([V])
#   visited[V]=True

#   while queue:
#     v=queue.popleft()
#     print(v,end=" ")

#     for i in graph[v]:
#       if not visited[i]:
#         queue.append(i)
#         visited[i]=True

# inputs=sys.stdin.readline
# N,M,K=map(int,inputs().split())
# graph=[[] for i in range(N+1)]
# visited=[False]*(N+1)

# for i in range(M):
#   vertex1,vertex2=map(int,inputs().split())
#   graph[vertex1].append(vertex2)
#   graph[vertex2].append(vertex1)

# for i in graph:
#   i.sort()

# dfs(graph,visited,K)
# visited=[False]*(N+1)
# print('')
# bfs(graph,visited,K)

import sys
from collections import deque

def dfs(graph,visited,v):
    print(v,end=' ')
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            
inputs=sys.stdin.readline
n,m,v = map(int,inputs().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    vertex1, vertex2 = map(int,inputs().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

for i in graph: 
    i.sort()

dfs(graph,visited,v)
print()
visited = [False] * (n+1)
bfs(graph,visited,v)
