# chapter04 구현
# 실전문제
# 왕실의 나이트
# 8x8 고정
# -- 입력 a1
# -- 출력 2
# -- 입력 c2
# -- 출력 6


# 1. x + 1, y - 2
# 2. x + 2, y - 1
# 3. x + 2, y + 1
# 4. x + 1, Y + 2
# 5. x - 1, y + 2
# 6. x - 2, y + 1
# 7. x - 2, y - 1
# 8. x - 1, y - 2
### 내 답안
# arr = list(input())
# x = ord(arr[0]) - 96
# y = int(arr[1])
#
# result = 0
# if (x + 1 < 9 and y - 2 > 0):
#     result += 1
# if (x + 2 < 9 and y - 1 > 0):
#     result += 1
# if (x + 2 < 9 and y + 1 < 9):
#     result += 1
# if (x + 1 < 9 and y + 2 < 9):
#     result += 1
# if (x - 1 > 0 and y + 2 < 9):
#     result += 1
# if (x - 2 > 0 and y + 1 < 9):
#     result += 1
# if (x - 2 > 0 and y - 1 > 0):
#     result += 1
# if (x - 1 > 0 and y - 2 > 0):
#     result += 1
#
# print(result)

### 책 답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향으로 이동가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)