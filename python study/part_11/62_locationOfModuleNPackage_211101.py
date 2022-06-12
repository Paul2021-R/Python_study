# 패키지, 모듈의 위치 
# 해당 명령어를 사용하면 파이선 패키지와 모듈 위치를 볼 수 있다. 
# 동시에 지정된 라이브러리에 넣게 되면, 내가 썻던 모듈을 다른데서도 활용이 가능하단 소리가 된다. 
import inspect
import random
print(inspect.getfile(random))

from travel import *
print(inspect.getfile(thailand))