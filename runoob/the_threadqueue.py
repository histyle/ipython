#线程优先级队列（Queue）

import threading
import time
import queue
exitFlag = 0

class myThread(threading.Thread):
    

    #init
    def __init__(self, threadId,name,q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.q = q

    def run(self):
        print("开始线程：" + self.name)
        threadName = self.name
        q = self.q
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print ("%s processing %s" % (threadName, data))
            else:
                queueLock.release()
            time.sleep(1)   
        print ("退出线程：" + self.name)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")