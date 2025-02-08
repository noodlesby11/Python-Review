#raise:使代码主动抛出异常
try:
    score = int(input("输入成绩："))
    if (score<0)|(score>100):
        raise Exception("分数范围不正确")
except Exception as e:
    print(e)
else:
    print("输入的分数是：",score)