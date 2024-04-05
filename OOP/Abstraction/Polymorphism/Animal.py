class Animal:
    def __init__(self, name,legs):
        self.name = name
        self.legs = legs

    def makeNoise(self):
        print(f"{self.name} is making a strange noise")

class Dog(Animal):
    def __init__(self, name, legs, breed):
        super().__init__(name, legs)
        self.breed = breed
    
    @staticmethod
    def makeNoise(self):
        print("dog is barking")

class Bird(Animal):
    def __init__(self, name, legs, wingspan):
        super().__init__(name, legs)
        self.wingspan = wingspan
    
    def makeNoise(self):
        print("bird is tweeting")

class Snake(Animal):
    def __init__(self, name, legs, length):
        super().__init__(name, legs)
        self.length = length
    
    def hiss(self):
        super().makeNoise()


dog = Dog("Dog", 4, "German Shepherd")
dog.makeNoise(dog)
snake = Snake("Snake", 0, 5)
snake.hiss()
Dog.makeNoise(dog)