class Animal:
    def __init__(self, name,legs):
        self.name = name
        self.legs = legs

class Dog(Animal):
    def __init__(self, name, legs, breed):
        super().__init__(name, legs)
        self.breed = breed
    
    def bark(self):
        print(f"The {self.legs}-legged {self.name} barks.")

class Bird(Animal):
    def __init__(self, name, legs, wingspan):
        super().__init__(name, legs)
        self.wingspan = wingspan
    
    def tweet(self):
        print(f"The {self.legs}-legged {self.name} tweets.")

class Snake(Animal):
    def __init__(self, name, legs, length):
        super().__init__(name, legs)
        self.length = length
    
    def hiss(self):
        print(f"The {self.legs}-legged {self.name} hisses.")


dog = Dog("Dog", 4, "German Shepherd")
dog.bark()