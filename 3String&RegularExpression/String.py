#字符串是不可变数据类型
#字符串方法
Str=' abcdEFGH '
print(Str.lower())#全部转换为小写，结果为一个新的字符串
print(Str.upper())#全部转换为大写，结果为一个新的字符串
print(Str.split("d"))#将字符串按照指定字符进行分隔，结果为列表类型
print(Str.count("cd"))#指定字符串在字符串中出现的次数
print(Str.find("dE"))#查询指定字符串，若不存在则返回-1，存在则返回首次出现索引
print(Str.index("FG"))#与find相同，但不存在则报错
print(Str.startswith("ab"))#查询字符串是否以指定字串开头
print(Str.endswith("H"))#查询字符串是否以指定字串开头
print(Str.replace("cd","34"))#使用new替换原字符串中所有的old结果是新字符串
print(Str.center(20))#使字符串在指定范围内居中
print(Str.center(20,"*"))#使字符串在指定范围内居中,选择填充字符
print(Str.join("12345"))#在指定字符串的每个元素（除最后一个字符）后面都增加该字符串
print(Str.lstrip())#去掉字符串左侧指定字符，若为空则表示空格
print(Str.rstrip())#去掉字符串右侧指定字符，若为空则表示空格
print(Str.strip())#去掉字符串两侧指定字符，若为空则表示空格

print("字符串的格式化","-"*40)
#字符串的格式化
#1.使用占位符的字符串的格式化
i = 10
f = 11.11
print("字符串：%s,整型：%d,浮点型：%f" % (Str,i,f))
print("字符串：%s,整型：%d,浮点型：%.2f" % (Str,i,f))
#2.使用f-string的字符串的格式化，python3.6
print(f"字符串：{Str},整型：{i},浮点型：{f}")
#3.使用字符串的format方法
print("字符串：{0},整型：{1},浮点型：{2}".format(Str,i,f))
#字符串的详细控制，:引导符号，*表示宽度不够时的填充符号，<左对齐>右对齐^居中对齐，数字20为宽度
print("左对齐：{0:*<20}".format(Str))
print("右对齐：{0:*>20}".format(Str))
print("居中对齐：{0:*^20}".format(Str))
#千位分隔符,只用于整数和浮点数
print('{0:,}'.format(1234567.876556))
#浮点数精度
print('{0:.2f}'.format(123.23213))
#字符串类型设置最大显示宽度
print('{0:.2}'.format("1234567"))
#整数类型使用不同进制表示
a = 17
print("二进制:{0:b}十进制:{0:d}八进制:{0:o}十六进制{0:x}".format(a))
#浮点数的类型控制
b=3.1415926
print('{0:.2f},{0:.2e},{0:.2%}'.format(b))

print("字符串的数据验证","-"*40)
#字符串的数据验证方法
s = "123一二三"
s2 = "acb一二"
print("所有字符都是阿拉伯数字:",s.isdigit())
print("所有字符都是数字(包括中文数字罗马数字):",s.isnumeric())
print("所有字符都是字母（包含中文字符）：",s2.isalpha())
print("所有字符都是数字或字母（包含中文字符）：",s2.isalnum())
print("所有字符都是小写：",s2.islower())
print("所有字符都是大写：",s2.isupper())
print("所有字符都是首字母大写：",s.istitle())
print("所有字符都是空白字符（\\n\\t等）：",s.isspace())

print("字符串的拼接","-"*40)
#字符串的拼接方法
h = 'hello'
h1 = 'world'
print(h+h1)
print(''.join([h,h1]))#使用空字符串进行拼接
print('hello''world')
print('%s%s'%(h,h1))
print(f'{h}{h1}')
print('{0}{1}'.format(h,h1))

print("字符串的去重","-"*40)
#字符串的去重方法
h3='adfassfdafacaffaffd'
#1.not in
hs = ''
for i in h3:
    if i not in hs:
        hs+=i
print(hs)
#2.索引not in
hs2=''
for i in range(len(h3)):
    if h3[i] not in hs2:
        hs2+=h3[i]
print(hs2)