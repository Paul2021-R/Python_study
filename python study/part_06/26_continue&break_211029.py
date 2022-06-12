# Continue 와 Break 
absent = [2, 5, 9]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue # 해당 반복문에서 조건에 충족 시 특정 명령을 진행하지 않고 다음으로 넘어 간다. 
    if student in no_book:
        print("오늘 수업 여기까지다... {0} 은 교무실로.".format(student))
        break # 만나는 즉시 바로 반복문을 탈출하고 종결시켜버린다. 
    print("{0}야, 책 읽어봐!".format(student))
