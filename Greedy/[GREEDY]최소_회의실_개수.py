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
# 1. 최선이 무엇인가?
# 2. 이전과 이후를 생각하지 않고 현재 가장 좋아보이는 선택지를 고른다.
# 가장 좋아보이는 것은 무엇인가?
# 여기선 제일 작은 수의 회의실 갯수를 가져야하기 때문에 한 회의실에 최대한 많은 수의 회의를 넣어야 한다.

# 배운점
# * 반복문에서 이전 데이터는 배열의 인덱스를 사용하지 말고 일시적인 변수에 저장하고 업데이트
# 3
# 0 40
# 10 30
# 10 20
