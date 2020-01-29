from tkinter import *
from tkinter import messagebox
import sqlite3 as lite
from sqlite3 import Error
import csv
import sys
import os
import allocate
import numpy
import string
from test import col_nums
from test import basket_nums
import db_modify
import time

exec(open("./test.py").read())
exec(open("./allocate.py").read())
db = r"test.db"
conn = allocate.create_connection(db)

fields = ('Course','Classroom','Slot','Row')
fields2 = ['Slot','Row','Classroom']
e = []
slots = [0,0,0,0,0,0,0,0]

colours= ["#c3c388","#ecffb3","#d9b3ff","#e6b3b3","#ffd9b3","#b3e6ff","#ffdf80","#99ff99","#ffb3b3","#d9d9d9"]

''' Function: force_add
    Called when a user hits the 'add' button. Checks for slot, row and classroom (if added) existance. Also checks for pre-added course anomaly and adds the course to database.

    Parameters:
        root - the main tkinter window/frame object.
        entries - entries is a python dictionary object containing the fields: "Slot", "Row", "Course code" and "Classroom" of the record.
        conn - conn is a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def force_add(root, entries, conn):
    course = str(entries['Course'].get())
    slot = str(entries['Slot'].get())
    classroom = str(entries['Classroom'].get())
    row_no = int(entries['Row'].get())

    # remove case sensitivity
    slot = slot.upper()
    slot = slot.strip()
    course = course.upper()
    course = course.strip()
    course = course.replace(" ", "")
    classroom = classroom.upper()
    classroom = classroom.strip()
    classroom = classroom.replace(" ", "")

    if conn is not None:
        cur = conn.cursor()

        # check course existence
        find_error = 1
        cur.execute("SELECT * FROM Course_Data")
        data = cur.fetchall()
        for row in data:
            if row[1]==course:
                find_error = 0
        if find_error==1:
            error_msg = "     Course Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        #check classroom existence
        if(classroom!=""):
            cur.execute("SELECT * FROM Classroom_Data")
            data = cur.fetchall()
            find_error = 1
            for row in data:
                classs = str(row[1])
                classs = classs.strip()
                if(classroom == classs):
                    find_error = 0
            if find_error==1:
                error_msg = "     Classroom Does Not Exist"
                label = Label(root, text=error_msg, fg="red")
                label.grid(row=11, column=0, sticky=W)
                label.after(3000, label.destroy)
                return None

        # check slot existence
        slot_no = ord(slot)
        if slot_no<ord("A") or slot_no>ord("H"):
            error_msg = "     Slot Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # check row existence
        if row_no>20 or row_no<1:
            error_msg = "     Row Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # row already occupied
        s = int(ord(slot)-ord("A"))
        labno = row_no-1+20*s
        st = e[labno].cget("text")
        if st!="-":
            error_msg = "     Row Already Occupied"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # pre added course anomaly
        cur.execute("SELECT * FROM Allocated_subjs")
        data = cur.fetchall()
        for row in data:
            if course==str(row[0]):
                error_msg = "     Course Already Added"
                label = Label(root, text=error_msg, fg="red")
                label.grid(row=11, column=0, sticky=W)
                label.after(3000, label.destroy)
                return None

        # Instructor_Slots
        cur.execute("SELECT * FROM Course_Data WHERE Course_No=?", (course,))
        data = cur.fetchall()[0]
        instructors = str(data[4])
        instructors_list1 = instructors.split(',')
        instructors_list2 = instructors.split('/')
        l1 = len(instructors_list1)
        l2 = len(instructors_list2)
        instructors_list = []
        if(l1>=l2):
            instructors_list = instructors_list1
        else:
            instructors_list = instructors_list2

        # allocation
        for i in instructors_list:
            i = i.strip()
            i = i.upper()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Professor_Data")
            data = cur.fetchall()
            for row in data:
                name = ""
                shortname = str(row[1])
                shortname = shortname.strip()
                shortname = shortname.upper()
                if(i==shortname):
                    name = str(row[2])
                    cur = conn.cursor()
                    cur.execute("INSERT INTO Instructor_Slots Values (?,?,?,?)", (name,i,slot,course))
                    conn.commit()
        cur = conn.cursor()
        cur.execute("INSERT INTO Allocated_Subjs Values (?,?,?,?)", (course,slot,classroom, str(row_no)))
        conn.commit()

        s = int(ord(slot)-ord("A"))
        labno = row_no-1+20*s
        st = course+"\n"+classroom
        e[labno].config(text=st, bg=colours[s])
        slots[s]+=1

    else:
        label = Label(root, text="     Database Lost Connection", fg="red")
        label.grid(row=9, column=0, sticky=W)
        label.after(3000, label.destroy)
        root.quit

''' Function: constraint_check
    Called when a user hits the 'constraint check' button. Applies the Classroom, Instructor, Core course, Basket Course constraints on the record entered. Gives warning regarding each constraint if found anomaly.

    Parameters:
        root - the main tkinter window/frame object.
        entries - entries is a python dictionary object containing the fields: "Slot", "Row", "Course code" and "Classroom" of the record.
        conn - conn is a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def constraint_check(root, entries, conn):
    course = str(entries['Course'].get())
    slot = str(entries['Slot'].get())
    classroom = str(entries['Classroom'].get())
    row_no = int(entries['Row'].get())

    # remove case sensitivity
    slot = slot.upper()
    slot = slot.strip()
    course = course.upper()
    course = course.strip()
    course = course.replace(" ", "")
    classroom = classroom.upper()
    classroom = classroom.strip()
    classroom = classroom.replace(" ", "")

    if conn is not None:
        cur = conn.cursor()

        # check course existence
        find_error = 1
        cur.execute("SELECT * FROM Course_Data")
        data = cur.fetchall()
        for row in data:
            if row[1]==course:
                find_error = 0
        if find_error==1:
            error_msg = "     Course Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        #check classroom existence
        if(classroom!=""):
            cur.execute("SELECT * FROM Classroom_Data")
            data = cur.fetchall()
            find_error = 1
            for row in data:
                classs = str(row[1])
                classs = classs.strip()
                if(classroom == classs):
                    find_error = 0
            if find_error==1:
                error_msg = "     Classroom Does Not Exist"
                label = Label(root, text=error_msg, fg="red")
                label.grid(row=11, column=0, sticky=W)
                label.after(3000, label.destroy)
                return None

        # check slot existence
        slot_no = ord(slot)
        if slot_no<ord("A") or slot_no>ord("H"):
            error_msg = "     Slot Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # check row existence
        if row_no>20 or row_no<1:
            error_msg = "     Row Does Not Exist"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # row already occupied
        s = int(ord(slot)-ord("A"))
        labno = row_no-1+20*s
        st = e[labno].cget("text")
        if st!="-":
            error_msg = "     Row Already Occupied"
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=11, column=0, sticky=W)
            label.after(3000, label.destroy)
            return None

        # pre added course anomaly
        cur.execute("SELECT * FROM Allocated_subjs")
        data = cur.fetchall()
        for row in data:
            if course==str(row[0]):
                error_msg = "     Course Already Added"
                label = Label(root, text=error_msg, fg="red")
                label.grid(row=11, column=0, sticky=W)
                label.after(3000, label.destroy)
                return None

        # classroom clash
        if(classroom!=""):
            cur.execute("SELECT * FROM Allocated_Subjs WHERE Slot =?",(slot))
            data = cur.fetchall()
            for row in data:
                classe = str(row[2])
                if classe==classroom:
                    error_msg = "     Classroom " + classe + " allotted twice \n in slot " + slot + " for " + str(row[0]) + " and " + course
                    label = Label(root, text=error_msg, fg="red")
                    label.grid(row=11, column=0, sticky=W)
                    label.after(5000, label.destroy)

        # instructor clash
        cur.execute("SELECT * FROM Course_Data WHERE Course_No=?", (course,))
        data = cur.fetchall()[0]
        instructors = str(data[4])
        instructors_list1 = instructors.split(',')
        instructors_list2 = instructors.split('/')
        l1 = len(instructors_list1)
        l2 = len(instructors_list2)
        instructors_list = []
        if(l1>=l2):
            instructors_list = instructors_list1
        else:
            instructors_list = instructors_list2
        cur.execute("SELECT * FROM Instructor_Slots WHERE Slot =?",(slot))
        teacher = cur.fetchall()
        for i in instructors_list1:
            i = i.strip()
            i = i.upper()
            for row in teacher:
                y = str(row[1])
                y = y.strip()
                y=y.upper()
                if(i==y):
                    error_msg = "     Faculty " + str(row[0]) + "\n is getting "+ course + " and " + str(row[3]) + " in slot " + slot
                    label = Label(root, text=error_msg, fg="red")
                    label.grid(row=12, column=0, sticky=W)
                    label.after(5000, label.destroy)
        for i in instructors_list2:
            i = i.strip()
            i = i.upper()
            for row in teacher:
                y = str(row[1])
                y=y.upper()
                if(i==y):
                    error_msg = "     Faculty " + str(row[0]) + "\nis getting "+ course + " and " + str(row[3]) + " in slot " + slot
                    label = Label(root, text=error_msg, fg="red")
                    label.grid(row=13, column=0, sticky=W)
                    label.after(5000, label.destroy)

        #  core clash
        i = 5
        may_clash = []
        while(i<col_nums):
            col = str(data[i])
            col = col.strip()
            if(col=="C"):
                may_clash.append(i)
            i=i+1
        cur.execute("SELECT * FROM Course_Data WHERE Course_No <> ?", (course,))
        data = cur.fetchall()
        for i in may_clash:
            for row in data:
                col =str(row[i])
                col =col.strip()
                if(col=="C"):
                    subject = str(row[1])
                    subject = subject.strip()
                    cur.execute("SELECT * FROM Allocated_Subjs WHERE Course_No =?", (subject,))
                    D = cur.fetchall()
                    if(D):
                        col = str(D[0][1])
                        if(slot==col):
                            error_msg = "     Core Course Clash with " + subject + "\n"
                            label = Label(root, text=error_msg, fg="red")
                            label.grid(row=14, column=0, sticky=W)
                            label.after(5000, label.destroy)

        # basket clash
        for i in range(basket_nums):
            found=0
            tab = "Basket_" + str(i+1)
            cur.execute("SELECT * FROM " + tab)
            data = cur.fetchall()
            for row in data:
                subject = str(row[0])
                subject = subject.strip()
                if(subject==course):
                    found=1
                    break
            if(found==1):
                for row in data:
                    subject = str(row[0])
                    subject = subject.strip()
                    cur.execute("SELECT * FROM Allocated_Subjs WHERE Course_No =?", (subject,))
                    D = cur.fetchall()
                    if(D):
                        col = str(D[0][1])
                        if(slot==col):
                            error_msg = "     Basket Clash with " + subject + "\n"
                            label = Label(root, text=error_msg, fg="red")
                            label.grid(row=15, column=0, sticky=W)
                            label.after(5000, label.destroy)

    else:
        label = Label(root, text="     Database Lost Connection", fg="red")
        label.grid(row=9, column=0, sticky=W)
        label.after(3000, label.destroy)
        root.quit

