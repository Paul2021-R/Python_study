# # chess
# 나동빈 15 - 3

str = input()

ret_num = 0
ret_str = []

for i in range(len(str)):
    if str[i] >= "1" and str[i] <= "9":
        ret_num += int(str[i])
    else:
        ret_str.append(str[i])
ret_str.sort()
print(*ret_str, sep="", end="")
if ret_num != 0:
    print(ret_num, end="")
print("\n")
