# 사용자 정의 예외 처리
# 직접 에러를 만드는 것 

class BigNumberError(Exception):
    def __init__(self,msg): # 에러 자체 내부에 메시지를 넣어 주는 방법
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("1. 한 자리 숫자를 입력하세요 : ")))
    nums.append(int(input("2. 한 자리 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    if nums[0] >= 10 or nums[1] >= 10: ## 조건을 걸어 의도적으로 에러라고 발생시키는데 사용하는 구문. 
        raise BigNumberError("입력값 : {0}, {1}".format(nums[0], nums[1])) # raise 로 에러라고 인지시킨다. 
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 이것에 해당되지 않으므로
    print("잘못 입력 하셨습니다.")
except BigNumberError as err: # 실행 시 해당 에러가 발생하며,
    print("에러 발생, 한 자리 숫자만 입력하여주세요.")
    print(err)