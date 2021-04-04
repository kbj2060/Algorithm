n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]

room.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for s, e in room:
    if s >= end:
        end = e
        cnt += 1

print(cnt)
