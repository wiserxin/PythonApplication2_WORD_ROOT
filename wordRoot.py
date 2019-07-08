# -*- coding: utf-8 -*-
import xlrd

ExcelFile=xlrd.open_workbook(r'src.xlsx')

sheet=ExcelFile.sheet_by_index(0)

global roots
global means
global exmps

roots = sheet.col_values(0)
means = sheet.col_values(1)
exmps = sheet.col_values(2)

def getM( theRoot ): #get meanings
    try:
        if(theRoot.isdigit()):
            i = int(theRoot)-1
        else:
            i = roots.index(theRoot)
        return str(i+1) + ': ' + roots[i] + '\n\n' + means[i] + "\n\n" + exmps[i]
    except :  
        #print(e)
        return 'No such object ...'


#print(getM('a'))
#print(getM('qqq'))




"""
def read_excel():
    #文件位置
    ExcelFile=xlrd.open_workbook(r'src.xlsx')
    #获取目标EXCEL文件sheet名
    print (ExcelFile.sheet_names())
    #------------------------------------
    #若有多个sheet，则需要指定读取目标sheet例如读取sheet2
    #sheet2_name=ExcelFile.sheet_names()[1]
    #------------------------------------
    #获取sheet内容【1.根据sheet索引2.根据sheet名称】
    #sheet=ExcelFile.sheet_by_index(1)
    sheet=ExcelFile.sheet_by_name('TestCase002')
    #打印sheet的名称，行数，列数
    print (sheet.name,sheet.nrows,sheet.ncols)
    #获取整行或者整列的值
    rows=sheet.row_values(2)#第三行内容
    cols=sheet.col_values(1)#第二列内容
    print (cols,rows)
    #获取单元格内容
    print (sheet.cell(1,0).value.encode('utf-8'))
    print (sheet.cell_value(1,0).encode('utf-8'))
    print (sheet.row(1)[0].value.encode('utf-8'))
    #打印单元格内容格式
    print (sheet.cell(1,0).ctype)

if __name__ =='__main__':
    read_excel()
"""
