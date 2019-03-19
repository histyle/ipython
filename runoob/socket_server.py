import socket
import sys

#创建socket对象
server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

port = 8888

#绑定端口号
server_socket.bind((host,port))

#设置最大连接数
server_socket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr = server_socket.accept()
    print("socket connect addr is %s" % str(addr))

    msg = 'welcome to python'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
