'''
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''


#
import os
log = 'runoob\\logs.txt'

if os.path.isfile(log):
   print('{} has been exits'.format(log))
else:
   print('{} does not exits'.format(log)) 

wlog = open(log,mode="w")
#print(log.name,log.close,log.mode)

wlog.write("hello.python")

#刷新文件内容
wlog.flush()
wlog.close()


rlog = open(log,mode="r")

print(rlog.readlines())