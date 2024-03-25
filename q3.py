import random
class Monster:

    __types = ["Goblin", "Orc", "Imp"]
    __life = range(10,21)
    __otherAttributes = range(7,13)

    def __init__(self):
        self.type = random.choice(type(self).__types)
        self.life = random.choice(type(self).__life)
        self.strength = random.choice(type(self).__otherAttributes)
        self.agility = random.choice(type(self).__otherAttributes)
        self.skill = random.choice(type(self).__otherAttributes)
        self.luck = random.choice(type(self).__otherAttributes)

    def __str__(self):
        return f"Type - {self.type} - Life: {self.life}, Strength: {self.strength}, Agility: {self.agility}, Skill: {self.skill}, Luck: {self.luck}"
    

if __name__ == "__main__":
    m1 = Monster()
    m2 = Monster()
    m3 = Monster()
    