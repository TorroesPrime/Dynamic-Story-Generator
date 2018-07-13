import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import random
source = pd.read_excel('library.xlsx', sheet_name='names')
HumanMaleNames = source['HumanMaleNames']
HumanFemaleNames = source['HumanFemaleNames']
HumanLastNames = source['HumanLastNames']
HumanTitles = source['HumanTitles']
BloodAngelNames = source['BloodAngelNames']
BloodAngelTitles = source['BloodAngelTitles']
DarkAngelNames = source['DarkAngelNames']
DarkAngelTitles = source['DarkAngelTitles']
SpaceWolvesNames = source['SpaceWolvesNames']
SpaceWolvesTitles = source['SpaceWolvesTitles']
UltramarinesNames = source['UltramarinesNames']
UltramarinesTitles = source['UltramarinesTitles']
BlackTemplarsNames = source['BlackTemplarsNames']
BlackTemplarsTitles = source['BlackTemplarsTitles']
print("Human Male name: "+random.choice(HumanMaleNames))
print("Human Female name: "+random.choice(HumanFemaleNames))
print("Human Last name: "+str(random.choice(HumanLastNames)))
print("Blood Angels name: "+str(random.choice(BloodAngelNames)))
print("Dark Angels name: "+str(random.choice(DarkAngelNames)))
print("Space Wolves Name: "+str(random.choice(SpaceWolvesNames)))
print("Space Wolves Title: "+str(random.choice(SpaceWolvesTitles)))
print("Ultramarines Name: "+str(random.choice(UltramarinesNames)))
print("Black Templar names: "+str(random.choice(BlackTemplarsNames)))
