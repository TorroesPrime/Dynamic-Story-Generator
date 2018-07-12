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
class skill(object):
    def __init__ (self, name, stat, training, advCheck, descrip):
        """skill object. Not finished obviously.

    But the idea is to have a skill object with a name that would be a string(name), what stat
    from the character that skill tests on(stat), an integer value of 0, 1, or 2 to show the
    level of training if any a character has in that skill (training) a boolean value to
    determine if it is an advanced skill or not (advCheck), and a multi-line string for the
    description (descrip)."""
        self._name = name
        self._stat = stat
        self._training = training
        self._advCheck = advCheck
        self._descrip = descrip

    def skill_info(self):
        if self._stat == 'Stat_Strength':
            test_name = 'Strength'
        if self._training == 0:
            skill_training = 'Basic, untrained'
        elif self._training == 1:
            skill_training = 'Basic, trained'
        elif self._training == 2:
            skill_training = 'Advanced, trained'
        print('Skill: '+self._name+'\nTest on: '+test_name+'\nTraining: '+skill_training+'\nDescription: '+self._descrip)
    def SkillTest():
        pass
    """SkillTest is used when a character needs to perform a test against a skill.

    Um... nothing much more then that right now. In the game, you first determine if the skill
    is an advanced skill or not. If it is, you then see if you have training in that skill.
    Basically if it's a basic skill and you don't have any training in it, you test on the
    associated stat with a -20 modifier. If it's an advanced skill that you # you don't have
    training in you test with a 50% modifer. If you have training in it you test at the stat
    value, if you have mastered the skill (a 2 for training) you test with a +10 modifier"""
        
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
#character sheet just prints out the info of an instance.
    def CharSheet(self):
        """Character sheet function.

        This function outputs the stats and info for each character in their own sheet for reference or
        debugging"""
        print('Name:            '+self.name)
        print('Weapon Skill:    '+str(self.Stat_WS))
        print('Ballistic Skill: '+str(self.Stat_BS))
        print('Strength:        '+str(self.Stat_Tough))
        print('Agility:         '+str(self.Stat_Agility))
        print('Intelligence:    '+str(self.Stat_Int))
        print('Perception:      '+str(self.Stat_Perc))
        print('Will Power:      '+str(self.Stat_WP))
        print('Fellowship:      '+str(self.Stat_Fell))
        print('*'*75)
        
    #def Test(self, checked):
    #    if checked in self.Char_Stats:
    #        roll = random.randint(1, 100)
    #        if self.Char_Stats[checked] > roll or roll == 1:
    #            DoS= (self.Char_Stats[checked]-roll)%10
    #            print("{} succeeded their {} check with a {} and got {} degrees of success!".format(self.name, checked, roll, DoS))
    #            return 
    #        else:
    #            print("{} failed their {} check with a {}...".format(self.name, checked, roll))
    #    else:
    #            print("{} doesn't have that stat.  Check your typos.".format(self.name))
    #@property
    def StatTest(self, checked, degree, output):
        """StatTest Docstring

        This is a function used to test against a given character stat. The first variable
        'checked' is the stat to be tested, called by name. The second is the degree of
        difficulty for the test, a positive or negative number ranging from -60 to 60. The
        last variable is a boolean value that controls whether the function outputs
        additional material used for testing. when a test against a stat is made (say a
        character tried to shoot at a target) the StatTest function is called and passed
        the appropriate stat to be tested and the degree of difficulty. In this case,
        the ballistic skill stat is tested, and it's an easy shot, so the degree is 10.
        The characters Stat_BS plus 10 is compared to the result of a
        random.randint(1,100). If the result is higher the test is failed. if the result
        is lower the test is passed. If it is passed how much it passed by may be needed
        to be known. The difference between the result and the combination of the stat
        and modifier is modulated by ten and that result set to DoS. The result of the
        check and the DoS is then returned."""
        statResult =[]
        DoS = 0
        check = False
        if checked in self.Char_Stats:
            roll = random.randint(1, 100)
            if output == True:
                print("+++{} is attempting a {} check. Using their base value of {} with a modifer of {}.".format(self.name, checked, self.Char_Stats[checked], degree))
                print('+++The roll resulted in a {}.'.format(roll))
            value = self.Char_Stats[checked]+int(degree)
            if value > roll or roll == 1:
                DoS= int((value-roll)/10)
                if output == True:
                    print("+++{} succeeded their {} check with a {} and got {} degrees of success!".format(self.name, checked, roll, DoS))
                    print("===================end of skill check===================")
                check = True
                statResult.append(check)
                statResult.append(DoS)
                #print(check)
                #print(DoS)
                return statResult
                
            else:
                if output == True:
                    print("+++{} failed their {} check with a {}...".format(self.name, checked, roll))
                    print('===================end of skill check===================')
                check = False
                statResult.append(check)
                statResult.append(DoS)
                #print(check)
                #print(DoS)
                #return self.DoS self.StatTest
                return DoS, statResult
                
                #return statResult
                
        else:
                print("{} doesn't have that stat.  Check your typos.".format(self.name))
        
        #return self.DoS self.StatTest
        return DoS, StatTest
    
    def StatBuilder(raceBonus):
        """StatBuilder function

        Rather then having int(random.randint(1,20)+raceBonus) for each stat,
        This method will generate the stat each time it is called, returning
        the integar in stat."""
        stat = int(random.randint(1,20)+raceBonus)
        return stat
    
    def AutoMaker(type):
        """AutoMaker method

        Automatic constructor. It just automatically builds an object when called.
        So far only implimented for SpaceMarine type characters."""
        if type =="SpaceMarine":
            raceBonus = 30
