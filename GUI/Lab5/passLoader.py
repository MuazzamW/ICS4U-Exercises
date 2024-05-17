import random

class passLoader:
    def __init__(self):
        self.__file = open('GUI/Lab5/password.txt','r')
        self.__passwords = []
        self.__search = []
        self.__names = []
        self.__associated = {}
        for line in self.__file:
            self.__search.append(line.strip().split()[0])
            self.__passwords.append(line.strip().split())
        self.__file.close()
    
        with open('GUI/Lab5/names.txt','r') as nameFile:
            next(nameFile)
            for line in nameFile:
                self.__names.append(line.strip())
            
            for name in self.__names:
                user = random.choice(self.__search)
                while user in self.__associated.values():
                    user = random.choice(self.__search)
                self.__associated[name] = user

        self.sortNames()
        self.writeNames()


    def getPassword(self, user):
        try:
            index = self.__search.index(user)
            return self.__passwords[index][1]
        except ValueError:
            return ValueError

    def associateNames(self):
        return self.__associated

    def sortNames(self):
        #sort dictionary by last name
        self.__associated = dict(sorted(self.__associated.items(), key=lambda item: item[0].split()[1]))
    
    def search(self, lastName):
        #search for last name
        for key, value in self.__associated.items():
            if key.split()[1] == lastName:
                return f"User: {key}, Username: {value}, Password: {self.getPassword(value)}\n"

    def writeNames(self):
        #create new file
        nameFile = open('GUI/Lab5/namesSorted.txt','w')
        for key, value in self.__associated.items():
            nameFile.write(f'{key}, {value}\n')
        nameFile.close()

if __name__ == "__main__":
    passLoader()