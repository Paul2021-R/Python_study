# 리스트 []

# 지하철을 칸 별로 10명, 20명, 30명  => 연속적인 공간에 한꺼번에 넣는 것 
# 기본 변수 설정
# subway1 = 10
# subway2 = 20
# subway3 = 30

# 리스트 방법 
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 리스트에서 특정 객체가 몇 번째에 있는가? 
print(subway.index("조세호")) # 1번 위치

# 리스트에 특정 객체를 넣기
subway.append("하하")
print(subway)

# 리스트에 특정 객체를 중간에 넣기 
subway.insert(1, "정형돈")
print(subway)

# 리스트 뒤에서부터 빼기 
print("빠진 사람 : "+ subway.pop(), subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지? 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능 
num_list = [6, 2, 1, 7, 9, 0, 4]
num_list.sort() # 오름차순으로 올라가는 것이 디폴트 값
print(num_list)

# 뒤지기 
num_list.reverse()
print(num_list)

# # 모든 내용 삭제
# num_list.clear()
# print(num_list)

# 다양한 자료형과 함께 활용이 가능하다. 
mix_list = ["류한솔", 21, "930910-1066512", False, True]
#print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)