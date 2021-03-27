# Copyright (C) 2021  wfxzf

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

###############################################################################################################################
##  使用方法  :   执行路径下新建image文件夹，将要转PDF的图片用数字命名（如 1.png,2.png,3.png）放入此文件夹中。                    ##                                        
##  将按照数字顺序将图片合成为PDF，仅支持jpg\gif\png格式                                                                        ##
##  其他格式需要修改  “if "jpg" in x or 'png' in x or "JPG" in x or 'PNG' in x or "GIF" in x or 'gif' in x:”处后使用           ##
################################################################################################################################



from PIL import Image
import os


def rea(pdf_name):
    file_list = os.listdir('image')#文件夹

    pic_number = 0
    im_list = []
    for x in file_list:
        if  'png' in x or 'PNG' in x or "GIF" in x or 'gif' in x:
            pic_number = pic_number + 1
            os.rename('image/'+x,'image/'+x[:-3]+'jpg')
        if "jpeg" in x:
            pic_number = pic_number + 1
            os.rename('image/'+x,'image/'+x[:-4]+'jpg')
        if  "jpg" in x or 'JPG' in x:
            pic_number = pic_number + 1


    new_pic=[]
    for i in range(1,pic_number+1):
        new_pic.append(str(i)+'.jpg')
    
    im1 = Image.open('image/'+new_pic[0])#记得改文件夹
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open('image/'+i)#记得改文件夹
        img = img.convert('RGB')
        im_list.append(img)
    print(len(im_list))
    im1.save(pdf_name, "PDF", resolution=300.0, save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)



if __name__ == '__main__':
    print("合成")
    pdf_name = input("请输入合成PDF文件名称：")
    if ".pdf" in pdf_name:
      rea(pdf_name=pdf_name)
    else:
      rea(pdf_name="{}.pdf".format(pdf_name))
    input("按任意键结束")