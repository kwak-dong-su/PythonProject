print_data='''
----------------------
오늘에 대한 정보입니다.
----------------------
'''
print(print_data)
# print('----------------------')
# print('오늘에 대한 정보입니다.')
# print('----------------------')

weather, temperature, schedule = input('날씨, 온도, 스케쥴 입력>> ').split(',')
# weather=input('오늘의 날씨는? ')
# temperature=input('오늘의 온도는? ') #"10.3"
# schedule=input('오늘의 저녁 스케줄은? ')
print('----------------------')
print('오늘은', weather+'이고,', float(temperature)-1, '도이고', schedule+'에 머무를 예정입니다.')

