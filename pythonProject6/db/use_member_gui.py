import tkinter
from tkinter import *
from tkinter import messagebox
from db.member_dao import memberDAO

dao=memberDAO()

def create():
    id2 = id_entry.get()
    pw2 = pw_entry.get()
    name2 = name_entry.get()
    tel2 = tel_entry.get()
    vo=(id2, pw2, name2, tel2)
    dao.create(vo)

    id_entry.delete(0, END)
    pw_entry.delete(0, END)
    name_entry.delete(0, END)
    tel_entry.delete(0, END)

    img = tkinter.PhotoImage(file='img1.png')
    result2.configure(image=img)
    result2.image=img



def delete():
    id2 = id_entry.get()
    vo=(id2)
    dao.delete(vo)
    img = tkinter.PhotoImage(file='img2.png')
    result2.configure(image=img)
    result2.image = img

def select():
    id2 = id_entry.get()
    vo=(id2)
    one=dao.read(vo)
    print(one)
    img = tkinter.PhotoImage(file='img3.png')
    result2.configure(image=img)
    result2.image = img

def login():
    id2=id_entry.get()
    pw2=pw_entry.get()
    vo=(id2, pw2)
    one=dao.login(vo)
    if one!=None:
        print('로그인 성공>',one)
    else:
        print('로그인 실패')
    img = tkinter.PhotoImage(file='img4.png')
    result2.configure(image=img)
    result2.image = img


w=Tk()
w.geometry("500x750")
w.config(bg='lightgreen')

img = tkinter.PhotoImage(file='img1.png')
result2 = Label(w, image=img, width=400, height=400)
result2.pack()

id=Label(w, text='아이디', font=('맑은 고딕', 10))
id.pack()
id_entry=Entry(w, font=('맑은 고딕', 10), bg='lightgray', fg='black')
id_entry.pack()

pw=Label(w, text='비밀번호', font=('맑은 고딕', 10))
pw.pack()
pw_entry=Entry(w, font=('맑은 고딕', 10), bg='lightgray', fg='black')
pw_entry.pack()

name=Label(w, text='이름', font=('맑은 고딕', 10))
name.pack()
name_entry=Entry(w, font=('맑은 고딕', 10), bg='lightgray', fg='black')
name_entry.pack()

tel=Label(w, text='연락처', font=('맑은 고딕', 10))
tel.pack()
tel_entry=Entry(w, font=('맑은 고딕', 10), bg='lightgray', fg='black')
tel_entry.pack()

b1=Button(w, text='회원가입', font=('맑은 고딕', 10), bg='gray', command=create)
b1.pack()

b2=Button(w, text='회원탈퇴', font=('맑은 고딕', 10), bg='gray', command=delete)
b2.pack()

b3=Button(w, text='회원정보', font=('맑은 고딕', 10), bg='gray', command=select)
b3.pack()

b4=Button(w, text='로그인', font=('맑은 고딕', 10), bg='gray', command=login)
b4.pack()

w.mainloop()
