import random
import threading
import time
import tkinter
from tkinter import *
from tkinter import Label


class RacingCar:
    #멤버변수
    name=''
    score=0
    label1=Label
    x1=0
    y1=0


    #초기화함수
    def __init__(self, name, label, x1, y1):
        #self: 클래스로 생성한 객체!
        #c1 = RacingCar('appleCar'), c2, c3
        #self==c1
        # c1.name='applecar'
        self.name=name
        self.label1=label
        self.x1=x1
        self.y1=y1

    #멤버함수
    def runCar(self):
        while True:
            # 랜덤하게 움직일 값을 생성해서
            # 랜덤생성한 jump값을 기존의 x에 더해준다.
            # y축 값은 변하지 않음.
            jump=random.randint(1, 20)
            self.x1+=jump
            self.label1.place(x=self.x1, y=self.y1)
            time.sleep(0.1)
            if self.x1>500:
                RacingCar.score += 1
                score_label = Label(w, text='{0} {1}등!'.format(self.name,RacingCar.score), font=('맑은 고딕', 15))
                score_label.pack()
                break


def run_start():
    # 라벨 객체 만들어서 w에 끼워넣어야 함.
    ## 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.


    run_list=list()
    y1 = 100
    for i in range(10):
        run_list.append(RacingCar('appleCar', car_list[0], 10, y1))
        y1 += 50

    # c1 = RacingCar('appleCar', car_label1, 10, 100)
    # c2 = RacingCar('summerCar', car_label2, 10, 150)
    # c3 = RacingCar('springCar', car_label3, 10, 200)

    thread_list=list()
    for i in range(10):
        thread_list.append(threading.Thread(target=run_list[i].runCar()))


    # t1 = threading.Thread(target=c1.runCar)
    # t2 = threading.Thread(target=c2.runCar)
    # t3 = threading.Thread(target=c3.runCar)
    # t1.start()
    # t2.start()
    # t3.start()

if __name__ == '__main__':

    w=Tk()

    w.geometry('600x900')
    w.title('멀티 스레드 자동차 경주')
    b=Button(w, text='멀티 스레드 시작', command=run_start)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

    car_list=list()
    num = 0
    y1 = 100
    for i in range(10):
        imgname='car'+str(num%3+1)+'.gif'
        print(imgname)
        p1 = PhotoImage(file=imgname)
        car_list.append(Label(w, image=p1))
        car_list[i].place(x=10, y=y1)
        num += 1
        y1+=50



    # p1=PhotoImage(file='car1.gif')
    # car_label1=Label(w, image=p1)
    # car_label1.place(x=10, y=100)
    #
    # p2 = PhotoImage(file='car2.gif')
    # car_label2=Label(w, image=p2)
    # car_label2.place(x=10, y=150)
    #
    # p3 = PhotoImage(file='car3.gif')
    # car_label3: Label=Label(w, image=p3)
    # car_label3.place(x=10, y=200)
    w.mainloop()


