from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import font as tkfont
import sqlite3 as lite
import csv
import sys
import os
import allocate
import numpy

db = r"test.db"
conn = allocate.create_connection(db)

def search(self ,type, item):
    if conn is not None:
        cur = conn.cursor()
        if type == "classdata":
            cur.execute("SELECT * FROM Classroom_Data WHERE Class=\"" + item + "\"")
            data = cur.fetchall()
            if len(data)>0:
                data = data[0]
                a = tk.Label(self ,text = "Sr_No: ")
                a.grid(row = 6,column = 0)
                a1 = tk.Label(self ,text = data[0])
                a1.grid(row = 6,column = 2)
                b = tk.Label(self ,text = "Class Name:  ")
                b.grid(row = 7,column = 0)
                b1 = tk.Label(self ,text = data[1])
                b1.grid(row = 7,column = 2)
                c = tk.Label(self ,text = "Strength: ")
                c.grid(row = 8,column = 0)
                c1 = tk.Label(self ,text = data[2])
                c1.grid(row = 8,column = 2)
                a.after(4000, a.destroy)
                a1.after(4000, a1.destroy)
                b.after(4000, b.destroy)
                b1.after(4000, b1.destroy)
                c.after(4000, c.destroy)
                c1.after(4000, c1.destroy)
            else:
                a = tk.Label(self ,text = "         Class " + item + " not found")
                a.grid(row = 6,column = 0)
                a.config(fg="red")
                a.after(4000, a.destroy)
        if type == "profdata":
            cur.execute("SELECT * FROM Professor_Data WHERE FullName=\"" + item + "\"")
            data = cur.fetchall()
            if len(data)>0:
                data = data[0]
                a = tk.Label(self ,text = "Sr_No: ")
                a.grid(row = 6,column = 0)
                a1 = tk.Label(self ,text = data[0])
                a1.grid(row = 6,column = 2)
                b = tk.Label(self ,text = "ShortName:  ")
                b.grid(row = 7,column = 0)
                b1 = tk.Label(self ,text = data[1])
                b1.grid(row = 7,column = 2)
                c = tk.Label(self ,text = "FullName: ")
                c.grid(row = 8,column = 0)
                c1 = tk.Label(self ,text = data[2])
                c1.grid(row = 8,column = 2)
                a.after(4000, a.destroy)
                a1.after(4000, a1.destroy)
                b.after(4000, b.destroy)
                b1.after(4000, b1.destroy)
                c.after(4000, c.destroy)
                c1.after(4000, c1.destroy)
            else:
                a = tk.Label(self ,text = "       Professor " + item + " not found")
                a.grid(row = 6,column = 0)
                a.config(fg="red")
                a.after(4000, a.destroy)
        if type == "clgdata":
            cur.execute("SELECT * FROM Course_Data WHERE Course_No=\"" + item + "\"")
            data = cur.fetchall()
            if len(data)>0:
                data = data[0]
                a = tk.Label(self ,text = "Sr_No: ")
                a.grid(row = 6,column = 0)
                a1 = tk.Label(self ,text = data[0])
                a1.grid(row = 6,column = 2)
                b = tk.Label(self ,text = "Course_No:  ")
                b.grid(row = 7,column = 0)
                b1 = tk.Label(self ,text = data[1])
                b1.grid(row = 7,column = 2)
                c = tk.Label(self ,text = "Course_Title: ")
                c.grid(row = 8,column = 0)
                c1 = tk.Label(self ,text = data[2])
                c1.grid(row = 8,column = 2)
                d = tk.Label(self ,text = "Credits_L_T_P_C: ")
                d.grid(row = 9,column = 0)
                d1 = tk.Label(self ,text = data[3])
                d1.grid(row = 9,column = 2)
                e = tk.Label(self ,text = "Instructor: ")
                e.grid(row = 10,column = 0)
                e1 = tk.Label(self ,text = data[4])
                e1.grid(row = 10,column = 2)
                a.after(4000, a.destroy)
                a1.after(4000, a1.destroy)
                b.after(4000, b.destroy)
                b1.after(4000, b1.destroy)
                c.after(4000, c.destroy)
                c1.after(4000, c1.destroy)
                d.after(4000, d.destroy)
                d1.after(4000, d1.destroy)
                e.after(4000, e.destroy)
                e1.after(4000, e1.destroy)
            else:
                a = tk.Label(self ,text = "       Course " + item + " not found")
                a.grid(row = 6,column = 0)
                a.config(fg="red")
                a.after(4000, a.destroy)

