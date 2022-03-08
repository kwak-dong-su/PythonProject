class Phone:
    def text(self):
        print('문자를 보내다.')

    def call(self):
        print('전화통화하다.')


class SamsungPhone(Phone):
    name=''

    def __init__(self, name):
        self.name=name

    def game(self):
        print('{0}과 게임하다.'.format(self.name))

    def internet(self, time):
        print('{0}시간 인터넷하다'.format(time))

class ApplePhone(Phone):
    size=0

    def __init__(self, size):
        self.size=size

    def picture(self):
        print('사진을 찍다.')

    def youtube(self, time, subject):
        print('{0}시간동안 {1}라는 주제로 유튜브하다'.format(time, subject))