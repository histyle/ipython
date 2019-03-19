'''
参数说明:

function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。

'''

import _thread
import time


#function
def print_time(theadName,delay):
    count = 0
    while count < 5:
        time.sleep(5)
        count += 1
        print("%s: %s" %(theadName,time.ctime(time.time())))


#创建两个线程
try:
   _thread.start_new_thread(print_time,("thread-1",2))
   _thread.start_new_thread(print_time,("thread-2",4))
except:
    print ("Error: 无法启动线程")


while 1:
    pass
