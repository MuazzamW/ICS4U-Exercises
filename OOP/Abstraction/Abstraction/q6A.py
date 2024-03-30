class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self):
        name = input("Enter the name: ")
        self.__name = name
    
    def set_phone(self):
        phone = input("Enter the phone number: ")
        self.__phone = phone
    
    def set_email(self):
        email = input("Enter the email: ")
        self.__email = email
    
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email
    
    def __str__(self):
        return f"Name: {self.__name}, Phone: {self.__phone}, Email: {self.__email}"
    

contacts = []

for i in range(5):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    contacts.append(Contact(name, phone, email))

def modify_contact():
    name = input("Enter the name of the contact you want to modify: ")
    for contact in contacts:
        if contact.get_name() == name:
            contact.set_name()
            contact.set_phone()
            contact.set_email()
            break
    else:
        print("Contact not found")

def display_contacts():
    for contact in contacts:
        print(contact)

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    for contact in contacts:
        if contact.get_name() == name:
            contacts.remove(contact)
            break
    else:
        print("Contact not found")

