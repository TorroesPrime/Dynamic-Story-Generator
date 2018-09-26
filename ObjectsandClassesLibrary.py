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
    including Weapon Skill (Stat_WS), Ballistic skill (Stat_BS), Strength(Stat_Strength),
    Toughness(Stat_Toughness), Agility(Stat_Agility),Intelligence(Stat_Int),
    Perception(Stat_Perc), Fellowship(Stat_Fell), fatigue, and wounds. the 'Stats' are copied into the
    Char_Stats dictionary to make it easier to run through all the stats when making a stat check or test."""
    def __init__ (self, race, gender, Fname, Lname, Stat_WS, Stat_BS, Stat_Strength, Stat_Tough, Stat_Agility, Stat_Int, Stat_Perc, Stat_WP, Stat_Fell, wounds):
        self.race = race
        self.raceBonus = 0
        self.gender = gender
        self.Fname = Fname
        self.Lname = Lname
        self.FullName = Fname+" "+Lname
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
        self.fatigue = 0
        self.wounds = wounds
        
   # def StatBuilder(racebonus):
   #     stat = int(random.randint(1,20+raceBonus)
   #     return stat
    @classmethod
    def AutoMaker(type):

        """AutoMaker method. 
        Automatic constructor. It just automatically builds a character object when called."""
        if type == "Human":
            race = 'human'
            raceBonus = 25
        else:
            race = 'human'
            raceBonus = 20
        #print(raceBonus)
        #print(race)
        coinflip = random.randint(1,2)
        if coinflip == 1:
            gender = 'Male'
        else:
            gender = 'Female'
        Stat_WS = int(random.randint(1,20)+raceBonus)
        Stat_BS = int(random.randint(1,20)+raceBonus)
        Stat_Strength = int(random.randint(1,20)+raceBonus)
        Stat_Tough = int(random.randint(1,20)+raceBonus)
        Stat_Agility = int(random.randint(1,20)+raceBonus)
        Stat_Int = int(random.randint(1,20)+raceBonus)
        Stat_Perc = int(random.randint(1,20)+raceBonus)
        Stat_WP = int(random.randint(1,20)+raceBonus)
        Stat_Fell = int(random.randint(1,20)+raceBonus)
        wounds = random.randint(1,10)+18
        fatigue = 0
        if gender == 'Male':
            Fname = random.choice(HumanMaleNames)
        else:
            Fname = random.choice(HumanFemaleNames)
        Lname = random.choice(HumanLastNames)
#returns a character Object with the values generated and selected.
        return character(race, gender, Fname, Lname, Stat_WS, Stat_BS, Stat_Strength, Stat_Tough, Stat_Agility, Stat_Int, Stat_Perc, Stat_WP, Stat_Fell, wounds)

    def character_sheet(self):
        """Character sheet Generation function. Outputs a charactersheet with the characteristics."""
        print(divider)
        print("Character Name: "+self.FullName+"    Character Race: "+self.race+"     Gender: "+self.gender)
        print("Character Wounds: "+str(self.wounds)+"         Character Fatigue: "+str(self.fatigue))
        print(divider)
        print(div_char)
        print(" WS:{WS}  BS:{BS}    S:{S}    T:{T}   Ag:{Ag}   Int:{Int}  Per:{Per}   WP:{WP}   Fel:{Fel}      ".format(WS=self.Stat_WS, BS=self.Stat_BS, S=self.Stat_Strength , T=self.Stat_Tough , Ag=self.Stat_Agility, Int=self.Stat_Int,Per=self.Stat_Perc,WP=self.Stat_WP,Fel=self.Stat_Fell))
        print(divider)
        for skill in skills:
            print
        print(pageBreak)

#        print(spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS)+spacer+str(self.Stat_WS))
class RogueTrader(character):
    race = 'human'
    raceBonus = random.randint(20,28)
    def character_sheet(self):
        print('yes')
        #pass
    

class CharacterSkill(object):
    @classmethod
    def __init__ (self, name, char, rank, descrip):
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


