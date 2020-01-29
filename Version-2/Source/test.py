import sqlite3 as lite
import csv
import sys

con = None
try:
    con = lite.connect('timetable_database.db')
    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS profdata")
    cur.execute("CREATE TABLE IF NOT EXISTS Professor_Data ('Sr_No' TEXT, 'ShortName' TEXT, 'FullName' TEXT);")
    if(cur.execute("SELECT COUNT() FROM Professor_Data").fetchone()[0] == 0):
        file= open('teachers.csv', 'r', encoding="utf8")
        dr = csv.reader(file, delimiter= ',',)
        line_count=0
        for t in dr:
            if(line_count==0):
                line_count=line_count+1
            else:
                t[0] = t[0].strip()
                t[1] = t[1].strip()
                t[2] = t[2].strip()
                cur.execute("INSERT INTO Professor_Data Values (?,?,?)", t)
        file.close()    
        con.commit()

    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS Classroom_Data")
    cur.execute("CREATE TABLE IF NOT EXISTS Classroom_Data ('Sr_No' TEXT, 'Class' TEXT, 'Strength' TEXT);")    
    if(cur.execute("SELECT COUNT() FROM Classroom_Data").fetchone()[0] == 0):
        file= open('class.csv', 'r', encoding="utf8")
        dr = csv.reader(file, delimiter= ',',)
        line_count=0
        for t in dr:
            if(line_count==0):
                line_count=line_count+1
            else:
                t[0] = t[0].strip()
                t[1] = t[1].strip()
                t[2] = t[2].strip()
                cur.execute("INSERT INTO Classroom_Data Values (?,?,?)", t)
        file.close()    
        con.commit()

    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS Course_Data")
    file= open('courses.csv', 'r', encoding="utf8")
    dr = csv.reader(file, delimiter= ',',)
    line_count=0
    col_nums=0
    for t in dr:
        col_nums = len(t)
        break
    #print(col_nums)
    if(cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Course_Data'").fetchone()[0] ==0):
        lis1 = []
        for i in range(col_nums-5):
            x = "col_" + str(i+6)
            string = ", '" + x + "' TEXT"
            lis1.append(string)
        string = "".join(lis1)
        cur.execute("CREATE TABLE IF NOT EXISTS Course_Data ('Sr_No' TEXT, 'Course_No' TEXT, 'Course_Title' TEXT, 'Credits_L_T_P_C' TEXT, 'Instructor' TEXT" + string +  ");")    
        for t in dr:
            # if(line_count==0):
            #     line_count=line_count+1
            # else:
            list1 = []
            for i in range(col_nums-1):
                list1.append(',?')
            string = "(?" + "".join(list1) + ")"
            t[1] = t[1].replace(" ", "")
           # print(t[1])
            cur.execute("INSERT INTO Course_Data Values " + string, t)
        file.close()    
        con.commit()

    cur = con.cursor()
    if(cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Basket_1'").fetchone()[0] ==0):
        file = open('baskets.csv', 'r', encoding="utf8")
        dr = csv.reader(file, delimiter= ',')
        line_count=0
        basket_nums=0
        for t in dr:
            if(line_count==0):
                basket_nums=len(t)
                line_count=line_count+1
                for i in range(basket_nums):
                    table = "Basket_" + str(i+1)
                    cur.execute("CREATE TABLE IF NOT EXISTS " + table + " ('Course_No' TEXT);")
            else:
                basket_nums=len(t)
                for i in range(basket_nums):
                    table = "Basket_" + str(i+1)
                    t[i] = t[i].replace(" ", "")
                    cur = con.cursor()
                    cur.execute("INSERT INTO " + table + " Values (?)", (t[i],))
                    con.commit()

        file.close()

    file = open('baskets.csv', 'r', encoding="utf8")
    dr = csv.reader(file, delimiter= ',',)
    basket_nums=0
    for t in dr:
        basket_nums=len(t)
        break
    file.close()

finally:    
    if con:
        con.close()
