#集合是无序不重复的元素序列，只能存储不可变数据类型，集合是可变数据类型
#集合的创建
from turtledemo.forest import doit1

s={1,200,"fdf"}
s1=set()#创建空集合
s2={}#创建的是字典类型
print(s2)
#集合的操作符号
A={1,2,3,4,5}
B={2,4,7,8,9}
print(A&B)#交集操作
print(A|B)#并集操作
print(A-B)#差集操作
print(A^B)#补集操作
print(A.add(10))#若集合不含该元素则添加
print(A.remove(10))#若集合存在该元素则删除，不存在则报错
B.clear()#清空集合元素
#集合的遍历
for item in A:
    print(item,end=" ")
print()
for index,item in enumerate(A):
    print(index,"->",item)
#集合的删除
del s
#集合的生成式与列表相同
