from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] < array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()
# 수행시간 출력
print("선택 정렬 성능 측정 :", end_time - start_time)

# 삽입 정렬 수행시간 측정
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
# 측정 종료
end_time = time.time()
# 수행시간 출력
print("삽입 정렬 성능 측정 :", end_time - start_time)

# 계수 정렬

array = []
for _ in range(10000):
    array.append(randint(1, 100))
count = [0] * (max(array) + 1)

start_time = time.time()
for i in range(len(array)):
    count[array[i]] += 1
# 각 데이터에 해당하는 인덱스 값을 증가 시킨다.

array_new = []
for i in range(len(count)):
    for j in range(count[i]):
        array_new.append(i)

# 측정 종료
end_time = time.time()
# 수행시간 출력
print("계수 정렬 성능 측정 :", end_time - start_time)

# 배열 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()
array.sort()
end_time = time.time()
print("기본 정렬 라이브러리 성능 측정 :", end_time - start_time)
