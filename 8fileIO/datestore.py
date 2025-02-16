lst1=['AAA','BBB','CCC']
lst2=[
     ['A','B','C'],
     ['AA','BB','CC'],
     ['AAA','BBB','CCC']
]
lst3=[
    {'A':'1','B':'2','C':'3'},
    {'AA':'11','BB':'22','CC':'33'},
    {'AAA':'111','BBB':'222','CCC':'333'}
]
#文件存储和读取一维数据
def writefile(ls):
    with open('store.csv','w') as file:
        #将列表转换成字符串
        file.write(','.join(ls))
def readfile(src):
    with open(src,'r') as file:
        s=file.read()
        l=s.split(',')
        print(l)

#文件存储和读取二维数据
def writefile2(ls):
    with open('store2.csv','w',encoding='utf-8') as f:
        for item in ls:#将列表拼接到一起
            lines=','.join(item)
            f.write(lines)
            f.write('\n')
def readfile2(src):
    date=[]#用于存储每一个列表
    with open(src,'r',encoding='utf-8') as file:
        lst=file.readlines()
        for item in lst:
            l=item[:len(item)-1].split(',')
            date.append(l)
    print(date)

#文件存储键值对 使用json模块
"""
json.dumps(obj):将python数据类型转换成json格式，即编码
json.loads(s):将json格式的字符串转换成python数据类型，即解码
json.dump(obj,file):将编码结果存储到file中
json.load(file):将解码结果储存到file中
"""
import json
def writefile3(lst):
    with open('store3.txt','w') as file:
        json.dump(lst,file,ensure_ascii=False,indent=4)#ensure_ascii设置中文，indent设置缩进
def readfile3(src):
    with open(src,'r',encoding='utf-8') as file:
        l=json.load(file)
        print(l)

if __name__ =='__main__':
    #writefile3(lst3)
    readfile3('store3.txt')