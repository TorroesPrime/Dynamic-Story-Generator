import xlrd
workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
HumanMaleNames = []
print('the name at column 1, row 20 is: '+worksheet.cell(4,2).value)
row = 1
j = worksheet.cell(row,1).value
while j != xlrd.empty_cell.value:
    HumanMaleNames.append(j)
    row += 1
    print(str(j)+' added to list')
    print(str(row))

