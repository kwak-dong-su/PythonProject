from object.worker import Worker

if __name__ == '__main__':
    w1=Worker('홍길동', 25, '남')
    w2=Worker('김길동', 23, '여')
    w3=Worker('박길동', 28, '남')
    w4=Worker('이길동', 21, '남')
    w5=Worker('장길동', 29, '여')

    print(Worker.t_info)
    print('평균 나이 {0}세'.format(Worker.age/Worker.t_worker))
    print('남자 직원 {0}명, 여자 직원 {1}명'.format(Worker.m_worker,Worker.f_worker))