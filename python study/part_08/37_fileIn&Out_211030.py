# 파일 입출력 
# 파일 쓰기및 저장
score_file=open("score.txt","w", encoding="utf8") # 이름, 목적(w = 쓰기), 인코딩 정보 (한글은 항상 utf8 을 써야 깨짐을 방지 할 수 있다.)
print("수학 : 0",file = score_file)
print("영어 : 50",file = score_file)
score_file.close()

# 기존의 파일의 아래에 추가 저장 방법 
score_file = open("score.txt","a", encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 해당 명령어로는 순수하게 삽입인지라 자동으로 줄바꿈이 되진 않는다. 
score_file.close()

# 파일 전체 읽기
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read()) # 전체 출력 
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline()) # 줄 별로 읽기 동작을 수행, 커서는 다음 줄로 이동. 즉 내가 원하지 않더라도 개행이 됨.
print(score_file.readline()) 
print(score_file.readline(), end = "") 
print(score_file.readline(), end = "")  # 개행 없이 가도록 끝을 없애줌 
score_file.close()

# 몇 줄 인지 모를 때 
score_file = open("score.txt", "r", encoding = "utf8")
while 1:
    line = score_file.readline() # line 에 값이 들어가지 않을 때, if not 구문에 걸려 반복문을 빠져 나오게 된다. 
    if not line:
        break
    print(line, end = "")
score_file.close()

# list 에 값을 넣어서 처리할 것 
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # 모든 라인을 불러와서 list 형태로 저장함 
for line in lines:
    print(line, end = "")
score_file.close()