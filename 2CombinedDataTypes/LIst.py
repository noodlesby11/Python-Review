#存储多个值的连续空间称为序列
#序列的切片操作[开始:结束:间隔]，不包括结束符
s="0123456789"
print(s[0:9:2])
print()
print(s[:5:1])#省略开始符默认0
print(s[:5:])#省略间隔默认1
print(s[:5])
print()
print(s[0::1])#省略结束符默认到最后一个符号
print(s[0::])
print(s[0: ])
print()
print(s[::2])#只有间隔
#序列的操作
print("序列的操作","-"*40)
ss = "678"
print(ss in s)
print(ss not in s)
print(len(ss))
print(max(s))#ASCII码
print(min(s))
print(s.index("2"))
print(s.count("3"))#第一次出现的索引
#列表
print("列表:可变组合数据类型","-"*40)
#创建列表 两种方法
lis = ['hello', 'world', 7, 999, 10.4]
lis2 = list('hello')
lis3 = list(range(1,11))
#列表操作
print(lis)
print(lis2)
print(lis3)
print(lis+lis2+lis3)
print(lis*3)
#列表的遍历 3种方法
for item in lis:
    print(item,end=" ")
print()
for i in range(1,len(lis)):
    print(i,"-->",lis[i],end=' ')
print()
for index,item in enumerate(lis):
    print(index,item,end=' ')
print()
for index,item in enumerate(lis,start=1):
    print(index,item,end=' ')
print()
#列表的特殊操作
lis.append('add')#在列表的最后添加元素
lis.insert(3,'aaa')#在列表的index位置插入object
lis.pop(0)#输出第index个元素，并从列表中删除
lis.remove('aaa')#删除列表中的第一个出现的元素
lis.reverse()#将列表反转
lis4=lis.copy()
lis.clear()#删除列表中所有元素
#删除列表
del lis
del lis2
del lis3
del lis4
#使用列表生成式
#lis = [ expression for item in range]
#lis = [ expression for item in range if condition]
lis5 = [item for item in range(1,11)]
print(lis5)
lis6 = [item*2 for item in range(1,11)]
print(lis6)
lis7 = [item for item in range(1,44) if item%2==0]
print(lis7)
#二维列表
lis8=[
    ['A','B','C'],
    [1,2,3],
    [4,5,6]
]
print(lis8)
#二维列表的遍历
for row in lis8:
    for item in row:
        print(item ,end='\t')
    print()