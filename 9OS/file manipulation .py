#OS模块用于目录与文件相关操作
"""
getcwd():获取当前工作路径
listdir(path):获取path路径下的文件和目录信息，没有path则为当前路径
mkdir(path):在指定路径下创建目录
makedirs(path):创建多级目录
rmdir(path):删除path下的空目录
removedirs(path):删除多级目录
chdir(path):把path设置为当前目录
walk(path):遍历目录树，结果为元组，包含路径名、所有目录列表和文件列表
remove(path):删除path指定的文件
rename(old,new):将old重命名为new
stat(path):获取path指定的文件信息
startfile(path):启动path指定的文件
"""
import os
print("当前工作路径：",os.getcwd())
print("指定目录下的文件：",os.listdir('D:/PythonCode'))
#遍历目录树
for dirs,dirlst,filelst in os.walk('D:/PythonCode/PythonReview'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('-'*40)
#获取文件信息
print(os.stat('../8FileIO/a.txt'))
#启动路径下的文件
os.startfile("calc.exe")