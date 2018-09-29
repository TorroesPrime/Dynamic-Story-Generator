#notes added
import random
#from library import *
from library import *
from import3 import *
from skill_builder import skills

"""library is a series of lists of strings. They are used for selecting names of characters,
selecting what role SpaceMarine characters get. etc. """
def intro():
    """Introduction to file

        This file contains the classes and methods used for each Character.
        -class skill(object): skill objects for a characters including the SkillTest Method
        +skill.SkillTest: Used when a Character performs a test on a selected skill.
        -class Character(object): Basic characer class.
        +CharSheet: Produces a Character sheet.
        +StatTest: Used to test on a given stat.
        +StatBuilder: used to generate stats at Character generation.
        +Automaker: a factory method for generating characters at random.
        -class SpaceMarine(Character): Character class for space marines, inherits from class
        Character
        +CharSheet: Produces a Character sheet for a Space Marine Character.
        """
    intro =     """Introduction to file

        This file contains the classes and methods used for each Character.
        -class skill(object): skill objects for a characters including the SkillTest Method
        +skill.SkillTest: Used when a Character performs a test on a selected skill.
        -class Character(object): Basic characer class.
        +CharSheet: Produces a Character sheet.
        +StatTest: Used to test on a given stat.
        +StatBuilder: used to generate stats at Character generation.
        +Automaker: a factory method for generating characters at random.
        -class SpaceMarine(Character): Character class for space marines, inherits from class \n Character
        +CharSheet: Produces a Character sheet for a Space Marine Character.
        """
    print(intro)


#        print(spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill))
class RogueTrader(character):
    race = 'human'
    racebonus = random.randint(20,28)
    def character_sheet(self):
        print('yes')
        #pass

    
class weapon(object):
    #just adding something to test git functionality
    """weapon class. Any sort of weapon used by a Character.

    name: the name of the weapon. A string
    descript: the description of the weapon. A multi-line string.
    weaponClass:  describes what class the weapon is. possible options are 'exocitc' 'melee' 'thrown' 'pistol' 'basic' 'heavy' or 'mounted'. Will be a string.
    weaponRange: The distance the weapon can shoot. will be 0 if weaponClass is 'melee' or 'thrown'.
    Rof: weapons rate of fire. Will be an interger. Determines how many attacks the weapon makes each turn.
    Damage: how much damage the weapon is capable of inflicting for each sussessful attack. an integer.
    Pen: penetration, a rating of how much armor the weapon can break through while remaining effective at dealing damage. an integer.
    Clip: how rounds of ammunition the weapon can hold before it must be reloaded. an integer
    reload: a string denoting if it takes a full or half turn to reload the weapon.
    special: a string denoting if the weapon has any sort of special quality to it.
    weight: an integer that represents how much the weapon weighs.
    requisition: cost of purchasing the weapon from the armory. an integer.
    renown: a string denoting the renown level a Character must have to purchase a weapon from the armory. """
   # def __init__ (self, name, descript, weaponClass, weaponRange, RoF, Damage, Pen, clip, reload, special, weight, requisition, renown ):
   #     self._name = name
   #     self._descript = descript
   #     self._weaponClass = weaponClass
   #     self._range = weaponRange
   #     self._roF = Rof
   #     self._damage = Damage
   #     self._pen = Pen
   #    self._clip = clip
   #    self._reload = reload
   #     self._special = special,
   #    self._weight = weight
   #     self._requisition = requisition
   #     self._renown = renown


