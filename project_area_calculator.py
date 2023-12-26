#!/usr/bin/env python
# coding: utf-8

# In[16]:


# area calculator function

import sys
from tkinter import Tk, simpledialog, messagebox
   
#width = int(input('Enter width:'))
#height = int(input('Enter height'))
    
#create function to calculate
def area_calculator(width_info,height_info):
    area = int(width_info)*int(height_info)
    return area

root = Tk()
root.withdraw() #withdraw GUI window

while True:
    simpledialog.askstring
    width_info = '' # set variable to receive input 
    height_info = '' # set variable to receive input 
    width_info = simpledialog.askstring('Area Calculator','Enter width: ') #pop dialog box
    height_info = simpledialog.askstring('Area Calculator','Enter height: ') 
    area_calculator(width_info,height_info) # set variable to store result from function 
    area_result = str(area_calculator(width_info,height_info)) # convert to string 
    messagebox.showinfo('Area Calculator','The area of rectangle is: '+area_result) # print out 
    root.destroy()
    sys.exit()


# In[ ]:





# In[ ]:




