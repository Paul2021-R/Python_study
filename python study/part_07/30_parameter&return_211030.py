# 전달 값과 반환 값 

balance = 0

def deposit(balance, money):
    print("입금이 완료 되었습니다. 입금액은 {1}원, 현재 잔액은 {0}원 입니다.".format((balance+money), money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 출금은 {0}원 되셨으며, 현재 잔액은 {1}원 입니다.\n".format(money, balance-money))
        balance = balance - money
        return balance 
    else : 
        print("잔액이 부족합니다. \n")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # 튜플 형식으로 값을 전달할 수 있다. 


while 1:
    answer = input("입금 하시겠습니까? (y/n)\n")
    if answer == "y":
        money = int(input("입금액을 입력하세요.\n"))
        balance = deposit(balance, money)

    else:
        print("입금을 종료합니다.")
        print("최종 입금액은 %d원 입니다. 감사합니다.\n" %balance)
        break
while 1:
    answer = input("출금을 하시겠습니까?(y/n)\n")
    if answer == "y":
        money = int(input("출금액을 입력하세요.\n"))
        balance = withdraw(balance, money)
    
    else:
        print("출금을 종료합니다. 감사합니다.\n")
        break

commission, balance = withdraw_night(balance, 500) # 따라서 리턴 값을 받는 것도 그러한 형태를 그대로 취하여 받을 수 있다. 
print("수수료 {0}원 이며, 잔액은 {1} 원입니다.".format(commission, balance))