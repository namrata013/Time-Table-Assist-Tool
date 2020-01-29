# CS308 Final Project - Time Table Assist Tool
## Team No - 9
#### Team Members are : 

###### Namrata Malkani : B17096
###### Aashima : B17031
###### Akhil Rajput : B17033

 A python, SQLite based assist tool.

## Tools and Technologies

* Python 3
* Tkinter Library for GUI
* Numpy python module
* SQLite for Database Management

## About the application

#### Raw Data (User Dependent)

* These excel/odt files would specify what are the tables and column fields. These need to be converted to CSV format in order to be imported in SQL Database and must be put in the Time-Table-Assist-Tool folder. 
* User will be responsible that the CSV files and Database are compatible.
 baskets -> baskets.csv
 class -> class.csv
 teachers -> teachers.csv
 courses -> courses.csv
 (Done by test.py)

#### Database

All tables are in test.db
The Database is made of two parts:
* One with 3 + n prepopulated tables that are created in the beginning by the user provided raw data. (Done by test.py)
***Course_Data
***Classroom_Data
***Professor_Data
***Basket_i

Where i can vary between 1 to N and the estimate is found by reading the baskets.csv file.

* Other with 2 tables created at run time in order to practice the constraints and store the created time table efficiently.
***Allocated_Subjs
***Instructor_Slots

#### Graphic User Interface (GUI)

This is how the user is able to utilize the tool. The interface is created on tkinter module.

## Pre-requisites - Local

* Python 3 
* Tkinter Library 
* Numpy Module
* SQLite3 
**For more information on installation, refer to the User Manual. 

## Getting Started

* Clone the repo. (i.e. git clone https://github.com/namrata013/Time-Table-Assist-Tool.git)

## Building & Running

Once you have the pre-requisite services up, then you are ready to build and run the application. To run the application open terminal and type the following commands (for ubuntu users; for instructions regarding windows, refer the user manual):
* cd Time-Table-Assist-Tool
Check your python version. If you have version 3.6 and above:
* python3 gui.py
else if the version is 3.5:
* which python3
copy the output that this command prints. Say, it is "/usr/bin/python3" (as in most cases), then:
* /usr/bin/python3 gui.py
* You will be able to run the application because of the database provided by us already. You can use this tool for yourself by deleting the csv files from ./Time-Table-Assist-Tool/Database and providing your own ones. But compatibility should be taken care of.

## Releases

There are 2 releases. Version-1.0 is able to notify of the anomalies arising from Classroom Constraints and instructor constraints and display the updated tables on run time. Version-2 comes with better GUI, with facility to modify the user provided Database that has been read from the CSVs, ability to store the created time table and display on every run unless deleted by the user themselves and inclusion of Core courses and Basket courses based constraints.

