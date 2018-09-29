class CharacterStats:

    weapon_skill = None
    ballistic_skill = None
    strength = None
    toughness = None
    agility = None
    intelligence = None
    perception = None
    will_power = None
    fellowship = None
    race_bonus = 0

    def __init__(self):
        pass

    def getRandomStatvalue(self):
        return int(random.randint(1, 20) + self.race_bonus)

    def randomizeMe(self):
        self.weapon_skill = self.getRandomStatvalue()
        self.ballistic_skill = self.getRandomStatvalue()
        self.strength = self.getRandomStatvalue()
        self.toughness = self.getRandomStatvalue()
        self.agility = self.getRandomStatvalue()
        self.intelligence = self.getRandomStatvalue()
        self.perception = self.getRandomStatvalue()
        self.will_power = self.getRandomStatvalue()
        self.fellowship = self.getRandomStatvalue()
        self.race_bonus = self.getRandomStatvalue()