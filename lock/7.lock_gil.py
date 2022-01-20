'''
说明: 对集合进行排序的时候, 会对集合进行读和写, 导致线程不安全. gil锁将整个排序业务锁住,保证`arr.sort()`线程安全
'''
import time
from threading import RLock, Thread
from typing import List


def bubble_sort(arr: List):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                time.sleep(0.001)
                arr[j], arr[j+1] = arr[j+1], arr[j]


def req1(arr: List):
    bubble_sort(arr)


def req2(arr: List, lock: RLock):
    # lock:模拟arr.sort()操作的gil锁, 实际是c语言的锁
    with lock:
        bubble_sort(arr)


def req3(arr: List):
    arr.sort()


def main1():
    list = [1, 2, 4, 77, 5, 66, 6]
    tasks = [Thread(target=req1, args=(list,)) for i in range(2)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list


def main2():
    list = [1, 2, 4, 77, 5, 66, 6]
    lock = RLock()
    tasks = [Thread(target=req2, args=(list, lock)) for i in range(2)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list


def main3():
    list = [1, 2, 4, 77, 5, 66, 6]
    tasks = [Thread(target=req3, args=(list,)) for i in range(2)]
    for i in tasks:
        i.start()
    for i in tasks:
        i.join()
    return list


print(f'不加锁,线程不安全:\t期待:[1, 2, 4, 5, 6, 66, 77], 实际: {main1()}')
print(f'加锁,线程安全:\t\t期待:[1, 2, 4, 5, 6, 66, 77], 实际: {main2()}')
print(f'加gil锁,线程安全:\t期待:[1, 2, 4, 5, 6, 66, 77], 实际: {main3()}')
'''
输出: 
    不加锁,线程不安全:      期待:[1, 2, 4, 5, 6, 66, 77], 实际: [1, 2, 4, 5, 66, 77, 6]
    加锁,线程安全:          期待:[1, 2, 4, 5, 6, 66, 77], 实际: [1, 2, 4, 5, 6, 66, 77]
    加gil锁,线程安全:       期待:[1, 2, 4, 5, 6, 66, 77], 实际: [1, 2, 4, 5, 6, 66, 77]
'''
