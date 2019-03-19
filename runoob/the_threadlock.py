#线程同步

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    

    #init
    def __init__(self, threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        threadName = self.name
        delay = self.counter
        counter = 5
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
        # 释放锁，开启下一个线程
        threadLock.release()    
        print ("退出线程：" + self.name)


threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myThread(1,"thread-1",1)
thread2 = myThread(1,"thread-2",3)

#开始新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
