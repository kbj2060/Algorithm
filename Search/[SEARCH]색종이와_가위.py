from sys import stdin

n, k = list(map(int, stdin.readline().split()))
result = 'NO'
start, end = 0, n

while start <= end:
    mid = (start + end) // 2
    pieces = (mid + 1) * (n - mid + 1)
    if k == pieces:
        result = 'YES'
        break
    elif k > pieces:
        start = mid + 1
    else:
        end = mid - 1

print(result)
