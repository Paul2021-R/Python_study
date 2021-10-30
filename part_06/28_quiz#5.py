'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사다. 
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하라

조건 1: 승객별 운행 소요시간은 5~50분 사이 난수로 정해진다. 
조건 2: 당신은 소요시간이 5~15분 사이 승객만 매칭해야 한다. 

출력문 예제
[O] 1번째 손님 (소요시간 :15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분 
'''
from random import *

total = 0

for customer in range(1, 51):
    #time = int((random() * 46)+5) #위 아래 명령 모두 동일한데, 일반적으로 쓰기엔 randrange가 훨씬 편한 것 같다. 
    time = randrange(5, 50)
    if time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        total += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("\n총 탑승 승객 : {}분".format(total))
