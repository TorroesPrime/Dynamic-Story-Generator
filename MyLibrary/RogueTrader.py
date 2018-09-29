from MyLibrary.GameCharacter import GameCharacter
import random

class RogueTrader(GameCharacter):
    race = 'human'
    racebonus = random.randint(20,28)
    def character_sheet(self):
        print('yes')
        #pass