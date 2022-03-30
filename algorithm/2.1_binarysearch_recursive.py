def location(S, low, high):
    if low > high:
        return -1
    else:
        mid = low + high // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            return location(S, low, mid - 1)
        else:
            return location(S, low + 1, high)


S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
loc = location(S, 0, len(S))
print("S = ", S)
print("x's loc = ", loc)

# Call by reference 방식이라서 x의 값을 함수로 전달하지 않아도 작동한다. 개신기함.
