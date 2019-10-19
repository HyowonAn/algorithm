b = [[0] * 101 for i in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
c = 0


def f(y, x, o):
    b[y][x] = 1
    for d in o:
        y, x = y + dy[d], x + dx[d]
        b[y][x] = 1


def m(d, g):
    r = [d]
    if g == 0:
        return r
    else:
        for _ in range(g):
            for i in range(len(r) - 1, -1, -1):
                r.append((r[i] + 1) % 4)
    return r


for i in range(int(input())):
    x, y, d, g = map(int, input().split())
    f(y, x, m(d, g))

for i in range(100):
    for j in range(100):
        if sum(map(sum, [b[i][j:j + 2], b[i + 1][j:j + 2]])) == 4:
            c += 1
print(c)
