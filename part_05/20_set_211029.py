# 집합(set)
# 중복 안 됨, 순서 없음 
my_set = {1, 2, 3, 3, 3}
print(my_set) # 중복을 허락하지 않아, 3이 한 번만 출력함. 더불어 {}로 묶지만 사전과 다른 점은 키값이 없다는 점이다. 

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합을 구해내는 방법 
print(java & python)
print(java.intersection(python)) # 요런 명령어를 활용하는 방법도 있음 

# 합집합을 출력 하는 방법 
print(java | python)
print(java.union(python))
print(java or python) # 이 녀석은 다르게 출력한다 왜그런 걸까?

# 차집합을 출력 하는 방법
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어났을때?
python.add("김태호")
print(python)

# java 까먹어서 빼야할 때 
java.remove("김태호")
print(java)