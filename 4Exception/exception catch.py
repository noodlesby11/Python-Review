#python中的异常处理
"""
try:
    可能会抛出异常的代码
except 异常类型A：
    异常处理代码
except 异常类型B：
    异常处理代码
else:
    没有异常要执行的代码
finally:
    无论有没有异常都执行的代码
"""
try:
    num1 = int(input("请输入被除数："))
    num2 = int(input("请输入除数："))
except  ZeroDivisionError:
    print("除数为0")
except  ValueError:
    print("输入不是数字")
except  BaseException:
    print('未知异常')
else:
    print("结果为：%s"%(num1/num2))
finally:
    print("结束")