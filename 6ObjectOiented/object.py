#类的定义
"""
首位下划线开头：特殊方法
_add_():加法
_sub_():减法
_lt_(),_le_(),_eq_():<,<=,==
_gt_(),_ge_(),_ne_():>,>=,!=
_mul_(),_truediv_():乘，非整除
_mod_(),_floordiv_():取余，整除
_pow_():求幂
单下划线开头：protected只能本类和子类访问
双下划线开头：private只能类本身去访问
"""
class Person:
    __school='中学'
    # 初始化方法
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    # 类中的函数，自带一个参数self
    def show(self):
        print(f"我叫:{self.name}")
    #静态方法,不会自带self,不能调用实例属性，也不能调用实例方法
    @staticmethod
    def sem():
        print("静态方法,不会自带self,不能调用实例属性，也不能调用实例方法")
    #类方法方法,自带cls,不能调用实例属性，也不能调用实例方法
    @classmethod
    def cam(cls):
        print("类方法,不能调用实例属性，也不能调用实例方法")\
    #私有化的方法
    def __pri(self):
        print("这是一个私有函数")
    #使用@property修改方法使方法变成属性使
    @property
    def age(self):
        return self.__age
    #将使用@property修改的属性设置为可写
    @age.setter
    def age(self,value):
        self.__age = value

#类的实例化
p=Person('小米',19)
print(p.name)
print(type(p))

#动态绑定属性
p1=Person('小红','12')
p2=Person('小蓝','13')
p1.gender='女'
print(p1.gender)
#动态绑定方法
def p2f():
    print("动态绑定方法给p2")
p2.fun = p2f#函数的赋值
p2.fun()

#类私有函数和属性的访问方法
print(p._Person__school)
p._Person__pri()

#使用@property修改方法使方法变成属性使
print(p.age)

#Object类：所有类的父类
'''
__new__():系统调用用于创建对象
__init__():创建对象时手动调用，用于初始化对象属性值
__str__():对象的描述，返回字符串类型，默认返回对象的内存地址
'''
'''
特殊属性：
obj.__dict__:对象的属性字典
obj.__class__:对象所属的类
class.__bases__:类的父类元组
class.__base__:类的父类
class.__mro__:类的层次结构
class.__subclasses__():类的子类列表
'''