''' Function: deletion
    Called when a user hits the delete button. Its function is to delete a given entry from the slotwise course distribution table and all its occurances in the database.

    Parameters:
        root - the main tkinter window/frame object.
        entries - entries is a python dictionary object containing the fields: "Slot" and "Row" of the record to be deleted.
        conn - conn is a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def deletion(root, entries, conn):
    slot = str(entries['Slot'].get())
    row_no = int(entries['Row'].get())

    # remove case sensitivity
    slot = slot.upper()
    slot = slot.strip()

    slot_no = ord(slot)

    # check slot existence
    if slot_no<ord("A") or slot_no>ord("H"):
        error_msg = "     Slot Does Not Exist"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check row existence
    if row_no>20 or row_no<1:
        error_msg = "     Row Does Not Exist"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check if slot is empty
    slot_no = ord(slot) - ord("A")
    if slots[slot_no]==0:
        error_msg = "     Slot "+slot+" is Empty"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check if row is empty
    labe = e[row_no-1+slot_no*20]
    labe_txt = labe.cget("text")
    if labe_txt=="-":
        error_msg = "     Row "+str(row_no)+" is Empty"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    labelz = labe_txt.split('\n')
    labe.config(text="-",bg=colours[slot_no])
    course_code = str(labelz[0])
    slots[slot_no] = slots[slot_no]-1

    cur = conn.cursor()
    cur.execute("DELETE FROM " + "Instructor_Slots" + " WHERE " + "Course_No = '" + course_code + "'")
    cur.execute("DELETE FROM " + "Allocated_Subjs" + " WHERE " + "Course_No = '" + course_code + "'")
    conn.commit()

    error_msg = "     "+course_code+" from Slot "+slot+" successfully\n deleted"
    label = Label(root, text=error_msg)
    label.grid(row=11, column=0, sticky=W)
    label.after(3000, label.destroy)
    return None

''' Function: addclass
    Called when a user hits the 'add classroom' button. Add a class or update the class of an existing record.

    Parameters:
        root - the main tkinter window/frame object.
        entries - entries is a python dictionary object containing the fields: "Slot" ,"Row" and "classroom" of the record.
        conn - conn is a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def addclass(root, entries, conn):
    slot = str(entries['Slot'].get())
    row_no = int(entries['Row'].get())
    classroom = str(entries['Classroom'].get())

    # remove case sensitivity
    slot = slot.upper()
    slot = slot.strip()
    classroom = classroom.upper()
    classroom = classroom.strip()
    classroom = classroom.replace(" ", "")
    slot_no = ord(slot)

    # check slot existence
    if slot_no<ord("A") or slot_no>ord("H"):
        error_msg = "     Slot Does Not Exist"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check row existence
    if row_no>20 or row_no<1:
        error_msg = "     Row Does Not Exist"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check if slot is empty
    slot_no = ord(slot) - ord("A")
    if slots[slot_no]==0:
        error_msg = "     Slot "+slot+" is Empty"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # check if row is empty
    labe = e[row_no-1+slot_no*20]
    labe_txt = labe.cget("text")
    if labe_txt=="-":
        error_msg = "     Row "+str(row_no)+" is Empty"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=11, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    labelz = labe_txt.split('\n')
    course_code = str(labelz[0])

    cur = conn.cursor()
    #check classroom existence
    cur.execute("SELECT * FROM Classroom_Data")
    data = cur.fetchall()
    find_error = 1
    for row in data:
        classs = str(row[1])
        classs = classs.strip()
        if(classroom == classs):
            find_error = 0
    if find_error==1:
        error_msg = "     Classroom Does Not Exist"
        label = Label(root, text=error_msg, fg="red")
        label.grid(row=12, column=0, sticky=W)
        label.after(3000, label.destroy)
        return None

    # classroom clash
    cur.execute("SELECT * FROM Allocated_Subjs WHERE Slot =?",(slot))
    data = cur.fetchall()
    for row in data:
        classe = str(row[2])
        if classe==classroom:
            error_msg = "     Classroom " + classe + " allotted twice \n in slot " + slot + " for " + str(row[0]) + " and " + course
            label = Label(root, text=error_msg, fg="red")
            label.grid(row=12, column=0, sticky=W)
            label.after(5000, label.destroy)
            return None

    cur.execute("UPDATE Allocated_Subjs SET Class = ? WHERE Course_No =?",(classroom,course_code))
    conn.commit()
    st = course_code+"\n"+classroom
    labe.config(text=st,bg=colours[slot_no])

