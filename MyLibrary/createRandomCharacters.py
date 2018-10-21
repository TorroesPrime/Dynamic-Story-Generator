# from MyLibrary.CharacterStats import CharacterStats
# from MyLibrary.Human import HumanCharacter
# from MyLibrary.RogueTrader import RogueTrader
# from MyLibrary.GameCharacter import GameCharacter
import random
from CharacterStats import CharacterStats
from Human import HumanCharacter
from RogueTrader import RogueTrader
from GameCharacter import GameCharacter
from DataLibrary import FnamesHumanM, FnamesHumanF, LnamesHuman

traders = []
humans = []


def createRandomCharacter(characterType):
    random_stats = CharacterStats()
    random_stats.randomizeMe()
    gender = getRandomGender()
    firstName = getRandomFirstName()
    lastName = getRandomLastName()

    return GameCharacter(firstName, lastName, gender, characterType, random_stats)


def getRandomFirstName():
    firstName = random.choice(FnamesHumanF)
    # return fName.choice(F-namesHumanM)
    return firstName
    # if gender == "Male":
    #    return name.choice(F-namesHumanM)
    # else:
    #    return name.choice(F-namesHumanF)


def getRandomLastName():
    # Modify me so I return something from your text files.
    lastName = random.choice(LnamesHuman)
    return lastName


def getRandomGender():
    select = random.randint(1, 2)
    if select == 1:
        gender = "Female"
    else:
        gender = "Male"
    return gender


fName = getRandomFirstName()
lName = getRandomLastName()
gender = getRandomGender()
stats = CharacterStats()
characterStats = stats.randomizeMe()
# RogueTrader =createRandomCharacter(RogueTrader(getRandomFirstName(),getRandomLastName(),getRandomGender(),"Human",CharacterStats.randomizeMe()))
trader01 = createRandomCharacter(RogueTrader(fName, lName, gender, "Human", characterStats))
for i in range(0, 4):
    fName = getRandomFirstName()
    lName = getRandomLastName()
    gender = getRandomGender()
    stats = CharacterStats()
    characterStats = stats.randomizeMe()
    # RogueTrader = createRandomCharacter(RogueTrader(getRandomFirstName(),getRandomLastName(),getRandomGender(),"Human",CharacterStats.randomizeMe()))
    traders.append(createRandomCharacter(RogueTrader(fName, lName, gender, "Human", characterStats)))
    # traders.append(RogueTrader)

for person in traders:
    person.getFullName()
    print(person.full_name)
    person.character_sheet()
# for i in range(0,4):
#    humans.append(createRandomCharacter(HumanCharacter()))

# Do stuff with your lists of characters.
