
'''
说明: 多线程安全例子: 只对共享变量做写操作
'''
from threading import Thread
from typing import List


def req(list: List, loop_count: int):
    total = 0
    for i in range(loop_count):
        total += 1
    list.append(total)


def main(thread_count: int, loop_count: int):
    list = []
    tasks = [Thread(target=req, args=(list, loop_count))
             for i in range(thread_count)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    count = 0
    for i in list:
        count += i
    return count


if __name__ == '__main__':
    thread_count = 20
    loop_count = 1000
    res = main(thread_count, loop_count)
    print(f'期待:{thread_count*loop_count},实际:{res}')

'''
输出:
    期待:20000,实际:20000
'''