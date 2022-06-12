# 튜플
# 리스트와는 다르게 내용 변경이나 추가를 할 수 없다. 
# 단, 당연히 속도가 더 빠르기 때문에 사용되는 경우가 있다. 

menu = ("돈까스", "치즈 돈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") # 당연히 안된다. 
# 고정시켜서만 사용 된다.

# 활용도 
# # 원래 형태 
# name = "김종국"
# age = 20
# hobby = "coding"
# print (name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 이런 식으로 한꺼번에 묶어서 사용이 가능하다. 단, 이런 활용은 딱히 효과적으로 보이진 않는다. 