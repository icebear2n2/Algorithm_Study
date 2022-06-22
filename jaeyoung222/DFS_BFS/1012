from collections import deque
t = int(input())
for _ in range(t) :
    n,m,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for i in range(k) :
        a,b = map(int,input().split())
        graph[a][b] = 1

    def bfs(graph, visited) :
        cnt = 0
        q = deque()
        for ii in range(n) :
            for iii in range(m) :
                if visited[ii][iii] != 1 :
                    visited[ii][iii] = 1
                    if graph[ii][iii] == 1 :
                        cnt += 1
                        q.append([ii,iii])
                    while q :
                        p = q.popleft()
                        if p[0]+1 < n and graph[p[0]+1][p[1]] == 1 and visited[p[0]+1][p[1]] == 0 :
                            visited[p[0]+1][p[1]] = 1
                            q.append([p[0]+1,p[1]])
                        if p[0]-1 >= 0 and graph[p[0]-1][p[1]] == 1 and visited[p[0]-1][p[1]] == 0 :
                            visited[p[0]-1][p[1]] = 1
                            q.append([p[0]-1,p[1]])
                        if p[1]+1 < m and graph[p[0]][p[1]+1] == 1 and visited[p[0]][p[1]+1] == 0 :
                            visited[p[0]][p[1]+1] = 1
                            q.append([p[0],p[1]+1])
                        if p[1]-1 >= 0 and graph[p[0]][p[1]-1] == 1 and visited[p[0]][p[1]-1] == 0 :
                            visited[p[0]][p[1]-1] = 1
                            q.append([p[0],p[1]-1])
                    
        return print(cnt)
    visited = [[0]*m for _ in range(n)]
    bfs(graph, visited)
