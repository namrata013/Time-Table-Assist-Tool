# CS308 Final Project - Time Table Assist Tool
## Team No - 9
#### Team Members are : 

###### Akhil Rajput : B17033
###### Suraj Kumar : B17064
###### Aashima : B17031
###### Namrata Malkani : B17096

 A python, SQLite based assist tool.

## Tools and Technologies

* Python 3
* Tkinter Library for GUI
* SQLite for Database Management

## About the application

#### Raw Data (User Dependent)

* These excel/odt files would specify what are the tables and column fields. These need to be converted to CSV format in order to be imported in SQL Database. 
* User will be responsible that the CSV files and Database are compatible.

#### Database

The Database is mainly divided in two parts.
* One with 3 prepopulated tables that are created in the beginning by the user provided raw data. (test.db)
* Other with 8 tables created at run time in order to practice the constraints and display results, errors and warnings. (runtime.db)

#### Graphic User Interface (GUI)

This is how the user is able to utilize the tool. The interface is created on tkinter module for version 1 of the software.

## Pre-requisites - Local

* Python 3 (mostly preinstalled, preferably version 3.6 and above)
* Tkinter Library (sudo apt-get install python3-tk or sudo apt-get install python3.6-tk)
* SQLite3 (sudo apt-get install SQLite3)

## Getting Started

* Clone the repo. (i.e. git clone https://github.com/namrata013/Time-Table-Assist-Tool.git)

## Building & Running

Once you have the pre-requisite services up, then you are ready to build and run the application. To run the application open terminal and type the following commands:
* cd Time-Table-Assist-Tool
* cd GUI
Check your python version. If you have version 3.6 and above:
* python3 gui.py
else if the version is 3.5:
* which python3
copy the output that thsi command prints. Say, it is "/usr/bin/python3" (as in most cases).
* /usr/bin/python3 gui.py
* You will be able to run the application because of the database provided by us already. You can use this tool for yourself by deleting the csv files from ./Time-Table-Assist-Tool/Database and providing your own ones. But compatibility should be taken care of.

## Releases

There are 2 releases. The current Version-1.0 is able to notify of the errors and display the updated tables on run time. Version-2 is is targetted to come equipped with better GUI and better management and inclusion of more database based constraints.

