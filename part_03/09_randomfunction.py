# 랜덤 함수(난수)
from random import *

print(random()) # 난수를 생성해 낸다. 0.0 ~ 1.0 사이의 임의의 값을 생성한다. 
print(random() * 10)
print (int(random() * 10)) # 0 ~ 10미만의 임의의 값을 생성할 수 있다. 
print (int(random() * 10 + 1)) # 이렇게 하면 0이 제외된 1 ~ 10까지의 임의의 값이 나오게 된다. 
print (int(random() * 10 + 1)) 
print ("-")
# 로또 값 구하는 난수(활용)
print("int() 형 변환과 random() 함수 조합 : ", int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성 
print("-")
print("randrange() 사용한 경우 : ", randrange(1, 45)) # 1 ~ 46 미만의 임의의 값 생성 방법
print("-")
print("randint() 사용한 경우 : ", randint(1, 45)) # 1 ~ 45, 양 끝을 포함한 임의의 값을 생성하는 방법이다

# 해당 기능을 활용한다면, 다양한 상황에서 다른 조건의 값을 불러내는 것이 가능해 보인다. 
