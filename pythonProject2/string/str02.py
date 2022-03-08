# 주민번호 13자리를 입력을 받아서
# 나이와 성별을 판별해보세요.
import datetime
today=datetime.datetime.today()
print(today.year, today.month, today.day)

year=2022
num=input('주민번호 13자리 입력 > ')

born=num[0:2]
count=int(num[0:2])
age=1
gender=""

if num[6]=='1' or num[6]=='3':
    gender="남자"
else:
    gender="여자"

if born[0]=='0' or born[0]=='1' or born[0]=='2':
    count=count+2000
else:
    count=count+1900

while(count!=year):
    age=age+1
    count=count+1

print('나이는 {0}세, 성별은 {1}입니다.'.format(age, gender))