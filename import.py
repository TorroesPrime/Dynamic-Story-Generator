import xlrd
workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
HumanMaleNames = []
print('the name at column 1, row 20 is: '+worksheet.cell(4,2).value)
iteration = 1
j = worksheet.cell(1,iteration).value
while j != xlrd.empty_cell.value:
    HumanMaleNames.append(j)
    iteration += 1
    print(str(iteration)+'name added to list')
