# 패키지
# 모듀들을 모아놓은 집합을 의미한다. 

import travel.thailand
# 직접적인 임포트는 모듈이나 패키지만 가능하다. 
# 클래스, 함수는 직접적으로 임포트 불가능핟.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
tirp_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