''' Function: remember
    Reads the existing entries in allocated_subjs table and displays at appropriate position.
    Parameters:
        root - the main tkinter window/frame object.
        conn - a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def remember(root, conn):
    cur = conn.cursor()
    limit = 8
    index = 0
    for i in ascii_uppercase:
        cur.execute("SELECT * FROM Allocated_Subjs WHERE Slot =?",(str(i)))
        data = cur.fetchall()
        for row in data:
            s = int(ord(i)-ord("A"))
            labno = int(row[3])-1+20*s
            st = row[0]+"\n"+row[2]
            e[labno].config(text=st,bg=colours[s])
            slots[s]+=1
        index += 1
        if index==limit:
            break

def clearance(root, conn, entries):
    response = messagebox.askquestion("New Time Table","Do you wish to continue?\n\nAll progress will be lost")
    if response=='yes':
        index = 0
        limit = 8
        for i in ascii_uppercase:
            slot_no = int(ord(i) - ord("A"))
            num = slots[slot_no]
            for n in range(20):
                e[n+ slot_no*20].config(text="-",bg=colours[slot_no])
            index += 1
            if index==limit:
                break
        cur = conn.cursor()
        cur.execute("DROP TABLE Instructor_Slots")
        cur.execute("DROP TABLE allocated_subjs")
        conn.commit()
        for i in range(8):
            slots[i] = 0
        exec(open("./allocate.py").read())
        conn = allocate.create_connection(db)

''' Function: generate_2
    An assisting function to generate which takes the filename and generates the time table in it as a .csv

    Parameters:
        top - tkinter window frame
        filename - gives the filename chosen by user

    Returns:
        None.
