import tkinter as tk
import passLoader

class Window(tk.Tk):
    
    def __init__(self):
      super().__init__()

      self.title("Window")
      self.resizable(False, False)


class pass_lookup(Window):
    def __init__(self):
      super().__init__()
      self.title("pass_lookup")
      self.__passLoader = passLoader.passLoader()

      #declare labels
      self.userLabel = tk.Label(self, text="Enter the user name")
      self.passLabel = tk.Label(self, text="Enter the Password")

      #declare entry
      self.userName = tk.Entry(self, width=10)
      self.passWord = tk.Entry(self, width=10)

      #declare button
      self.loginButton = tk.Button(self, text="login", command=lambda: self.check_login(self.userName.get(), self.passWord.get()))
      self.passLookupButton = tk.Button(self, text="Pass Lookup", command = self.consoleLookup)
      self.searchByLastName = tk.Button(self, text="Search by Last Name", command = self.searchByLastName)

      #grid layout
      self.userLabel.grid(row=0, column=0)
      self.passLabel.grid(row=1, column=0)
      
      self.userName.grid(row=0, column=1)
      self.passWord.grid(row=1, column=1)
      
      self.loginButton.grid(row=2, column=0)
      self.passLookupButton.grid(row=3, column=0)
      self.searchByLastName.grid(row=4, column=0)

    def searchByLastName(self):
        #open new window
        search = tk.Tk()
        search.title('Search')

        #declare labels
        searchLabel = tk.Label(search, text='Enter the last name to search for')
        searchLabel.pack()

        #declare entry
        searchEntry = tk.Entry(search, width=10)
        searchEntry.pack()

        #declare button
        searchButton = tk.Button(search, text='Search', command=lambda: self.search(searchEntry.get()))
        searchButton.pack()

        search.mainloop()

    def search(self, lastName):
        #open new window
        result = tk.Tk()
        result.title('Result')

        #declare label
        resultLabel = tk.Label(result, text=self.__passLoader.search(lastName))
        print(self.__passLoader.search(lastName))
        resultLabel.pack()

        result.mainloop()

    def check_login(self, user, password):
        if self.__passLoader.getPassword(user) == password:
            print('Login Successful')
            #open new window
            success = tk.Tk()
            success.title('Success')

            #successLabel
            successLabel = tk.Label(success, text='Login Successful')
            successLabel.pack()

            success.mainloop()

        else:
            print('Login Failed')

            #open new window
            failed = tk.Tk()
            failed.title('Failed')

            #failedLabel
            failedLabel = tk.Label(failed, text='Login Failed, user not found or password incorrect')
            failedLabel.pack()

            failed.mainloop()

    def consoleLookup(self):
       user = ''
       user = input('Enter a user name or type quit to exit: ')
       while user!='quit':
          
          password = self.__passLoader.getPassword(user)
          if password != ValueError:
              print(f'The password for {user} is {password}')
          else:
              print("User not found!")
          user = input('Enter a user name or type quit to exit: ')

    def getNames(self):
        return self.__passLoader.associateNames()

if __name__ == "__main__":
    app = pass_lookup()
    print(app.getNames())
    app.mainloop()
