# more for ease of organization, this file would be used to create all the
# characters. Also easier to test.
from classes import *

SM_01 = SpaceMarine.AutoMaker("SpaceMarine")
SM_02 = SpaceMarine.AutoMaker("SpaceMarine")
SM_03 = SpaceMarine.AutoMaker("SpaceMarine")
SM_05 = SpaceMarine.AutoMaker("SpaceMarine")


#SM_01.CharSheet()

SM_01.StatTest('Ballistic Skill',10,True)
#SM_01.StatTest('Weapon Skill',0,False)
#SM_01.StatTest('Strength',-10,False)
#SM_01.StatTest('Toughness',0, False)
#SM_01.StatTest('Agility',0, False)
#SM_01.StatTest('Perception',0, False)
#SM_01.StatTest('Will Power',0, False)
#SM_01.StatTest('Intelligence',0, False)
#SM_01.StatTest('Fellowship',50, False)

#if SM_01.StatTest:
#   print('True')

SM_01.CharSheet()
