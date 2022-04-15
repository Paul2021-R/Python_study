def merge(U, V):
    S = []
    i = j = 0
    while i < len(U) and j < len(V):
        print("U[i] : ", U[i], "V[j]: ", V[j])
        if U[i] < V[j]:
            S.append(U[i])  # append 덧붙이다는 뜻이라서, 뒤에 붙는다. 즉, S의 끝에 붙인다고 보면 될 듯 하다.
            i += 1
        else:
            S.append(V[j])
            j += 1
        print("changing(while) : ", S)
    if i < len(U):
        S += U[i : len(U)]
    else:
        S += V[j : len(V)]
    print("changing(finished) : ", S)
    return S


def mergesort(S):
    n = len(S)
    if n <= 1:
        return S
    else:
        mid = n // 2
        U = mergesort(S[0:mid])  # 슬라이싱이라고 한다.
        V = mergesort(S[mid:n])
        return merge(U, V)


S = [40, 23, 1, 56, 3, 6, 2, 23, 15, 30, 32]
print("original S : ", S)
S = mergesort(S)
print("Sorted S : ", S)
