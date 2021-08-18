# chapter04 구현
# 실전문제
# <게임 개발하기>

## 입력

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 4 4     # 4 x 4 맵 생성(세로 크기 N, 가로 크기 M)
# 1 1 0   # (1,1)에 북쪽(0)을 바라보고 서 있는 캐릭터
# 1 1 1 1 # 첫 줄은 모두 바다
# 1 0 0 1 # 둘째 줄은 바다/육지/육지/바다
# 1 1 0 1 # 셋째 줄은 바다/바다/육지/바다
# 1 1 1 1 # 넷째 줄은 모두 바다

# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 0 0 1
# 1 1 1 1 1

## 출력
# 3
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())

vertical = []
for i in range(n):
    horizontal = list(map(int, input().split()))
    vertical.append(horizontal)

print(vertical)
result = 0

while True:
    d += 1
    d %= 4

    if (d == 0):
        # 북쪽
        y -= 1
    elif (d == 1):
        # 동쪽
        x += 1
    elif (d == 2):
        # 남쪽
        y += 1
    elif (d == 3):
        # 서쪽
        x -= 1
    # print('방문해봄!', vertical[y][x], ".... y", y, "x", x)

    if(y >= 0 and y < n and x >= 0 and x < m and vertical[y][x] == 0):
        # print('새로 방문했다!!!', vertical[y][x], ".... y", y, "x", x)
        vertical[y][x] = 1
        result += 1
        continue

    # 롤백
    if (d == 0):
        # 북쪽
        y += 1
    elif (d == 1):
        # 동쪽
        x -= 1
    elif (d == 2):
        # 남쪽
        y -= 1
    elif (d == 3):
        # 서쪽
        x += 1

    # print('돌아왔음...', vertical[y][x], ".... y", y, "x", x)

    if (y < 0 or y >= n or x < 1 or x >= m or vertical[y][x] == 1):
        break

print(result)

