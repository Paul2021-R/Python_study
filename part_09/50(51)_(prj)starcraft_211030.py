from random import *
class Unit:
    def __init__(self, name, hp, l_speed):
        self.name = name
        self.hp = hp
        self.l_speed = l_speed
        print("{0},유닛이 생성되었습니다.".format(name))

    def move(self, location):
        #print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.l_speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):# 상속 받는 곳을 기록한다. 
    def __init__(self, name, hp, damage, l_speed):
        Unit.__init__(self, name, hp, l_speed) # U nit 객체의 속성을 상속받는다. 
        self.damage = damage
        print("체력 : {0}\n공격력 : {1}".format(hp, damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))


class flyable: # 날 수 있는 기능을 가진 클래스 
    def __init__(self, f_speed):
        self.f_speed = f_speed

    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.f_speed))

class f_attack(AttackUnit, flyable):
    def __init__(self, name, hp, damage, f_speed): 
        AttackUnit.__init__(self, name, hp, damage, 0) 
        flyable.__init__(self, f_speed)

    def move(self, location): # 메소드 오버라이딩이란 이런 것
        self.fly(self.name, location)

class Marine(AttackUnit): #마린 유닛 클래스 구성
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 50, 5, 5)

    def steampack(self): # 스팀팩 기능 구현 
        if self.hp > 10:
            self.hp -= 10
            self.l_speed *= 1.5
            self.damage *= 1.2
            print("{0} : 스팀팩을 사용합니다. (hp 10감소)".format(self.name))
        else :
            print("{0} : 스팀팩을 사용이 불가능 합니다.".format(self.name))

class Tank(AttackUnit): # 시즈탱크 클래스 작성 
    
    seize_developed = False # 시즈모드 개발 여부 . 클래스 자체가 가지는 특성은 최 상단에 작성함(일종의 클래스 내부의 지역변수로 고려됨. )
    
    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 10, 20)
        self.seize_mode = False # 

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
            
        elif self.seize_mode == False:
            print("{0} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else: 
            print("{0} : 시즈 모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
    
class Wraith(f_attack):
    
    clocking_developed = False
    
    def __init__(self):
        f_attack.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False 

    def clocking(self):
        if Wraith.clocking_developed == False:
            print("{0} : 클로킹 모드를 개발해주십시오.".format(self.name))
            return 
        if self.clocked == True:
            print ("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 활성화 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("Notice. Game is now")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#게임 실행
game_start()

# 마린 3기 

m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기
t1 = Tank()
t2 = Tank()

# 레이스 1기

w1 = Wraith()

# 유닛 일괄 관리 
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동 
for unit in attack_units:
    unit.move(1)

# 탱크 시즈 모드 개발
Tank.seize_developed = True
Wraith.clocking_developed = True
print("[알림] 시즈모드 레디")
print("[알림] 클로킹 레디")

# 공격 모드 준비 
for unit in attack_units:
    if isinstance(unit, Marine):# 특정 인스턴스인지를 확인
        unit.steampack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack(1)

# 전군 피해 
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_start()
