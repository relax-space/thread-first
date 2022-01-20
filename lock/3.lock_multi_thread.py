'''
说明: 互斥锁: 线程2可以释放线程1的锁
'''
from threading import Lock, Thread


def req1(lock: Lock, value: int):
    if value == 0:
        lock.acquire()
        print(1)
    else:
        lock.release()
        print(2)
    pass


def main():
    lock = Lock()
    tasks = [Thread(target=req1, args=(lock, i)) for i in range(2)]
    for i in tasks:
        i.start()

    for i in tasks:
        i.join()


if __name__ == '__main__':
    main()
