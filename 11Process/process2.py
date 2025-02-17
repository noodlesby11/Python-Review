#process常用的属性和方法
"""
name:别名，默认为Process-N
pid:进程对象的PID值
is_alive():进程是否执行完
join(timeout):等待timeout秒
start():启动进程
run():如果没有指定target参数，会使用父类的run方法
terminate():强制终止进程
"""
import os
from multiprocessing import Process


def sub_process(name):
    print(f"当前进程：{os.getpid()},父进程为：{os.getppid()},名称{name}")

def sub_process2(name):
    print(f"当前进程：{os.getpid()},父进程为：{os.getppid()},名称{name}")

if __name__ == '__main__':
    print("主进程：",os.getpid())
    for i in range(5):
        #若没有指定target参数，则会调用process类中的run方法
        #若指定了target参数，则会调用target方法
        p1=Process(target=sub_process,args=('A',))
        p2=Process(target=sub_process,args=('B',))
        #启动子进程
        p1.start()
        p2.start()
    #阻塞子进程
    print("进程结束")