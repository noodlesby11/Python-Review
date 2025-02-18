#使用继承的方式创建线程
import time
from threading import Thread
class SubThread(Thread):
    #编写一个初始化方法
    def __init__(self,name):
        #调用父类的初始化方法
        super().__init__()
        self.name = name
    #重写父类中的run方法
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f"名称{self.name}正在执行任务{i}")

if __name__ == '__main__':
    print("主线程开始执行：")
    l=[SubThread('thread'+str(i)) for i in range(2)]
    for item in l:
        item.start()
    for item in l:
        item.join()
    print("线程结束")