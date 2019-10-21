from tkinter import *
from tkinter import messagebox
import sqlite3 as lite
import csv
import sys
con = lite.connect('runtime.db')
con2 = lite.connect('test.db')
fields = ('Course', 'Slot', 'Classroom')
fields2 = ["Slot"]
e = []
slots = [0,0,0,0,0,0,0,0]

#new name for gui.py
#also is changed some column names of tables in the DB like Sr. no. -> SrNo etc that had spaces between them

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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[0]
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[0] = slots[0]+1
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
                label.grid(row=8, column=0, sticky=W)
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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[1] + 20
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[1]=slots[1]+1 
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
                label.grid(row=8, column=0, sticky=W)
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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[2] + 40
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[2]=slots[2]+1
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
                label.grid(row=8, column=0, sticky=W)
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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[3]+60
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[3]=slots[3]+1
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
                label.grid(row=8, column=0, sticky=W)
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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[4]+80
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[4]=slots[4]+1
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
                label.grid(row=8, column=0, sticky=W)
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
            label.grid(row=6, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[5]+100
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[5]=slots[5]+1
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
                label.grid(row=6, column=0, sticky=W)
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
            label.grid(row=8, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[6]+120
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[6]=slots[6]+1
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
                label.grid(row=6, column=0, sticky=W)
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
            label.grid(row=6, column=0, sticky=W)
            label.after(2000, label.destroy)
        else:
            labno = slots[7]+140
            st = course+ "\n" + classroom
            e[labno].config(text=st)
            slots[7]=slots[7]+1
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
                label.grid(row=6, column=0, sticky=W)
                label.after(2000, label.destroy)

    else:
        label = Label(root, text="Slot does not Exist")
        label.grid(row=6, column=0, sticky=W)
        label.after(2000, label.destroy)
    con.commit()

def deleteIt(root, entries):
    sslot = str(entries['Slot'].get())
    if sslot == "":
        return
    slotIs = "Slot" + sslot
    slot = ord(sslot) - ord('A')
    print("Slot = "+str(slot))
    if slots[slot] == 0:
        label = Label(root, text="No value to delete in " + slotIs)
        label.grid(row=6, column=0, sticky=W)
        label.after(2000, label.destroy)
        return
    labe = e[slots[slot]-1 + slot*20]
    labe_txt = labe.cget("text")
    labelz = labe_txt.split('\n')
    e[slots[slot]-1 + slot*20].config(text="-")
    course_code = str(labelz[0])
    slots[slot] = slots[slot]-1 
    cur = con.cursor()
    print("DELETE FROM " + slotIs + " WHERE " + "CourseNo = '" + course_code + "'")
    cur.execute("DELETE FROM " + slotIs + " WHERE " + "CourseNo = '" + course_code + "'")
    cur.execute("DELETE FROM " + "facultySlots" + " WHERE " + "Slot = '" + sslot + "'")
    cur.execute("DELETE FROM " + "allCoursesAdded" + " WHERE " + "CourseNo = '" + course_code + "'")
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
       label.grid(row=8, column=0, sticky=W)
       label.after(2000, label.destroy)
   con.commit()
   show_all_databases()

def save_database(entries):
    label = Label(root, text="Feauture Under Progress")
    label.grid(row=8, column=0, sticky=W)
    label.after(2000, label.destroy)

def makeform(root, fields, base):
    #table displays
    lr = []
    lc = []
    for i in range(0,20):
        row = Frame(root)
        s = "row" + str(i+1)
        lr.append(Label(root, text = s));
    for i in range(1,9):
        s = "Slot" + chr(ord('A')+int(i-1))
        lc.append(Label(root, text = s));
    for i in range(0,20):
        lr[i].grid(row = i+1, column = 12, sticky = W, pady = 1)   

    for i in range(0,8):
        lc[i].grid(row = 0, column = i+14, sticky = W, padx = 3)
    for i in range(0,160):
        e.append(Label(root, text = "-", borderwidth=2, relief="groove", width=6, height=2));

    for i in range(0,160):
        r = i%20 + 1
        c = int(i/20)+2
        e[i].grid(row = r, column = c+12, pady = 2);
    #form
    entries = {}
    i=base
    for field in fields:
        i=i+1
        row = Frame(root)
        lab = Label(row, width=10, text=field+": ", anchor='w')
        ent = Entry(row)
        # ent.insert(0,"0")
        row.grid(row = i, column = 0, sticky = W, padx = 3, pady = 1)
        lab.grid(row = i, column = 0, sticky = W, padx = 1, pady = 1)
        ent.grid(row = i, column = 2, sticky = W, padx = 1, pady = 1)
        entries[field] = ent
    return entries

def set_runtime_database():

   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotA")
   cur.execute("CREATE TABLE slotA ('CourseNo' TEXT PRIMARY KEY, 'Class' TEXT UNIQUE);")
   con.commit()
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotB")
   cur.execute("CREATE TABLE slotB ('CourseNo' TEXT PRIMARY KEY, 'Class' TEXT UNIQUE);")
   con.commit()
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotC")
   cur.execute("CREATE TABLE slotC ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotD")
   cur.execute("CREATE TABLE slotD ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotE")
   cur.execute("CREATE TABLE slotE ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotF")
   cur.execute("CREATE TABLE slotF ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotG")
   cur.execute("CREATE TABLE slotG ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS slotH")
   cur.execute("CREATE TABLE slotH ('CourseNo' TEXT PRIMARY KEY,'Class' TEXT UNIQUE);")
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS allCoursesAdded")
   cur.execute("CREATE TABLE allCoursesAdded ('CourseNo' TEXT PRIMARY KEY);")
   con.commit()
   cur.execute("DROP TABLE IF EXISTS facultySlots")
   cur.execute("CREATE TABLE facultySlots ('ShortName' TEXT, 'Slot' TEXT);")
   con.commit()

if __name__ == '__main__':

   set_runtime_database()
   root = Tk()
   ents = makeform(root, fields, -1)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   butt_row = Frame(root)
   butt_row.grid(row = 3, column = 0, sticky = W, padx = 1, pady = 1)
   b1 = Button(butt_row, text = 'Add', command=(lambda e = ents: check_constraints(root,e)))
   b1.grid(row = 3, sticky = W, padx = 1, pady = 1, columnspan=2)
   b3 = Button(butt_row, text = 'Quit', command = root.quit)
   b3.grid(row = 3, column = 4, sticky = W, padx = 1, pady = 1, columnspan=2)
   ents2 = makeform(root, fields2, 3)
   butt_row2 = Frame(root)
   butt_row2.grid(row = 5, column = 0, sticky = W, padx = 1, pady = 1)
   b2 = Button(butt_row2, text = 'Delete', command=(lambda e = ents2: deleteIt(root,e)))
   b2.grid(row = 5, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   # b2 = Button(root, text='Save', command=(lambda e = ents: save_database(e)))
   # b2.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()
   con.close()
   con2.close()
