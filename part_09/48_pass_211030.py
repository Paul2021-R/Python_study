# pass

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
        pass # 아무것도 안하고 일단 넘어가는 것. 

supply_depot = buildingUnit("supply_depot", 500, 3)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
# pass 라고 기재 되어 있으면, 아무것도 하지 않고 기능 이름만을 구현한 거나 마찬가지다. 