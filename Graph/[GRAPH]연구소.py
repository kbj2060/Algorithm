from sys import stdin

n, m = list(map(int, stdin.readline().split()))
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, +1, 0, 0], [0, 0, +1, -1]
investigate_dx, investigate_dy = [-1, -1, -1, 0, 0, +1, +1, +1], [+1, 0, -1, +1, -1, +1, -1, 0]
print(graph)