
'''
说明：线程不安全的例子: 在多线程中，如果不加锁, 既做读又做写，会导致数据不对，举例说明不对的原因
分析: 在get执行之后,put执行之前切换出线程, 不能保证将要存入的变量(b+1),是从内存获取的最新数据
关键步骤: [13220-06 put 7] 这一步的7是通过代码中b+1获取的,这b不是从内存中获取的值,而是这一步获取的值为6[17528-00 get 6]. 内存中b已经被另外的线程变成9了[17528-02 put 9],但是这一步
b却是6,导致b+1为7

'''
from threading import Thread, current_thread
from typing import List

step_list: List = []


def sleep():
    for j in range(100000):
        j += 1


def req(list: List):
    for i in range(0, 10):
        b = list[0]
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} get {b}')
        sleep()
        step_list.append(
            f'{"%05d" % current_thread().ident}-{"%02d"%i} put {b+1}')
        list[0] = b + 1


def main():
    list = [0]
    tasks = []
    for i in range(2):
        tasks.append(Thread(target=req, args=(list,)))
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
main期待:20,实际:16
13220-00 get 0  // 线程：13220
13220-00 put 1
13220-01 get 1
13220-01 put 2
13220-02 get 2
13220-02 put 3
13220-03 get 3
13220-03 put 4
13220-04 get 4
13220-04 put 5
13220-05 get 5
13220-05 put 6
13220-06 get 6
17528-00 get 6 // 切换新的线程：17528，新的线程从内存中获取到了正确的数据6
17528-00 put 7
17528-01 get 7
17528-01 put 8
17528-02 get 8
17528-02 put 9
17528-03 get 9
13220-06 put 7 // 切换回线程：13220，错误从这里开始，正确的应该从内存获取9在加1，所以正确应该是13220-06 put 10
13220-07 get 7
13220-07 put 8
13220-08 get 8
13220-08 put 9
13220-09 get 9
13220-09 put 10 // 正确的应该是 17528-03 put 13
17528-03 put 10 // 正确的应该是 17528-03 put 14
17528-04 get 10 
17528-04 put 11
17528-05 get 11
17528-05 put 12
17528-06 get 12
17528-06 put 13
17528-07 get 13
17528-07 put 14
17528-08 get 14
17528-08 put 15
17528-09 get 15
17528-09 put 16 // 正确的应该是 17528-03 put 20


'''