def add(self ,type, item):
    if conn is not None:
        cur = conn.cursor()
        if type == "classdata":
            cur.execute("SELECT COUNT(*) FROM Classroom_Data WHERE Class=\"" + item[0] + "\"")
            cnt = cur.fetchall()
            cnt = cnt[0][0]
            if cnt==0 and item[1].isdigit()==True:
                cur.execute("SELECT COUNT(*) FROM Classroom_Data")
                data = cur.fetchall()
                print(data[0][0])
                sr_no = int(data[0][0])+1
                cur.execute("INSERT INTO Classroom_Data VALUES (?,?,?)", (sr_no,item[0],item[1]))
                txt = "         Added " + item[0] + " at Sr.no. " + str(sr_no)
                la = tk.Label(self ,text = txt)
                la.grid(row = 16,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            elif item[1].isdigit()==False:
                la = tk.Label(self ,text = "         Strength should be an integer")
                la.grid(row = 16,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "         Class " + item[0] + " already exists")
                la.grid(row = 16,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)

        if type == "profdata":
            cur.execute("SELECT COUNT(*) FROM Professor_Data WHERE FullName=\"" + item[1] + "\"")
            cnt = cur.fetchall()
            cnt = cnt[0][0]
            if cnt==0:
                cur.execute("SELECT COUNT(*) FROM Professor_Data")
                data = cur.fetchall()
                #print(data[0][0])
                sr_no = int(data[0][0])+1
                cur.execute("INSERT INTO Professor_Data VALUES (?,?,?)", (sr_no,item[0],item[1]))
                txt = "       Added " + item[1] + " at Sr.no. " + str(sr_no)
                la = tk.Label(self ,text = txt)
                la.grid(row = 16,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "       Professor " + item[1] + " already added")
                la.grid(row = 16,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        conn.commit()

def edit(self ,type, item):
    if conn is not None:
        cur = conn.cursor()
        if type == "classdata":
            cur.execute("SELECT COUNT(*) FROM Classroom_Data WHERE Class = \""+ item[0] +"\"")
            data = cur.fetchall()
            if int(data[0][0])>0 and item[1].isdigit()==True:
                cur.execute("UPDATE Classroom_Data SET Strength=\"" + item[1] + "\" WHERE Class = \""+ item[0] +"\"")
                la = tk.Label(self ,text = "         Replaced " + item[0] + "'s Strength with " + item[1])
                la.grid(row = 23,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            elif item[1].isdigit()==False:
                la = tk.Label(self ,text = "         Strength should be an integer")
                la.grid(row = 23,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "         No class with name: " + item[0])
                la.grid(row = 23,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        if type == "profdata":
            cur.execute("SELECT COUNT(*) FROM Professor_Data WHERE FullName = \""+ item[1] +"\"")
            data = cur.fetchall()
            if int(data[0][0])>0:
                cur.execute("UPDATE Professor_Data SET ShortName=\"" + item[0] + "\" WHERE FullName = \""+ item[1] +"\"")
                la = tk.Label(self ,text = "       Replaced " + item[1] + "'s ShortName with " + item[0])
                la.grid(row = 23,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "       No Professor with name: " + item[1])
                la.grid(row = 23,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        if type == "clgdata":
            cur.execute("SELECT COUNT(*) FROM Course_Data WHERE Course_No = \""+ item[0] +"\"")
            data = cur.fetchall()
            if int(data[0][0])>0:
                profs = (item[3]).split(',')
                print(profs)
                flag=True
                for prof in profs:
                    prof = prof.strip()
                    cur.execute("SELECT COUNT(*) FROM Professor_Data WHERE ShortName = \""+ prof +"\"")
                    data2 = cur.fetchall()
                    if int(data2[0][0])==0:
                        flag=False
                        la = tk.Label(self ,text = "         No Professor with name " + prof)
                        la.grid(row = 23,column = 0)
                        la.config(fg="red")
                        la.after(4000, la.destroy)
                        break
                if flag==True:
                    x = (item[3]).replace(" ","")
                    x = (x).replace(",",", ")
                    cur.execute("UPDATE Course_Data SET Course_Title=\"" + item[1] + "\", Credits_L_T_P_C=\""+ item[2] + "\", Instructor=\"" + x + "\" WHERE Course_No = \""+ item[0] +"\"")
                    la = tk.Label(self ,text = "         Replaced " + item[0] + "'s data")
                    la.grid(row = 23,column = 0)
                    la.config(fg="blue")
                    la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "       No Course with code: " + item[0])
                la.grid(row = 23,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        conn.commit()

def deleteIt(self ,type, item):
    if conn is not None:
        cur = conn.cursor()
        if type == "classdata":
            cur.execute("SELECT COUNT(*) FROM Classroom_Data WHERE Class = \""+ item +"\"")
            cnt = cur.fetchall()
            if int(cnt[0][0])>0:
                cur.execute("SELECT Sr_No FROM Classroom_Data WHERE Class = \""+ item +"\"")
                dels = cur.fetchall()
                cur.execute("SELECT COUNT(*) FROM Classroom_Data")
                ttl_cnt = cur.fetchall()
                cur.execute("DELETE FROM Classroom_Data WHERE Class = \"" + item + "\"")
                print(ttl_cnt)
                dels = int(dels[0][0])
                cur.execute("UPDATE Classroom_Data SET Sr_No=\"" + str(dels) + "\" WHERE Sr_No = \""+ str(ttl_cnt[0][0]) +"\"")
                la = tk.Label(self ,text = "         Deleted " + item)
                la.grid(row = 29,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "         No class with name: " + item)
                la.grid(row = 29,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        if type == "profdata":
            cur.execute("SELECT COUNT(*) FROM Professor_Data WHERE FullName = \""+ item +"\"")
            cnt = cur.fetchall()
            if int(cnt[0][0])>0:
                cur.execute("SELECT Sr_No, ShortName FROM Professor_Data WHERE FullName = \""+ item +"\"")
                dels = cur.fetchall()
                inst_name = str(dels[0][1])
                cur.execute("SELECT COUNT(*) FROM Professor_Data")
                ttl_cnt = cur.fetchall()
                cur.execute("DELETE FROM Professor_Data WHERE FullName = \"" + item + "\"")
                dels = int(dels[0][0])
                cur.execute("UPDATE Professor_Data SET Sr_No=\"" + str(dels) + "\" WHERE Sr_No = \""+ str(ttl_cnt[0][0]) +"\"")
                cur.execute("SELECT Course_No FROM Course_Data WHERE Instructor = \""+ inst_name +"\"")
                crs_list = cur.fetchall()
                for crs in crs_list:
                    cur.execute("UPDATE Course_Data SET Instructor=\""+"N.A."+"\" WHERE Course_No = \""+ str(crs[0]) +"\"")
                cur.execute("SELECT Instructor,Course_No FROM Course_Data")
                inst_list = cur.fetchall()
                for inst in inst_list:
                    crs_num = inst[1]
                    instss = inst[0].split(',')
                    if len(inst[0])>1:
                        for inst1 in instss:
                            inst2 = inst1.strip()
                            if inst2==inst_name:
                                instss.remove(inst1)
                                strr = "\"" + instss[0]
                                for ins in instss[1:]:
                                    strr = strr + ", " + ins
                                strr = strr + "\""
                                #print(str(strr) + " ------------ " + str(crs_num) + " ---- " + str(inst_name) + " ----- " + str(instss))
                                cur.execute("UPDATE Course_Data SET Instructor="+strr+" WHERE Course_No = \""+ crs_num +"\"")
                                break

                la = tk.Label(self ,text = "         Deleted " + item)
                la.grid(row = 29,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "       No Professor with name: " + item)
                la.grid(row = 29,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        if type == "clgdata":
            cur.execute("SELECT COUNT(*) FROM Course_Data WHERE Course_No = \""+ item +"\"")
            cnt = cur.fetchall()
            if int(cnt[0][0])>0:
                cur.execute("SELECT Sr_No FROM Course_Data WHERE Course_No = \""+ item +"\"")
                dels = cur.fetchall()
                cur.execute("SELECT COUNT(*) FROM Course_Data")
                ttl_cnt = cur.fetchall()
                print(ttl_cnt)
                cur.execute("DELETE FROM Course_Data WHERE Course_No = \"" + item + "\"")
                dels = int(dels[0][0])
                cur.execute("UPDATE Course_Data SET Sr_No=\"" + str(dels) + "\" WHERE Sr_No = \""+ str(ttl_cnt[0][0]) +"\"")
                la = tk.Label(self ,text = "         Deleted " + item)
                la.grid(row = 26,column = 0)
                la.config(fg="blue")
                la.after(4000, la.destroy)
            else:
                la = tk.Label(self ,text = "       No Course with code: " + item)
                la.grid(row = 26,column = 0)
                la.config(fg="red")
                la.after(4000, la.destroy)
        conn.commit()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SelectPage, Class, Teacher, Courses):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("SelectPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
class SelectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select Table to Modify", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=4)
        waste = tk.Label(self, text="")
        waste.grid(row=1, column=0, columnspan=4)
        button1 = tk.Button(self, text="Class", command=lambda: controller.show_frame("Class"))
        button1.grid(row = 2,column = 3)
        button2 = tk.Button(self, text="Professor", command=lambda: controller.show_frame("Teacher"))
        button2.grid(row = 3,column = 3)
        button3 = tk.Button(self, text="Courses", command=lambda: controller.show_frame("Courses"))
        button3.grid(row = 4,column = 3)
        label1 = tk.Label(self, text="Modify classroom data          ")
        label1.grid(row=2, column=0, columnspan=3)
        label2 = tk.Label(self, text="Modify Faculty information    ")
        label2.grid(row=3, column=0, columnspan=3)
        label3 = tk.Label(self, text="Modify Courses data               ")
        label3.grid(row=4, column=0, columnspan=3)

class Class(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Modify Classroom Data", font=controller.title_font)
        label.grid(row=0, column=0)
        a = tk.Label(self ,text = "Class Name").grid(row = 4,column = 0)
        a1 = tk.Entry(self)
        a1.grid(row = 4,column = 2)
        button = tk.Button(self, text="Search",
                            command=lambda: search(self ,"classdata", a1.get()))
        button.grid(row = 10,column = 0)

        # b_2 = tk.Label(self ,text = "Sr_No").grid(row = 12,column = 0)
        # b_1 = tk.Entry(self)
        b0 = tk.Label(self ,text = "Class Name").grid(row = 13,column = 0)
        b1 = tk.Entry(self)
        b2 = tk.Label(self ,text = "Strength").grid(row = 14,column = 0)
        b3 = tk.Entry(self)
        # b_1.grid(row = 12,column = 2)
        b1.grid(row = 13,column = 2)
        b3.grid(row = 14,column = 2)
        button1 = tk.Button(self, text="Add",
                            command=lambda: add(self ,"classdata", (b1.get(), b3.get())))
        #button1.grid(row = 15,column = 0)
        button1.grid(row = 17,column = 0)
        # d_2 = tk.Label(self ,text = "Sr_No").grid(row = 18,column = 0)
        # d_1 = tk.Entry(self)
        d0 = tk.Label(self ,text = "ClassName(Key)").grid(row = 20,column = 0)
        d1 = tk.Entry(self)
        d2 = tk.Label(self ,text = "New Strength").grid(row = 21,column = 0)
        d3 = tk.Entry(self)
        # d_1.grid(row = 18,column = 2)
        d1.grid(row = 20,column = 2)
        d3.grid(row = 21,column = 2)
        button4 = tk.Button(self, text="Replace",
                            command=lambda: edit(self ,"classdata", (d1.get(), d3.get())))
        button4.grid(row = 25,column = 0)

        c = tk.Label(self ,text = "ClassName").grid(row = 27,column = 0)
        c1 = tk.Entry(self)
        c1.grid(row = 27,column = 2)
        button2 = tk.Button(self, text="Delete",
                            command=lambda: deleteIt(self ,"classdata", c1.get()))
        button2.grid(row = 30,column = 0)
        button3 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("SelectPage"))
        button3.grid(row = 32,column = 0)

class Teacher(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Modify Faculty Data", font=controller.title_font)
        label.grid(row=0, column=0)
        a = tk.Label(self ,text = "FullName").grid(row = 4,column = 0)
        a1 = tk.Entry(self)
        a1.grid(row = 4,column = 2)
        button = tk.Button(self, text="Search",
                            command=lambda: search(self ,"profdata", (a1.get()).title()))
        button.grid(row = 10,column = 0)

        # b_2 = tk.Label(self ,text = "Sr_No").grid(row = 12,column = 0)
        # b_1 = tk.Entry(self)
        b0 = tk.Label(self ,text = "ShortName").grid(row = 14,column = 0)
        b1 = tk.Entry(self)
        b2 = tk.Label(self ,text = "FullName").grid(row = 13,column = 0)
        b3 = tk.Entry(self)
        # b_1.grid(row = 12,column = 2)
        b1.grid(row = 14,column = 2)
        b3.grid(row = 13,column = 2)
        button1 = tk.Button(self, text="Add",
                            command=lambda: add(self ,"profdata", ((b1.get()), (b3.get()).title())))
        button1.grid(row = 17,column = 0)

        # d_2 = tk.Label(self ,text = "Sr_No").grid(row = 18,column = 0)
        # d_1 = tk.Entry(self)
        d0 = tk.Label(self ,text = "New ShortName").grid(row = 21,column = 0)
        d1 = tk.Entry(self)
        d2 = tk.Label(self ,text = "FullName(Key)").grid(row = 20,column = 0)
        d3 = tk.Entry(self)
        # d_1.grid(row = 18,column = 2)
        d1.grid(row = 21,column = 2)
        d3.grid(row = 20,column = 2)
        button4 = tk.Button(self, text="Replace",
                            command=lambda: edit(self ,"profdata", ((d1.get()), (d3.get()).title())))
        button4.grid(row = 25,column = 0)

        c = tk.Label(self ,text = "FullName").grid(row = 27,column = 0)
        c1 = tk.Entry(self)
        c1.grid(row = 27,column = 2)
        button2 = tk.Button(self, text="Delete",
                            command=lambda: deleteIt(self ,"profdata", (c1.get()).title()))
        button2.grid(row = 30,column = 0)
        button3 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("SelectPage"))
        button3.grid(row = 32,column = 0)

class Courses(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Modify Course Data", font=controller.title_font)
        label.grid(row=0, column=0)
        a = tk.Label(self ,text = "Course_No").grid(row = 4,column = 0)
        a1 = tk.Entry(self)
        a1.grid(row = 4,column = 2)
        button = tk.Button(self, text="Search",
                            command=lambda: search(self ,"clgdata", (a1.get()).upper()))
        button.grid(row = 12,column = 0)
        d0 = tk.Label(self ,text = "Course_No(Key)").grid(row = 15,column = 0)
        d1 = tk.Entry(self)
        d2 = tk.Label(self ,text = "New Course_Title").grid(row = 16,column = 0)
        d3 = tk.Entry(self)
        d4 = tk.Label(self ,text = "New Credits_L_T_P_C").grid(row = 17,column = 0)
        d5 = tk.Entry(self)
        d6 = tk.Label(self ,text = "New Instructor(ShortName)").grid(row = 18,column = 0)
        d7 = tk.Entry(self)
        d1.grid(row = 15,column = 2)
        d3.grid(row = 16,column = 2)
        d5.grid(row = 17,column = 2)
        d7.grid(row = 18,column = 2)
        button4 = tk.Button(self, text="Replace",
                            command=lambda: edit(self ,"clgdata", ((d1.get()).upper(), d3.get(), d5.get(), (d7.get()))))
        button4.grid(row = 21,column = 0)

        c = tk.Label(self ,text = "Course_No").grid(row = 24,column = 0)
        c1 = tk.Entry(self)
        c1.grid(row = 24,column = 2)
        button2 = tk.Button(self, text="Delete",
                            command=lambda: deleteIt(self ,"clgdata", (c1.get()).upper()))
        button2.grid(row = 27,column = 0)
        button3 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("SelectPage"))
        button3.grid(row = 30,column = 0)

def main():
    app = SampleApp()
    app.mainloop()
