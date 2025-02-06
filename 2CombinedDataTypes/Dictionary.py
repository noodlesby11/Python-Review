#字典类型使用一个信息查找另一个信息，构成键值对
#字典的创建方式,字典中的键是无序的
d = {1:'A',2:'B',3:'C',2:'D'}#键相同时值会进行覆盖
print(d)

lst1 =[1,2,3]
lst2 = ['A','B','C']
zi = zip(lst1,lst2)#并非字典类型需要转换
d1 = dict(zi)
print(zi)
print(d1)

d2 = dict(A=1,B=2,C=3)#左侧为key，右侧为value
print(d2)
#字典的取值
print(d2["A"])
print(d1.get(1))
#字典遍历key和value的元组
for item in d1.items():
    print(item)
#分别遍历出key和value
for key,item in d2.items():
    print(key,item)
#字典的操作
print(d.keys())#获取所有的key
print(d.values())#获取所有的values
print(d.pop(2,"不存在"))#提取key对应的value,若不存在则输出设置好的值
print(d.popitem())#随机删除元素
d.clear()#清空字典
#字典的删除
del d
del d1
del d2
#字典的生成式
import random
d3={item:random.randint(1,100) for item in range(4)}#前为value后为key
print(d3)

lst3 =[1,2,3]
lst4 = ['A','B','C']
d4={key:value for key,value in zip(lst3,lst4)}
print(d4)