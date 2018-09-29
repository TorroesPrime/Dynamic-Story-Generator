from MyLibrary.CharacterStats import CharacterStats
from MyLibrary.Human import HumanCharacter
from MyLibrary.RogueTrader import RogueTrader
from MyLibrary.GameCharacter import GameCharacter

traders = []
humans = []


def getRandomFirstName():
    #Modify me so I return something from your text files.
    pass

def getRandomeLastName():
    #Modify me so I return something from your text files.
    pass

def getRandomSex():
    """
    Less fun than it sounds.
    :return:
    """
    sex = ["Male", "Female"]
    return sex.choice(sex.list_upper)


def createRandomCharacter(characterType):
    random_stats = CharacterStats()
    random_stats.randomizeMe()
    return GameCharacter(getRandomFirstName(), getRandomFirstName(), getRandomSex(), characterType, random_stats)


for i in range(0,4):
    traders.append(createRandomCharacter(RogueTrader()))

for i in range(0,4):
    humans.append(createRandomCharacter(HumanCharacter()))

#Do stuff with your lists of characters.