'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
예) http://naver.com
규칙 1: http:// 부분은 제외 => naver.com
규칙 2: 처음 만나는 점 이후 부분은 제외 => naver
규칙 3: 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
			(nav)				(5)			(1)			(!)
예) 생성된 비밀번호 : nav51!
'''
URL = "http://naver.com"
PASSWORD = URL[7:10] + str(len(URL[7:URL.index(".")])) + str(URL[7:URL.index(".")].count("e")) + "!"
print (f"비밀번호 : {PASSWORD}")

url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# quiz 3 New version
url = "https://www.notion.so/ryu93notion/6-806e7fc28f6540cc81ae048540676469"
if url[4] == "s":
    modi_url = url.replace("https://", "")
else : 
    modi_url = url.replace("http://", "")
modi2 = modi_url[0:modi_url.index(".")]
password = modi2[:3] + str(modi2.count("e")) + "!"
# password = modi2[:3] + str(modi2.count("e")), "!" # 이렇게 '콤마'로 묶어서 넣어두니 아예 배열 처럼 인식을 해버린다..! 
#print(modi_url)
#print(modi2)
print(password)