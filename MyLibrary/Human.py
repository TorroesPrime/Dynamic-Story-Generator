from MyLibrary.CharacterRace import CharacterRace


class HumanCharacter(CharacterRace):

    def __init__(self):
        self.name = "Human"
        self.bonus = 20