'''
Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다. 
보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

- X 주차 주간보고 -
부서 :
이름 : 
업무 요약 : 

1 ~ 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오. 

조건 : 파일명 = '1주차.txt', '2주차.txt', ... 와 같이 만듭니다. 

'''

# 내 스타일
for i in range(1, 6):
    with open("{0}주차.txt".format(i), "w", encoding = "utf8") as report_file:
        print("""- {0} 주차 주간보고 -\n부서 : 개발부서\n이름 : 류한솔\n업무 요약 : 기본 시스템 API구축""".format(i), end 
        = "", file = report_file)

for i in range(1, 6):
    with open("{0}주차.txt".format(i), "r", encoding = "utf8") as report_file:
        print(report_file.read())


