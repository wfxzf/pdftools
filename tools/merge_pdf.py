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


import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def MergePDF(outfile):

    file_list = os.listdir('pdf')#文件夹

    pdf_number = 0
    im_list = []
    for x in file_list:
        if  'PDF' in x or 'pdf' in x:
            pdf_number = pdf_number + 1
            os.rename('pdf/'+x,'pdf/'+x[:-3]+'pdf')

    output = PdfFileWriter()
    Pagenumber = 0

    new_pdf=[]
    for i in range(1,pdf_number+1):
        new_pdf.append(str(i)+'.pdf')



    for pdf_file in new_pdf:

        input = PdfFileReader(open('pdf/'+pdf_file, "rb"))
        Count = input.getNumPages()
        Pagenumber = Count + Pagenumber

        for i in range(Count):
            output.addPage(input.getPage(i))

    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()
    print("合并完成！")
    print("页数:"+str(Pagenumber))


# 主函数
def main():

    print("合成")
    pdf_name = input("请输入合成PDF文件名称：")
    if ".pdf" in pdf_name:
        MergePDF(pdf_name)
    else:
        MergePDF("{}.pdf".format(pdf_name))
    input("按任意键结束")

main()
