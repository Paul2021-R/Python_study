import time
import math


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    f = [0] * (n + 1)

    if n > 0:
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fib3(n):
    if n < 2:
        return n
    else:
        f = [0] * 2
        f[1] = 1
        i = 3
        for i in range(n - 1):
            ret = f[0] + f[1]
            f[0] = f[1]
            f[1] = ret
    return ret


for i in range(30):
    print(fib(i), end=" ")
    if i == 0:
        start = time.time()
    elif i == 29:
        last = time.time()
        print(f"fib {last - start:.5f} sec\n")
print("\n")
for i in range(30):
    print(fib2(i), end=" ")
    if i == 0:
        start = time.time()
    elif i == 29:
        last = time.time()
        print(f"fib2 {last - start:.5f} sec\n")
print("\n")
for i in range(30):
    print(fib3(i), end=" ")
    if i == 0:
        start = time.time()
    elif i == 29:
        last = time.time()
        print(f"fib3 {last - start:.5f} sec\n")
print("\n")