'''
def generate_2(top, filename):
    ans = filename.get()
    ans += ".csv"
    if os.path.exists(ans):
        os.remove(ans)
    for n in range(20):
        index = 0
        limit = 8
        output = []
        for i in ascii_uppercase:
            slot_no = int(ord(i) - ord("A"))
            labe = e[n+ slot_no*20]
            labe_txt = labe.cget("text").split('\n')
            txt = str(labe_txt[0])
            if len(labe_txt)==2:
                txt += "\n"+str(labe_txt[1])
            output.append(txt)
            index += 1
            if index==limit:
                break
        with open(ans,'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(output)
    csvFile.close()
    top.destroy()

''' Function: generate
    Called when user wants to generate a csv file corresponding to the time table.

    Parameters:
        root - the main tkinter window/frame object.
        conn - a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def generate(root, conn, entries):
    top = Toplevel(root)
    top.title("Generate Time Table")
    label1 = Label(top,text="Enter file name to create .csv file")
    label1.pack(pady = 10, padx = 10)
    label2 = Label(top,text="Example: timetable")
    label2.pack(pady = 10)
    filename = Entry(top)
    filename.pack(pady = 10, padx =10)
    b1 = Button(top, text = 'Save', command=(lambda : generate_2(top, filename)))
    b1.pack(pady = 10)

