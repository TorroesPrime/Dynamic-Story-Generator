import xlrd
import random
"""builds the library of lists used in character creation. The material is read in from library.xlsx and fed into a series of lists."""


workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
skills = workbook.sheet_by_name("skills")
HumanMaleNames = []
HumanFemaleNames = []
HumanLastNames = []
HumanTitles = []
BloodAngelNames = []
BloodAngelTitles = []
DarkAngelNames = []
DarkAngelTitles = []
SpaceWolvesNames = []
SpaceWolvesTitles = []
UltramarinesNames = []
UltramarinesTitles =[]
BlackTemplarsNames = []
BlackTemplarsTitles = []
DeamonSyllabals = []
races = []
row = 1
total_rows = worksheet.nrows
while row < total_rows:
    j = worksheet.cell(row,0).value
    HumanMaleNames.append(j)
    row += 1
#print('finished phase 1')
row = 1
while row < total_rows:
    if worksheet.cell(row,1).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,1).value
        HumanFemaleNames.append(j)
        row += 1
    else:
#        print('finished phase 2')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,2).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,2).value
        HumanLastNames.append(j)
        row += 1
    else:
#        print('finished phase 2')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,3).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,3).value
        HumanTitles.append(j)
        row += 1
    else:
#        print('finished phase 3')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,4).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,4).value
        BloodAngelNames.append(j)
        row += 1
    else:
#        print('finished phase 4')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,5).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,5).value
        BloodAngelTitles.append(j)
        row += 1
    else:
#        print('finished phase 5')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,6).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,6).value
        DarkAngelNames.append(j)
        row += 1
    else:
#        print('finished phase 6')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,7).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,7).value
        DarkAngelTitles.append(j)
        row += 1
    else:
#        print('finished phase 7')
        row = total_rows       
row = 1
while row < total_rows:
    if worksheet.cell(row,8).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,8).value
        SpaceWolvesNames.append(j)
        row += 1
    else:
#        print('finished phase 8')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,9).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,9).value
        SpaceWolvesTitles.append(j)
        row += 1
    else:
#        print('finished phase 9')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,10).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,10).value
        UltramarinesNames.append(j)
        row += 1
    else:
#        print('finished phase 10')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,11).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,11).value
        UltramarinesTitles.append(j)
        row += 1
    else:
#        print('finished phase 11')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,12).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,12).value
        BlackTemplarsNames.append(j)
        row += 1
    else:
#        print('finished phase 12')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,13).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,13).value
        BlackTemplarsTitles.append(j)
        row += 1
    else:
#        print('finished phase 13')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,14).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,14).value
        DeamonSyllabals.append(j)
        row += 1
    else:
#        print('finished phase 14')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,15).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,15).value
        races.append(j)
        row += 1
    else:
#        print('finished phase 15')
        row = total_rows
row = 1
HumanTitles_m = [x for x in HumanTitles if x != "Duchess"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Lady"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Damme"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Baroness"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Dame"]
HumanTitles_f = [x for x in HumanTitles if x != "Duke"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Lord"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Baron"]

def RandomDaemonNameGenerator(output):
    x = 0
    DaemonName = ''
    numOfSyllabals = random.randint(1,7)
    while x < numOfSyllabals:
        DaemonName = DaemonName+random.choice(DeamonSyllabals)+'\''
        DaemonName = DaemonName.capitalize()
        x += 1
#    if output == True:
#        print(DaemonName)
    return DaemonName
        
def DaemonNameGenerator(output, numOfSyllabals):
    x = 0
    DaemonName = ''
    while x < numOfSyllabals:
        DaemonName = DaemonName+random.choice(DeamonSyllabals)+'\''
        DaemonName = DaemonName.capitalize()
        x += 1
#    if output == True:
#        print(DaemonName)
    return DaemonName
    



