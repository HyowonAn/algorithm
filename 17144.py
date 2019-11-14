import sys
from itertools import combinations

sys.stdin = open('17144.txt', 'r')

r, c, t = map(int, input().split())
a = []
cleaner = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def spread():
    tmp = []
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                dust_spread = a[i][j] // 5
                counter = 0
                for rotation in range(4):
                    ni, nj = i + di[rotation], j + dj[rotation]
                    # 범위
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj] != -1:
                        counter += 1
                        tmp.append([ni, nj, dust_spread])
                tmp.append([i, j, a[i][j] - (dust_spread * counter)])
                a[i][j] = 0
    for i, j, dust in tmp:
        a[i][j] += dust


def left():
    dust = 0
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                dust += a[i][j]
    return dust


def clean():
    #상단부 대류
    #깨끗한 공기 방출
    a[cleaner[0][0]].insert(1,0)
    tmp = a[cleaner[0][0]].pop()
    #위로올리기
    for i in range(cleaner[0][0]-1,-1,-1):
        tmp, a[i][-1] = a[i][-1], tmp
    a[0].insert(-1,tmp)
    tmp = a[0].pop(0)
    #아래로 내리기
    for i in range(1,cleaner[0][0],1):
        tmp, a[i][0] = a[i][0], tmp
    #하단부대류
    #깨끗한 공기 방출
    a[cleaner[1][0]].insert(1,0)
    tmp = a[cleaner[1][0]].pop()
    #아래로내리기
    for i in range(cleaner[1][0]+1,r):
        tmp, a[i][-1] = a[i][-1], tmp
    a[r-1].insert(-1,tmp)
    tmp = a[r-1].pop(0)
    #위로 올리기
    for i in range(r-2, cleaner[1][0],-1):
        tmp, a[i][0] = a[i][0], tmp


for i in range(r):
    tmp = list(map(int, input().split()))
    a.append(tmp)
    for j in range(c):
        if tmp[j] == -1:
            cleaner.append([i, j])

for _ in range(t):
    spread()
    clean()

print(left())
