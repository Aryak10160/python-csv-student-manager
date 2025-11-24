# python-csv-student-manager
Python CLI-based Student Management System (SDMS). Performs full CRUD operations on student records (ID, Name, Year). Ensures data persistence using the standard csv module for file storage and retrieval. Modular, simple, and reliable.
 
Simple Student Database Management System (SDMS)

Overview

This is a minimalist, command-line interface (CLI) application built in Python for managing student records. It performs essential CRUD (Create, Read, Update, Delete) operations and ensures data persistence by storing all records in a simple CSV file.

This project demonstrates core Python concepts including file handling, list manipulation, modular programming (functions), and the use of the csv and os standard libraries.

Features

The application is menu-driven and offers the following functionality:

Insert Data: Create and save a new student record.

Display Data (Single): Search for and display a student record using their unique Student ID.

Delete Data: Remove a student record from the database using their Student ID.

Update Year: Modify the academic year of an existing student record using their Student ID.

Display All: View all records currently stored in the database.

Exit: Save all current changes and terminate the application.

Technologies & Tools

Language: Python 3

Libraries:

csv: Used for reading and writing data to the persistent file.

os: Used to check for the existence of the data file (student_data.csv).

Data Storage: Local CSV file (student_data.csv).

Installation and Setup

Prerequisites

You need to have Python 3 installed on your system.

Steps to Run

Clone the Repository (or download the file):

git clone [YOUR_REPOSITORY_URL]
cd student-database-management


Ensure File is Present: Make sure the main script (studentdatabasemanagement 2.py) is in your current directory.

Execute the Script:

python studentdatabasemanagement 2.py


Start Interacting: The main menu will appear, prompting you to enter a choice (1-6).

Instructions for Use

Upon running the script, you will see the following menu:

====Menu====
1. insert data
2. display data (single)
3. delete data
4. update year
5. display all
6. exit
enter your choice: 


Key Operational Notes:

Initial Run: If student_data.csv does not exist, the application will create it automatically when the first record is inserted.

Persistence: All changes (insertions, updates, deletions) are immediately saved to student_data.csv.

Search Key: All operations (Display, Delete, Update) rely on the unique Student ID as the search key.

Testing

To test the application, follow these simple manual steps:

Test Case: Data Persistence

Steps: Insert a new record (e.g., ID: S101). Choose option 6 (Exit). Rerun the script. Choose option 5 (Display All).

Expected Result: The record S101 must be successfully loaded from the CSV file and displayed.

Test Case: Update Functionality

Steps: Insert a record (ID: S102, Year: 1). Choose option 4 and enter S102, setting the new Year to 3. Choose option 2 (Display Single) for S102.

Expected Result: The displayed record for S102 should show '3' for the Year field.

Test Case: Error Handling

Steps: Choose option 3 (Delete) and enter a Student ID that does not exist.

Expected Result: The program should display the message: "student id not found" and return to the main menu without crashing.

File Structure

The project primarily consists of two files:

studentdatabasemanagement 2.py: The main Python script containing all the application logic and menu system.

student_data.csv: The automatically generated file used for persistent storage of the student records.
