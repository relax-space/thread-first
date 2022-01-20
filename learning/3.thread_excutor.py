'''
说明:通过线程池实现多线程
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread
from typing import List


def req1(param):
    return f'{current_thread().ident} | {param}'


def main1(param: List):
    with ThreadPoolExecutor(max_workers=2) as exec:
        futures = []
        for i in param:
            futures.append(exec.submit(req1, i))
        return [i.result() for i in as_completed(futures)]


def main2(param):
    with ThreadPoolExecutor(max_workers=2) as exec:
        return list(exec.map(req1, param))


if __name__ == '__main__':
    param = [1, 2]
    res1 = main1(param)
    res2 = main2(param)
    print(f'main1结果{res1}')
    print(f'main2结果{res2}')

''''
输出:
    main1结果['16580 | 1', '16580 | 2']
    main2结果['11368 | 1', '11368 | 2']
'''
