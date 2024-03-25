class Widget:
    def __init__(self,color = "black",price = 0):
        self.__color = color
        self.__price = price

    def setColor(self):
        colour = input("Enter the color of the widget: ")
        self.__color = colour
    
    def setPrice(self):
        price = int(input("Enter the price of the widget: "))
        self.__price = price

    def getColor(self):
        return self.__color
    
    def getPrice(self):
        return self.__price
    
    def __str__(self):
        return f"Color: {self.__color}, Price: {self.__price}"

if __name__ == "__main__":
    w1 = Widget()
    w2 = Widget("Blue", 20)

    print(w1)
    print(w2)

    w1.setColor()
    w1.setPrice()

    w2.setColor()
    w2.setPrice()

    print(w1.getColor())
    print(w1.getPrice())

    print(w2.getColor())
    print(w2.getPrice())
    

