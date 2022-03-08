import random
import threading
import datetime
import time


def a1():
    now=datetime.datetime.now()
    for i in range(100):
        time.sleep(5)
        print(str(now.hour)+":"+str(now.minute)+":"+str(now.second)+":"+str(now.microsecond))

def a2():
    list=['음식1', '음식2', '음식3', '음식4', '음식5', '음식6', '음식7', '음식8', '음식9', '음식10', ]
    for one in list:
        time.sleep(10)
        print(one)

def a3():
    for i in range(1, 501):
        time.sleep(1)
        print('카운트>>',i)

thread1=threading.Thread(target=a1)
thread2=threading.Thread(target=a2)
thread3=threading.Thread(target=a3)

thread1.start()
thread2.start()
thread3.start()