#函数的定义
def get_sum(num1,num2):
    print(num1+num2)

#函数的参数传递
#位置参数：调用函数时参数的顺序和个数必须与定义相同,默认为位置参数
get_sum(1,3)
#关键字参数：使用 形参名称=值 的方式传参，顺序可以与定义不同
# 可以与位置传参一起用，但关键字传参必须在位置传参后
get_sum(num2=1,num1=2)
#默认值参数：函数定义时设置形参的默认值，调用函数时形参未赋值则使用默认值
# 函数定义时默认值参数放最后
def get_sum2(num1=1,num2=1):
    print(num1+num2)
get_sum2(3)

#函数的参数传递
#个数可变的位置参数：参数前加*,参数为元组类型
def fun(*p):
    print(type(p),len(p))
fun(1,2,2,3,4,5)
fun([1,2,3,4,5])#列表作为一个参数传递
fun(*[1,2,3,4,5])#列表所有元素进行参数传递
#个数可变的关键字参数：参数前加**,参数为字典类型
def dfun(**p):
    for key,value in p.items():
        print(key,"-->",value)
    print(type(p),len(p))
dfun(A="a",B="b",C='c')
d = {"A":"a","B":"b","C":'c'}
dfun(**d)#若要传递字典，需要进行解包

#函数的返回值
def rget_sum(num1,num2):
    return num1+num2
#返回值为多个时,返回一个元组
def rget_sum2(num1,num2):
    return num1+num2,num1-num2,num1*num2
add,sub,mul = rget_sum2(2,4)#解包赋值
print(rget_sum2(1,5))

#匿名函数   语法结构： result=lambda 参数列表:表达式
s=lambda a,b:a+b
print(s(1,99))

#函数的递归