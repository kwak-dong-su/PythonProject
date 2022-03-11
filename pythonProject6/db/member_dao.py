import pymysql


class memberDAO:
    #인스턴스 변수
    conn=None #변수 생성 위치가 중요!
        # 클래스 바로 아래에 생긴 변수는 클래스 안 전체에서 사용 가능
        # 전역변수(글로벌 변수)
    cur=None

    def __init__(self):
        # 함수내에서 처음으로 만들어진 변수(지역변수, 로컬변수)는
        # 함수 밖에서는 인식 불가
        # 변수 위치가 중요!
        # 파이썬에서 변수는 언제 만들어지나??
        # 변수명 = 초기값
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3366,
                user='root',
                password='1234',
                db='big',
                charset='utf8'
            )
            print('1.연결 성공!!', self.conn.host_info)

            # 연결된 통로(stream)을 통해, sql문을 보내보자.
            # 2. 연결된 통로를 지정(접근할 수 있는 커서 객체를 획득)
            self.cur = self.conn.cursor()
        except Exception as e:
            pass

    def create(self, vo):
        try:

            # 3. sql문을 보내보자.
            sql = "insert into member values (%s, %s, %s, %s)"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한 것 반영해줘!
            # self.conn.close()

        except Exception as e:
            print('db연결 중 에러 발생!!')
            print('에러정보>> ', e)

    def read(self, id):
        try:
            # 3. sql문을 보내보자.
            sql = "select * from member where id=%s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, (id))
            print('sql문 전송 결과>', result)

            # read인 경우, 커서로 연결통로의 검색결과를 꺼내주어야 한다.
            row=self.cur.fetchone()
            # self.conn.close()
            return row

        except Exception as e:
            print('db연결 중 에러 발생!!')
            print('에러정보>> ', e)


    def login(self, vo):
        try:
            # 3. sql문을 보내보자.
            sql = "select * from member where id=%s and pw=%s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)
            # self.conn.close()
            one = self.cur.fetchone()

            return one

        except Exception as e:
            print('db연결 중 에러 발생!!')
            print('에러정보>> ', e)

    def delete(self, vo):
        try:
            # 3. sql문을 보내보자.
            sql = "delete from member where id=%s"

            # 커서로 sql문을 보냄.
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한 것 반영해줘!
            # self.conn.close()

        except Exception as e:
            print('db연결 중 에러 발생!!')
            print('에러정보>> ', e)

