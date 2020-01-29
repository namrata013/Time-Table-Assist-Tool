import sqlite3
from sqlite3 import Error
import csv
import sys
import os
import allocate
import numpy
import string
from string import ascii_uppercase

def main():
    db = r"timetable_database.db"
    conn = allocate.create_connection(db)
    if conn is not None:
        
        # cur = conn.cursor()  
        # #cur.execute("DROP TABLE IF EXISTS Course_Data")
        # file= open('prev_courses.csv', 'r', encoding="utf8")
        # dr = csv.reader(file, delimiter= ',',)
        # line_count=0
        # col_nums=0
        # for t in dr:
        #     col_nums = len(t)
        #     break
        #print(col_nums)
        # if(cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Course_Data'").fetchone()[0] ==0):
            # lis1 = []
            # for i in range(col_nums-5):
            #     x = "col_" + str(i+6)
            #     string = ", '" + x + "' TEXT"
            #     lis1.append(string)
            # string = "".join(lis1)
            # cur.execute("CREATE TABLE IF NOT EXISTS Prev_Course_Data ('Sr_No' TEXT, 'Course_No' TEXT, 'Course_Title' TEXT, 'Credits_L_T_P_C' TEXT, 'Instructor' TEXT" + string +  ");")    
            # for t in dr:
            #     # if(line_count==0):
            #     #     line_count=line_count+1
            #     # else:
            #     list1 = []
            #     for i in range(col_nums-1):
            #         list1.append(',?')
            #     string = "(?" + "".join(list1) + ")"
            #     t[1] = t[1].replace(" ", "")
            # # print(t[1])
            #     cur = conn.cursor()
            #     cur.execute("INSERT INTO Prev_Course_Data Values " + string, t)
            #     conn.commit()
            # file.close()    

        file = open('previous_time_table.csv', 'r', encoding="utf8")
        dr = csv.reader(file, delimiter= ',',)
        slots=0
        line=0
        for t in dr:
            if(slots==0):
                slots = len(t)
            else:
                line=line+1
                for i in range(slots):
                    t[i]=t[i].strip()
                    t[i]=t[i].upper()
                    t[i]=t[i].replace(" ","")
                    subj = ""
                    classroom = ""
                    f=0
                    for j in t[i]:
                        if(j==")"):
                            break
                        if(f==1):
                            classroom=classroom+j
                        if(j=="("):
                            f=1
                        if(f==0):
                            subj=subj+j
                    slot = ascii_uppercase[i]
                    row_no = line
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Allocated_Subjs WHERE Course_No=?", (subj,))
                    D = cur.fetchall()
                    if(len(subj)!=0 and len(D)==0):
                        cur.execute("SELECT * FROM Course_Data WHERE Course_No=?", (subj,))
                        # print(subj)
                        data = cur.fetchall()
                        # if(D):
                        #     print(D)
                        if(data):
                            instructors = str(data[0][4])
                            instructors_list1 = instructors.split(',')
                            instructors_list2 = instructors.split('/')
                            l1 = len(instructors_list1)
                            l2 = len(instructors_list2)
                            instructors_list = []
                            if(l1>=l2):
                                instructors_list = instructors_list1
                            else:
                                instructors_list = instructors_list2

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
                                        cur.execute("INSERT INTO Instructor_Slots Values (?,?,?,?)", (name,i,slot,subj))
                                        conn.commit()
                        cur = conn.cursor()
                        cur.execute("INSERT INTO Allocated_Subjs Values (?,?,?,?)", (subj, slot,classroom, str(row_no)))
                        conn.commit()        
        file.close()
    if conn:
        conn.close()

if __name__ == '__main__':
    main()