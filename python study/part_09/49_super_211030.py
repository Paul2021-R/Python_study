# super

class Unit:
    def __init__(self, name, hp, l_speed):
        self.name = name
        self.hp = hp
        self.l_speed = l_speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.l_speed))

class AttackUnit(Unit):# 상속 받는 곳을 기록한다. 
    def __init__(self, name, hp, damage, l_speed):
        Unit.__init__(self, name, hp, l_speed) # Unit 객체의 속성을 상속받는다. 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}\n공격력 : {1}".format(hp, damage))
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class flyable: # 날 수 있는 기능을 가진 클래스 
    def __init__(self, f_speed):
        self.f_speed = f_speed
    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.f_speed))

class f_attack(AttackUnit, flyable):
    def __init__(self, name, hp, damage, f_speed): 
        AttackUnit.__init__(self, name, hp, damage, 0) 
        flyable.__init__(self, f_speed)
    def move(self, location): # 메소드 오버라이딩이란 이런 것,....
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class buildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)  기존의 방식
        super().__init__(name, hp, 0) # super를 쓰는 것으로 unit 을 따로 적지 않아도 되며 self 를 적지 않는게 차이다. 상속을 한다고 기재 되어 있으면 자동으로 가게 된다. 단, 문제는 다중 상속일 때이다. 
        self.location = location

class Unit:
    def __init__(self):
        print("Unit  생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__() # 다중 상속 시에는 super 활용하지 않는다. 

dropship = FlyableUnit()