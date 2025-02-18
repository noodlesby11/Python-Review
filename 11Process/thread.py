#线程是CUP可调度的最小单位，被包含在进程中，是进程中实际运行的单位
"""
Thread(group=None,target,name,args,kwargs)
group:创建线程对象的进程组
target:表示线程要执行的任务
name:线程名称，默认Tread-n
args:表示调用函数的位置参数，以元组形式进行传递
kwargs:表示调用函数的关键字参数，以字典形式进行传递
"""
import threading
from threading import Thread
import time
def task():
    for i in range(3):
        time.sleep(1)
        print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__=='__main__':
    start = time.time()
    print("主线程开始执行")
    #线程
    lst = [Thread(target=task) for i in range(2)]

    for item in lst:
        item.start()
    for item in lst:
        item.join()
    print(f"一共耗时{time.time()-start}")