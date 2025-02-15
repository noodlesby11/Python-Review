#pillow是图像处理的第三方库，支持图像的存储、处理和显示
from PIL import Image
#加载图片
im=Image.open('python3.jpg')
#加载RGB图像的颜色通道，返回的是图像的副本
r,g,b,*_=im.split()
#合并通道
om=Image.merge(mode='RGB',bands=(b,g,r))
om.save('python3_.png')