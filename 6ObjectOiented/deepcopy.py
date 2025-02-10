#浅拷贝和深拷贝
from copy import deepcopy


class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu=CPU()
disk=Disk()
com=Computer(cpu,disk)
com1=com#变量对象的赋值,指向的是同一个对象


#类对象的浅拷贝,产生一个新的对象，但是对象的子对象仍指向同一对象
import copy
com2= copy.copy(com)

#类对象的深拷贝,产生一个新的对象，对象的子对象也重新创建
com3=copy.deepcopy(com)

print(com,"子类对象的内存地址",com.cpu,com.disk)
print(com1,"1子类对象的内存地址",com1.cpu,com1.disk)
print(com2,"2子类对象的内存地址",com2.cpu,com2.disk)
print(com3,"3子类对象的内存地址",com3.cpu,com3.disk)