# 다중 상속 
# 상속을 한 번 받고 끝날리가 있나. 
# 부모 클래스를 2회 이상 받는 경우를 말한다. 
# 부모 클래스 -> 상속을 주는 클래스, 자식 클래스 -> 상속을 받는 클래스 

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛 
class AttackUnit(Unit):# 상속 받는 곳을 기록한다. 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit 객체의 속성을 상속받는다. 
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

class f_attack(AttackUnit, flyable):#공격, 날수 있다 두가지를 동시에 만족하며, 두 부모의 기능을 모두 쓸 수 있음을 의미한다. 
    def __init__(self, name, hp, damage, f_speed): #다중 상속 시 콤마로 구분
        AttackUnit.__init__(self, name, hp, damage) # self 그 자체는 절대 잊지 말것 
        flyable.__init__(self, f_speed)

valkirie = f_attack("valkirie", 200, 8, 5)
valkirie.fly("valkirie", 3)

# 클래스를 작성할 때는, 아주 기초적인 공통 기능을 중심으로 먼저 작성하고, 점점더 복잡하게 고려하는 것을 생각하면 될 것 같다. 