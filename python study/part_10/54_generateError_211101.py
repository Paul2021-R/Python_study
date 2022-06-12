# 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("1. 한 자리 숫자를 입력하세요 : ")))
    nums.append(int(input("2. 한 자리 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    if nums[0] >= 10 or nums[1] >= 10: ## 조건을 걸어 의도적으로 에러라고 발생시키는데 사용하는 구문. 
        raise ValueError # raise 로 에러를 발생시킨다. 
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("잘못 입력 하셨습니다.")
