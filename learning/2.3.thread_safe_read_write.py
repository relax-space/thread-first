
'''
说明：线程安全的例子: 在多线程中，既做读又做写的时候，加锁保证数据准确
分析: 加锁之后,在get执行之后,put执行之前,不会切换出线程, 保证将要存入的变量(b+1),是从内存获取的最新数据


'''
import time
from threading import Lock, Thread, current_thread
from typing import List

step_list: List = []


def sleep():
    for j in range(100000):
        j += 1


def req(lock: Lock, list: List):
    for i in range(0, 10):
        with lock:
            b = list[0]
            step_list.append(
                f'{"%05d" % current_thread().ident}-{"%02d"%i} get {b}')
            time.sleep(0.01)
            step_list.append(
                f'{"%05d" % current_thread().ident}-{"%02d"%i} put {b+1}')
            list[0] = b + 1


def main():
    list = [0]
    tasks = []
    lock = Lock()
    for i in range(2):
        tasks.append(Thread(target=req, args=(lock, list,)))
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list[0]


if __name__ == '__main__':
    res = main()
    print(f'main期待:20,实际:{res}')
    for i in step_list:
        print(i)

'''
输出:
main期待:20,实际:20
14748-00 get 0
14748-00 put 1
14748-01 get 1
14748-01 put 2
14748-02 get 2
14748-02 put 3
14748-03 get 3
14748-03 put 4
17644-00 get 4
17644-00 put 5
17644-01 get 5
17644-01 put 6
17644-02 get 6
17644-02 put 7
17644-03 get 7
17644-03 put 8
17644-04 get 8
17644-04 put 9
17644-05 get 9
17644-05 put 10
17644-06 get 10
17644-06 put 11
17644-07 get 11
17644-07 put 12
17644-08 get 12
17644-08 put 13
17644-09 get 13
17644-09 put 14
14748-04 get 14
14748-04 put 15
14748-05 get 15
14748-05 put 16
14748-06 get 16
14748-06 put 17
14748-07 get 17
14748-07 put 18
14748-08 get 18
14748-08 put 19
14748-09 get 19
14748-09 put 20


'''
