import sqlite3 as lite
import csv
import sys

con = None

try:
    con = lite.connect('test.db')

    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS profdata")
    cur.execute("CREATE TABLE IF NOT EXISTS Professor_Data ('Sr_No' TEXT, 'ShortName' TEXT, 'FullName' TEXT);")
    file= open('teachers.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    line_count=0
    for t in dr:
        if(line_count==0):
            line_count=line_count+1
        else:
            cur.execute("INSERT INTO Professor_Data Values (?,?,?)", t)
    file.close()    
    con.commit()

    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS Classroom_Data")
    cur.execute("CREATE TABLE IF NOT EXISTS Classroom_Data ('Sr_No' TEXT, 'Class' TEXT, 'Strength' TEXT);")    
    file= open('class.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    line_count=0
    for t in dr:
        if(line_count==0):
            line_count=line_count+1
        else:
            cur.execute("INSERT INTO Classroom_Data Values (?,?,?)", t)
    file.close()    
    con.commit()

    cur = con.cursor()  
    #cur.execute("DROP TABLE IF EXISTS Course_Data")
    cur.execute("CREATE TABLE IF NOT EXISTS Course_Data ('Sr_No' TEXT, 'Course_No' TEXT, 'Course_Title' TEXT, 'Credits_L-T-P-C' TEXT, 'Instructor' TEXT, 'MS_Mtech_PhD_IphD' TEXT, '1st_Sem' TEXT, '3rd_Sem_CS' TEXT, '3rd_Sem_EE' TEXT,  '3rd_Sem_ME' TEXT, '3rd_Sem_CE' TEXT, '5th_Sem_CS' TEXT, '5th_Sem_EE' TEXT, '5th_Sem_ME' TEXT, '5th_Sem_CE' TEXT, '7th_Sem_CE' TEXT, '7th_Sem_CS' TEXT, '7th_Sem_EE' TEXT, '7th_Sem_ME' TEXT, 'MV_1st_sem' TEXT, 'MV_3rd_sem' TEXT, 'MS_1st_sem' TEXT, 'MS_3rd_sem' TEXT,  'MP_1st_sem' TEXT, 'MP_3rd_sem' TEXT,  'MA_1st_sem' TEXT, 'MA_3rd_sem' TEXT,  'Mtech_EEM_1st_sem' TEXT, 'Mtech_EEM_3rd_sem' TEXT, 'Mtech_MES_1st_sem' TEXT,   'Mtech_MES_3rd_sem' TEXT, 'Mtech_STE_1st_sem' TEXT,  'Mtech_STE_3rd_sem' TEXT,   'MT_Bio_1st_sem' TEXT, 'MT_Bio_3rd_sem' TEXT, 'MSc_chem_1st_sem' TEXT,  'MSc_Chem_3rd_sem' TEXT, 'MSc_math_1st_sem' TEXT, 'MSc_math_3rd_sem' TEXT, 'MSc_Physics_1st_sem' TEXT, 'MSc_Physics_3rd_sem' TEXT, 'IPhD_1st_sem' TEXT, 'IPhD_3rd_sem' TEXT, 'IPhD_5th_sem' TEXT, 'Competence' TEXT);")    
    file= open('courses.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    line_count=0
    for t in dr:
        if(line_count==0):
            line_count=line_count+1
        else:
            cur.execute("INSERT INTO Course_Data Values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", t)
    file.close()    
    con.commit()


finally:    
    if con:
        con.close()