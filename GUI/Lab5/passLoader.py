class passLoader:
    def __init__(self):
        self.__file = open('GUI/Lab5/password.txt','r')
        self.__passwords = []
        self.__search = []
        for line in self.__file:
            self.__search.append(line.strip().split()[0])
            self.__passwords.append(line.strip().split())
        self.__file.close()
    
    def getPassword(self, user):
        try:
            index = self.__search.index(user)
            return self.__passwords[index][1]
        except ValueError:
            print('User not found')
            return ValueError
if __name__ == "__main__":
    passLoader()