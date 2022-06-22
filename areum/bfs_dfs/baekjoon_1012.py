def dfs(farm, i, j):
    """
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    (0,4) -> + 1
    (2,0) -> 재귀적으로
    (2,1) ->
    (2,2) ->
    (2,3) ->
    (2,4) ->
    """

    if i < 0 or i >= len(farm) or j < 0 or j >= len(farm[0]) or farm[i][j] != 1:
        return
    farm[i][j] = 0
    dfs(farm, i+1, j)
    dfs(farm, i-1, j)
    dfs(farm, i, j+1)
    dfs(farm, i, j-1)


# 0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는 땅
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    """
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    """
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    """
    [0, 0, 0, 0, 1]
    [0, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    """

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                dfs(farm, i, j)
                cnt += 1
    print(cnt)