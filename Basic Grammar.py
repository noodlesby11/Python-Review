#输出函数
print("HelloWorld")
print('HeloWorld2')
print('Hello','World')
print('Hello'+'World')
'''
输出函数，x始终为字符串函数
'''
x=input('提示文字 ')
print(x)
#python中的关键字
import keyword
print(keyword.kwlist)
'''
python中标识符命名规则
1.不能适用关键字
2.第一个字符不能用数字
3.严格区分大小写
4.可以使用中文但不建议
命名规范：
1.模块名全部小写，下划线分隔，例如：grame_main
2.包名尽量短小，全部小写，不推荐使用下划线，例如：com.python
3.类名采用单词首字母大写形式，例如：MyClass
4.模块内部的类采用"_"+名称形式，例如：_InnerMyClass
5.函数、类属性和方法的命名，全部小写，下划线分隔
'''
#python中的数据类型
num = 123
num2 = 0b1011
num3 = 0o7654
num4 = 0xabcdef
string = 'abc'
flo = 123.1
comp = 1+1j
print(type(num))
print(type(string))
print(type(flo))
#转义字符：\n,\t,\‘,\",\\
#一个\t代表8个字符,字符串前加R进行转义
print("1234567\t1111")
print("1234567111111")
print(R"1234567\t1111")
print("1234567\\t1111")
#字符串索引正向从0开始，负向从-1开始
print('ABCDEF'[0])
print('ABCDEF'[-1])
print('ABCDEF'[-4:-1])#从-4开始到-1结束，不包含结束位
print('ABCDEF'[-4:])#从-4开始
print('ABCDEF'[2:])
print('ABCDEF'[:2])#到2结束
#一般字符串操作
a = '123'
b = '1234'
print(a+b)
print(a*3)
print(a in b)
#类型自动转换：显式和隐式
#隐式
c = 1
d = 2
print(c/d,type(c/d))
#显式
print("float转int",int(10.1))#去尾
print("int转float",float(10))
print("str转int",int("1")+int("1"))
#进制转换，结果为字符串类型
print(bin(10))
print(oct(10))
print(hex(10))
#eval函数：去掉字符串中的引号并执行，与input函数一起使用
e = '1+2'
print(eval(e))
#运算符：+,-,*,/,//,%,**
print("整除",10//3)
print("取余",10%3)
print('求幂',2**3)
#赋值(+=)，比较，逻辑运算(and or not)
#位运算符：与&，或|，非~，异或^,左移<<,右移>>
print(bin(0b101&0b110))
print(bin(0b101|0b110))
print(bin(~0b110))
print(bin(0b101^0b110))
print('左移相当于*',2<<3)
print('右移相当于/',4>>2)
print('右移相当于/',-4>>2)
