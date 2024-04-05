class Hero:

    def __init__(self, strength, dexterity, intelligence, health):
        self.__strength = strength
        self.__dexterity = dexterity
        self.__intelligence = intelligence
        self.__health = health

    def __str__(self):
        return self.__dict__.__str__()
    

class Warrior(Hero):

    def __init__(self, strength, dexterity, intelligence, endurance):
        super().__init__(strength, dexterity, intelligence)
        self.__endurance = endurance
    
    def attack(self):
        damageTaken = int(0.1(self.__endurance))
        print(f"Damage taken: {damageTaken}")
    
    def __str__(self) -> str:
        return super().__str__()


class Wizard(Hero):

    def __init__(self, strength, dexterity,   intelligence, focus):
        super().__init__(strength, dexterity, intelligence)
        self.__focus = focus

    def attack(self):
        damage = self.__strength + self.__focus//10
        print(damage)
    
    def __str__(self) -> str:
        return super().__str__()

w1 = Warrior(10, 5, 3, 7)

wiz = Wizard(3, 5, 10, 8)

print(w1)
print(wiz)