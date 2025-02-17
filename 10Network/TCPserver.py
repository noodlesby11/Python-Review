#使用TCP通信的服务器端单次通信
#AF_INET表示用于Internet间的通信
#SOCK_STREAM表示使用UDP协议
from socket import socket,AF_INET,SOCK_STREAM

#创建socket对象
server_socket=socket(AF_INET,SOCK_STREAM)

#绑定IP与端口
ip_port=('127.0.0.1',88)
server_socket.bind(ip_port)

#开始监听，设置最大连接数量
server_socket.listen(5)
print("服务器已经启动")

#等待客户端连接
client_socket,client_addr=server_socket.accept()

#接收数据
data=client_socket.recv(1024)
print("接收到的数据为：",data.decode('utf-8'))

#关闭
server_socket.close()

