# 모듈 직접 실행 

# 모듈 내에서 직접 실행 여부 확인 방법 

# 1 모듈 내에서 확인 조건문을 작성하라 
'''
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요")
    trip_to = ThailandPackage() # 직접 안에서 실행한 경우
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
'''
# 2 외부 호출 시 표시를 남겨둔 뒤, 외부에서 실행시켜 본다. 

# 3 해당 기능을 활용하면 내외부 모듈 점검에 도움이 될 것으로 보인다. 