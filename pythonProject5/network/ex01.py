import random
import threading

def a1():
    for i in range(1, 101):
        print('증가>>', i)

def a2():
    for i in range(1, 101):
        print('감소>>', 101-i)

def a3():
    text=['@', '#', '$', '\\']
    for _ in range(100):
        print('특수>>', random.choice(text))

thread1=threading.Thread(target=a1)
thread2=threading.Thread(target=a2)
thread3=threading.Thread(target=a3)

thread1.start()
thread2.start()
thread3.start()