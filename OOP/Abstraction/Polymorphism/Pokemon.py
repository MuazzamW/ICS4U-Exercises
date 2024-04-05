class Pokemon:
    def __init__(self, name, level,type):
        self.name = name
        self.level = level
        self.hp = level * 10
        self.type = type

    def __repr__(self):
        return "Pokemon: {name}, Level: {level}, HP: {hp}".format(name=self.name, level=self.level, hp=self.hp)

    def opponent(self):
        return "Opponent: {name}, Level: {level}, HP: {hp}".format(name=self.name, level=self.level, hp=self.hp)

    def lose_health(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def gain_health(self, heal):
        self.hp += heal

    def attack(self, opponent):
        damage = 10
        opponent.lose_health(damage)
    
class Pikachu(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Electric")
    
    def attack(self, opponent):
        damage = 10
        opponent.lose_health(damage)
        print("Pikachu used Thunderbolt")
    
    def specialAttack(self, opponent):
        damage = 20
        opponent.lose_health(damage)
        print("Pikachu used Thunder")
    
class Charmander(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Fire")
    
    def attack(self, opponent):
        damage = 10
        opponent.lose_health(damage)
        print("Charmander used Ember")
    
    def specialAttack(self, opponent):
        damage = 20
        opponent.lose_health(damage)
        print("Charmander used Fire Blast")

class Squirtle(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, "Water")
    
    def attack(self, opponent):
        damage = 10
        opponent.lose_health(damage)
        print("Squirtle used Water Gun")
    
    def specialAttack(self, opponent):
        damage = 20
        opponent.lose_health(damage)
        print("Squirtle used Hydro Pump")