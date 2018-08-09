import xlrd
from classes import *
workbook = xlrd.open_workbook("library.xlsx")
skills = workbook.sheet_by_name("skills")
row = 1
cols = 0
skills_library = []
skills_total_rows = skills.nrows
while row < skills_total_rows:
    while cols < 4:
        j = skills.cell(row,cols).value
        #print(j)
        if cols == 0:
            name = j
            #return name
        elif cols == 1:
            char = j
            #return char
        elif cols == 2:
            rank = j
            #return rank
        else:
            descrip = j
            #return descrip
        #print(i)
        cols += 1
    
    skill_01= skill(name, char, rank, descrip)
    #skill_01.skill_output()
    skills_library.append(skill_01)
    row += 1
    cols = 0
for skill in skills_library:
    print('='*80)
    skill.skill_output()
    

print('finished')
#name = "name_01"
#char = "Char_01"
#rank = 0
#descrip = """long description of the skill"""
#skill_01 = skill(name, char, rank, descrip)
#skill_01.skill_output()
