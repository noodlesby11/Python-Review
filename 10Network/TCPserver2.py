#使用TCP通信的服务器端进行多次通信的情况
import socket

#创建socket对象
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定IP与端口
ip='127.0.0.1'
port=88
server_socket.bind((ip,port))

#开始监听,设置最大连接数量
server_socket.listen(5)
print("服务器已启动")

#等待客户端连接
client_socket,client_addr=server_socket.accept()

#接收来自客户端的数据
info=client_socket.recv(1024).decode('utf-8')#初始化变量
while info!='bye':
    if info !=' ':
        print("数据：",info)
    #服务器进行回复
    data=input('输入服务器回复：')
    server_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')
#关闭
client_socket.close()
server_socket.close()