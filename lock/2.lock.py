'''
说明: 在锁被释放之前, 别的线程不能操作锁作用域内的代码
'''
import time
from threading import Lock, Thread
from typing import List


def req1(list: List):
    with lock:
        # 1. 线程1: b的值为0
        # 3. 线程2: b的值为1
        b = list[0]
        time.sleep(0.001)
        # 2. 线程1: list[0]的值为1
        # 4. 线程2: list[0]的值为2
        list[0] = b+1


list = [0]
lock = Lock()
tasks = [Thread(target=req1, args=(list,)), Thread(target=req1, args=(list,))]
for i in tasks:
    i.start()
for i in tasks:
    i.join()
print(list[0])

'''
输出: 2
'''
