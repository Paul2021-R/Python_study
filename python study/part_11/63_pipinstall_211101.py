# pip install 
# 패키지 설치방법. 
# 이미 잘 만들어진 패키지를 잘 가져다 쓰는 것도 중요하다. 
# pipy 홈페이지에서 필요한 패키지를 다운로드 받아서 사용하면 된다. 
# 이번 학습에서는 'beautifulsoup 4' 를 기준으로 햇다. 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

'''
패키지 관련 주요 명령어 
pip install {패키지 이름} : 패키지 설치
pip list : 패키지 설치 된 내역 보여주기
pip show {패키지 이름} : 특정 패키지의 구체적인 정보 확인 가능 
pip install --upgrade {패키지 이름} : 특정 패키지 버전을 올리는 것
pip uninstall {패키지 이름} : 특정 패키지 삭제 
'''