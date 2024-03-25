class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def reduce(self):
        gcd = self.__gcd(self.num, self.den)
        self.num = self.num // gcd
        self.den = self.den // gcd

    def __gcd(self, a, b):
        if b == 0:
            return a
        return self.__gcd(b, a % b)
    
    def setNum(self):
        num = int(input("Enter the numerator: "))
        self.num = num
    
    def setDen(self):
        den = int(input("Enter the denominator: "))
        self.den = den

    def __str__(self):
        self.reduce()
        return f"{self.num}/{self.den}"
    

if __name__ == "__main__":
    f1 = Fraction(12, 24)
    f2 = Fraction(1, 2)

    print(f1)
    print(f2)

    f1.reduce()
    f2.reduce()
    
    f1.setNum()
    f1.setDen()

    f2.setNum()
    f2.setDen()

    print(f1)
    print(f2)