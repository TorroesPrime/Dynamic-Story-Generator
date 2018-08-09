import xlrd
from classes import *

workbook = xlrd.open_workbook("library.xlsx")
skills = workbook.sheet_by_name("skills")
row = 1
cols = 0
skills =()
i = 0
skills_total_rows = skills.nrows
while i < skills_total_rows:
    skill_01 = skill(name, char, rank, descrip)
    skills.append(skill_01)
    i += 1

print(skills)
