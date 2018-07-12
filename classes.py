import random
from library import *
"""library is a series of lists of strings. They are used for selecting names of characters,
selecting what role SpaceMarine characters get. etc. """
def intro():
    """Introduction to file

        This file contains the classes and methods used for each character.
        -class skill(object): skill objects for a characters including the SkillTest Method
        +skill.SkillTest: Used when a character performs a test on a selected skill.
        -class Character(object): Basic characer class.
        +CharSheet: Produces a character sheet.
        +StatTest: Used to test on a given stat.
        +StatBuilder: used to generate stats at character generation.
        +Automaker: a factory method for generating characters at random.
        -class SpaceMarine(Character): character class for space marines, inherits from class
        character
        +CharSheet: Produces a character sheet for a Space Marine Character.
        """
    intro =     """Introduction to file

        This file contains the classes and methods used for each character.
        -class skill(object): skill objects for a characters including the SkillTest Method
        +skill.SkillTest: Used when a character performs a test on a selected skill.
        -class Character(object): Basic characer class.
        +CharSheet: Produces a character sheet.
        +StatTest: Used to test on a given stat.
        +StatBuilder: used to generate stats at character generation.
        +Automaker: a factory method for generating characters at random.
        -class SpaceMarine(Character): character class for space marines, inherits from class \n character
        +CharSheet: Produces a character sheet for a Space Marine Character.
        """
    print(intro)
