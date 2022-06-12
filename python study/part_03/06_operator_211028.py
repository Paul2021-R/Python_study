# 연산자에 대여 알아보기
print (1 + 1) # 2
print (1 - 1) # 0
print (5 * 6) # 30
print (7 / 4) # 1.75 정수 계산으로 안 끝나고 실수까지 구해주네? 
print (7 // 4) # 1 순수하게 몫만을 구하고 싶을 때는 // 라고 입력하면 된다 
print (7 % 4) # 나눈 나머지 보여준다

print (2 ** 3) # 2^3 = 8

print (4 > 7) # False 크다 작다 
print (4 >= 4) # True 크거나 같다 

print (3 == 3) # True 전 값과 후 값이 같은지를 조건으로 성립하는지를 본다
print (4 == 3) # False 
print (3 + 4 == 7) #True

print (3 != 4) # True 

print (not(1 != 3)) # 1은 3과 다르다 이므로 True 가 나오는데, 그것에 NOT 이므로 False 가 나온다. 
print ((3 > 0) and (3 < 5)) # True 항을 두개 넣어서 and로 묶어서 사용 하는 경우 
print ((3 > 0) & (3 < 5)) # & 기호 사용도 됨 

print ((3 * 2 == 6) or (3 * 2 != 6)) # True or 연산. 하나 만 맞으면 됨
print ((3 * 2 == 6) | (3 * 2 != 6)) # or 대신 | 를 써도 됨 

print(3 < 4 < 5) # 연속으로 3개의 항으로 부등호 연산도 가능하다. 
print(7 < 4 < 5)