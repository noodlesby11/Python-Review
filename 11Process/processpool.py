#进程池。同时管理大量进程
"""
apply_async(func,args,kwargs):使用非阻塞方式调用函数func
apply(func,args,kwargs):使用阻塞方式调用函数func
close():关闭进程池，不再接收新任务
terminate():不管任务是否完成，立即终止
join():阻塞主进程，必须在terminate()或close()之后使用
"""
import os
import time
from multiprocessing import Pool

def sub_process(name):
    print(f"当前进程：{os.getpid()},父进程为：{os.getppid()},名称{name}")
    time.sleep(1)

if __name__ =='__main__':
    start = time.time()
    print("父进程开始执行")
    p=Pool(3)
    #创建进程
    for i in range(10):
        #使用非阻塞的方式运行
        p.apply_async(func=sub_process,args=(i,))
    #关闭进程池
    p.close()
    #阻塞父进程
    p.join()
    print("父进程执行完毕，时间为：",time.time()-start)