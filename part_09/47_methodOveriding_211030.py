# 메소드 오버라이딩 
# 자식 클래스에서 정의한 메소드를 쓰고 싶을 때, 메소드를 새롭게 정의 내릴 수 있다. 

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

virture = AttackUnit("virture", 80, 20, 10)

battle = f_attack("battle", 500, 25, 3)

virture.move(3)
# battle.fly("battle", 3)
battle.move(3)
# 지상, 공중 양쪽이 다른 함수를 쓰다보니 굉장히 번거롭고 불편하니, 한번에 알아서 지상 내지는 공중으로 가도록 만드는게 오버라이딩 이다. 
# 오버라이딩의 포인트는, 자식 클래스에서 다시 메소드를 정의하고, 그 정의 메소드가 부모 클래스의 기능을 호출하는 방식으로 호출의 형태를 통일화를 시키는 것에 있다. 
