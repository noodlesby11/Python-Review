#UDP通信接收方
from socket import socket,AF_INET,SOCK_DGRAM

#创建socket对象
receiver_socket=socket(AF_INET,SOCK_DGRAM)

#绑定IP与端口
ip_port=('127.0.0.1',88)
receiver_socket.bind(ip_port)

#接收发送方的数据
recv_data,addr=receiver_socket.recvfrom(1024)
print("接收到的数据为：",recv_data.decode('utf-8'))

#回复发送方
data=input("输入要回复的数据：")
receiver_socket.sendto(data.encode('uft-8'),addr)

#关闭
receiver_socket.close()