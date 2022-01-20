# thread-first

- 线程安全: 对共享变量的一系列操作放到锁中即可
- gil锁: 解释器层面的锁, 比如:list.sort()方法,在调用前加gil锁,调用结束后解除锁,所以线程安全
- rlock和lock的区别: rlock: 同一个线程内可以锁多次, 不能解锁其他线程的锁. lock: 一个线程可以解锁另一个线程的锁
- 线程同步: 可以参看另外一篇文章[condition-first](https://github.com/relax-space/condition-first.git)


1. [thread简单例子](docs/1.thread.md)

2. [什么样的代码会线程安全?](docs/2.thread_safe.md)

3. [线程池](docs/3.thread_executor.md)

4. [lock、rlock和gil锁的区别](docs/4.lock.md)

:ribbon: :ribbon: 读后有收获可以请作者喝咖啡：

<img src="https://images.gitee.com/uploads/images/2021/1226/125920_9f0e6151_9674723.png" width="60%"/>