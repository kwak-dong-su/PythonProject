class TV:
    channel=0
    inch=0
    on_off=False

    def print_inch(self):
        print('화면크기는 {0}인치 입니다'.format(self.inch))

    def change_channel(self, channel):
        self.channel=channel
        print(' 채널을 {0}번으로 변경합니다.'.format(channel))

    def tv_on_off(self):
        self.on_off= not self.on_off
        if self.on_off:
            print('TV를 켭니다')
        else:
            print('TV를 끕니다.')


    def __str__(self):
        return str(self.channel)+', '+str(self.inch)+', '+str(self.on_off)