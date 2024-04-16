import tkinter as tk
import random

class Maze:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('maze game')
        
        #create frames to spilt 
        self.topframe = tk.Frame(self.window)
        self.bottomframe = tk.Frame(self.window)
        self.topframe.pack()
        self.bottomframe.pack()
        
        self.iconpaths = [ [1,4,4,3,4,4,4,4],
                           [3,3,4,3,3,4,3,4],
                           [3,4,4,4,4,4,3,4],
                           [4,4,3,3,3,3,4,4],
                           [3,4,4,4,4,4,4,2]
                          ]
        self.rows = len(self.iconpaths)
        self.columns = len(self.iconpaths[0])

        self.label_grid=[]
    
        for row in range(self.rows):
            for col in range(self.columns):
                self.image1 = tk.PhotoImage(file='GUI/bh'+str(self.iconpaths[row][col])+'.png')
                label = tk.Label(self.topframe,image=self.image1)
                label.image = self.image1 
                label.grid(row=row,column=col,padx=5,pady=5)
                
                self.label_grid.append(label)
        
        self.rightbutton = tk.Button(self.bottomframe,text='Right',command=lambda:self.right())
        self.rightbutton.pack(side='left')
        self.leftbutton = tk.Button(self.bottomframe,text='Left',command=lambda:self.left())
        self.leftbutton.pack(side='left')
        self.upbutton = tk.Button(self.bottomframe,text='Up',command=lambda:self.up())
        self.upbutton.pack(side='left')
        self.downbutton = tk.Button(self.bottomframe,text='Down',command=lambda:self.down())
        self.downbutton.pack(side='left')
        
        self.x=0
        self.y=0
        self.window.mainloop()
    def right(self):
        if self.x+1>=self.columns:
            print('Going off the board')
        elif self.iconpaths[self.y][self.x+1]==4:
            print('Moving right')
            self.image1=tk.PhotoImage(file='GUI/bh4.png')
            self.image2=tk.PhotoImage(file='GUI/bh1.png')
            self.label_grid[self.y*self.columns+self.x].config(image=self.image1)
            self.label_grid[self.y*self.columns+self.x].image = self.image1
            
            self.x=self.x+1
            self.label_grid[self.y*self.columns+self.x].config(image=self.image2)
            self.label_grid[self.y*self.columns+self.x].image = self.image2
            
        else:
            print('It is a wall')
            
    def left(self):
        if self.x-1<0:
            print('Going off the board')
        elif self.iconpaths[self.y][self.x-1] == 4:
            print('Moving left')
            self.image1 = tk.PhotoImage(file='GUI/bh4.png')
            self.image2 = tk.PhotoImage(file='GUI/bh1.png')
            self.label_grid[self.y*self.columns+self.x].config(image=self.image1)
            self.label_grid[self.y*self.columns+self.x].image = self.image1
            
            self.x = self.x - 1
            self.label_grid[self.y*self.columns+self.x].config(image=self.image2)
            self.label_grid[self.y*self.columns+self.x].image = self.image2
            
            
            
    def up(self):
        if self.y-1<0:
            print('Going off the board')
        elif self.iconpaths[self.y-1][self.x]==4:
            print('Moving up')
            self.image1 = tk.PhotoImage(file='GUI/bh4.png')
            self.image2 = tk.PhotoImage(file='GUI/bh1.png')
            self.label_grid[self.y*self.columns+self.x].config(image=self.image1)
            self.label_grid[self.y*self.columns+self.x].image = self.image1
            
            self.y = self.y - 1
            self.label_grid[self.y*self.columns+self.x].config(image=self.image2)
            self.label_grid[self.y*self.columns+self.x].image = self.image2        
            
    def down(self):
        if self.y+1>=self.rows:
            print('Going off the board')
        elif self.iconpaths[self.y+1][self.x]==4:
            print('Moving down')
            self.image1 = tk.PhotoImage(file='GUI/bh4.png')
            self.image2 = tk.PhotoImage(file='GUI/bh1.png')
            self.label_grid[self.y*self.columns+self.x].config(image=self.image1)
            self.label_grid[self.y*self.columns+self.x].image = self.image1
            
            self.y = self.y + 1
            self.label_grid[self.y*self.columns+self.x].config(image=self.image2)
            self.label_grid[self.y*self.columns+self.x].image = self.image2
            
        





m1 = Maze()