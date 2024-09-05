# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Hoang Nguyen,09/03/2024,Created Script
#   
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ""  # Holds combined string data separated by a comma.
json_data: str = ""  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str = ""  # Hold the choice made by the user.

# Processing --------------------------------------- #
class FileProcessor:
    # Functions that work with Json files

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        # Read the data from the file
        try:
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            raise ValueError ("File not found.", e)
        except Exception as e:
            raise ValueError ("There was non-specific error!", e)
        
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Write data from the list of dict. to file
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print(f"Data successfully saved to {FILE_NAME}")
        except Exception as e:
            raise ValueError("There was a error occured while writing to the file", e)
        
class IO:
    # Functions that perform input and output tasks from user
    pass

    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        if error:
            print(f"{message}: {error}")
        else:
            print(message)

    @staticmethod
    def output_menu(menu: str):
        # Display a menu
        print(menu)

    @staticmethod
    def input_menu_choice():
        #choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2","3","4"):
                print("Please select only 1, 2, 3, or 4")
        except Exception as e:
            raise ValueError(e)
        return choice
    
    @staticmethod
    def output_student_courses(student_data: str):
        # Display the current data
        print("Current Student Registration: ")
        for row in student_data:
            print(f"{row['FirstName']} {row['LastName']} {row['Course']}")
        print()

    @staticmethod
    def input_student_data(student_data: list):
        #Student Data for the user
        try:
            student_first_name= input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError ("The first name should not contain numbers. ")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError ("The last name should not contain numbers. ")
            course_name = input("Enter the course name: ")
            if not course_name.isalpha():
                raise ValueError ("The Cours name should contain a letter")
            student_data = {"FirstName":student_first_name, 
                            "LastName": student_last_name, 
                            "Course":course_name.strip()}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
             print(e)
             print("-- Technical Error Message -- ")
        except Exception as e:
             print("--Technical Error Message--")
             print("Run into unexpected exception: {e}")
        return student_data
    
FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data= students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    if menu_choice == "2":
        IO.output_student_courses(students)
    
    if menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    
    elif menu_choice == "4":
        print("Exiting the program")
        break
    else:
        print("Please only choose option 1, 2, 3 or 4")