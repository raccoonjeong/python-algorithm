# 입력 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
#
# 출력 1
# 2
# ===========
# 입력 2
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 2
# 3

# 내 답안
lineCount, rowCount = map(int, input().split())
smallerNumbers = [0]*lineCount

for i in range(lineCount):
    arr = list(map(int, input().split()))
    arr.sort()
    smallerNumbers[i] = arr[0]

smallerNumbers.sort(reverse=True)
print(smallerNumbers[0])


# 책 답안1
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().splitO)
result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().splitO))
    # 현재 줄에서 '가장 작은 수, 찾기
    min_value = min(data)
    # '가장 작은 수,들 중에서 가장 큰 수 찿기
    result = max(result, min_value)

print(result) # 최종 답안 출력


# 책 답안2
# N, 이을 공백으로 구분하여 입력받기
n, m = map(int, input().splitO)
result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int(input().split())))
    # 현재 줄에서 '가장 작은 수, 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        # ’가장 작은 수,들 중에서 가장 큰 수 착기
        result = max(result, min_value)
print(result) # 최종 답안 출력
