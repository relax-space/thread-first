'''
说明: 锁使用不当,容易引起死锁
'''
import time
from threading import Lock, Thread


def req1():
    with lock1:
        print(1)
        time.sleep(0.01)
        print(3)
        # 线程1: 等待lock2释放锁
        with lock2:
            print(4)
        print(5)


def req2():
    with lock2:
        print(2)
        # 线程2: 等待lock1释放
        with lock1:
            print(6)
        print(7)


lock1 = Lock()
lock2 = Lock()
tasks = [Thread(target=req1), Thread(target=req2)]
for i in tasks:
    i.start()

for i in tasks:
    i.join()

print(list)

'''
输出:
    1
    2
    3
'''
