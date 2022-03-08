# 제어문
# 순차문: 입력--> 처리--> 출력
# 조건문: if, if~else, if~elif~..else
# 반복문: while, for
# 정리문제
# -------------
# 숫자입력>> 32
# 숫자입력>> 20
# 연산자 입력(+,-)>> +
#두 수를 더한 결과는 52입니다.
#(두 수를 뺸 결과는 12입니다.)

num1=input('숫자입력>> ')
num2=input('숫자입력>> ')
oper=input('연산자 입력(+,-)>> ')

if oper=='+':
    print('두 수를 더한 결과는 '+str(int(num1)+int(num2))+'입니다')
elif oper=='-':
    print('두 수를 뺀 결과는 '+str(int(num1)-int(num2))+'입니다')
else:
    print('연산자를 다시 입력해주세요.!')