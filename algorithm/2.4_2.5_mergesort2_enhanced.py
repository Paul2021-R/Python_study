def merge2(S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if S[i] < S[j]:
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1
    if i <= mid:
        U += S[i : mid + 1]
    else:
        U += S[j : high + 1]
    for k in range(low, high + 1):
        S[k] = U[k - low]


# 결국 U[0] 부터 들어가고, U 는 정렬이 된 리스트이니 S U 두개로 공간이 절약된다. 따라서 추가적 원소 수를 대략 n 개로 절약 할 수 있다.


def mergesort2(S, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        mergesort2(S, mid + 1, high)
        merge2(S, low, mid, high)


import sys

S = [40, 23, 1, 56, 3, 6, 2, 23, 15, 30, 32]
print(sys.getrecursionlimit())
print("original S : ", S)
mergesort2(S, 0, len(S) - 1)
print("Sorted S : ", S)
