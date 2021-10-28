# 문자열 처리 함수
python = "Python is Amazing"
print (python.lower()) # 문자열 소문자화
print (python.upper()) # 문자열 대문자화
print (python[0].isupper()) # 해당 문자가 대문자인지 확인하는 함수 
print (len(python)) # 문자열을 세주는 명령어 
print (python.replace("Python","Java")) # 특정 문자(열)을 찾아서 바꿔주는 함수

index = python.index("n") # 특정 문자가 어디 위치에 있는지, 위치값을 반환한다. 
print(index)
index = python.index("n", index + 1) # 위치를 특정지어서, 2번째 n을 구하는 방법 
print(index)

print(python.find("n")) # index 함수랑 같음 
print(python.find("Java")) # 단, 해당하지 않는게 나오면 -1이라고 값이 나옴 
# print(python.index("Java")) # index 명려어의 경우, 오류가 나게 된다.
# 더불어 16번 라인에서 프로그램이 진행되지 않고 멈춰 버린다. 

print(python.count("n")) # 특정 글자가 몇 번 나왔는지 반환하는 함수다. 