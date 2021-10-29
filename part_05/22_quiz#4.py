'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최한다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였다. 
댓글 작성자 중 추첨으로 1명은 치킨, 3명은 커피 쿠폰을 받는다. 
추천 프로그램을 작성하시오. 

조건 1 : 편의상 댓글이 20명이 작성하였고, 아이디는 1 ~ 20이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 추첨, 단 중복 불가
조건 3 : random 모듈, shuffle, sample을 활용 

출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1 
커피 당첨자 : [2, 3, 4] 
-- 축하합니다 --
'''
# # 활용 예제 
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import * 

# 1번 내가 생각해서 구현한 방법
id = range(1, 21)
id = list(id)
print(" -- 당첨자 발표 -- ")
#shuffle(id)
i = set(sample(id, 1))
id = set(id)
id = id.difference(i)
i = list(i)
print("치킨 당첨자 : "+str(i[0]))
print("커피 당첨자 : "+str(sample(id, 3)))
print(" -- 축하합니다 -- ")

# 2번 저자가 구현한 방법
users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하 합니다 -- ")