import sys
import itertools

sys.stdin = open('14889.txt', 'r')
difference_min = 999999

n = int(input())

# make style as
# 0 0 0 0 0 0 0
# 0 0 2 3 4 5 6
# 0 2 0 4 5 6 7
# 0 5 6 0 4 3 5
# 0 1 3 4 0 1 3
# 0 1 5 6 7 0 3
# 0 1 2 2 4 4 0
mat = [[0]*(n+1)] + [list(map(int, ('0 ' +input()).split())) for _ in range(n)]

for start_team in itertools.combinations(range(1, n+1), n//2):
    sl1 = 0
    for e in itertools.permutations(start_team,2):
        sl1 += mat[e[0]][e[1]]
    link_team = []
    for i in range(1,n+1):
        if i not in start_team:
            link_team.append(i)
    sl2 = 0
    for e in itertools.permutations(link_team,2):
        sl2 += mat[e[0]][e[1]]
    diff = abs(sl1-sl2)
    if difference_min > diff:
        difference_min = diff

print(difference_min)

