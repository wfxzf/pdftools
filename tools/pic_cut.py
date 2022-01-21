# coding: utf-8
from PIL import Image
import os
import os.path
import numpy as np
import cv2
#指明被遍历的文件夹
rootdir = 'image'
for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)
   
        img = Image.open(currentPath)
        print (img.format, img.size, img.mode)
        #img.show()
        box1 = (0, 550, 1080, 2070)#设置左、上、右、下的像素
        image1 = img.crop(box1) # 图像裁剪
        print(filename)
        image1.save('image\\'+filename) 