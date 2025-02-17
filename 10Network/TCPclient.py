#使用TCP通信的客户端单次通信
import socket

#创建socket对象
client_socket=socket.socket()

#连接服务器，发送请求
ip='127.0.0.1'
port=88
client_socket.connect((ip,port))
print("与服务器建立连接")

#发送数据
client_socket.send('hello'.encode('utf-8'))

#关闭
client_socket.close()
print("发送完毕")