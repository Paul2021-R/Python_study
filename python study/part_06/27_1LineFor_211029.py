# 한줄 for 
#출석 번호가 1 ~ 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104. 
students = [1, 2, 3, 4, 5]
print (students)
students = [i + 100 for i in students] # for 문 활용이 굉장히 유연한 듯.. 
print(students)

students = ["아이언맨", "그루트", "토르", "스타로드"]
students = [len(i) for i in students] # 명령문 for i in 범위
print (students)

students = ["Iron man", "Star Loard", "Thor"]
print(students)
students = [i.upper() for i in students]
print(students)