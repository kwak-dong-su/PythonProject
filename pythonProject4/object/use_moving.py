import object.moving as m #module까지 써주어야 함

# class의 instance인 object!
c1=m.Car('red', '네모') #new Car()
c2=m.Car('green', '세모')
#객체 생성시 자동으로 멤버변수값을 초기화해주는 함수를 하나 만들자!
#(생성자 메소드, 초기화 해주는것, initializer(이니셜라이저)

# c2.shape='세모'
# c2.color='green'
print(c1)
print(c2)
c1.speed_up()
c2.speed_down()
print('---------------')
b1=m.Bike('black', '동그라미', True)
b1.color='black'
b1.speed_up()
b1.light_on_off()
b1.light_on_off()
print(b1)