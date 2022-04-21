# chess
# 나동빈 15 - 2

pos = input()
pos_x = ["a", "b", "c", "d", "e", "f", "g", "h"]
pos_y = [1, 2, 3, 4, 5, 6, 7, 8]
cnt = 0

p_y = int(pos[1])
p_x = 0
n_x = 0
n_y = 0

mov_1 = [2, -2]
mov_2 = [1, -1]

for i in range(1, 8):
    if pos_x[i - 1] == pos[0]:
        p_x = i
        break

# print("current x : ", p_x, "current y : ", p_y)

for mov in mov_1:
    for mov2 in mov_2:
        n_x = mov + p_x
        n_y = mov2 + p_y
        # print(n_x, ", ", n_y)
        if n_x in range(1, 8) and n_y in range(1, 8):
            cnt += 1

for mov in mov_1:
    for mov2 in mov_2:
        n_y = mov + p_y
        n_x = mov2 + p_x
        # print(n_x, ", ", n_y)
        if n_x in range(1, 8) and n_y in range(1, 8):
            cnt += 1

print(cnt)
