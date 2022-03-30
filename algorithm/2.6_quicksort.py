def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]  # swap
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    print(S[pivotpoint])
    print(S)
    return pivotpoint


def quicksort(S, low, high):
    if high > low:
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1, high)


S = [4, 40, 1, 56, 3, 6, 2, 23, 15, 30, 32]
print("original S : ", S, "len : ", len(S) - 1)
# partition(S, 0, len(S) - 1)
quicksort(S, 0, len(S) - 1)
print("Sorted S : ", S)
