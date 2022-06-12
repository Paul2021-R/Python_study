n = int(input("정수를 입력해주세요."))  # 안에다가 집어넣으면 디폴트 값으로 넣을 수 있는듯.

print(n)


data = list(map(int, input("넣을 값을 입력해주세요. 여러개라면 콤마(,)로 구분짓습니다.\n").split(",")))

data.sort(reverse=False)
# 정렬 메소드 활용 예시. 이때 핵심은 reverse에 대한 옵션을 사용 시 True, False 를 대문자로 정확하게 정해줘야 한다는 점일듯.
print(data)

n, m, k = map(int, input("구분은 공백으로 합니다.\n").split())
print("n = ", n, "m = ", m, "k = ", k)

import sys

data = sys.stdin.readline().rstrip()

print(data)
