import sqlite3 as lite
from sqlite3 import Error
import sys
import string
import allocate
from test import col_nums

exec(open("./test.py").read()) 
exec(open("./allocate.py").read()) 

def execute_query(conn, query,printf):
    try:
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if(printf==1):
            for row in data:
                print(row)
        conn.commit()
        return data

    except Error as e:
        print(e)



def chooseCourse(string, conn):
    string =string.upper()
    if conn is not None:
        Col = "Course_No"
        query = "SELECT DISTINCT " + Col + " FROM Course_Data WHERE " + Col + " LIKE '" + string + "%'"
        d= execute_query(conn,query,1)
    else:
        print("Error! cannot create the database connection.")



def allocation(table,course,classroom,conn):
    if conn is not None:
        if(table[0]=='L'):
            slot = str(table)
        else:
            slot = str(table[4])
        cur = conn.cursor()

        #pre added course anomaly
        cur.execute("SELECT * FROM Allocated_Subjs")
        data = cur.fetchall()
        for row in data:
            if(course==str(row[0])):
                print("Course already added!\n")
                return None

        #classroom clash
        cur.execute("SELECT * FROM " + table)
        data = cur.fetchall()
        for row in data:
            classe = str(row[1])
            if(classe==classroom):
                print("classroom " + classe + " allotted twice in slot " + slot + " in " + str(row[0]) + " and " + course + ".\n")
                return None

        #instructor clash
        cur.execute("SELECT * FROM Course_Data WHERE Course_No=?", (course,))
        data=cur.fetchall()[0]
        instructors = str(data[4])
        instructors = instructors.split(',')
        cur.execute("SELECT * FROM Instructor_Slots WHERE Slot =?",(slot))
        teacher = cur.fetchall()
        for i in instructors:
            i = i.strip()
            for row in teacher:
                y = str(row[1])
                if(i==y):
                    print("Faculty " + str(row[0]) + " is getting "+ course + " and " + str(row[3]) + " in slot " + slot + "!\n")
                    return None
        
        #core clash
        i=6
        may_clash = []
        while(i<44):
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
                            print("Core Course Clash with " + subject + "!\n")
                            return None 

        #basket clash        
        for i in range(col_nums):
            found=0
            tab = "Basket_" + str(i+1)
            cur.execute("SELECT * FROM " + tab)
            data = cur.fetchall()
            for row in data:
                subject = str(row[0])
                subject = subject.strip()
                subject = subject[:2]+" "+subject[2:]
                if(subject==course):
                    found=1
                    break;
            if(found==1):
                for row in data:
                    subject = str(row[0])
                    subject = subject.strip()
                    subject = subject[:2]+" "+subject[2:]
                    cur.execute("SELECT * FROM Allocated_Subjs WHERE Course_No =?", (subject,))
                    D = cur.fetchall()
                    if(D):
                        col = str(D[0][1]) 
                        if(slot==col):
                            print("Basket Clash with " +subject + "!\n")
                            return None   

        #allocation
        for i in instructors:
            i = i.strip()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Professor_Data")
            data = cur.fetchall()
            for row in data:
                name = ""
                shortname = str(row[1])
                shortname = shortname.strip()
                if(i==shortname):
                    name = str(row[2])
                    cur.execute("INSERT INTO Instructor_Slots Values (?,?,?,?)", (name,i,slot,course))
                    conn.commit()
        cur = conn.cursor()
        cur.execute("INSERT INTO " + table + " Values (?,?)", (course,classroom))
        conn.commit()
        cur = conn.cursor()
        cur.execute("INSERT INTO Allocated_Subjs Values (?,?)", (course,slot))
        conn.commit()

    else:
        print("Error! cannot create the database connection.")  



def viewClassrooms(conn):
    if conn is not None:
        print("List of Classrooms:\n")
        query = "SELECT DISTINCT * FROM Classroom_Data"
        d= execute_query(conn,query,1)
    else:
        print("Error! cannot create the database connection.")



def viewFaculties(conn):
    if conn is not None:
        print("List of Faculties:\n")
        query = "SELECT ShortName, FullName FROM Professor_Data"
        d= execute_query(conn, query,1)
    else:
        print("Error! cannot create the database connection.")



def viewCoursesinSlot(conn,slot):
    table = "slot"+slot
    if conn is not None:
        print("List of courses in slot " + slot + ":\n")
        query = "SELECT Course_No FROM " + table
        d= execute_query(conn, query,1)
    else:
        print("Error! cannot create the database connection.") 


def viewFacultiesinSlot(conn,slot):
    table = "slot"+slot
    if conn is not None:
        print("List of Faculties in slot " + slot + ":\n")
        query = "SELECT FullName FROM Instructor_Slots WHERE Slot = " + slot
        d= execute_query(conn, query,1)
    else:
        print("Error! cannot create the database connection.")


def viewAllCoursesAllocated(conn):
    if conn is not None:
        print("List of Courses Allotted:\n")
        query = "SELECT Course_No FROM Allocated_Subjs"
        d= execute_query(conn, query,1)
    else:
        print("Error! cannot create the database connection.")



def UserInterface(conn):
    print("Choose a subject to allocate slot and classroom:\nCS|EE|ME|CE|IC|HS|EN|DP|PH|MA|BY|CY\n")
    string = input()
    chooseCourse(string,conn)
    print("Choose a course in the subject" + string + " :\n")
    course = input()
    print("Choose a slot:\n")
    slot = input()
    print("List of Classrooms:\n")
    viewClassrooms(conn)
    print("Choose a classroom:\n")
    classroom = input()
    slot = slot.upper()
    slot =slot.strip()
    course = course.upper()
    course = course.strip()
    if(course[2]!=" "):
        course = course[:2] + " " + course[2:]
    classroom = classroom.upper()
    classroom = classroom.strip()
    if(slot[0]=='L'):
        table = str(slot)
    else:
        table = "slot"+slot
    allocation(table,course,classroom,conn)


    
def main():
    db= r"test.db"
    conn = allocate.create_connection(db)
    UserInterface(conn) 
    
    if conn:
        conn.close()


if __name__ == '__main__':
    main()