import xlrd
workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
HumanMaleNames = []
HumanFemaleNames = []
HumanLastNames = []
#print('the name at column 1, row 20 is: '+worksheet.cell(4,2).value)
row = 1
j = worksheet.cell(1,0).value
print(j)
row += 1
j = worksheet.cell(2,0).value
print(j)
row += 1
j = worksheet.cell(row,0).value
print(j)
LastRow = 1
total_rows = worksheet.nrows
print(total_rows)
while row < total_rows:
    j = worksheet.cell(row,0).value
    HumanMaleNames.append(j)
    #print("j: "+j)
    row += 1
print('pass phase 1')
row = 1
while row < total_rows:
    if worksheet.cell(row,1).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,1).value
        HumanFemaleNames.append(j)
        row += 1
        print(j)
    else:
        print('finished phase 2')
print(HumanMaleNames)
print(HumanFemaleNames)
#else:
#    print(LastRow)
#HumanMaleNames.append(j)
#print(row)
#print(HumanMaleNames)

#j = worksheet.cell(2,0).value
#print(j)
#j = worksheet.cell(3,0).value
#print(j)
#row += 2
#j = worksheet.cell(row,0).value
#print(j)
#print(str(row))
#while row < 300:
#while worksheet.cell(row,0) != xlrd.empty_cell.value:
#    LastRow += 1
#    row += 1
#row = 1
#while worksheet.cell(row,0) != xlrd.empty_cell.value:
#    j = worksheet.cell(row,0).value
    #print(j)
#    #print(str(row))
#    HumanMaleNames.append(j)
#    row += 1
#while worksheet.cell(row,0) < LastRow:
#    j = worksheet.cell(row,0).value
    #print(j)
    #print(str(row))
#    HumanMaleNames.append(j)
#    row += 1
#print(HumanMaleNames)
print("finished")
#while j != xlrd.empty_cell.value:
#    HumanMaleNames.append(j)
#    row += 1
#    print(str(j)+' added to list')
 #   print(str(row))
