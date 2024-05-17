import app as a
import sqlite3

MENU_PROMPT = """-- Coffee Bean App --
Please choose from the following options:
1) add a new bean
2) see all beans
3) find a bean by name

Your selection: """

def menu():
    connection = sqlite3.connect('data.db')
    a.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "4":
        if user_input == "1":
            name = input("Enter bean name: ")
            method = input("Enter how you've prepared it: ")
            rating = int(input("Enter your rating score: "))

            a.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = a.get_all_beans(connection)
            for bean in beans:
                print(bean)
                #print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == "3":
            name = input("Enter bean name to find: ")
            beans = a.get_beans_by_name(connection, name)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == "4":
            break


menu()