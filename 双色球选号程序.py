# 双色球选号程序

from random import choice

red = []
red_s = []
blue = []
blue_s = []
for red_value in range(1, 34):
    red.append(red_value)
for blue_value in range(1, 17):
    blue.append(blue_value)

# 蓝球
index = []
for index_value in range(0, len(blue)):
    index.append(index_value)
temp = choice(blue)
blue_s.append(temp)
for ind in index:
    if temp == blue[ind]:
        del blue[ind]
        break

# 红球
i = 0
while i < 6:
    index = []
    for index_value in range(0, len(red)):
        index.append(index_value)
    temp = choice(red)
    red_s.append(temp)
    for ind in index:
        if temp == red[ind]:
            del red[ind]
            break
    i += 1
print(sorted(red_s))
print(blue_s)
