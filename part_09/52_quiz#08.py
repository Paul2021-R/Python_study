'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다. 
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년 

[코드]

    Class House:
        # 매물 초기화
        def __init__(self, location, house_type, deal_type, price, completitio_year):
            pass

        # 매물 정보 표시 
        def show_detail(self):
            pass
'''

# 마이 버전
class House:
    
    notice_on = False

    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completition_year):
        self.location = location
        self.houseT = house_type
        self.deal = deal_type
        self.price = price
        self.completition = completition_year
        if House.notice_on == True:
            print("{0}의 {1}가 등록 되었습니다.".format(self.location, self.houseT))
        else:
            return

    # 매물 정보 표시 
    def show_detail(self):
        print(self.location, self.houseT, self.deal, self.price, self.completition)

House.notice_on = False # 업데이트 표시 여부 스위치 

h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

all = []
all.append(h1)
all.append(h2)
all.append(h3)


# i = 0
# for house in all:
#      i += 1
# print("총 {0}대의 매물이 있습니다.".format(str(i)))
print("총 {0}대의 매물이 있습니다.".format(len(all)))

for house in all:
    house.show_detail()
