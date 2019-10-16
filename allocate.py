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
        # create projects table
        limit=8
        index=0
        for i in ascii_uppercase:
        	tabName="slot"+i
        	index+=1
        	sql_create_table = "CREATE TABLE IF NOT EXISTS " + tabName + " ('Course No.' text NOT NULL, 'Instructor' text, 'Class' text);"
        	create_table(conn, sql_create_table) 
        	if index==limit:
        		break;

    else:
    	print("Error! cannot create the database connection.")
    
	if con:
		con.close()

if __name__ == '__main__':
    main()