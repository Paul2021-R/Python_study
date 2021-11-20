# # 출력 연습
# print('Hello World!')

# # 문장 2번 출력
# for we_love_kriii in range(0, 2):
#     print("강한친구 대한육군")

# # 고양이
# print ("\\    /\\\n )  ( ')\n(  /  )\n \\(__)|")

# # 개
# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")
# # 역슬래쉬 한번 해줘야함
# # 쌍따옴표 역시 \ 를 넣어줘야 문자로만 인식함. 

# # A + B
# a, b = map(int, input().split())
# print(a+b)
# # map (func.iterable) : 순차적으로 병렬로 연결된 변수에 반복가능한 객체 함수를 설정하여 입력시킨다. 최소 인자가 두개 이상이어야 한다. 
# # iterable : 반복 가능한 객체 
# # 대표적인 iterable type = list, dict, set, str, bytes, tuple, range 
# # input() : 키보드 입력을 받는다.
# # split() : intput의 옵션 중 하나. 구분된 형태로 각각 문자열로 값을 취한다. 

# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# print(a + b + c)

# # A - B
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a - b)

# # A * B
# a, b = map(int, input().split())
# print(a * b)

# # A / B
# a, b = map(int, input().split())
# print(a / b)

# # mathmetics
# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# # // 나눈 값만 구하는 것. 
# # / 나눴을 때 소숫점까지 구하는 것.

# # reminder
# a, b, c = map(int, input().split())
# ans1 = (a+b)%c
# ans2 = ((a%c)+(b%c))%c
# ans3 = (a*b)%c
# ans4 = ((a%c)*(b%c))%c
# print(ans1)
# print(ans2)
# print(ans3)
# print(ans4)

# a, b, c = map(int, input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)
# # 백준 코딩 테스트 상에서 보면, 실질적으로 속도상 차이는 없었음. 
# # 메모리 사용량까지 동일한 것으로 볼 때 print 함수 돌아가는 과정에서 변수 임의 지정 및 출력이 되는 것으로 보여진다. 따라서 양 쪽의 큰 차이보단 관리적차원과 효율적 차원에서 어느쪽이 나은지 고려하면 될듯. 

# #  multiplication
# a = input()
# b = input()

# # 변수 지정 후 연산부
# # 문제에서 자리수를 맞추지 않고 출력하는 걸 요구했으므로, 최종 연산시에만 자리수에 맞춰서 합을 구한다. 
# ans3 = int(a) * int(b[2])
# ans4 = int(a) * int(b[1])
# ans5 = int(a) * int(b[0])
# ans6 = ans3 + (ans4 * 10) + (ans5 * 100)

# print(ans3)
# print(ans4)
# print(ans5)
# print(ans6)

a, b = map(int, input("두 개의 값을 입력하세요.").split(','))
print ("{0} 을 입력하셨군요?".format(a))
print ("{0} 을 입력하셨군요?".format(b))