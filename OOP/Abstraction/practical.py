class Food:
    def __init__(self, name, price, fat, carbs, fiber):
        self.__name = name
        self.__price = price
        self.__fat = fat
        self.__carbs = carbs
        self.__fiber = fiber

    def __str__(self):
        return f"Name: {self.__name}, Price: ${self.__price:.2f}, Fat: {self.__fat}g, Carbs: {self.__carbs}g, Fiber: {self.__fiber}g"

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_fat(self):
        return self.__fat
    
    def get_carbs(self):
        return self.__carbs
    
    def get_fiber(self):
        return self.__fiber
    

class LunchOrder:
    def __init__(self):
        self.__burger = Food("Hamburgers", 1.85, 9, 33, 1)
        self.__salad = Food("Salads", 2.00, 1, 11, 5)
        self.__fries = Food("Fries", 1.30, 11, 36, 4)
        self.__soda = Food("Sodas", 0.95, 0, 38, 0)
        self.__total = 0
        self.__add_items()


    def __add_items(self):
        items = dir(self)
        items = [getattr(self,item) for item in items if item.startswith("_LunchOrder__")][1:]
        items.pop(len(items)-1)
        for item in items:
            print(item)
        for item in items:
            num = int(input(f"Enter the number of {item.get_name()} you want to order: "))
            self.__total += item.get_price() * num     
        
        print(f"Total: ${self.__total:.2f}")

order1 = LunchOrder()

