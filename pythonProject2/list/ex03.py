import datetime
import random

food=['감자', '고구마', '양파']
print(food[1])
print(food[0:2])
print(food[1:3])
food[0]='라면'
print(food)

today=datetime.datetime.today()
month=today.month
season=''
if month>=3 and month<=5:
    season='봄'
elif month>=6 and month<=8:
    season = '여름'
elif month>=9 and month<=11:
    season = '가을'
elif month==12 or month==1 or month==2:
    season = '겨울'
print('지금은 {0}월, {1}입니다.'.format(month, season))

sum=0
for i in range(10, 21):
    sum+=i
print(sum)

target=55 #random.randint(1, 100) 1~99까지
count=0
while True:
    num = int(input('숫자 입력>> '))
    count+=1
    if num>target:
        print('더 작은 숫자를 입력하세요!')
    elif num<target:
        print('더 큰 숫자를 입력하세요!')
    else:
        print('정답입니다! (입력 횟수: {0}회)'.format(count))
        break


start=int(input('시작값 입력>> '))
end=int(input('끝값 입력>> '))

count=end-start+1
sum=0
average=0
for i in range(start, end+1):
    sum+=i
print('시작과 끝 사이의 개수는 {0}개, 합계는 {1}, 평균은 {2}입니다.'.format(count, sum, sum/count))


mv_list=[]
ti_list=[]
seat=0
for i in range(10):
    mv_list.append(0)

while True:
    seat=int(input('예매 좌석(1~10번) 입력(0 입력시 종료) >>'))
    if seat>10 or seat<0:
        print('올바른 좌석번호를 입력하세요.')
    elif seat!=0:
        if mv_list[seat-1]==1:
            print('이미 선택하신 좌석입니다.')
        else:
            mv_list[seat-1]=1
            ti_list.append(seat)
            print('선택되었습니다.')
    else:
        print('예매하신 좌석 번호는 {0}, 총 {1}개이고, 금액은 {2}원입니다.'.format(ti_list, len(ti_list), len(ti_list)*10000))
        break







