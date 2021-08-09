# 내 답안
arrayWithoutMinus = input().split('-')
result = 0
for (index,value) in enumerate(arrayWithoutMinus):
    temp = value.split('+')
    num = 0
    for t in temp:
        num += int(t)
    if index == 0:
        result += num
    else:
        result -= num

print(result)
