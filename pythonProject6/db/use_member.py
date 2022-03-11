import sys
from db.member_dao import memberDAO

if __name__ == '__main__':
    dao=memberDAO()

    while True:
        choice=input('cud중 선택>> 1)회원가입, 2)회원탈퇴, 3)회원정보, 4)로그인처리>> ')
        if choice=='1':
            id=input('id입력>> ')
            pw=input('pw입력>> ')
            name=input('name입력>> ')
            tel=input('tel입력>> ')
            vo=(id, pw, name, tel)
            dao.create(vo)
        elif choice=='2':
            id = input('삭제할 id입력>> ')
            vo=(id)
            dao.delete(vo)
        elif choice=='3':
            id = input('조회할 id입력>> ')
            vo=(id)
            one=dao.read(vo)
            print('id: {0} \t pw: {1} \t name: {2} \t tel: {3}'.format(one[0], one[1], one[2], one[3]))
        elif choice=='4':
            id=input('id 입력>> ')
            pw=input('pw 입력>> ')
            vo=(id, pw)
            one=dao.login(vo)
            if one!=None:
                print('로그인 성공', one)
            else:
                print('로그인 실패')
        else:
            sys.exit()