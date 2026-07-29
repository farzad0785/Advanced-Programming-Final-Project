Student Management & Analytics System.
A Python-based educational system management project built for an Advanced Programming course. 
It manages student records, courses, and majors, and provides GPA calculation, transcript viewing, sorting, and statistical analysis of grades.

Two reports are in the docs directory in both English and Persian, and codes are in the src directory.

The project is organized into 8 modules, each with a single responsibility. Modules import functions or classes from one another as needed.
1. Utils.py
	General-purpose helper functions used across the program: input validation (e.g. checking capitalization, numeric input) and a custom sorting utility.
2. Major.py
   Manages fields of study (majors), validating and storing them for use by other classes.
3. Person.py
  Parent class for Student; validates and stores personal info (first name, last name, national ID).
4. Student.py
  Child class of Person. Stores student ID, degree level, major, term, course codes, and grades.
  Handles GPA calculation, transcript generation, adding/removing courses, and pass/fail checks. Implements dunder-methods to compare students by GPA.
5. Subject.py
  Manages the courses offered each term (code, name, units) and validates course selection. Implements dunder methods to compare courses by unit count.
6. EduSysManager.py
  Central manager that coordinates all students: add/remove students, add/remove courses, search, and sort.
7. Analytics.py
  Computes grade statistics (max, min, mean, standard deviation, pass/fail counts) for students filtered by a chosen basis and key (e.g. degree level, term, major, course).
8. Main.py
  Entry point of the program; drives a command-based interactive session using a dictionary of available commands.

Requirements: 1. Python 3.x | 2. NumPy

Getting Started:
python Main.py

Follow the on-screen prompts to manage students, courses, and run analytics. Exit at any time via the program's exit command.
Author: Ali Asghar Rashidabadi — Computer Sciencem