#SpaceMarine have a bonus of 30 to their rolled stats.
            chapter = random.choice(chapters)
#randomly selects a chapter from the chapters list in library
            if chapter == 'Blood Angel':
                name = random.choice(names_BloodAngels)
#if chapter == Blood Angel, randomly select a name from the names_BloodAngels list in library
            elif chapter == 'Ultramarine':
                name = random.choice(names_Ultramarines)
#if chapter == Ultramarine, randomly select a name from the names_Ultramarines list in library
            elif chapter == 'Black Templar':
                name = random.choice(names_BlackTemplar)
#if chapter == Black Templar, randomly select a name from the names_BlackTemplar list in library
            elif chapter == 'Space Wolve':
                name = random.choice(names_SpaceWolves)
#if chapter == Space Wolve, randomly select a name from the names_SpaceWolves list in library
            elif chapter == 'Dark Angel':
                name = random.choice(names_DarkAngels)
#if chapter == Space Wolve, randomly select a name from the names_SpaceWolves list in library
            Stat_WS = Character.StatBuilder(raceBonus)
            Stat_BS = Character.StatBuilder(raceBonus)
            Stat_Strength = Character.StatBuilder(raceBonus)
            Stat_Tough = Character.StatBuilder(raceBonus)
            Stat_Agility = Character.StatBuilder(raceBonus)
            Stat_Int = Character.StatBuilder(raceBonus)
            Stat_Perc = Character.StatBuilder(raceBonus)
            Stat_WP = Character.StatBuilder(raceBonus)
            Stat_Fell = Character.StatBuilder(raceBonus)
#each of the stats is just an integer.
            if chapter == 'Black Templar':
                role = random.choice(bt_roles)
#if chapter == Black Templar, then randomly select a role from the bt_roles list in library
            elif chapter == 'Space Wolve':
                role = random.choice(sw_roles)
#if chapter == Space Wolve, then randomly select a role from the sw_roles list in library
            else:
                role = random.choice(sm_roles)
#otherwise just use SM_roles
            role = random.choice(sm_roles)
            Years_SM = random.randint(1,100)
            Years_DW = random.randint(1,30)
            if Years_DW > Years_SM:
                Years_DW = random.randint(1,30)
            wounds = random.randint(1,10)+18
#returns a spaceMarineObject with the values generated and selected. 
            return SpaceMarine(name,Stat_WS,Stat_BS,Stat_Strength,Stat_Tough,Stat_Agility,Stat_Int,Stat_Perc,Stat_WP,Stat_Fell,chapter,role, Years_SM, Years_DW, wounds)
        

