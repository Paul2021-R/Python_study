# class 

# name = "marine"
# hp = 40
# damage = 5
# print ("{} 유닛이 생성되었습니다." .format(name))
# print ("체력 : {0}\n공격력 : {1}".format(hp, damage))
# # 이렇게 작성하는 것은 비효율적이다... 

# 틀을 만들어 서로 연관이 있는 함수와 변수의 집합체로 효율적으로 만드는 것이다. 

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}\n공격력 : {1}".format(hp, damage))
# class 최초 만들기

marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank1 = Unit("tank", 150, 35) # 한꺼번에 만들어졌다. 객체이다.
#객체 안에 존재 = 인스턴스 
# self 를 제외하고 나머지는 동일하게 들어가야만 한다. 

#맴버 변수란, 객체 안에 들어있는 변수들을 의미한다. 
wraith1 = Unit("wraith", 80, 10)
print("유닛 이름 : {0}\n공격력 : {1}".format(wraith1.name, wraith1.damage)) # .으로 연결하여 멤버 변수자체를 호출한 것이다. 

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (빼앗음) 
wraith2 = Unit("wraith takened", 80, 10)
wraith2.clocking = True # 새로운 멤버 변수를 새로이 만들었다. 내가 확장을 한 개체만 저장이 된다.
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))