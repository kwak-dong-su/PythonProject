#북마크 테이블에 대한 crud기능 처리를 하고 싶음.
# from db import dao
# from 패키지 import 모듈명
#--> 모듈.함수(), 모듈.클래스명()
import sys
from tkinter import messagebox

from db.dao import *
# from 패키지명.모듈명 import 함수명, 클래스명, *
#--> 함수()

if __name__ == '__main__':
    while True:
        choice=input('cud중 선택>> 1)c, 2)u, 3)d, 4)r(one), 5)r(all)>> ')
        if choice=='1':
            id=input('id입력>> ')
            name=input('name입력>> ')
            url=input('url입력>> ')
            img=input('img입력>> ')
            vo=(id, name, url, img)
            create(vo)
        elif choice=='2':
            #id가 1이면, name은 naver2로 변경
            id = input('id입력>> ')
            name = input('수정할 name입력>> ')
            vo=(name, id)
            update(vo)
        elif choice=='3':
            # id가 1이면 삭제
            id = input('삭제할 id입력>> ')
            vo=(id)
            delete(vo)
        elif choice=='4':
            id=input('조회할 id 입력>>')
            row=read(id) #id를 주면서 검색해와라!

            messagebox.showinfo('결과', '검색결과는 '+row[0]+", "+row[1]+", "+row[2]+", "+row[3])
        elif choice=='5':
            all=all()
            ## 출력해주세요
            print('id \t name \t url \t img')
            print('-----------------------------------------------')
            for one in all:
                print('{0} \t {1} \t {2} \t {3}'.format(one[0], one[1], one[2], one[3] ))

        else:
            sys.exit()