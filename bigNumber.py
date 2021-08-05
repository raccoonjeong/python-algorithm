# 입력
# 5 8 3
# 2 4 5 4 6

# 출력
# 46

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

print(N,M,K)
print(arr)

arr.sort()
#
# newArr = [0] * N * 2
cnt = 0 # 실제 더해진 횟수
result = 0 # 결과값
for i in range(K):
    temp = arr.pop()
    for i in range(K):
        if (cnt < M):
            print(temp)
            result += temp
            cnt += 1

print(result)