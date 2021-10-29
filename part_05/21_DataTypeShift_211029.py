# 자료 구조의 변형
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
# 필요에 따라 각각의 형태에 따라 활용 정도가 달라지고, 아마도 데이터가 많아지면, 그 많은 데이터들의 처리 과정에서 최적화가 필요할 것이다. 
# 따라서 지금은 그냥 있는데로 바로 명령어를 실행시키는 것으로 충분하나. 데이터가 많다면 많은 데이터 처리의 효율성을 위해 자료구조의 변형을 먼저 줄 수 있을 것이다. 