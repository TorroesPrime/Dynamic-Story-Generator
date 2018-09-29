class CharacterSkillGroup:
    name = None
    char = None
    rank = None
    topic = None
    description = None

    def __init__(self, name, char, rank, topic, description):

        """
        skill object. Not finished obviously. This class is for skills that have multiple variations,
        for things like Pilot(civilian ground vehicles), Pilot(Atmospheric Vehicles) and Pilot(Void Craft).
        """

        self.name = name
        self.char = char
        self.topic = topic
        self.rank = rank
        self.description = description
        self.skill = {"Name" : self.name, "Characteristic":self.char,"Topic":self.topic,"Rank":self.rank,"Description":self.description}

    def SkillTest(self):
        pass
    """SkillTest is used when a Character needs to perform a test against a skill.

    Um... nothing much more then that right now. In the game, you first determine if the skill
    is an advanced skill or not. If it is, you then see if you have training in that skill.
    Basically if it's a basic skill and you don't have any training in it, you test on the
    associated stat with a -20 modifier. If it's an advanced skill that you don't have
    training in you test with a 50% modifer. If you have training in it you test at the stat
    value, if you have mastered the skill (a 2 for training) you test with a +10 modifier"""