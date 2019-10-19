import sys
import collections

sys.stdin = open('16234.txt', 'r')
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
t = 0


def bfs(v):
    q = collections.deque()
    point = [v]
    level = 0
    f_p = v[:]
    visited[v[0]][v[1]] = True
    q.append(v)

    while q:
        level += 1
        for _ in range(len(q)):
            v = q.popleft()
            for a in range(4):
                i = v[0] + di[a]
                j = v[1] + dj[a]
                if 0 <= i <= n-1 and 0 <= j <= n-1 and not (visited[i][j]):
                    if l <= abs(land[v[0]][v[1]] - land[i][j]) <= r:
                        point.append([i, j])
                        q.append([i, j])
                        visited[i][j] = True
    if level == 1:
        visited[f_p[0]][f_p[1]] = False
    else:
        total_point.append(point)


while True:
    total_point = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs([i, j])
    if not total_point:
        break
    else:
        for points in total_point:
            result = sum(map(lambda x: land[x[0]][x[1]], points)) // len(points)
            for p in points:
                land[p[0]][p[1]] = result
        t += 1
print(t)
