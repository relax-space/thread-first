'''
说明: 阻塞的例子
例子1: 对于互斥锁, 同一个线程连续调用两次acquire会阻塞
'''
from threading import Lock, RLock, Thread


def block():
    lock = Lock()
    lock.acquire()
    print('===> 3')
    # 阻塞在此
    lock.acquire()
    print('===> 4')


def alive():
    lock = RLock()
    lock.acquire()
    print('===> 1')
    # 不阻塞
    lock.acquire()
    print('===> 2')


Thread(target=alive).start()
Thread(target=block).start()


'''
输出:
    ===> 1
    ===> 2
    ===> 3
'''
