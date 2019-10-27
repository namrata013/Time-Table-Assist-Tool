import os
from tkinter import * 
# from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.title('Time Table Assist')
 
def open_file(f_type): 
    # ent.delete(0,END)
    file = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')]) 
    if file is not None: 
        content = file.read()
        filename = f_type + ".csv"
        f= open(filename,"w")
        f.write(content)
        f.close()
        if f_type=="class":
            lab1.config(text="File opened successfully!!", fg="blue")
            global c
            c=1
        elif f_type=="teacher":
            lab2.config(text="File opened successfully!!", fg="blue")
            global t
            t=1            
        else:
            lab3.config(text="File opened successfully!!", fg="blue")
            global d
            d=1

def com_test():
    lab2.config(text="File opened successfully!!")
    # e.Delete(0, END)

def com_start():
    # global c
    # global t
    # global d
    os.system('python3 gui.py')
    if int(c)==1 and int(t)==1 and int(d)==1:
        lab4.config(text="Ready!!", fg="green")
    else:
        lab4.config(text="not Ready :(", fg="red")

labintro=Label(root, text="Welcome! Please input the files to begin!", borderwidth=5, fg="dark green", font=('Times', '20', 'bold'))
labintro.grid(row=0, column=0, columnspan=3, padx=50, pady=10)

butclass=Button(root, text="Add Class File", command= lambda:open_file("class"), borderwidth=3, width=18, height=2)
butteach=Button(root, text="Add Teachers File", command= lambda:open_file("teacher"), borderwidth=3, width=18, height=2)
butdata=Button(root, text="Add Courses File", command= lambda:open_file("data"), borderwidth=3, width=18, height=2)

# buttest=Button(root, text="press", command=com_test, borderwidth=3, width=18, height=2)
# buttest.grid(row=4, column=0, pady=5)

buttest=Button(root, text="Start", command=com_start, borderwidth=3, width=18, height=2, font=('Helvetica','11', 'bold'), fg="blue")
buttest.grid(row=4, column=0, pady=5)

butclass.grid(row=1, column=0, padx=7, pady=5)
butteach.grid(row=2, column=0, padx=7, pady=5)
butdata.grid(row=3, column=0, padx=7, pady=5)

# e=Entry(root, borderwidth=5, width=50)
# e.grid(row=1, column=1)
lab1=Label(root, text="No file Selected")
lab1.grid(row=1, column=1)
lab2=Label(root, text="No file Selected")
lab2.grid(row=2, column=1)
lab3=Label(root, text="No file Selected")
lab3.grid(row=3, column=1)
lab4=Label(root, text="")
lab4.grid(row=4, column=1)



# btn1 = Button(butt_row, text ='Add Class file', command = lambda:open_file("class")) 
# btn1.grid(row = 0, column = 0,sticky = W, padx = 20, pady = 10, columnspan=5)
# btn2 = Button(butt_row, text ='Add Teachers file', command = lambda:open_file("teachers")) 
# btn2.grid(row = 0, column = 5,sticky = W, padx = 20, pady = 10, columnspan=5)
# btn3 = Button(butt_row, text ='Add Courses file', command = lambda:open_file("data")) 
# btn3.grid(row = 0, column = 10,sticky = W, padx = 20, pady = 10, columnspan=5)
  
root.mainloop() 
