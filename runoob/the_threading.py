#使用 threading 模块创建线程

import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    

    #init
    def __init__(self, threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        threadName = self.name
        delay = self.counter
        counter = 5
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
        print ("退出线程：" + self.name)




#创建新线程
thread1 = MyThread(1,"thread-1",1)
thread2 = MyThread(1,"thread-2",3)

#开始新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("stop the thread")
