import turtle
import threading
import random



def go_random():
    t = turtle.Pen()

    for _ in range(10):
        if random.randint(1,2)==1:
            t.left(90)
        else:
            t.right(90)
        t.forward(random.randint(30,100))

def go_square():
    t = turtle.Pen()
    for _ in range(4):
        t.right(90)
        t.forward(100)


def go_star():
    t = turtle.Pen()
    for _ in range(50):
        t.right(132)
        t.forward(200)

if __name__ == '__main__':
    # run1=threading.Thread(target=go_random())
    # run2=threading.Thread(target=go_square())
    # run3=threading.Thread(target=go_star())
    while True:
        choice=input('선택 1)랜덤 2)별 >> ')
        if choice=='1':
            go_random()
        elif choice=='2':
            go_star()


