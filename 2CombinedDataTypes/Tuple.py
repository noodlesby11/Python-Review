#元组的pyth中内置的不可变序列,比列表访问速度快，可以作为字典的键
#元组的创建
#使用小括号创建元组,如果只有一个元素逗号不能省略
t= ("hello",[1.2,11,"A"],10,"p")
tt= ("hello",)
print(t)
print(tt)
#使用内置函数创建元组
t1 = tuple("python")
print(t1)
t2 = tuple([1.2,11,"A"])
print(t2)
#元组的删除
del t
del tt
del t1
del t2
#元组的访问
t3 = ("py","th","on")
print(t3[0:2:1])
#元组的遍历
for item in t3:
    print(item,end=' ')
print()
for i in range(len(t3)):
    print(i,t3[i],end='\t')
print()
for index,item in enumerate(t3,start=1):
    print(index,item,end='\t')
print()
#元组生成式,使用元组生成式后需要转换成元组
t4 = (item for item in range(1,6))#t4不是元组对象
t5 = tuple(t4)
print(t4)
print(t5)