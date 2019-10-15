import sqlite3 as lite
import csv
import sys

con = None

try:
    con = lite.connect('test.db')

    cur = con.cursor()  
    cur.execute("DROP TABLE IF EXISTS profdata")
    cur.execute("CREATE TABLE profdata ('Sr. No.' TEXT, 'ShortName' TEXT, 'FullName' TEXT);")
    file= open('teachers.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    for t in dr:
    	cur.execute("INSERT INTO profdata Values (?,?,?)", t)
    file.close()    
    con.commit()

    cur = con.cursor()  
    cur.execute("DROP TABLE IF EXISTS classdata")
    cur.execute("CREATE TABLE classdata ('Sr. No.' TEXT, 'Class' TEXT, 'Strength' TEXT);")    
    file= open('class.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    for t in dr:
    	cur.execute("INSERT INTO classdata Values (?,?,?)", t)
    file.close()    
    con.commit()

    cur = con.cursor()  
    cur.execute("DROP TABLE IF EXISTS clgdata")
    cur.execute("CREATE TABLE clgdata ('Sr. No.' TEXT, 'Course No.' TEXT, 'Course Title' TEXT, 'Credits L-T-P-C' TEXT, 'Instructor' TEXT);")    
    file= open('data.csv', 'r')
    dr = csv.reader(file, delimiter= ',',)
    for t in dr:
    	cur.execute("INSERT INTO clgdata Values (?,?,?,?,?)", t)
    file.close()    
    con.commit()


finally:    
    if con:
        con.close()