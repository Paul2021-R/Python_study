# # if (분기문)
# weather = input("How about today's weather?\n")
# if weather == "rain" or weather == "snow": #default condition 희한하게도 | 가 제대로 먹히지 않는다.
#     print("Preparing your umbralla")
# elif weather == "dust": 
#     print("Preparing your mask")
# else:
#     print("You don't need to prepare anything")

temp = int(input("기온은 어떤가요?(숫자만 입력하여 주세요)\n"))
if (30 <= temp):
    print("엄청 덥네요... 주의!")
elif 10 <= temp < 30: # 조건을 통합하여 작성하는 방법
    print("날씨가 괜찮네요 :)")
elif 0 <= temp and temp < 10: # 조건을 and 나 or 을 활용하는 방법
    print("조심하세요! 따뜻한 옷은 필수 입니다. ")
else :
    print("너무 춥네요. 나가지 마세요!")