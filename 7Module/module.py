"""
import 模块名称 [as 别名]
from 模块名称 import 变量/函数/类/*
同名情况会出现覆盖情况，使用打点调用
"""

"""
包：含有_init_.py的目录，可以避免模块名称相冲突的问题
使用 包名.模块名 调用
"""
import admin.my_admin as a
a.info()

from admin import my_admin as b
b.info()

from admin.my_admin import info
info()

from admin.my_admin import *
print(name)