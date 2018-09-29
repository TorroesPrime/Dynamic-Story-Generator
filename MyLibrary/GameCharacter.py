import random


class GameCharacter:
    """
    GameCharacter class.

    The basic Character class. Each Character has a string for their name (name), 10 basic characteristics
    including Weapon Skill (stats_weapon_skill), Ballistic skill (stats_ballistic_skill), Strength(stat_strength),
    Toughness(stat_toughness), Agility(stat_agility),Intelligence(stat_int),
    Perception(stat_perc), Fellowship(stat_fellowship), fatigue, and wounds. the 'Stats' are copied into the
    char_stats dictionary to make it easier to run through all the stats when making a stat check or test.
    """

    def __init__(self, race, gender, firstname, lastname, stats_weapon_skill, stats_ballistic_skill, stat_strength,
                 stat_tough, stat_agility, stat_int, stat_perc, stat_will_power, stat_fellowship, wounds):
        self.race = race
        self.race_bonus = 0
        self.gender = gender
        self.first_name = firstname
        self.last_name = lastname
        self.full_name = firstname + " " + lastname
        self.char_stats = {'Weapon Skill': 0, 'Ballistic Skill': 0, 'Strength': 0, 'Toughness': 0, 'Agility': 0,
                           'Intelligence': 0, 'Perception': 0, 'Will Power': 0, 'Fellowship': 0, }
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

    # def StatBuilder(race_bonus):
    #     stat = int(random.randint(1,20+racebonus)
    #     return stat

    def AutoMaker(self, character_type):

        """AutoMaker method.
        Automatic constructor. It just automatically builds a Character object when called."""
        if character_type == "Human":
            race = 'human'
            race_bonus = 25
        else:
            race = 'human'
            race_bonus = 20
        # print(race_bonus)
        # print(race)
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            gender = 'Male'
        else:
            gender = 'Female'
        stats_weapon_skill = int(random.randint(1, 20) + race_bonus)
        stats_ballistic_skill = int(random.randint(1, 20) + race_bonus)
        stat_strength = int(random.randint(1, 20) + race_bonus)
        stat_tough = int(random.randint(1, 20) + race_bonus)
        stat_agility = int(random.randint(1, 20) + race_bonus)
        stat_int = int(random.randint(1, 20) + race_bonus)
        stat_perc = int(random.randint(1, 20) + race_bonus)
        stat_will_power = int(random.randint(1, 20) + race_bonus)
        stat_fellowship = int(random.randint(1, 20) + race_bonus)
        wounds = random.randint(1, 10) + 18
        fatigue = 0
        if gender == 'Male':
            firstname = random.choice(HumanMaleNames)
        else:
            firstname = random.choice(HumanFemaleNames)
        lastname = random.choice(HumanLastNames)
        # returns a Character Object with the values generated and selected.
        return GameCharacter(race, gender, firstname, lastname, stats_weapon_skill, stats_ballistic_skill, stat_strength,
                             stat_tough, stat_agility, stat_int, stat_perc, stat_will_power, stat_fellowship, wounds)

    def character_sheet(self):
        """Character sheet Generation function. Outputs a charactersheet with the characteristics."""
        print(divider)
        print(
            "Character Name: " + self.full_name + "    Character Race: " + self.race + "     Gender: " + self.gender)
        print("Character Wounds: " + str(self.wounds) + "         Character Fatigue: " + str(self.fatigue))
        print(divider)
        print(div_char)
        print(" WS:{WS}  BS:{BS}    S:{S}    T:{T}   Ag:{Ag}   Int:{Int}  Per:{Per}   WP:{WP}   Fel:{Fel}      ".format(
            WS=self.stats_weapon_skill, BS=self.stats_ballistic_skill, S=self.stat_strength, T=self.stat_tough,
            Ag=self.stat_agility, Int=self.stat_int, Per=self.stat_perc, WP=self.stat_will_power,
            Fel=self.stat_fellowship))
        print(divider)
        for skill in skills:
            print
        print(pageBreak)