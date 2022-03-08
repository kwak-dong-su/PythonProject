class Bike:
    #멤버변수 3개
    color=''
    shape=''
    light=False

    def __init__(self, color, shape, light):
        self.color=color
        self.shape=shape
        self.light=light

    #멤버함수 3개
    def speed_up(self):
        print(self.color + '색인 바이크의 속도를 up!')

    def light_on_off(self):
        self.light=not self.light
        if(self.light==True):
            print('라이트를 켰습니다.')
        else:
            print('라이트를 껐습니다.')

    def __str__(self):
        return self.color + ', ' + self.shape
    #객체 1개 b1만 생성해서, 멤버변수값 넣고, 프린트
    #멤버함수 2개 이상 호출.(리턴x, 리턴0)


class Car:

    #멤버변수
    color=''
    shape=''

    #이니셜라이저(멤버변수 초기화할 목적으로 만들어두는 함수)
    #객체 생성시 자동호출됨.
    #객체가 2개가 만들어지면, 2번 호출!
    def __init__(self, color, shape):
        self.color=color
        self.shape=shape

    #멤버함수

    def speed_up(self):
        print(self.color+'색인 자동차의 속도를 up!')

    def speed_down(self):
        print('자동차의 속도를 down!')

    def __str__(self):
        return self.color+', '+self.shape
