# while 반복문 

# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if (index == 0):
#         print("커피가 폐기처분 되었습니다.")

# customer = "Ironman"
# index = 5
# while 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if (index == 0):
#         break

customer = "Thor"
person = "Unknow"

while (person != customer):#조건에 만족할 때까지 반복하는데, 이때 확정이 되면 프로그램을 만나서 탈출하고 종료하게 된다. 
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?\n") 