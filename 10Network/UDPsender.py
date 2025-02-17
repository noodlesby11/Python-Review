#使用UDP通信的发送端
#AF_INET表示用于Internet间的通信
#SOCK_DGRAM表示使用UDP协议
from socket import socket,AF_INET,SOCK_DGRAM

#创建socket对象
sender_socket=socket(AF_INET,SOCK_DGRAM)

#绑定IP与端口
ip_port=('127.0.0.1',88)
sender_socket.bind(ip_port)

#准备发送的数据
data=input("输入要发送的数据:")

#发送数据
sender_socket.sendto(data.encode('utf-8'),ip_port)

#接收返回数据
recv_data,addr=sender_socket.recvfrom(1024)
print("接收到的数据为：",recv_data.decode('utf-8'))

#关闭
sender_socket.close()