"""
for _ in range():
언더 스코어 : 변수 이름을 _로 기입, 의미없는 값으로 단순히 반복 횟수만 채울 때 사용, 크게 신경쓰이지 않아도 되는 변수를 의미
"""
from collections import deque


def dfs(edges, v, visited):
    visited[v] = True
    print(v, end=' ')

    for e in edges[v]:
        if not visited[e]:
            dfs(edges, e, visited)


def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True


n, m, v = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
# [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]

for i in range(1, n + 1):
    edges[i].sort()
# [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]

visited = [False] * (n + 1)
dfs(edges, v, visited)
print()
visited = [False] * (n + 1)
bfs(edges, v, visited)