from tkinter import *

root = Tk()
root.title("GUI Practice")
# root.geometry("680x480")  # 기본 창 크기 설정
# root.geometry("680x480+100+300")  # 가로, 세로 크기, x 좌표, y 좌표
# root.resizable(False, False)  # 너비, 높이 변경 불가

btn1 = Button(root, text="버튼 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼 2222222222222222")
# padding 을 통한 크기 가변형
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼 3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼 4")
# 가로세로를 고정 지정함으로써 더이상 건드릴 수 없다.
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="./gui_practice/src/small_apple.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("button is clicked.")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
