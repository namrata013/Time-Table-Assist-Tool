import sqlite3
from sqlite3 import Error
import sys
from string import ascii_uppercase

''' Function: create_connection
   create a database connection to the SQLite database specified by db_file

    Parameters:
       db_file - database file
      
    Returns:
       Connection object or None
'''
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e) 
    return conn


''' Function: create_table
   create a table from the create_table_sql statement

    Parameters:
       conn - Connection object
       create_table_sql - a CREATE TABLE statement
      
    Returns:
       no return value
'''
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"timetable_database.db"
    # create a database connection
    conn = create_connection(database) 
    # create tables
    if conn is not None:

        #create allocated subjects and allocated instructors tables
        query = "CREATE TABLE IF NOT EXISTS Allocated_Subjs ('Course_No' text PRIMARY KEY, 'Slot' text NOT NULL, 'Class' text, 'Row_No' text);"
        create_table(conn, query)
        query = "CREATE TABLE IF NOT EXISTS Instructor_Slots ('FullName' text, 'ShortName' text, 'Slot' text NOT NULL, 'Course_No' text);"
        create_table(conn, query)

    else:
        print("Error! cannot create the database connection.")
    
    if conn:
        conn.close()

if __name__ == '__main__':
    main()