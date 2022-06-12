# 예외처리 
# 에러 발생 시를 처리해 주는 것을 말한다. 
## unexpected indent : 다른 문장들과 들여쓰기가 달라서 발생하는 경우가 있을 수있다. 

# try : # 해당 명령문으로 작동하다가, 정상 작동이 아니라고 판단되면
#     print("나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력하세요. : "))
#     num2 = int(input("두번째 숫자를 입력하세요. : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError: # 해당 에러가 발생시 예외 처리용 명령을 찾아서 실행한다. 
#     print("에러가 발생 하였습니다.")
# except ZeroDivisionError as err:
#     #err = "Hi"
#     print(err)

try : # 해당 명령문으로 작동하다가, 정상 작동이 아니라고 판단되면
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요. : ")))
    nums.append(int(input("두번째 숫자를 입력하세요. : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 해당 에러가 발생시 예외 처리용 명령을 찾아서 실행한다. 
    print("에러가 발생 하였습니다.")
except ZeroDivisionError as err:
    #err = "Hi"
    print(err)
# 현재 인덱스 상에 존재하지 않게 된 값이 있을 때 처리 방법 
except: # 위에 기록된 예외 처리 사항과는 다른 경우의 에러는 여기서 확인된다. 
    print("알 수 없는 에러가 발생하였습니다.")
