# 입력
# 5 8 3
# 2 4 5 4 6
# 출력
# 46
### 내 답안
n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
firstBig = arr.pop()
secondBig = arr.pop()
secondCount = m // (k+1)

result = (m - secondCount) * firstBig + secondCount * secondBig

print(result)


### 책 풀이1
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split()) # N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second # 두번째로 큰 수를 한번 더하기
    m -= 1 # 더할 때마다 1씩 빼기
print(result)


### 책 풀이2
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split()) # N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result)
