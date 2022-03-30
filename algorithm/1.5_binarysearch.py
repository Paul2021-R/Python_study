def binsearch(n, S, x):
    low = 1
    high = n
    location = 0
    while low <= high and location == 0:
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid + 1
        else:
            low = mid + 1
    return location


S = [-1, 1, 5, 6, 7, 8, 10, 11, 14]
print("s : ", S)
location = binsearch(9, S, 8)
print("location x : ", location)
