#创建的任何类继承自Object类,一个父类可以有多个子类
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"姓名{self.name}，年龄{self.age}")

#Student继承Person类
class Student(Person):
    #初始化方法父类属性直接调用
    def __init__(self,name,age,stuno):
        super().__init__(name,age)
        self.stuno=stuno

s=Student('小白',10,12344)

#子类继承所有父类的保护和公开的变量方法
class Father1:
    def __init__(self,name):
        self.name = name
    def show1(self):
        print("父类1中的方法")

class Father2:
    def __init__(self,age):
        self.age = age
    def show2(self):
        print("父类2中的方法")
#多继承
class Son(Father1,Father2):
    def __init__(self,name,age,gender):
        Father1.__init__(self,name)
        Father2.__init__(self,age)
        self.gender = gender
    #子类的方法重写
    def show1(self):
        super().show1()
        print("子类重写父类1方法")
    def show2(self):
        super().show2()
        print("子类重写父类2方法")

son=Son('name',19,'男')
son.show1()
son.show2()