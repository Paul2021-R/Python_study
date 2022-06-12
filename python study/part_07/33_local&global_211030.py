# 지역변수와 전역변수 

# 지역 변수 = 함수 내에서만 사용 후 함수 호출이 끝나면 사라지는 것
# 전역 변수 = 프로그램 내 전체에서 사용 가능한 변수 

gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun이란 변수를 사용하도록 세팅을 하는 것 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    # gun 이라는 변수는 함수 내에서 초기화가 되어있지 않고, 이상태로는 함수 안의 gun은 지역변수로 지정되어 있어서 쓸 수 없다 ->전역 변수를 활용해야함


# 전역 변수는 코드 관리가 안되어 전달값으로 지정하여 사용하는 편이 좋다. 

def checkpoint_ret(gun, soldiers): # 여기서 gun 은 전역 변수가 아님. 지역 변수로 되어 버리는 것임
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun 

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2) # 전역 변수가  리턴값을 받아서 수정 되도록 한 것
print("남은 총 : {0}".format(gun))

