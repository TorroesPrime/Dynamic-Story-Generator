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
class character(object):
    """Character class.

    The basic character class. Each character has a string for their name (name), 10 basic characteristics
    including Weapon Skill (stats_weapon_skill), Ballistic skill (stats_ballistic_skill), Strength(stat_strength),
    Toughness(stat_toughness), Agility(stat_agility),Intelligence(stat_int),
    Perception(stat_perc), Fellowship(stat_fellowship), fatigue, and wounds. the 'Stats' are copied into the
    char_stats dictionary to make it easier to run through all the stats when making a stat check or test."""
    def __init__ (self, race, gender, firstname, lastname, stats_weapon_skill, stats_ballistic_skill, stat_strength, stat_tough, stat_agility, stat_int, stat_perc, stat_will_power, stat_fellowship, wounds):
        self.race = race
        self.racebonus = 0
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.Fullastname = firstname+" "+lastname
        self.char_stats = {'Weapon Skill':0,'Ballistic Skill':0,'Strength':0,'Toughness':0,'Agility':0,'Intelligence':0,'Perception':0,'Will Power':0,'Fellowship':0,}
        self.stats_weapon_skill = stats_weapon_skill
        self.stats_ballistic_skill = stats_ballistic_skill
        self.stat_strength = stat_strength
        self.stat_tough = stat_tough
        self.stat_agility = stat_agility
        self.stat_int = stat_int
        self.stat_perc = stat_perc
        self.stat_will_power = stat_will_power
        self.stat_fellowship = stat_fellowship
        self.char_stats['Weapon Skill'] = int(stats_weapon_skill)
        self.char_stats['Ballistic Skill'] = int(self.stats_ballistic_skill)
        self.char_stats['Strength'] = int(self.stat_strength)
        self.char_stats['Toughness'] = int(self.stat_tough)
        self.char_stats['Agility'] = int(self.stat_agility)
        self.char_stats['Intelligence'] = int(self.stat_int)
        self.char_stats['Perception'] = int(self.stat_perc)
        self.char_stats['Will Power'] = int(self.stat_will_power)
        self.char_stats['Fellowship'] = int(self.stat_fellowship)
        self.fatigue = 0
        self.wounds = wounds
        
   # def StatBuilder(racebonus):
   #     stat = int(random.randint(1,20+racebonus)
   #     return stat
    @classmethod
    def AutoMaker(cls, type):

        """AutoMaker method. 
        Automatic constructor. It just automatically builds a character object when called."""
        if type == "Human":
            race = 'human'
            racebonus = 25
        else:
            race = 'human'
            racebonus = 20
        #print(racebonus)
        #print(race)
        coinflip = random.randint(1,2)
        if coinflip == 1:
            gender = 'Male'
        else:
            gender = 'Female'
        stats_weapon_skill = int(random.randint(1,20)+racebonus)
        stats_ballistic_skill = int(random.randint(1,20)+racebonus)
        stat_strength = int(random.randint(1,20)+racebonus)
        stat_tough = int(random.randint(1,20)+racebonus)
        stat_agility = int(random.randint(1,20)+racebonus)
        stat_int = int(random.randint(1,20)+racebonus)
        stat_perc = int(random.randint(1,20)+racebonus)
        stat_will_power = int(random.randint(1,20)+racebonus)
        stat_fellowship = int(random.randint(1,20)+racebonus)
        wounds = random.randint(1,10)+18
        fatigue = 0
        if gender == 'Male':
            firstname = random.choice(HumanMaleNames)
        else:
            firstname = random.choice(HumanFemaleNames)
        lastname = random.choice(HumanLastNames)
#returns a character Object with the values generated and selected.
        return character(race, gender, firstname, lastname, stats_weapon_skill, stats_ballistic_skill, stat_strength, stat_tough, stat_agility, stat_int, stat_perc, stat_will_power, stat_fellowship, wounds)

    def character_sheet(self):
        """Character sheet Generation function. Outputs a charactersheet with the characteristics."""
        print(divider)
        print("Character Name: "+self.Fullastname+"    Character Race: "+self.race+"     Gender: "+self.gender)
        print("Character Wounds: "+str(self.wounds)+"         Character Fatigue: "+str(self.fatigue))
        print(divider)
        print(div_char)
        print(" WS:{WS}  BS:{BS}    S:{S}    T:{T}   Ag:{Ag}   Int:{Int}  Per:{Per}   WP:{WP}   Fel:{Fel}      ".format(WS=self.stats_weapon_skill, BS=self.stats_ballistic_skill, S=self.stat_strength , T=self.stat_tough , Ag=self.stat_agility, Int=self.stat_int,Per=self.stat_perc,WP=self.stat_will_power,Fel=self.stat_fellowship))
        print(divider)
        for skill in skills:
            print
        print(pageBreak)

#        print(spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill)+spacer+str(self.stats_weapon_skill))
class RogueTrader(character):
    race = 'human'
    racebonus = random.randint(20,28)
    def character_sheet(self):
        print('yes')
        #pass
    

class CharacterSkill(object):
    @classmethod
    def __init__ (cls, name, char, rank, descrip):
        """skill object. Not finished obviously.

    But the idea is to have a skill object with a name that would be a string(name), what characteristic
    from the character that skill tests on(char), an integer value of 0, 1, 2, or 3 to show the
    level of training if any a character has in that skill (rank), and a multi-line string for the
    description (descrip)."""
        self._name = name
        self._char = char
        self._rank = rank
        self._descrip = descrip
        self._skill = {"Name" : self._name, "Characteristic":self._char,"Rank":self._rank,"Description":self._descrip}
    
    def skill_output(self):
        print("Skill Name: "+self._name+"\nCharacteristic: "+self._char+"\nDescription: "+self._descrip)
    def skill_info(self):
        pass
    def SkillTest(self):
        pass
    """SkillTest is used when a character needs to perform a test against a skill.

    Um... nothing much more then that right now. In the game, you first determine if the skill
    is an advanced skill or not. If it is, you then see if you have training in that skill.
    Basically if it's a basic skill and you don't have any training in it, you test on the
    associated stat with a -20 modifier. If it's an advanced skill that you don't have
    training in you test with a 50% modifer. If you have training in it you test at the stat
    value, if you have mastered the skill (a 2 for training) you test with a +10 modifier"""
    
class CharacterSkillGroup(object):
    def __init__ (self, name, char, rank, topic, descrip):
        """skill object. Not finished obviously. This class is for skills that have multiple variations, for things like Pilot(civilian ground vehicles), Pilot(Atmospheric Vehicles) and Pilot(Void Craft)."""
        self._name = name
        self._char = char
        self._topic = topic
        self._rank = rank
        self._descrip = descrip
        self._skill = {"Name" : self._name, "Characteristic":self._char,"Topic":self._topic,"Rank":self._rank,"Description":self._descrip}

    def SkillTest(self):
        pass
    """SkillTest is used when a character needs to perform a test against a skill.

    Um... nothing much more then that right now. In the game, you first determine if the skill
    is an advanced skill or not. If it is, you then see if you have training in that skill.
    Basically if it's a basic skill and you don't have any training in it, you test on the
    associated stat with a -20 modifier. If it's an advanced skill that you don't have
    training in you test with a 50% modifer. If you have training in it you test at the stat
    value, if you have mastered the skill (a 2 for training) you test with a +10 modifier"""
    
class weapon(object):
    #just adding something to test git functionality
    """weapon class. Any sort of weapon used by a character.

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
    renown: a string denoting the renown level a character must have to purchase a weapon from the armory. """
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


