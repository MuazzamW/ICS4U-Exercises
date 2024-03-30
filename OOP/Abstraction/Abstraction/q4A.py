class Lightbulb:
    def __init__(self,state = "off"):
        self.__state = state
    
    def toggle(self):
        if self.__state == "on":
            self.__state = "off"
        else:
            self.__state = "on"
        self.display()
    
    def display(self):
        print(f"The lightbulb is {self.__state}")

l = Lightbulb()
l.toggle()
l.toggle()