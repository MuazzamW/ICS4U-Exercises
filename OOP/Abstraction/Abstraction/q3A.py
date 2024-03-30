class Thingamajig:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def setX(self):
        x = int(input("Enter the value for x: "))
        self.__x = x
    def setY(self):
        y = int(input("Enter the value for y: "))
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __str__(self):
        return f"X: {self.__x}, Y: {self.__y}"
    
    
t = Thingamajig(1,2)

t.setX()
t.setY()

print(t)
