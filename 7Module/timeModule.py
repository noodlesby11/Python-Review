import time
now=time.time()
print('获取当前时间戳：',now)
#获取指定时间戳的本地时间struct_time对象
local=time.localtime(now)
print(local)
print(type(local))
#当前时间戳的易读字符串
print(time.ctime())
#日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S %B %A',time.localtime()))
#字符串转struct_time类型
print(time.strptime("2000-01-10",'%Y-%m-%d'))