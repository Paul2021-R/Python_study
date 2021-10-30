# 표준 입출력 
print("Python", "Java", "JavaScript", sep = ",", end = "?") # 해당 옵션으로 ,의 구분자를 변경 시킬 수 있다.
print("무엇이 더 재밌을 까요?")
# sep = 구분자를 바꾸는 옵션(디폴트 = 띄워쓰기)
# end = 끝 부분을 바꾸는 옵션(디폴트 = 개행)

import sys
print("Python", "Java", file=sys.stdout) #표준 출력으로 처리됨
print("Python", "Java", file=sys.stderr) #표준 에러로 처리됨 로그 처리시 에러로 입력되어 버리는 것이다. 

# 시험 성적 예시
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":")
# (문자열) 이라면 
# ljust(숫자) : 숫자 크기 만큼 왼쪽으로 공간을 만들고 정렬한다. 
# rjust(숫자) : 상위의 오른쪽 정렬 버전 

# 은행 대기 순번표식 출력
# 001 002 003...
for num in range(1, 21):
    print("대기번호 : "+ str(num).zfill(3))

# 표준 입력 
# 핵심! 표준 입력을 사용했을 때 문자열로 입력을 받으므로, 정수형으로 저장이 필요하거나, 사용시 충돌을 막기 위해서는 후처리의 단계가 필요하다는 사실을 기억할 것. 
answer = input("아무 값이나 입력하세요 : ")
print("입력한 값은"+answer+"입니다.")