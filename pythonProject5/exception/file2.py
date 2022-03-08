
try:
    file2 = open('member.txt', 'r')

    print('이름 \t 나이 \t 연락처')
    print('-----------------------')
    for line in file2:
        one=line.split(',')
        print(one[0]+"\t"+one[1]+"\t"+one[2],end='')
except:
    print('파일 쓰기 실패')
finally:
    try:
        file2.close()
    except:
        print('file2를 closing하지 못했습니다.')
