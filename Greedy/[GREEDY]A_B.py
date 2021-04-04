import sys

target, data = map(int, sys.stdin.readline().split(' '))
cnt = 0

while True:
    if data < target or data == target:
        break

    if str(data)[-1] == '1':
        data = int(str(data)[:-1])
        cnt += 1
    elif data % 2 == 0:
        data = int(data / 2)
        cnt += 1
    else:
        break

if data == target:
    cnt += 1
else:
    cnt = -1

print(cnt)
