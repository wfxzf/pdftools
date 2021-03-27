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
##  使用方法  :   输入要切分的文件名，输入文件名，起止页面即可输入，所有文件均在同一目录下                                               ##                                                                                                                                              ##
###############################################################################################################################


import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


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
