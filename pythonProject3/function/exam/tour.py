def spring(month, locaion):
    print('{0}월에 {1}에 가요!'.format(month, locaion))

#default로 설정하고 싶으면 파라미터 위치를 뒤에서붜 써주어야 한다.
#앞의 파라미터는 입력해주고, 입력해주지 않은 뒤의 파라미터를
#default값으로 입력해주라고 처리되기 때문!
#location, month, price=10000
def summer(location, month, price=10000):
    if month==6:
        price-=2000
    elif month==7:
        price-=1000
    elif month==8:
        pass
    else:
        price+=2000

    print('{0}월에 {1}를 가는 비용은 {2}원입니다.'.format(month, location, price))


