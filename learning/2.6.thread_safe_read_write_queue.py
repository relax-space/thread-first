
'''
说明：线程安全的例子: 在多线程中，既做读又做写，如果用queue来传递,可以保证数据准确
分析: `b = queue_res.get()`这段代码里面加了互斥锁, 只有整句话执行完成, 别的线程才能在此执行此段代码, 所以线程安全
'''
import time
from queue import Queue
from threading import Thread, current_thread
from typing import List

step_list: List = []


def sleep():
    for j in range(100000):
        j += 1


def req(queue_res: Queue):
    for i in range(0, 10):
        time.sleep(0.0001)
        b = queue_res.get()
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} get {b}')
        time.sleep(0.0001)
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} put {b+1}')
        queue_res.put(b + 1)


def main():
    queue_res = Queue()
    queue_res.put(0)
    tasks = []
    for i in range(2):
        tasks.append(Thread(target=req, args=(queue_res,)))
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return queue_res.get()


if __name__ == '__main__':
    res = main()
    print(f'main期待:20,实际:{res}')
    for i in step_list:
        print(i)


'''
输出:
main期待:20,实际:20
19164-00 get 0
19164-00 put 1
18796-00 get 1
18796-00 put 2
19164-01 get 2
19164-01 put 3
18796-01 get 3
18796-01 put 4
19164-02 get 4
19164-02 put 5
18796-02 get 5
18796-02 put 6
19164-03 get 6
19164-03 put 7
18796-03 get 7
18796-03 put 8
19164-04 get 8
19164-04 put 9
18796-04 get 9
18796-04 put 10
19164-05 get 10
19164-05 put 11
18796-05 get 11
18796-05 put 12
19164-06 get 12
19164-06 put 13
18796-06 get 13
18796-06 put 14
19164-07 get 14
19164-07 put 15
18796-07 get 15
18796-07 put 16
19164-08 get 16
19164-08 put 17
18796-08 get 17
18796-08 put 18
19164-09 get 18
19164-09 put 19
18796-09 get 19
18796-09 put 20

'''
