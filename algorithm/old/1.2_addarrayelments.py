# Algorithm 1.2 Add Array Elements


def sum(n, S):
    result = 0
    for i in range(n):
        result = result + S[i]
    return result


S = [1, 2, 3, 4]
n = 3

result = sum(n, S)
print("result is = ", result)
