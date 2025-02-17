"""
文件的打开模式：
r:只读模式打开，文件的指针在文件开头，文件不存在则异常
rb:只读模式打开二进制文件
w:覆盖写模式，文件不存在则创建
wb:覆盖写二进制文件模式，文件不存在则创建
a:追加写模式，文件不存在则创建
+:与w,r,a一起使用，在原功能基础上增加同时读写功能
"""
#写文件
def my_write(s):
    #打开文件
    file = open('a.txt','w',encoding='utf-8')
    #操作文件
    file.seek(0)
    file.write(s)
    #关闭
    file.close()
#读文件
def my_read():
    #打开文件
    file = open('a.txt','r',encoding='utf-8')
    #操作文件
    s=file.read()
    print(s)
    #关闭
    file.close()
#文件的复制
def my_copy(src,new_path):
    f1=open(src,'rb')
    f2=open(new_path,'wb')
    #边读边写
    s=f1.read()
    f2.write(s)
    #先打开的后关
    f2.close()
    f1.close()
'''
file.read(size):从文件读取size个字符或字节，没有size则默认全部读取
file.readline(size):读取一行数据，如果给定参数则读取这一行的size个字符或字节
file.readlines():从文件读取全部内容，结果为列表类型
file.write(s):将字符串s写入文件，别的类型不行
file.writelines(lts):将内容全部为字符串的列表写入文件
file.seek(offset):改变当前文件操作指针的位置，英文一个字节，中文gbk占两个字节，utf-8占三个字节
'''
if __name__=='__main__':
    my_write('示例文字')
    my_read()