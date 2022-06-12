# for (반복문)

# i = int(input("대기팀은 총 몇 팀인가요?\n")) # PC 입력 방법

# for waiting_no in range(i):
#     print("대기 번호 : {0}".format(waiting_no + 1)) # 번호 출력은 1부터라서 변수로 지정된 waiting_no에다가 1을 더 해주었다.

starbucks = ["아이언맨", "토르", "그루트"]

for customer in starbucks:
    print("{0} 손님, 주문 하신 아이스 커피가 나왔습니다!".format(customer))
# C 언어 대비 강점은 반복의 연산 과정을 따로 직접 지정하지 않아도 된다는 점인듯.. 