''' Function: modify
    Called when user wants to erase the existing time table and create a new one.

    Parameters:
        root - the main tkinter window/frame object.
        conn - a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def modify(root, conn, entries):
    response = messagebox.askquestion("Modify Database","Do you wish to continue?\n\nAll progress will be lost")
    if response=='yes':
        index = 0
        limit = 8
        for i in ascii_uppercase:
            slot_no = int(ord(i) - ord("A"))
            num = slots[slot_no]
            for n in range(20):
                e[n+ slot_no*20].config(text="-",bg=colours[slot_no])
            index += 1
            if index==limit:
                break
        cur = conn.cursor()
        cur.execute("DROP TABLE Instructor_Slots")
        cur.execute("DROP TABLE Allocated_subjs")
        conn.commit()
        for i in range(8):
            slots[i] = 0
        exec(open("./allocate.py").read())
        conn = allocate.create_connection(db)

        db_modify.main()

''' Function: reload
    Called when user wants to completely remove all the existing database tables and create new ones.

    Parameters:
        root - the main tkinter window/frame object.
        conni - a connection object that represents the database and using which we can manipulate the database.

    Returns:
        None.
'''
def reload(root, conni, entries):
    response = messagebox.askquestion("Reload Database","Do you wish to continue?\n\nAll progress will be lost")
    if response=='yes':

        cur = conni.cursor()
        cur.execute("DROP TABLE Classroom_Data")
        cur.execute("DROP TABLE Professor_Data")
        cur.execute("DROP TABLE Course_Data")
        cur.execute("DROP TABLE Instructor_Slots")
        cur.execute("DROP TABLE Allocated_subjs")
        conni.commit()

        index = 0
        limit = 8
        for i in ascii_uppercase:
            slot_no = int(ord(i) - ord("A"))
            num = slots[slot_no]
            for n in range(20):
                e[n+ slot_no*20].config(text="-",bg=colours[slot_no])
            index += 1
            if index==limit:
                break
        for i in range(8):
            slots[i] = 0

        exec(open("./test.py").read())
        exec(open("./allocate.py").read())
        global db
        db = r"test.db"
        global conn
        conn = allocate.create_connection(db)


''' Function: makeform
    Create the slotwise distributed table and create forms for requesting courses/classrooms to be added or deleted from the slotwise distribution table.

    Parameters:
        root - the main tkinter window/frame object.
        fields - contains a tuple of form entries/fields that need to be added in the GUI.
        base - start marker for adding form entries on the grid.

    Returns:
        returns all the form's entry objects in the form of python dictionary object.
