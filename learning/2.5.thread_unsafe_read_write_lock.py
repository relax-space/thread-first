
'''
说明：线程不安全的例子: 在多线程中，既做读又做写，如果只对写加锁,也会导致数据不对
'''
from threading import Lock, Thread, current_thread
from typing import List

step_list: List = []


def sleep():
    for j in range(100000):
        j += 1


def req(lock: Lock, list: List):
    for i in range(0, 10):
        b = list[0]
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} get {b}')
        sleep()
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} put {b+1}')
        # 只锁写
        with lock:
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
main期待:20,实际:17
17024-00 get 0
17024-00 put 1
17024-01 get 1
17024-01 put 2
17024-02 get 2
17024-02 put 3
17024-03 get 3
17024-03 put 4
17024-04 get 4
17024-04 put 5
17024-05 get 5
17024-05 put 6
17024-06 get 6
17024-06 put 7
17024-07 get 7
18336-00 get 7
18336-00 put 8
18336-01 get 8
18336-01 put 9
18336-02 get 9
18336-02 put 10
18336-03 get 10
17024-07 put 8
17024-08 get 8
17024-08 put 9
17024-09 get 9
17024-09 put 10
18336-03 put 11
18336-04 get 11
18336-04 put 12
18336-05 get 12
18336-05 put 13
18336-06 get 13
18336-06 put 14
18336-07 get 14
18336-07 put 15
18336-08 get 15
18336-08 put 16
18336-09 get 16
18336-09 put 17


'''
