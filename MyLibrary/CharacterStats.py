import random

class CharacterStats:

    weapon_skill = 0
    ballistic_skill = 0
    strength = 0
    toughness = 0
    agility = 0
    intelligence = 0
    perception = 0
    will_power = 0
    fellowship = 0
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