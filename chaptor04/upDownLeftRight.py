# 출력
# 5
# R R R U D D

# 입력
# 3 4

### 내 풀이
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# plan = list(map(str, input().split()))
# coordi = [1, 1]
# for i in plan:
#     if (i == 'U' and coordi[0] > 1):
#         coordi[0] -= 1
#     elif (i == 'D' and coordi[0] < n):
#         coordi[0] += 1
#     elif (i == 'L' and coordi[1] > 1):
#         coordi[1] -= 1
#     elif (i == 'R' and coordi[1] < n):
#         coordi[1] += 1
#
# print(coordi)

### 책 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 이동하는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)

## thinking & learning
## 책은 알고리즘이 아니라 프로그램을 만들어놨네
## 파이썬의 변수 스코프는 자바스크립트의 var와 유사함
