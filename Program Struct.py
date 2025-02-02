#顺序结构

#选择结构
print("单分支结构","-"*20)
#1.单分支
num = eval(input("输入一位数字:"))
if num == 1:
    print("这是1")

print("双分支结构","-"*20)
#2.双分支结构
if num%2 != 0:
    print("这是奇数")
else:
    print("这是偶数")

print("多分支结构","-"*20)
#3.多分支结构
score = eval(input("输入分数："))
if score > 100 or score < 0:
    print("错误成绩")
elif 90<= score < 100 :
    print("优秀")
elif 60<= score < 90:
    print("良好")
else:
    print("不合格")

print("嵌套结构","-"*20)
#4.嵌套结构
n = eval(input("输入一个数字:"))
if int(n/10) ==0 :
    print("输入了1位数")
    if num % 2 != 0:
        print("这是奇数")
    else:
        print("这是偶数")
elif int(n/100) ==0:
    print("输入了2位数")
    if num % 2 != 0:
        print("这是奇数")
    else:
        print("这是偶数")
elif int(n/1000) ==0:
    print("输入了3位数")
    if num % 2 != 0:
        print("这是奇数")
    else:
        print("这是偶数")
else:
    print("超过3位数")

print("匹配模式","-"*20)
#5.模式匹配（python3.11以上）
match num:
    case 1 : print("壹")
    case 2 : print("贰")
    case 3 : print("叁")
    case 4 : print("肆")
    case 5 : print("伍")
    case 6 : print("陆")
    case 7 : print("柒")
    case 8 : print("捌")
    case 9 : print("玖")
    case 0 : print("零")

print("for结构","-"*20)
#循环结构
#for循环  for 循环变量 in 遍历对象: 语句块
s = 0
for i in range(1,11):
    print(i)
    s += i
print(s)

print("for else结构","-"*20)
#for else 结构    for正常结束后执行else语句块
s = 0
for i in range(1,11):
    print(i)
    s += i
else:
    print(s)

print("while结构","-"*20)
#while结构       while 表达式:语句块
t=1
su=0
while t<=10:
    su+=t
    t+=1
print(su)

print("while else结构","-"*20)
#while else结构
t2=0
su2=0
while t2<=10:
    su2+=t2
    t2+=1
else:
    print(su2)

#循环嵌套

print("break语句","-"*20)
#break语句
x=0
while True:
   if x==10:
       break
   else:
       x+=1
   print(x,end=" ")

print("continue语句","-"*20)
#continue语句
for i in range(1,11):
    if i==5 : continue
    print(i,end=" ")

#pass
for i in range(1,100):
    pass