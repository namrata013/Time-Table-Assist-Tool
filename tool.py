import sqlite3 as lite
from sqlite3 import Error
import sys
import string
from string import ascii_uppercase
import allocate
from test import basket_nums
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



def allocation(slot,course,classroom,row_no,conn):
    if conn is not None:
        cur = conn.cursor()

        #pre added course anomaly
        cur.execute("SELECT * FROM Allocated_Subjs")
        data = cur.fetchall()
        for row in data:
            if(course==str(row[0])):
                print("Course already added!\n")
                return None

        #classroom clash
        cur.execute("SELECT * FROM Allocated_Subjs WHERE Slot =?",(slot))
        data = cur.fetchall()
        for row in data:
            classe = str(row[2])
            if(classe==classroom):
                print("classroom " + classe + " allotted twice in slot " + slot + " in " + str(row[0]) + " and " + course + ".\n")
                return None

        #instructor clash
        cur.execute("SELECT * FROM Course_Data WHERE Course_No=?", (course,))
        data=cur.fetchall()[0]
        instructors = str(data[4])
        instructors_list1 = instructors.split(',')
        instructors_list2 = instructors.split('/')
        l1 = len(instructors_list1)
        l2 = len(instructors_list2)
        if(l1>=l2):
            instructors_list = instructors_list1
        else:
            instructors_list = instructors_list2
        cur.execute("SELECT * FROM Instructor_Slots WHERE Slot =?",(slot))
        teacher = cur.fetchall()
        for i in instructors_list1:
            i = i.strip()
            i = i.lower()
            for row in teacher:
                y = str(row[1])
                y=y.lower()
                if(i==y):
                    print("Faculty " + str(row[0]) + " is getting "+ course + " and " + str(row[3]) + " in slot " + slot + "!\n")
                    return None
        for i in instructors_list2:
            i = i.strip()
            i = i.lower()
            for row in teacher:
                y = str(row[1])
                y=y.lower()
                if(i==y):
                    print("Faculty " + str(row[0]) + " is getting "+ course + " and " + str(row[3]) + " in slot " + slot + "!\n")
                    ans =input("Do you still wanna proceed (y/n)?\n")
                    if(ans == "n"):
                        return None
        
        #core clash
        i=5
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
                            print("Core Course Clash with " + subject + "!\n")
                            return None 

        #basket clash        
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
                    break;
            if(found==1):
                for row in data:
                    subject = str(row[0])
                    subject = subject.strip()
                    cur.execute("SELECT * FROM Allocated_Subjs WHERE Course_No =?", (subject,))
                    D = cur.fetchall()
                    if(D):
                        col = str(D[0][1]) 
                        if(slot==col):
                            print("Basket Clash with " +subject + "!\n")
                            return None   

        #allocation
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
                    cur.execute("INSERT INTO Instructor_Slots Values (?,?,?,?)", (name,i,slot,course))
                    conn.commit()
        cur = conn.cursor()
        cur.execute("INSERT INTO Allocated_Subjs Values (?,?,?,?)", (course,slot,classroom, str(row_no)))
        conn.commit()

    else:
        print("Error! cannot create the database connection.")  


#def deleteCourse(course, slot):


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


def checkClass(classroom,conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Classroom_Data")
    data = cur.fetchall()
    for row in data:
        classs = str(row[1])
        classs= classs.strip()
        if(classroom == classs):
            return 1
    return 0


def checkSlot(slot):
    for i in ascii_uppercase:
        if(slot==i):
            return 1
        if(i=="H"):
            return 0


def UserInterface(conn):
    print("Choose a subject to allocate slot and classroom:\nCS|EE|ME|CE|IC|HS|EN|DP|PH|MA|BY|CY\n")
    string = input()
    chooseCourse(string,conn)
    print("Choose a course in " + string + " :\n")
    course = input()
    course = course.upper()
    course = course.strip()
    course = course.replace(" ", "")

    print("Choose a slot:\n")
    slot = input()
    slot = slot.upper()
    slot =slot.strip()
    while(checkSlot(slot)==0):
        slot = input("No such slot! Enter again.")

    print("List of Classrooms:\n")
    viewClassrooms(conn)
    print("Choose a classroom:\n")
    classroom = input()
    classroom = classroom.strip()
    while(checkClass(classroom,conn)==0):
        classroom = input("No such classroom! Enter again.")

    row = 8

    allocation(slot,course,classroom,row,conn)


    
def main():
    db= r"test.db"
    conn = allocate.create_connection(db)
    UserInterface(conn) 
    
    if conn:
        conn.close()


if __name__ == '__main__':
    main()