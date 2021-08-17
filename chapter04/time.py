n = int(input())

# 0 = 1575
# 1 = 3150
# 2 = 4725
# 3 = 8325
# hour = n # 최대 n
# minu = 0 # 최대 60 -- 3, 13, 23, 30,31,32,33,34,35,36,37,38,39, 43, 53 -- 15개
# seco = 0 # 최대 60 -- 15개
#
# result = 0
# a = 0
#
# if (n >= 3 and n < 13):
#     a += 1
# elif (n >= 13 and n < 23):
#     a += 2
# elif (n >= 23):
#     a += 3
#
# print((16 * 16 - 2) * (int(n) + 1 - a) + (60 * 60) * a)
#
# print(result)

result = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            full = str(i) + '시' + str(j) + '분' + str(k) + '초'
            if ("3" in full):
                print(full)
                result += 1
print(result)
