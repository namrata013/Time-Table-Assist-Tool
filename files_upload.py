from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
#root.geometry('200x100') 
  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file(f_type): 
    file = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')]) 
    if file is not None: 
        content = file.read()
        filename = f_type + ".csv"
        f= open(filename,"w")
        f.write(content)
        f.close()

butt_row = Frame(root)
butt_row.grid(row = 0, column = 0, sticky = W, padx = 1, pady = 1)
btn1 = Button(butt_row, text ='Add Class file', command = lambda:open_file("class")) 
btn1.grid(row = 0, column = 0,sticky = W, padx = 1, pady = 1, columnspan=5)
btn2 = Button(butt_row, text ='Add Teachers file', command = lambda:open_file("teachers")) 
btn2.grid(row = 0, column = 5,sticky = W, padx = 1, pady = 1, columnspan=5)
btn3 = Button(butt_row, text ='Add Courses file', command = lambda:open_file("data")) 
btn3.grid(row = 0, column = 10,sticky = W, padx = 1, pady = 1, columnspan=5)
  
mainloop() 