# with 
# 좀더 편하게 파일을 열고 닫는, 명령을 수행하는 것이 가능함. 

import pickle

with open("profile.pickle", "rb") as profile_file: # 변수로 불러오고, 읽는 것까지 손쉽게 된다.
    print(pickle.load(profile_file))
# close할 필요 없다. 

# with 를 활용하여 일반 프로그램도 쉽고 빠르게 접근, 읽기, 쓰기가 가능하다. 
with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있습니다.")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())
