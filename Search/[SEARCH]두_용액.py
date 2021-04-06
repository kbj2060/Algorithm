from sys import stdin

n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))
LP, RP = 0, n-1
result = abs(values[LP] + values[RP])
pointers = [LP, RP]

while LP < RP:
    if abs(values[LP] + values[RP]) < result:
        result = abs(values[LP] + values[RP])
        pointers = [LP, RP]

    if abs(values[LP]) >= abs(values[RP]):
        LP += 1
    else:
        RP -= 1

print(values[pointers[0]], values[pointers[1]])
