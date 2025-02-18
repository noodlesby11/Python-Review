#线程之间可以共享数据,共享数据的安全性用锁进行控制
import threading
from  threading import Thread,Lock
import time
def task():
    for i in range(3):
        time.sleep(1)
        print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__=='__main__':
    start = time.time()
    #创建锁对象
    lock_obj = Lock()
    print("主线程开始执行")
    #线程
    lock_obj.acquire()#上锁
    lst = [Thread(target=task) for i in range(2)]
    lock_obj.release()#释放锁

    for item in lst:
        item.start()
    for item in lst:
        item.join()
    print(f"一共耗时{time.time()-start}")