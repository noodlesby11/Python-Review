from datetime import datetime
dt=datetime.now()
print("获取现在的时间:",dt)
#创建datetime类
dt1 = datetime(2020, 9, 9, 23, 00, 0o1)
print(dt1)
#日期比较大小
print(dt>dt1)
#datetime类型与字符串进行转换
now_str= dt.strftime('%Y-%m-%d %H-%M-%S')
print("类型：",type(now_str),"是什么：",now_str)
#字符串类型转datetime类型
str_datetime="2020-01-01 19-00"
dt2=datetime.strptime(str_datetime,'%Y-%m-%d %H-%M')
print(type(str_datetime),str_datetime)
print(type(dt2),dt2)

from datetime import timedelta
#timedelta表示时间间隔的类
td=dt-dt1
print(type(td),td)
#创建一个timedelate对象
td1=timedelta(10)
td2=timedelta(10,10)
print("td1时间间隔为:",td1)
print("td2时间间隔为:",td2)
