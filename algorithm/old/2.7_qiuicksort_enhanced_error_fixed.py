def partition2(S, low, high):
    pivotitem = S[low]
    print("start : ", S)
    i = low + 1
    j = high
    print(S[i], " : ", i, S[j], " : ", j)
    while i <= j:
        while S[i] < pivotitem:
            i += 1
            if i == high:
                S[low], S[high] = (
                    S[high],
                    S[low],
                )  # 해당 부분은 진행 도중 pivotitem이 리스트 S 의 최대 값일 경우,인덱스를 넘어서서 증가되는 경우를 방지하기 위해 만든 것으로, 이 경우 가장 큰 값임이 확실하므로, S[low] = pivotitem 을 S[high] 와 바꿔준다.(이미 최대 위치이므로) 그러나 이때 pivotitem이라는 기준이 그대로 최대값이므로, 이를 수정, i도 초기화 시켜줘야 다시 작동이 가능하다.
                pivotitem = S[low]
                i = low + 1
        while S[j] > pivotitem:
            j -= 1
        if i < j:
            S[i], S[j] = S[j], S[i]
        print(i, j, S)
    S[low], S[j] = S[j], S[low]
    # print(S[pivotpoint])
    print("final : ", S)
    return j


def quicksort2(S, low, high):
    if high > low:
        pivotpoint = partition2(S, low, high)
        quicksort2(S, low, pivotpoint - 1)
        quicksort2(S, pivotpoint + 1, high)


S = [4, 40, 1, 56, 3, 6, 2, 23, 15, 30, 32]
print("original S : ", S, "len : ", len(S) - 1)
# partition(S, 0, len(S) - 1)
quicksort2(S, 0, len(S) - 1)
print("Sorted S : ", S)
