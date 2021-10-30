# 기본값 

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반이기에 기본 데이터가 동일하게 있는 경우 

def profile(name, age = 17, main_lang = "Python"): # 전달 안 받았을 때는 기본으로 입력되도록 된다. 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 사용 방법은 쉽다. 
profile("유재석", 20, "파이썬")
