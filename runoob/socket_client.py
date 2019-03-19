import socket
import sys


#创建socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取主机名
host = socket.gethostname()
port = 8888

#连接服务，指定host，port
client.connect((host,port))

# 接收小于 1024 字节的数据
msg = client.recv(1024)

client.close()

print(msg)