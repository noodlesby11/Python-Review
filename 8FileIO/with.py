#with语句上下文管理器，无论是否产生异常都能保证with语句执行完毕后关闭已经打开的文件
"""
with open() as file:
    pass
"""
#复制文件
def filecopy(src,des):
    with open(src,'r',encoding='utf-8') as file:
        with open(src,'w',encoding='utf-8') as file2:
            file2.write(file.read())

