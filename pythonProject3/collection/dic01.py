hobby3= [
    {10: {'아침':'game', '저녁':'picture'}},
    {20: {'아침':'coffee', '저녁':'tour'}}
]
print(hobby3[1][20]['저녁'])



hobby2= {10: {'아침':'game', '저녁':'picture'}, 20:['tour', 'run', 'coding']}
print(hobby2[10]['저녁'])




hobby= {10: ['game', 'picture'], 20:['tour', 'run', 'coding']}
#10대의 취미 목록을 프린트
print(hobby[10])
#20대의 취미 목록을 프린트
print(hobby[20])
#20대의 취미 목록을 카운트
print(len(hobby[20]))




food={'아침':'토스트','점심':'한정식','저녁':'스프'}
print(food['아침']) #값을 확인할 때 : 딕셔너리이름[키]
food['아침']='커피' #값을 수정할 때
print(food)
food['간식']='쿠키' #값을 추가할 때
print(food)
del food['간식']
print(food)

#dic를 for-each문으로 돌렸을 때는 key만 가지고 온다.
for key in food:
    print(key, ':', food[key])

dict1={100: 'hong', 200: 'kim'}
print(dict1[100])

for key in dict1:
    print(key, ':', dict1[key])

key_list=dict1.keys()
print(key_list)
key_list2=list(key_list)
print(key_list2)

value_list=dict1.values()
print(value_list)

print(dict1.get(100))
print(100 in dict1) #결과가 bool
# 회원명단 중에서 500이 있나요?
if 500 in dict1:
    print('500회원이 존재합니다.')
else:
    print('존재하지 않습니다')