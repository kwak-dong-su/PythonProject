num1=int(input('숫자1: '))
num2=int(input('숫자2: '))

print(num1,'+',num2,'=',num1+num2)
print(num1,'-',num2,'=',num1-num2)
print(num1,'*',num2,'=',num1*num2)
print(num1,'/',num2,'=',num1/num2)

name=input('입력1: ')
age=input('입력2: ')

print(name+'은 '+age+'세 입니다.')
if int(age)>100:
    print('나이가 많으시군요!')
else:
    print('아직 어리시군요!')
    

hobby=input('hobby: ')
time=input('time: ')

print(hobby+'를 '+time+'시간 했습니다.')
if hobby=='달리기' and int(time)>=10:
    print('오늘 '+hobby+'는 충분')
elif hobby=='달리기' or int(time)<=10:
    print('어떤 운동이든 시작하세요!!')

