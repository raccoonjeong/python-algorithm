# 입력 55-50+40
# 출력 -35
# 내 답안
# [(10) , (50 + 30) , (20)]
arrayWithoutMinus = input().split('-')
result = 0

for (index, value) in enumerate(arrayWithoutMinus):
    temp = value.split('+')
    num = 0
    for t in temp: # [50, 30]
        num += int(t)
    if index == 0:
        result += num
    else:
        result -= num

print(result)
