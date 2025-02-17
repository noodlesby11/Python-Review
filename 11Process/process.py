#python中使用process函数创建进程
"""
process(group=None,target,name,args,kwargs)
group:表示分组，不使用保持默认
target:表示子进程要执行的任务
name:子进程名称
args:表示调用函数的位置参数，以元组形式进行传递
kwargs:表示调用函数的关键字参数，以字典形式进行传递
"""
import os
import time
from multiprocessing import Process


def pro():
    print(f"当前进程：{os.getpid()},父进程为：{os.getppid()}")
    time.sleep(1)

if __name__ == '__main__':
    print("主进程：",os.getpid())
    l=[]
    for i in range(5):
        #创建子进程
        p=Process(target=pro)
        #启动子进程
        p.start()
        l.append(p)
    #阻塞子进程
    for item in l:
        item.join()
    print("进程结束")
