# 메소드 

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}\n공격력 : {1}".format(hp, damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name # (self.x = 자기자신 , x = 입력된 값 )
        self.hp = hp
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


firebat = AttackUnit("firebat", 80, 10)
firebat.attack("5시")

firebat.damaged(40)
firebat.damaged(40)

