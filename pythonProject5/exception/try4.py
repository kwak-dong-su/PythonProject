
try:
    test_file=open('test.txt', 'r')
    lines=test_file.readlines()
    print(lines)
    for line in lines:
        print(line)
except FileNotFoundError:
    print('해당 파일을 찾을 수 없음.')
except IOError:
    print('읽고 쓰는데 문제가 생겼음.')
except:
    print('파일을 처리하는데 문제가 생겼음.')
finally:
    try:
        test_file.close()
    except:
        print('file closing하는데 문제가 생김.')
# 램에 만들어진 connection을 담당하는 stream객체를
# 메모리에서 지우는 역할을 수행
# close() 함수를 호출하지 않으면 메모리에 계속 남아있어서
# 반드시 메모리에서 지워주어야 한다.