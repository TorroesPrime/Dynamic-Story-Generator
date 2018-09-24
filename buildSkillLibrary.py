import xlrd
import random
from library import *
from classes import *
row = 1
column = 0
total_rows = worksheet.nrows
test = True

while row < total_rows:
    if worksheet.cell(row,21).value != xlrd.empty_cell.value:
        name = skillsWorksheet.cell(row,column).value
        column += 1
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
        char = skillsWorksheet.cell(row,column).value
        column += 1
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
        rank = int(skillsWorksheet.cell(row,column).value)
        column += 1
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
        descrip = skillsWorksheet.cell(row,column).value
        if test == True:
            print('Skill Name: '+str(name))
            print('Characteristic: '+str(char))
            print('Rank: '+str(rank))
            print('Skill Description: '+str(descrip))
        NewSkill = skill(name,char,rank,descrip)
        skills.append(NewSkill)
        column = 0
        row += 1
    else:
        if test == True:
            print('finished skills phase')
        row = total_rows

#row = 1
