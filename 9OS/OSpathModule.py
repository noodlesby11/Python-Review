#OS.path模块的函数
"""
abspath(path):获取文件的绝对路径
exists(path):判断目录是否存在
join(path,name):将目录与文件名进行拼接
splitext():分别获取文件名和后缀
basename(path):从path中提取文件名
dirname(path):从path中提取路径，不含文件名
isdir(path):判断路径是否有效
isfile(path):判断文件是否有效
"""
import os.path
print("获取文件的绝对路径:",os.path.abspath('./OSpathModule.py'))
print("判断目录是否存在:",os.path.exists('./a.txt'))
print("将目录与文件名进行拼接:",os.path.join('D:/PythonCode','a.txt'))
print("分别获取文件名和后缀:",os.path.splitext('OSpathModule.py'))#返回元组类型
print("从path中提取文件名",os.path.basename(r'D:\Python\Python311\python.exe'))
print("从path中提取路径，不含文件名",os.path.dirname(r'D:\Python\Python311\python.exe'))
print("判断路径是否有效:",os.path.isdir(r'D:\Python\Python3'))
print("判断文件是否有效:",os.path.isfile(r'D:\Python\Python3'))