#使用TCP通信的客户端多次通信
import socket

#创建socket对象
client_socket=socket.socket()

#连接服务器，发送请求
ip='127.0.0.1'
port=88
client_socket.connect((ip,port))
print("与服务器建立连接")

#发送数据
info=''
while info!='bye':
    #准备发送的数据
    data=input("输入发送的数据：")
    client_socket.send(data.encode('utf-8'))
    #判断
    if data=='bye':
        break
    #接收数据
    info=client_socket.recv(1024).decode('utf-8')
    print("接收到服务器的数据：",info)
#关闭
client_socket.close()
print("发送完毕")