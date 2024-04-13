import tkinter as tk


class Window(tk.Tk):
    
    def __init__(self):
      super().__init__()

      self.title("Window")
      self.resizable(False, False)


class mark_calculator(Window):
    def __init__(self):
      super().__init__()
      self.title("Mark Calculator")

      #declare labels
      self.label1 = tk.Label(self, text="Enter the score for test 1")
      self.label2 = tk.Label(self, text="Enter the score for test 2")
      self.label3 = tk.Label(self, text="Enter the score for test 3")
      self.averageLabel = tk.Label(self, text="Average")
      self.averageLabel2 = tk.Label(self, text="")

      #declare entry
      self.entry1 = tk.Entry(self, width=10)
      self.entry2 = tk.Entry(self, width=10)
      self.entry3 = tk.Entry(self, width=10)

      #declare button
      self.averageButton = tk.Button(self, text="Calculate Average", command=lambda: self.calculate_average(int(self.entry1.get()), int(self.entry2.get()), int(self.entry3.get())))
      self.quitButton = tk.Button(self, text="Quit", command=self.quit)

      #grid layout
      self.label1.grid(row=0, column=0)
      self.entry1.grid(row=0, column=1)

      self.label2.grid(row=1, column=0)
      self.entry2.grid(row=1, column=1)

      self.label3.grid(row=2, column=0)
      self.entry3.grid(row=2, column=1)

      self.averageLabel.grid(row=3, column=0)
      self.averageLabel2.grid(row=3, column=1)


      self.averageButton.grid(row=4, column=0)
      self.quitButton.grid(row=4, column=1)


    def calculate_average(self,*args):
      print(args)
      for arg in args:
        if not isinstance(arg, int):
          #error message
          return "Error: Please enter a number"
      test1, test2, test3 = map(int, args)
      average = (test1 + test2 + test3) / len(args)
      self.averageLabel2.config(text=f"{average:.2f}")
      print(average)

    def quit(self):
      self.destroy()        


if __name__ == "__main__":
    app = mark_calculator()
    app.mainloop()
