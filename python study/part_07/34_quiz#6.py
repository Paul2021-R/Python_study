'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오. 

* 표준 체중 : 각 개인의 키에 적당한 체중 
(성별에 따른 공식)
남자 : 키(m) * 키 (m) * 22
여자 : 키(m) * 키 (m) * 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산 
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째 자리까지 표시 

키 175cm 남자의 표준 체중은 67.38kg 입니다. 

'''

def std_weight(height, gender):
    if gender == "male":
        st_weight = round(((height / 100) ** 2 * 22), 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height, st_weight))
    else:
        st_weight = round(((height / 100) ** 2 * 21), 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height, st_weight))

def std_weight_ref(height, gender):
    if gender == "male":
        return height ** 2 * 22
    else:
        return height ** 2 * 21


std_weight(175, "male")
std_weight(175, "female")

height = 175
gender = "male"
weight = round(std_weight_ref(height / 100, gender), 2) # 이렇게 반올림을 해야 정확하게 나온다... 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))