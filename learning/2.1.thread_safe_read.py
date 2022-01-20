
'''
说明: 多线程安全例子: 只对共享变量做读操作
'''
from queue import Queue
from threading import Thread
from typing import List


def req(res_value: Queue, loop_count_list: List, i: int):
    total = 0
    for i in range(loop_count_list[i]):
        total += 1
    res_value.put(total)


def main(thread_count: int, loop_count_list: List):
    res_value = Queue()
    tasks = [Thread(target=req, args=(res_value, loop_count_list, i))
             for i in range(thread_count)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    count = 0
    for i in range(res_value.qsize()):
        count += res_value.get()
    return count


if __name__ == '__main__':
    thread_count = 20
    loop_count = 100
    loop_count_list = [loop_count]*thread_count
    res = main(thread_count, loop_count_list)
    print(f'期待:{thread_count*loop_count},实际:{res}')

'''
输出:
    期待:2000,实际:2000
'''
