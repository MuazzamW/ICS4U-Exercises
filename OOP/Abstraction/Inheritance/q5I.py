class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def getArea(self):
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):
        return 2 * 3.14 * self.__radius
    
    def getRadoius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.__height = height

    def getVolume(self):
        return self.getArea() * self.__height

    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height

c1 = Cylinder(5, 10)
print(c1.getVolume())