'''
说明: 
    1.append是线程安全: 因为没有报错,并且结果正确,在一些其他语言中比如java,如果集合不加锁就append的话,会报异常
    2.L[0] = L[0]+1 线程不安全,因为结果不是我们所期待的
注:
    线程安全的代码:https://docs.python.org/3.10/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
    避免gil: 使用多进程 或者 c扩展,比如zlib,hashlib
线程安全:
    L.append(x)
    L1.extend(L2)
    x = L[i]
    x = L.pop()
    L1[i:j] = L2
    L.sort()
    x = y
    x.field = y
    D[x] = y
    D1.update(D2)
    D.keys()
线程不安全:
    i = i+1
    L.append(L[-1])
    L[i] = L[j]
    D[x] = D[x] + 1
'''

from threading import Thread
from typing import List


def req1(param, list: List):
    list.append(param)


def main1():
    list = []
    tasks = []
    for i in range(2):
        tasks.append(Thread(target=req1, args=(i, list)))
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list


def req2(list: List):
    for i in range(100):
        b = list[0]
        for i in range(10000):
            i += 1
        list[0] = b + 1


def main2():
    list = [0]
    tasks = []
    for i in range(2):
        tasks.append(Thread(target=req2, args=(list,)))
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list[0]


if __name__ == '__main__':
    res1 = main1()
    res2 = main2()
    print(f'main1结果{main1()}')
    print(f'main2期待:200,实际:{main2()}')
'''
输出:
    main1结果[0, 1]
    main2期待:200,实际:169
'''