'''
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
        lr[i].grid(row = i+1, column = 12,sticky = W, pady = 1)

    for i in range(0,8):
        lc[i].grid(row = 0, column = i+14,sticky = W, padx = 3)
    for i in range(0,160):
        e.append(Label(root, text = "-", bg = colours[int(i/20)],borderwidth=2, relief="groove", width=9, height=2));

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

if __name__ == '__main__':
   db = r"test.db"
   conn = allocate.create_connection(db)
   root = Tk()
   root.resizable(0,0)
   root.title("Time-Table-Assist-Tool Version 1")
   ents = makeform(root, fields, 0)
   remember(root,conn)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   butt_row = Frame(root)
   butt_row.grid(row = 5, column = 0, sticky = W, padx = 1, pady = 1)
   b1 = Button(butt_row, text = 'Constraint Check', command=(lambda e = ents: constraint_check(root,e,conn)))
   b1.grid(row = 5, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   b8 = Button(butt_row, text = 'Add', command=(lambda e = ents: force_add(root,e,conn)))
   b8.grid(row = 5, column = 2,sticky = W, padx = 1, pady = 1, columnspan=2)
   ents2 = makeform(root, fields2, 5)
   butt_row2 = Frame(root)
   butt_row2.grid(row = 9, column = 0, sticky = W, padx = 1, pady = 1)
   b2 = Button(butt_row2, text = 'Delete', command=(lambda e = ents2: deletion(root,e, conn)))
   b2.grid(row = 10, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   b8 = Button(butt_row2, text = 'Add Classroom', command=(lambda e = ents2: addclass(root,e, conn)))
   b8.grid(row = 10, column = 2,sticky = W, padx = 1, pady = 1, columnspan=2)
   b3 = Button(root, text = 'New Time Table', command =(lambda e = ents: clearance(root,conn,e)))
   b3.grid(row = 16, column = 0, sticky = W, padx = 1, pady = 1, columnspan=2)
   b4 = Button(root, text = 'Quit', command = root.quit)
   b4.grid(row = 20, column = 0, sticky = W, padx = 1, pady = 1, columnspan=2)
   b5 = Button(root, text = 'Generate Time Table', command=(lambda e = ents: generate(root,conn,e)))
   b5.grid(row = 17, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   b6 = Button(root, text = 'Modify Database', command=(lambda e = ents: modify(root,conn,e)))
   b6.grid(row = 18, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   b7 = Button(root, text = 'Reload Database', command=(lambda e = ents: reload(root,conn,e)))
   b7.grid(row = 19, column = 0,sticky = W, padx = 1, pady = 1, columnspan=2)
   root.mainloop()
   if conn:
       conn.close()
