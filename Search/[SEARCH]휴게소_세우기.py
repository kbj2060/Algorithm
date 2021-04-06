from sys import stdin

N, M, L = list(map(int, stdin.readline().split()))
stations = sorted(list(map(int, stdin.readline().split())))

for _ in range(M):
    distances = [stations[0]]+[j-i for i, j in zip(stations, stations[1:])]+[L-stations[-1]]
    idx = distances.index(max(distances))

# 모르겠음..