# clock
# 나동빈 15 - 1
n = int(input())
clock = [0] * 6
limit = [0] * 2

limit[0] = n // 10
limit[1] = n % 10

# 01 23 45


ret = 0

while True:
    clock[5] += 1
    if clock[5] == 10:
        clock[4] += 1
        clock[5] = 0
    if clock[4] == 6:
        clock[3] += 1
        clock[4] = 0
    if clock[3] == 10:
        clock[2] += 1
        clock[3] = 0
    if clock[2] == 6:
        clock[1] += 1
        clock[2] = 0
    if clock[1] == 10:
        clock[0] += 1
        clock[1] = 0
    if 3 in clock:
        ret += 1
    if clock[0] == limit[0] and clock[1] == limit[1]:
        if clock[2] == 5 and clock[3] == 9:
            if clock[4] == 5 and clock[5] == 9:
                break
print(ret)
