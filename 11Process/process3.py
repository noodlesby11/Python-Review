#使用继承的方式创建子进程
from multiprocessing import Process
import os,time
class Subprocess(Process):
    #编写一个初始化方法
    def __init__(self,name):
        #调用父类的初始化方法
        super().__init__()
        self.name = name
    #重写父类中的run方法
    def run(self):
        print(f"当前进程：{os.getpid()},父进程为：{os.getppid()},名称{self.name}")

if __name__ == '__main__':
    print("主进程：",os.getpid())
    l=[]
    for i in range(5):
        #创建子进程
        p=Subprocess('K')
        #启动子进程
        p.start()
        l.append(p)
    #阻塞子进程
    for item in l:
        item.join()
    print("进程结束")