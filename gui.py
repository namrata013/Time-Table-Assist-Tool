from tkinter import *
from tkinter import messagebox
import sqlite3 as lite
import csv
import sys
con = lite.connect('runtime.db')
con2 = lite.connect('test.db')
fields = ('Course', 'Slot', 'Classroom')

def add_into_slot_database(entries):
    course = str(entries['Course'].get())
    slot = str(entries['Slot'].get())
    classroom = str(entries['Classroom'].get())

    # Check For Slot A
    if slot=="A":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotA")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotA Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for B
    elif slot=="B":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotB")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotB Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    #  Check for Slot C
    elif slot=="C":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotC")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotC Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for Slot D
    elif slot=="D":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotD")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotD Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for Slot E
    elif slot=="E":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotE")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotE Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for Slot F
    elif slot=="F":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotF")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotF Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for Slot G
    elif slot=="G":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotG")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotG Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    # Check for Slot H
    elif slot=="H":
        cur = con.cursor()
        errorBit = 0
        errorBit2 = 0
        cur.execute("SELECT * FROM slotH")
        data = cur.fetchall()
        for row in data:
            if row[1]==classroom:
                errorBit = 1
        if errorBit==1:
            label = Label(root, text="Two Courses in a slot cannot have same Classroom")
            label.pack()
            label.after(2000, label.destroy)
        else:
            per = con2.cursor()
            per.execute("SELECT * FROM clgdata")
            data2 = per.fetchall()
            instructors = ""
            for row in data2:
                if row[1]==course:
                    instructors = str(row[4])
                    instructors = instructors.split(',')
            for i in instructors:
                cur = con.cursor()
                cur.execute("SELECT * FROM facultySlots")
                data3 = cur.fetchall()
                for d3 in data3:
                    if d3[0]==i and d3[1]==slot:
                        errorBit2 = 1
            if errorBit2==0:
                cur = con.cursor()
                cur.execute("INSERT INTO slotH Values (?,?)", (course,classroom))
                con.commit()
                cur = con.cursor()
                cur.execute("INSERT INTO allCoursesAdded Values (?)", (course,))
                con.commit()
                cur = con.cursor()
                for i in instructors:
                    cur.execute("INSERT INTO facultySlots Values (?,?)", (i,slot))
                con.commit()
            else:
                label = Label(root, text="A faculty cannot take two classes in same slot")
                label.pack()
                label.after(2000, label.destroy)

    else:
        label = Label(root, text="Slot does not Exist")
        label.pack()
        label.after(2000, label.destroy)
    con.commit()

def show_all_databases():
    print("----------- -----------")
    print("allCoursesAdded")
    cur = con.cursor()
    cur.execute("SELECT * FROM allCoursesAdded")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotA")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotA")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotB")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotB")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotC")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotC")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotD")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotD")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotE")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotE")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotF")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotF")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotG")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotG")
    data = cur.fetchall()
    for row in data:
        print(row)
    print("slotH")
    cur = con.cursor()
    cur.execute("SELECT * FROM slotH")
    data = cur.fetchall()
    for row in data:
        print(row)

def check_constraints(root, entries):
   course = str(entries['Course'].get())
   slot = str(entries['Slot'].get())

   cur = con.cursor()
   errorBit = 0
   cur.execute("SELECT * FROM allCoursesAdded")
   data = cur.fetchall()
   for row in data:
       if row[0]==course:
           errorBit = 1
   if errorBit==0:
       cur = con.cursor()
       add_into_slot_database(entries)
   else:
       label = Label(root, text="Course Already Added")
       label.pack()
       label.after(2000, label.destroy)
   con.commit()
   show_all_databases()

def save_database(entries):
    label = Label(root, text="Feauture Under Progress")
    label.pack()
    label.after(2000, label.destroy)

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      # ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def set_runtime_database():

   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotA")
   cur.execute("CREATE TABLE slotA ('Course No.' TEXT PRIMARY KEY, 'Class' TEXT UNIQUE);")
   con.commit()
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotB")
   cur.execute("CREATE TABLE slotB ('Course No.' TEXT PRIMARY KEY, 'Class' TEXT UNIQUE);")
   con.commit()
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotC")
   cur.execute("CREATE TABLE slotC ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotD")
   cur.execute("CREATE TABLE slotD ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotE")
   cur.execute("CREATE TABLE slotE ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotF")
   cur.execute("CREATE TABLE slotF ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotG")
   cur.execute("CREATE TABLE slotG ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotH")
   cur.execute("CREATE TABLE slotH ('Course No.' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS allCoursesAdded")
   cur.execute("CREATE TABLE allCoursesAdded ('Course No.' TEXT PRIMARY KEY);")
   con.commit()
   cur.execute("DROP TABLE IF EXISTS facultySlots")
   cur.execute("CREATE TABLE facultySlots ('Short Name' TEXT, 'Slot' TEXT);")
   con.commit()

if __name__ == '__main__':

   set_runtime_database()
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Add',
      command=(lambda e = ents: check_constraints(root,e)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   b2 = Button(root, text='Save',
   command=(lambda e = ents: save_database(e)))
   b2.pack(side = LEFT, padx = 5, pady = 5)
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
   con.close()
   con2.close()
