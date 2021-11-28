
# 두수 비교하기
a, b = map(int, input().split())
if (a > b):
    print(">")
elif (a < b):
    print("<")
else:
    print("==")

a, b = map(int, input().split())
if a == b:
    print("==")
else :
    print(">" if a > b else "<")

## 시험성적 구분하기(범위 설정)
import sys
a = int(sys.stdin.readline())
if (90 <= a):
    print("A")
elif(80 <= a <= 89):
    print("B")
elif(70 <= a <= 79):
    print("C")
elif(60 <= a <= 69):
    print("D")
else:
    print("F")

#윤년
# 조건 1. 4의 배수, 100의 배수가 아닐 때
# 조건 2. 400의 배수일 때
import sys
year = int(sys.stdin.readline())
if (year < 0 | 4000 < year):
    # 들어가지 못하는 년수는 제외한다. 
    print("0")
elif (((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)):
    # 해당 문장에서 핵심은 4로는 나눠지고, 100으로 나눠지는건 둘다 참이어야 한다는 점이고, 400의 배수는 혼자 참이여도 적용이 된다는 점이다. 
    print("1")
else:
    print("0")

#틀린 답변
import sys
a = int(sys.stdin.readline())
if (((a % 4) == 0 & (a % 100) != 0) | (a % 400 == 0)):
    print("1")
else:
    print("0")

# 사분면 고르기
import sys
print("x값을 입력하시오.")
x = int(sys.stdin.readline())
print("y값을 입력하시오.")
y = int(sys.stdin.readline())

if (x > 0):
    if (y > 0):
        print("1")
    elif (y < 0):
        print("4")
elif (x < 0):
    if (y > 0):
        print("2")
    elif (y < 0):
        print("3")

# 사분면 고르기(short coding)
x = int(input("x 값을 입력하시오.\n"))
y = int(input("y 값을 입력하시오.\n"))
if x > 0:
    print(1 if y > 0 else 4)
elif x < 0:
    print(2 if y > 0 else 3)

# 알람시계
hh, mm = map(int,input().split())
mm_r = 0
if mm - 45 < 0:
    hh -= 1
    if hh < 0:
        hh = 24 + hh
    mm = (mm - 45)
    mm_r = 60 + mm
    print ("{0} {1}".format(hh, mm_r))
else :
    print("{0} {1}".format(hh, mm - 45))

# 알람시계(short coding)
a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)
# 이 방법은 이해하기 쉽진 않음. 수학적인 고려가 들어갔음.
a, b = map(int, input().split())
print((a-(b<45))%24, (b-45)%60)
# 이 방법은 비교 부호 연산자를 괄호로 묶을 시 참/ 거짓으로 변환된다는 점에서 착안함. b < 45 가 거짓이 성립하면 0이 되고, 참일 시 1이 되니 a에서 1을 줄일 수 있음. 
