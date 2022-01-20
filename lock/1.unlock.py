'''
说明: 不加锁会导致数据不准确, 本来希望list[0]的值被加两次, 但实际上只加了一次
'''
import time
from threading import Thread
from typing import List


def req1(list: List):
    # 1. 线程1: b的值为0
    # 2. 线程2: b的值为0
    b = list[0]
    time.sleep(0.001)
    # 3. 线程1: list[0]的值为1
    # 4. 线程2: list[0]的值为1
    list[0] = b+1


list = [0]
tasks = [Thread(target=req1, args=(list,)), Thread(target=req1, args=(list,))]
for i in tasks:
    i.start()
for i in tasks:
    i.join()
print(list[0])

'''
输出: 1
'''
