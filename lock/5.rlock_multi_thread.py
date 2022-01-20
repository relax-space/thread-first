'''
说明: rlock在多线程之间是互斥的, 只有在同一个线程才能重入
'''
import logging
import time
from datetime import datetime
from threading import RLock, Thread, current_thread
from typing import List


def req1(lock: RLock, flag: int, list: List):
    lock.acquire()
    if flag == 0:
        list.append(1)
    else:
        list.append(2)
        lock.release()
        lock.release()


def req2(lock: RLock, value: int):
    try:
        if value == 0:
            lock.acquire()
            logging.info(f'{current_thread().name} 1')
            # 1秒钟之后释放锁
            time.sleep(1)
            lock.release()
        if value == 1:
            lock.release()
    except Exception as e:
        logging.info(f'{current_thread().name} {e}')
        pass


def req3(lock: RLock, value: int):
    logging.info(f'{current_thread().name} start')
    # 多线程之间是互斥的: 线程4 会阻塞
    lock.acquire()
    logging.info(f'{current_thread().name} end')


def main1(lock: RLock):
    list = []
    req1(lock, 0, list)
    req1(lock, 1, list)
    assert [1, 2] == list, 'main1 error'


def main2(lock: RLock):

    tasks = [Thread(target=req2, args=(lock, i),
                    name=f'thread-{i+1}') for i in range(2)]
    for i in tasks:
        i.start()

    for i in tasks:
        i.join()


def main3(lock: RLock):

    tasks = [Thread(target=req3, args=(lock, i),
                    name=f'thread-{i+3}') for i in range(2)]
    for i in tasks:
        i.start()

    for i in tasks:
        i.join()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    lock = RLock()
    logging.info('==> 单线程acquire两次')
    main1(lock)
    logging.info('==> 线程2 无法释放线程1的acquire')
    main2(lock)
    logging.info('==> 多线程之间是互斥的: 线程3没有释放锁, 线程4无法获取锁')
    main3(lock)
