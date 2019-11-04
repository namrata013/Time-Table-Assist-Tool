import sqlite3
from sqlite3 import Error
import sys
from string import ascii_uppercase

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e) 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"test.db"
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