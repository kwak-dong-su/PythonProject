# def test_func():
#     try:
#         x=10
#         return x
#         print("테스트")
#     except Exception as e:
#         x=20
#         return x
#     finally:
#         x=30
#         return x
#
# print(test_func())
#
# print(all([]))
#
# if []:
#     print('참')
# else:
#     print('거짓')
#
# print(0.1+0.2+0.3==0.6)
# print(round(0.1+0.+0.2+0.3, 5)==round(0.6, 5))


# def add(num):
#     result=1
#     for i in range(num):
#         result+=1/3
#     for i in range(num):
#         result -= 1 / 3
#     return result
#
# print(1==(1+1/3-1/3))
# print(add(100)==(1+1/3-1/3))
# print(add(1000)==(1+1/3-1/3))
# print(add(10000)==(1+1/3-1/3))
# print(add(10000))
# print((1+1/3-1/3))
# try:
#     print("2"/"1")
# finally:
#     print("test")

# import glob
#
# output1=sorted(glob.glob('thread/*'), reverse=True)
# print(output1)

import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(type(m.start()))


pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))

print(pat.match("aaa@gmail.le.live"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))
