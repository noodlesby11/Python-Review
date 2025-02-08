#迭代器操作函数
lst=[11,333,44,75,4,98]
print("升序：",sorted(lst))
print("降序：",sorted(lst,reverse=True))
print("反向,结果为迭代器对象：",list(reversed(lst)))
#zip将两个对象打包成一个可迭代的zip对象
x=['a','b','v']
y=[10,20,30,40,50]#zip会以短的为主
zi=zip(x,y)
print(type(zi))
print(list(zi))
#enumerate:见前文
#all：返回对象中是否全部元素的布尔值都为True
z=[1,2,3,'',8]
print(all(y))
print(all(z))
#any：返回对象中是否有一个元素的布尔值为True
print(any(z))
#next:获取可迭代对象下一个元素
zi2=zip(x,y)
print(next(zi2))
print(next(zi2))
print(next(zi2))

#filter:通过指定函数过滤可迭代对象中的元素
def fun(num):
    return num%2==1 #偶数返回False,奇数返回True
o = filter(fun,range(11))
print(list(o))
#map：将可迭代对象中元素执行函数
def fun2(x):
    return x.upper()
m=['jjoot','ererrt','adffdf']
v= map(fun2,m)
print(list(v))