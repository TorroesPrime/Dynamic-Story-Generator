import xlrd
from library import skills
#from ObjectsandClassesLibrary import CharacterSkill, CharacterSkillGroup
from ObjectsandClassesLibrary import *
workbook = xlrd.open_workbook("library.xlsx")
skillsWorksheet = workbook.sheet_by_name("skills")
test = False
row = 1
column = 0
skills_library = []
skills_total_rows = skillsWorksheet.nrows
while row < skills_total_rows:
    if skillsWorksheet.cell(row,column).value != xlrd.empty_cell.value:
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
        NewSkill = CharacterSkill(name,char,rank,descrip)
        skills.append(NewSkill)
        column = 0
        row += 1
    else:
        if test == True:
            print('finished skills phase')
        row = skills_total_rows


skillsWorksheet = workbook.sheet_by_name("SkillGroups")
test = True
row = 1
column = 0
skills_library = []
skills_total_rows = skillsWorksheet.nrows
print("Skill Groups")
while row < skills_total_rows:
    if skillsWorksheet.cell(row,column).value != xlrd.empty_cell.value:
    #skill name
        name = skillsWorksheet.cell(row,column).value
        #column += 1
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
            print("Name: "+str(name))
        column += 1
    #skill_char
        char = skillsWorksheet.cell(row,column).value
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
            print("Characteristic: "+str(char))
        column += 1
    #topic
        topic = skillsWorksheet.cell(row,column).value
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
            print("topic: "+str(topic))
    #rank
        rank = skillsWorksheet.cell(row,column).value
        column += 1
        if test == True:
            print('column: '+str(column))
            print('row: '+str(row))
            print("rank: "+str(rank))
    #descrip
        descrip = skillsWorksheet.cell(row,column).value
        if test == True:
            print('Skill Name: '+str(name))
            print('Topic: '+str(topic))
            print('Characteristic: '+str(char))
            print('Rank: '+str(rank))
            print('Skill Description: '+str(descrip))
        NewSkill = CharacterSkillGroup(name,char,topic,rank,descrip)
        skills.append(NewSkill)
        column = 0
        row += 1
    else:
        if test == True:
            print('finished skills phase')
        row = skills_total_rows
#for SkillEntry in skills:
 #   print("------------------------"+SkillEntry._name+"------------------------")
 #  print(SkillEntry._descrip)