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
##  使用方法  :   执行路径下新建pdf文件夹，将要转PDF的图片用数字命名（如 1.pdf,2.pdf,3.pdf）放入此文件夹中。                    ##                                        
##  将按照数字顺序合成                                                                                                        ##
################################################################################################################################

# 只需修改存放PDF文件的文件夹变量：file_dir 和 输出文件名变量: outfile

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


# 合并同一目录下的所有PDF文件
def SegPDF(file,outfile):



    inputs = PdfFileReader(open(file, "rb"))
    
    output = PdfFileWriter()
    begin = int(input("开始页码"))
    end = int(input("截至页码"))

    for i in range(begin-1,end):
        output.addPage(inputs.getPage(i))

    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()
    print("拆分完成！")


# 主函数
def main():

    pdf_name = input("请输入当前目录下要拆分的PDF文件名称：")
    newpdf_name = input("请输入拆分后的PDF文件名称：")
    if ".pdf" in pdf_name and ".pdf" in newpdf_name:
        SegPDF(pdf_name,newpdf_name)
    else:
        if ".pdf" not in pdf_name and ".pdf" in newpdf_name:
            SegPDF("{}.pdf".format(pdf_name),newpdf_name)
        else:
            if ".pdf" in pdf_name and ".pdf" not in newpdf_name:
                SegPDF(pdf_name,"{}.pdf".format(newpdf_name))
            else:
                SegPDF("{}.pdf".format(pdf_name),"{}.pdf".format(newpdf_name))

    input("按任意键结束")

main()