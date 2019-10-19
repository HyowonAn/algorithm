import sys
from itertools import combinations

sys.stdin = open('15686.txt', 'r')
MAX = 999999
n, m = map(int, input().split())
houses = []
chickens = []
dist_max = 99999

# read
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j, e in enumerate(arr, 1):
        # case house
        if e == 1:
            houses.append([i, j])
        elif e == 2:
            chickens.append([i, j])

for chicken_combinations in combinations(chickens, m):
    dist_sum = 0
    # 집 중에 최단치킨집 검색
    for house in houses:
        dist_shortest = MAX
        for chicken in chicken_combinations:
            dist_tmp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if dist_shortest > dist_tmp:
                dist_shortest = dist_tmp
        dist_sum += dist_shortest
    if dist_max > dist_sum:
        dist_max = dist_sum

print(dist_max)
