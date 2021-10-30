# pickle
# 프로그램 상의 데이터를 파일 형태로 저장하는 것 
import pickle

# pickle 작성 방법 
profile_file = open("profile.pickle","wb") # 피클을 사용할 때는 항상 b= 바이너리 표시를 넣어야 함. 인코딩 설정할 필요는 따로 없다. 
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile의 정보를 profile_file에 저장하게 됨.
profile_file.close()

# pickle 읽어내는 방법

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # 파일의 정보를 변수에 불러오기가 됨 
print(profile)
profile_file.close()