# from random import *
# a = "치킨"
# b = "피자"
# c = "햄버거"

# front = '오늘 먹고 싶은 것은?'
# back = '입니다!'

# rand_num = int(random() * 10) # 0~ 9까지 
# if rand_num < 4:
#     print(front, a, back)
# elif 4 <= rand_num < 7:
#     print(front, b, back)
# else :
#     print(front, c, back)
# print(rand_num)

# from math import *
# print(floor(2.874361238)) #내림
# print(ceil(2.874361238)) #올림
# print(sqrt(2)) #제곱근 구하기 

# 임의의 숫자를 입력하는 방법 
# from random import *
# print(random())
# print(int(random()*40)) # 0 ~ 40 미만 이하의 임의의 값 생성
# print(randrange(0, 41)) # 위와 동일
# print(randint(0, 40)) # 위와 동일 

# 문자열 
# str1 = """심심하면 이렇게 적고
# 이렇게도 적을 수 있고
# 이렇게도 적을 수 있다."""
# print(str1)

# 문자열 슬라이싱 
# jumin = "930910-1077651"
# #jumin = "010820-2000000"
# if int(jumin[7]) == 1:
#     print("성별 : " + jumin[7] + "(남성)")
# else :
#     print("성별 : " + jumin[7] + "(여성)")
# if int(jumin[0] != 0):
#     print("출생년도 :", "19" + jumin[:2] + "년도")
# else:
#     print("출생년도 :", "20" + jumin[:2] + "년도")
# print("출생일자 :", jumin[2:4], "월", jumin[4:6], "일")
# print("음수 방식으로 구하기 :", jumin[-14:])

# 문자열 처리 방법 
# line = 'Python is interestig'
# print(line.index("i",8, 11))
# print(line.find("i", 8, 11))
# print(line.count("i",0,11))
# print(line.replace("Python", "C"))
# print(len(line.replace("Python", "C")))

# quiz 3 New version
url = "https://naver.com"
if url[4] == "s":
    modi_url = url.replace("https://", "")
else : 
    modi_url = url.replace("http://", "")
modi2 = modi_url[0:modi_url.index(".")]
password = modi2[:3] + str(modi2.count("e")) + "!"
# password = modi2[:3] + str(modi2.count("e")), "!" # 이렇게 '콤마'로 묶어서 넣어두니 아예 배열 처럼 인식을 해버린다..! 
print(modi_url)
print(modi2)
print(password)
