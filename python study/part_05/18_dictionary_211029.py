#사전 dictionary
# 코딩에서 필요한 키와 그 정보를 보여줄 수 있는 것
cabinet = {3:"유재석", 100:"김태호"} # 사전은 중괄호로 열고 닫는다. 선 숫자는 키값, 콜론 뒤 값이 본 값이다. 
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # get 명령어를 사용하여서도 값을 볼 수 있다. 
# print(cabinet[5]) # 정확한 키값을 입력하지 않으면, 아래의 명령어를 실행하지 않고 프로그램이 종료되어 버린다. 
print(cabinet.get(5)) # ✔️None 명령어 get 을 활용할 경우, 결과 값을 반환하므로, 당연히 오류가 아닌 정상 작동을 하게 된다. 이에 다음에 이어질 것들이 정상 실행될 수 있게 된다. 따라서 오류나 중간에 멈추는 것을 방지하기에는 리스트.get() 문법을 쓰는 게 최선이다. 

print(cabinet.get(5, "사용 가능")) #이렇게 작성시, 해당 자료가 없으면 출력 문자 지정 가능. 즉, 쓰지 않은 키값을 확인할 수 있다. 

# 키값이 존재하는지 여부 확인하는 방법
print(3 in cabinet) # boolean 형으로 결과를 보여줌 
print(5 in cabinet)

# 정수가 아닌 string 키값도 지정 가능 
cabinet_n = {"a1":"유재석", "a2":"하하"}
print(cabinet_n["a1"])

# 캐비넷 새값 추가하기 
print(cabinet_n)
cabinet_n["a3"] = "조세호" # 키 값에 따라서 덮어씌우기도 가능하다. 
print(cabinet_n)

# 리스트 값 삭제하기 
del cabinet_n["a3"]
print(cabinet_n)

# 캐비넷에서 key 만 출력 방법
print(cabinet_n.keys())

# 캐비넷에서  value만 출력 방법
print(cabinet.values())

# 캐비넷에서 key, value 쌍으로 출력 
print(cabinet_n.items())

# 모든 값을 삭제 
cabinet_n.clear()
print(cabinet_n)