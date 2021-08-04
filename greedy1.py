### 그리디 알고리즘1
N = int(input())
a = 500
b = 100
c = 50
d = 10

aCount = 0
bCount = 0
cCount = 0
dCount = 0

if (N//a >= 1):
    aCount = N//a
    N = N - (aCount * a)
print(N)
if (N//b >= 1):
    bCount = N//b
    N = N - (bCount * b)
print(N)
if (N//c >= 1):
    cCount = N//c
    N = N - (cCount * c)
print(N)
if (N//d >= 1):
    dCount = N//d
    N = N - (dCount * d)
print(N)
print(aCount,bCount,cCount,dCount)
print(aCount+bCount+cCount+dCount)

### 정답
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)