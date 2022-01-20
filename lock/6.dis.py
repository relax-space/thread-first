'''
说明: 
    a+=1线程不安全: 对共享变量a做了读(LOAD_NAME)和写(STORE_NAME)的操作,所以线程不安全
    b.append(1)线程安全: 对共享变量b只做了一个方法调用CALL_METHOD,因为有GIL锁,所以这个方法里面所有操作都是线程安全的
    b.sort()线程安全
概念:
    字节码: 也叫指令,比如: LOAD_NAME是一个字节码
    GIL锁: 保证每一个字节码都是线程安全的,其实也好理解,就是每个字节码[方法或者变量],在调用之前加锁,调用结束解锁
'''
from dis import dis

print('=> a+=1')
dis(compile('a+=1', '', 'exec'))
print('=> b.append(1)')
dis(compile('b.append(1)', '', 'exec'))
print('=> b.sort(1)')
dis(compile('b.sort()', '', 'exec'))


'''
=> a+=1
  1           0 LOAD_NAME                0 (a)
              2 LOAD_CONST               0 (1)
              4 INPLACE_ADD
              6 STORE_NAME               0 (a)
              8 LOAD_CONST               1 (None)
             10 RETURN_VALUE
=> b.append(1)
  1           0 LOAD_NAME                0 (b)
              2 LOAD_METHOD              1 (append)
              4 LOAD_CONST               0 (1)
              6 CALL_METHOD              1
              8 POP_TOP
             10 LOAD_CONST               1 (None)
             12 RETURN_VALUE
=> b.sort()
  1           0 LOAD_NAME                0 (b)
              2 LOAD_METHOD              1 (sort)
              4 CALL_METHOD              0
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
'''
