import turtle
import random


def click(x, y):
    count=0
    x2 = -400
    y2 = 400
    my_turtle.penup()  # 이동만!
    my_turtle.goto(x2, y2)
    while True:
        print(x, y)
        # x2=random.randint(-400, 400)
        # y2=random.randint(-400, 400)
        my_turtle.pensize(10)
        color_list=['green', 'blue', 'yellow', 'red', 'purple', 'pink']
        color_choice=random.choice(color_list)
        my_turtle.pencolor(color_choice)

        my_turtle.pendown()
        my_turtle.goto(x2, y2)
        if count%2==0:
            x2+=10
        else:
            y2-=10
        count+=1


my_turtle=turtle.Turtle('turtle')
turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(click, 1)
# my_turtle.pensize(20)
# my_turtle.pencolor('red')
turtle.done()

