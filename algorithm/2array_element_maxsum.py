n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
print(arr_a)
arr_b.sort()
l = n - 1
m = k
for i in range(0, m):
    if arr_a[i] < arr_b[l - i]:
        arr_a[i], arr_b[l - i] = arr_b[l - i], arr_a[i]
    else:
        m += 1
        continue

print(arr_a)
result = 0
for i in range(n):
    result += arr_a[i]
print(result)
