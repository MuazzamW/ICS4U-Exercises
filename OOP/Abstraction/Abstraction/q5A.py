class Account:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return 'Insufficient balance'
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def __str__(self):
        return f'Account Number: {self.__account_number}\nAccount Holder: {self.__account_holder}\nBalance: {self.__balance}'
    
if __name__ == "__main__":
    a1 = Account(123, 'John Doe', 1000)
    a2 = Account(456, 'Jane Doe', 5000)

    print(a1)
    print(a2)

    a1.deposit(500)
    print(a2.withdraw(100000))

    print(a1.get_balance())
    print(a2.get_balance())

    print(a1.get_account_number())
    print(a2.get_account_holder())
    
    print(a1)
    print(a2)