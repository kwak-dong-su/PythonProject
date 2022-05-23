a='global 변수입니다.'

def test():

    def test2():
        nonlocal a
        b='local 변수입니다'
        print(a, b) # 바로 바깥쪽 변수 a와 지역변수 b를 출력

    def test3():
        global a
        a='global 변수명 바꿔주기' # 전역변수 a의 값을 변경

    a='nonlocal 변수입니다'
    test2()
    test3()

if __name__ == '__main__':
    print(a) # 전역변수 a 출력 => global 변수입니다.
    test()
    print(a)

    def func1(*args, **kwargs):
        for x in args:
            print(x)
        if len(kwargs)>0:
            print(kwargs)


    func1("hi", 1, a=5)
