import tkinter as tk

#create window
main_window = tk.Tk()
#title
main_window.title('Profile Entry')
#size of window
main_window.geometry('500x300')

#create image
image1 = tk.PhotoImage(file = 'GUI/profile.gif')
#returns new photo image based on image1 by factor of x,y pixels
small_image = image1.subsample(4,4)

#create intro text label
img = tk.Label(main_window, image = small_image)
img.grid(row=0,column=0,rowspan=6,padx=5,pady=5)

enter_info = tk.Label(main_window,text='Please Enter your information',bg='lightgrey')
enter_info.grid(row=0,column=1,columnspan=4,padx=5,pady=5)

#name label
name_l = tk.Label(main_window,text='Name',bg='lightgrey')
name_l.grid(row=1,column=1,padx=5,pady=5)

#name textbox
name_t = tk.Entry(main_window,width=20)
name_t.grid(row=1,column=2,padx=5,pady=5)

#Create variables to store values retrieved from the menu button
item1 = tk.StringVar()
item2 = tk.StringVar()
item3 = tk.StringVar()
item4 = tk.StringVar()

#create a drop down menu
gender = tk.Menubutton(main_window,text='Gender')
gender.grid(row=2,column=2,padx=5,pady=5)

gender_value=''
def get_checked():
  global gender_value
  gender_value = item1.get()
  if gender_value =='1':
    gender_value='Male'
  elif gender_value=='2':
    gender_value=='Female'
  elif gender_value == '3':
    gender_value = 'Other'
  else:
    gender_value = 'Rather Not Say'


#new way to make drop down menu
# gender.menu.add_checkbutton(label='Male',variable=item1,command = get_checked)
# gender.menu.add_checkbutton(label='Female',variable=item2,command = get_checked)
# gender.menu.add_checkbutton(label='Other',variable=item3,command = get_checked)
# gender.menu.add_checkbutton(label='Rather Not Say',variable=item1,command = get_checked)

#add items to menu
gender.menu=tk.Menu(gender,tearoff=0)
gender['menu']=gender.menu 


#create eye colour
eye_l = tk.Label(main_window,text='Eye Colour',bg='lightgrey')
eye_l.grid(row=3,column=1,padx=5,pady=5)
eye_t = tk.Entry(main_window,width=20)
eye_t.grid(row=3,column=2,padx=5,pady=5)

#Height
height_l = tk.Label(main_window,text='Height',bg='lightgrey')
height_l.grid(row=4,column=1,padx=5,pady=5)
height_t = tk.Entry(main_window,width=20)
height_t.grid(row=4,column=2,padx=5,pady=5)
inch = tk.Label(main_window,text='inches',bg='lightgrey')
inch.grid(row=4,column=3,padx=5,pady=5)

#Weight
weight_l = tk.Label(main_window,text='Weight',bg='lightgrey')
weight_l.grid(row=5,column=1,padx=5,pady=5)
weight_t = tk.Entry(main_window,width=20)
weight_t.grid(row=5,column=2,padx=5,pady=5)
lbs = tk.Label(main_window,text='lbs',bg='lightgrey')
lbs.grid(row=5,column=3,padx=5,pady=5)

#create functions called by buttons
def register_app():
  global gender_value
  name_value = name_t.get()
  eye_value = eye_t.get()
  height_value = height_t.get()
  weight_value = weight_t.get()
  print(name_value,eye_value,height_value,weight_value)
  lst = []
  lst.append(name_value)
  lst.append(gender_value)
  lst.append(eye_value)
  lst.append(height_value)
  lst.append(weight_value)

def quit_app():
  main_window.destroy()



#create quit and register buttons
button_r = tk.Button(main_window,text='Register',command=register_app)
button_r.grid(row=8,column=1,padx=5,pady=5)
button_q = tk.Button(main_window,text='Quit',command=quit_app)
button_q.grid(row=8,column=2,padx=5,pady=5)


 
main_window.mainloop()