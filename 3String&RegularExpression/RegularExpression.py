#正则表达式：表示字符串符合的一种模式
#元字符：具有特殊含义的字符
"""
^   匹配的开始
$   匹配的结束
.   匹配任意字符
\w  匹配字母数字下划线
\W  匹配非字母数字下划线
\s  匹配任意空白字符\n\t等
\S  匹配任意非空白字符
\d  匹配任意十进制数字
"""
#限定符：用于限定匹配的次数
"""
?   匹配前面的字符1次或0次    cl?r    匹配clr或者cr
+   匹配前面的字符1次或多次    cl+r    匹配clr或者cllll……r
*   匹配前面的字符0次或者多次   cl*r    匹配cr或者cllll……r
{n} 匹配前面的字符n次           cl{2}r 匹配cllr
{n,}    匹配前面的字符最少n次     cl{2,}r 匹配cll……r
{n,m}   匹配前面的字符最少n次最多m次
[]      匹配[]中指定的字符  [0-9]   匹配0,1,2,3,4,5,6,7,8,9,0
^       匹配不在[]中指定的字符    [^0-9]  匹配0,1,2,3,4,5,6,7,8,9,0以外的字符
|       用于匹配|两边的任意字符    \d{18}|\d{15}   匹配15位或者18位身份证
[\u4e00-\u9fa5]     匹配任意汉字
()      改变限定符的作用，优先计算括号
"""
#re模块，用于实现正则表达式的操作
#match函数的使用：对字符串开头进行匹配若成功返回match对象，否则为None
import re
pattern = '\d\.\d+'
s= 'python3.11'
s1= '3.11python'
m=re.match(pattern,s,re.I)#re.I表示忽略大小写
m1=re.match(pattern,s1,re.I)
print(m)
print(m1)
print("匹配的起始位置：",m1.start())
print("匹配的结束位置：",m1.end())
print("匹配的区间：",m1.span())
print("待匹配的字符串：",m1.string)
print("匹配的数据：",m1.group())
#search函数的使用：对整个字符串进行匹配的第一个值若成功返回match对象，否则为None
m3=re.search(pattern,s,re.I)
print("search:",m3)
#findall函数的使用：对整个字符串所有匹配的值，返回列表对象
s2 = '3.11python3.6python3.1'
print("findall:",re.findall(pattern,s2,re.I))
#sub函数用于实现对于字符串中指定字串的替换
print(re.sub(pattern,'***',s2))
#split函数使用指定模式匹配的字符进行分隔,返回列表对象
print("split:",re.split(pattern,s2))