class SpaceMarine(Character):
    """the SpaceMarine character object class

        Inherits most of it's methods from the character class"""
    def __init__(self, name, Stat_WS, Stat_BS, Stat_Strength, Stat_Tough, Stat_Agility, Stat_Int, Stat_Perc, Stat_WP, Stat_Fell, chapter, role, Years_SM, Years_DW, wounds):
        self.raceBonus = 30
        self.chapter = chapter
        self.role = role
        self.name = name
        self.Char_Stats = {'WS':0,'Ballistic Skill':0,'Strength':0,'Toughness':0,'Agility':0,'Intelligence':0,'Perception':0,'Will Power':0,'Fellowship':0,}
        self.Stat_WS = Stat_WS
        self.Stat_BS = Stat_BS
        self.Stat_Strength = Stat_Strength
        self.Stat_Tough = Stat_Tough
        self.Stat_Agility = Stat_Agility
        self.Stat_Int = Stat_Int
        self.Stat_Perc = Stat_Perc
        self.Stat_WP = Stat_WP
        self.Stat_Fell = Stat_Fell
        self.Years_SM = Years_SM
        self.Years_DW = Years_DW
        self.wounds = wounds
        self.DoS = 0
        #self.StatTest = False
        self.Char_Stats['Weapon Skill'] = int(Stat_WS)
        self.Char_Stats['Ballistic Skill'] = int(self.Stat_BS)
        self.Char_Stats['Strength'] = int(self.Stat_Strength)
        self.Char_Stats['Toughness'] = int(self.Stat_Tough)
        self.Char_Stats['Agility'] = int(self.Stat_Agility)
        self.Char_Stats['Intelligence'] = int(self.Stat_Int)
        self.Char_Stats['Perception'] = int(self.Stat_Perc)
        self.Char_Stats['Will Power'] = int(self.Stat_WP)
        self.Char_Stats['Fellowship'] = int(self.Stat_Fell)
        self.armor_array = {'Head':0,'Shoulder_r':0,'Shoulder_l':0,'Arm_r':0,'Arm_l':0,'Torso':0,'Leg_r':0,'Leg_l':0,'Powerplant':0}

    def CharSheet(self):
        
        print('Name:            '+self.name)
        print('Chapter:         '+self.chapter)
        print('Role:            '+self.role)
        print('Weapon Skill:    '+str(self.Stat_WS))
        print('Ballistic Skill: '+str(self.Stat_BS))
        print('Strength:        '+str(self.Stat_Tough))
        print('Agility:         '+str(self.Stat_Agility))
        print('Intelligence:    '+str(self.Stat_Int))
        print('Perception:      '+str(self.Stat_Perc))
        print('Will Power:      '+str(self.Stat_WP))
        print('Fellowship:      '+str(self.Stat_Fell))
        print('Wounds:          '+str(self.wounds))
        print('Years as a Space Marine: '+str(self.Years_SM))
        print('Years as Death Watch:    '+str(self.Years_DW))
        print('====================Character Skills====================')
        print('='*56)
        #print(self.Char_skills)
        #for k, v in self.Char_skills.items():
        #    print(k,": ", "[X]"*v)
        #for key in self.Char_skills:
        #    print(str(self.Char_skills[key])+str(self.Char_skills[val]))
        
      

class planet(object):
#planet object.
    def __init__ (self, name, population, tithe, compliance, demography, gov_type, governor,adept,military,trade,codex):
        self.name = name
        self.population = population
        self.tithe=tithe
        self.compliance=compliance
        self.demography=demography
        self.gov_type=gov_type
        self.governor = governor
        self.adept = adept
        self.military = military
        self.trade = trade
        self.codex = codex

class weapon(object):
#weapon object.    
    def __init__ (self, name, weap_type, weap_range, RoF, Damage, Penetration, clip, weight):
        self.name = name
        self.weap_type = weap_type
        self.weap_range = weap_range
        self.RoF = RoF
        self.Damage = Damage
        self.clip = clip
        self.weight = weight
        
