Project Statement: Simple Student Database Management System (SDMS)

1. Problem Statement

Educational institutions require a simple, reliable method to manage student records. The primary challenge is to create a foundational, console-based application that ensures data persistence—meaning records must be securely saved to disk and reliably loaded back into memory across different execution sessions. This system must perform essential data management operations without relying on complex external database technologies.

2. Scope of the Project

The scope is limited to a fundamental, single-user, command-line interface (CLI) application.

Inclusions (What the project does):

Implementation of the core CRUD (Create, Read, Update, Delete) operations.

Data storage and retrieval via a local CSV file (student_data.csv).

Error handling for "record not found" scenarios.

Exclusions (What the project does not include):

A Graphical User Interface (GUI).

Advanced database features like complex query languages or concurrency control.

Input validation (e.g., checking if IDs are unique or if input is numeric).

3. Target Users

The primary target users for this system are:

Administrative Staff: Individuals or small teams who need a simple, local tool to maintain a registry of student data.

Students/Developers: Individuals learning Python who require a practical example of file I/O, modular programming, and data management principles.

4. High-Level Features

The application provides a menu-driven interface with the following high-level capabilities:

Record Creation (Insert): Entry of new student records (ID, Name, Branch, Year, etc.).

Data Persistence: Automatic saving of all changes to the CSV file and loading of data on startup.

Data Retrieval: Options to display all student records or search for a specific record by Student ID.

Record Modification: Ability to update specific fields (the academic year) of an existing record.

Record Deletion: Permanent removal of records based on the unique Student ID.
