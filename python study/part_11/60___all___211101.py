# __all__

# from random import *
from travel import *
# 왜 안됨? 
# 이유는 패키지 않에서 임포트 되기 원하는 것과 아닌 것에 대하여 구분처리를 해줘야 한다. 
# __init__.py파일 참조 
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()