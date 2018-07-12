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
class Character(object):
    """Character class.

    The basic character class. Each character has a string for their name (name), 10 basic stats
    including Weapon Skill (Stat_WS), Ballistic skill (Stat_BS), Strength(Stat_Strength),
    Toughness(Stat_Toughness), Agility(Stat_Agility),Intelligence(Stat_Int),
    Perception(Stat_Perc), and Fellowship(Stat_Fell). They also have wounds which is an
    integer. All of the stats are copied into the Char_Stats dictionary to make it easier to run
    through all the stats when making a stat check or test."""
    def __init__ (self, name, Stat_WS, Stat_BS, Stat_Strength, Stat_Tough, Stat_Agility, Stat_Int, Stat_Perc, Stat_WP, Stat_Fell, wounds):
        self.name = name
        self.Char_Stats = {'Weapon Skill':0,'Ballistic Skill':0,'Strength':0,'Toughness':0,'Agility':0,'Intelligence':0,'Perception':0,'Will Power':0,'Fellowship':0,}
        self.Stat_WS = Stat_WS
        self.Stat_BS = Stat_BS
        self.Stat_Strength = Stat_Strength
        self.Stat_Tough = Stat_Tough
        self.Stat_Agility = Stat_Agility
        self.Stat_Int = Stat_Int
        self.Stat_Perc = Stat_Perc
        self.Stat_WP = Stat_WP
        self.Stat_Fell = Stat_Fell
        self.Char_Stats['Weapon Skill'] = int(Stat_WS)
        self.Char_Stats['Ballistic Skill'] = int(self.Stat_BS)
        self.Char_Stats['Strength'] = int(self.Stat_Strength)
        self.Char_Stats['Toughness'] = int(self.Stat_Tough)
        self.Char_Stats['Agility'] = int(self.Stat_Agility)
        self.Char_Stats['Intelligence'] = int(self.Stat_Int)
        self.Char_Stats['Perception'] = int(self.Stat_Perc)
        self.Char_Stats['Will Power'] = int(self.Stat_WP)
        self.Char_Stats['Fellowship'] = int(self.Stat_Fell)
        self.fatigue = fatigue
        self.wounds = wounds
