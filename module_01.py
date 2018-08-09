from classes import *

char01 = character.AutoMaker("Human")
char01.character_sheet()
char01 = character.AutoMaker("Human")
char02 = character.AutoMaker("Human")
char03 = character.AutoMaker("Human")
char04 = character.AutoMaker("Human")
char05 = character.AutoMaker("Human")
char06 = character.AutoMaker("Human")
char07 = character.AutoMaker("Human")
char08 = character.AutoMaker("Human")
char09 = character.AutoMaker("Human")
char10 = character.AutoMaker("Human")


characters = [char01,char02,char03,char04,char05,char06,char07,char08,char09,char10]
for chars in characters:
    chars.character_sheet()

