# 모듈
# 부품처럼 만든다 뭘로? 파일로 
# 하나의 총체의 SW에서 부품만 교체 가능하도록 만들면, SW 관리보수 성능 향상에 매우 효과적일 수 있다.
# 함수, 클래스, 사전 등을 묶어 파일로 만들고, 해당 파일을 .py로 지정하는 형태다. 

# 모듈 사용 방법. 
# 같은 폴더에 있거나 파이썬 라이브러리 등 파일이 모여져 있는 곳에 쓸 모듈이 존재할 때 작동한다. 

#방법 1
import theater_module 
# 3명 영화보러 갈 때 가격 
theater_module.price(3)
# 4명 조조
theater_module.price_morning(4)
# 5명 군인
theater_module.price_soldier(5)

# 방법 2 
# 함수 명 자체를 줄여버림으로써 쓰기 편하게 만들기 
import theater_module as tp
tp.price(3)
tp.price_morning(4)
tp.price_soldier(5)

# 방법 3
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# 방법 4
from theater_module import price, price_morning
price(3)
price_morning(4)
#price_soldier(5) 오류 뜸. 왜냐면 지정이 import에서 구체적으로 되어 있기 때문이다. 

# 방법 5
# 특정 함수만 가져와 쓸 때는 이런 식으로 약칭을 지정해 줄 수 있다. 
from theater_module import price_soldier as price
price(5)
