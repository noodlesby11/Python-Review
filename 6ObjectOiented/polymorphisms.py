from turtledemo.nim import HUNIT


class Human:
    def show(self):
        print("我是人")

class Dog:
    def show(self):
        print("我是狗")

class Cat:
    def show(self):
        print("我是猫")

def fun(obj):
    obj.show()

h=Human()
d=Dog()
c=Cat()
#多态不关心数据类型，只关心是否有同名方法
fun(h)
fun(d)
fun(c)