# 외장함수 
# 직접 import 해서 사용해야 하는 함수들을 의미한다. 
# 구글링 : list of python modules
# Python modeule index 라는 페이지에서 내용을 볼 수 있다. 

# glob : 경로내의 폴더, 파일 목록 조회(윈도우 dir과 동일한 기능)
import glob
print(glob.glob("*.py")) 

# OS : 운영체제에서 제공하는 기본 기능 
import os
print(os.getcwd()) # 현재 디렉토리를 알려줌 

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os. rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다. ")

print(os.listdir()) # 현재 폴더 내의 목록을 보여준다. 

# time : 시간 관련 함수 들 
import time
print(time.localtime())
print(time.strftime("%Y %m %d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

# time delta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)