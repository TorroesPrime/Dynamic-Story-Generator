import xlrd
import random
from library import *
#from classes import *
#from classes import skill
#import ObjectsandClassesLibrary
#from ObjectsandClassesLibrary import CharacterSkill

workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
row = 1
#j = worksheet.cell(1,0).value
#row += 1
#j = worksheet.cell(2,0).value
#row += 1
j = worksheet.cell(row,0).value
LastRow = 1
total_rows = worksheet.nrows
column = 0
test = False
while row < total_rows:
    j = worksheet.cell(row,0).value
    HumanMaleNames.append(j)
    row += 1
if test == True:
        print('finished phase 1')
row = 1
while row < total_rows:
    if worksheet.cell(row,1).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,1).value
        HumanFemaleNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 2')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,2).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,2).value
        HumanLastNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 2')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,3).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,3).value
        HumanTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 3')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,4).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,4).value
        BloodAngelNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 4')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,5).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,5).value
        BloodAngelTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 5')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,6).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,6).value
        DarkAngelNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 6')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,7).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,7).value
        DarkAngelTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 7')
        row = total_rows       
row = 1
while row < total_rows:
    if worksheet.cell(row,8).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,8).value
        SpaceWolvesNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 8')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,9).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,9).value
        SpaceWolvesTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 9')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,10).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,10).value
        UltramarinesNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 10')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,11).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,11).value
        UltramarinesTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 11')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,12).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,12).value
        BlackTemplarsNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 12')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,13).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,13).value
        BlackTemplarsTitles.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 13')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,14).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,14).value
        DeamonSyllabals.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 14')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,16).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,16).value
        DeathWorldNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 15')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,17).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,17).value
        VoidBornNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 16')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,18).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,18).value
        ForgeWorldNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 17')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,19).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,19).value
        HiveWorldNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 18')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,20).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,20).value
        ImpWorldNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 19')
        row = total_rows
row = 1
while row < total_rows:
    if worksheet.cell(row,21).value != xlrd.empty_cell.value:
        j = worksheet.cell(row,21).value
        NobleBornWorldNames.append(j)
        row += 1
    else:
        if test == True:
            print('finished phase 20')
        row = total_rows
LastRow = 1
total_rows = skillsWorksheet.nrows
row = 1
HumanTitles_m = [x for x in HumanTitles if x != "Duchess"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Lady"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Damme"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Baroness"]
HumanTitles_m = [x for x in HumanTitles_m if x != "Dame"]
HumanTitles_f = [x for x in HumanTitles if x != "Duke"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Lord"]
HumanTitles_f = [x for x in HumanTitles_f if x != "Baron"]
#print("Human titles for male characters:")
#print(HumanTitles_m)

#rHM = random.choice(HumanTitles_m)+' '+random.choice(HumanMaleNames)+' '+random.choice(HumanLastNames)
#rHF = random.choice(HumanTitles_f)+' '+random.choice(HumanFemaleNames)+' '+random.choice(HumanLastNames)
#print(rHM)
#print(rHF)
#print("finished")
