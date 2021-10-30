# 가변 인자 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 :{0}\t나이 : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2 ,lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C#", "C++")
# profile("김태호", 25, "Python", "Java", "", "", "")

# 함수가 받는 값을 지정하게 되어버리면, 그것에 맞추지 않고는 해당 함수가 정상 작동하지 않는다. 
# 따라서 이를 해결하기도 하고, 혹여 더 많은 값을 받아야 하는 경우도 있다고 할 때 사용하는 것이 가변인자이다. 

def profile(name, age,*language): #가변인자로 *을 작성한 뒤, 해야하는 작업을 반복문으로 돌리면 활용이 용의하다. 
    print("이름 :{0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C#", "C++")
profile("김태호", 25, "Python", "Java")