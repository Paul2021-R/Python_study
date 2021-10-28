# 간단한 수식 만들기 
print("2 + 3 * 4 = " + str(2 + 3 * 4)) # 당연히 수식의 우선순위가 지정되어 있지 않으므로 기본 연산자 우선순위에 따라 3 * 4가 먼저 연산된다. 
print("(2 + 3) * 4 =", str((2 + 3) * 4)) # 우선순위 연산 

number = 2 + 3 * 4  # 변수 안에 넣어서 계산
sentence = "2 + 3 * 4"
print (number)
print (sentence + " = " + str(number)) # 변수를 활용해 조합 가능... 하나 변수로도 숫자만 들어 있을 경우 int 로 치므로 str변환이 필요

number = number + 2
print (number) # 저렇게 셀프 대입도 가능하다. C 랑 비슷 

number += 2 # 10번 라인의 축약형, *, -, / 등등 연산자 모두 축약형으로 작성이 가능하다. 
print (number)