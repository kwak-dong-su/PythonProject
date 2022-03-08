
try:
    file2 = open('member.txt', 'r')

    print('이름  나이  연락처')
    print('----------------')
    for line in file2:
        print(line)
except:
    print('파일 쓰기 실패')
finally:
    try:
        file2.close()
    except:
        print('file2를 closing하지 못했습니다.')
