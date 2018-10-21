class CharacterSkill:
    name = None
    char = None
    rank = None
    description = None
    skill = None

    def __init__(self, name, char, rank, descrip):
        """skill object. Not finished obviously.

    But the idea is to have a skill object with a name that would be a string(name), what characteristic
    from the Character that skill tests on(char), an integer value of 0, 1, 2, or 3 to show the
    level of training if any a Character has in that skill (rank), and a multi-line string for the
    description (descrip)."""

        self.name = name
        self.char = char
        self.rank = rank
        self.descrip = descrip
        self.skill = {"Name": self.name, "Characteristic": self.char, "Rank": self.rank,
                       "Description": self.descrip}

    def skill_output(self):
        print("Skill Name: " + self._name + "\nCharacteristic: " + self._char + "\nDescription: " + self._descrip)

    def skill_info(self):
        pass

    def SkillTest(self):
        pass

    """SkillTest is used when a Character needs to perform a test against a skill.

    Um... nothing much more then that right now. In the game, you first determine if the skill
    is an advanced skill or not. If it is, you then see if you have training in that skill.
    Basically if it's a basic skill and you don't have any training in it, you test on the
    associated stat with a -20 modifier. If it's an advanced skill that you don't have
    training in you test with a 50% modifer. If you have training in it you test at the stat
    value, if you have mastered the skill (a 2 for training) you test with a +10 modifier"""

