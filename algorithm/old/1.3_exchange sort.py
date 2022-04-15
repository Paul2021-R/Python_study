# Algorithm 1.3 Exchange Sort
def exchange(S):
    n = len(S)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if S[i] > S[j]:
                S[i], S[j] = S[j], S[i]  # swap
        print(S)  # 이렇게 하면, 같은 tab 위치에 따라 같이 실행되기도 한다... << 개꿀팁


S = [0, 3, 2, 133, 4, 11, 6, 7, 1, 9, 10]
print("original S = ", S)
exchange(S)
print("changed = ", S)
