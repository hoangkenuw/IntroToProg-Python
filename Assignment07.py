# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Hoang Nguyen, 09/08/2024,Created Script
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables

students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:

    def __init__(self,first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def first_name(self):
        return self.__first_name.title()
    
    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")
        
    @property
    def last_name(self):
        return self.__last_name.title()
    
    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
    
    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str =""):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name
    
    @property
    def course_name(self):
        return self.course_name
    
    @course_name.setter
    def course_name(self, value: str):
        try:
            self.course_name = value
        except ValueError:
            raise ValueError("Course name cannot be empty.")
            
    # TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"


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
        return student_data
        
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Write data from the list of dict. to file
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print(f"Data successfully saved to {FILE_NAME}")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
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
            student = {"FirstName":student_first_name, 
                            "LastName": student_last_name, 
                            "Course":course_name.strip()}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
             print(e)
        except Exception as e:
             print("Run into unexpected exception: {e}")
        return student_data

 # Main Body   
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data= students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    if menu_choice == "2":
        IO.output_student_courses(students)
    
    if menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        IO.output_student_courses(students)
    
    elif menu_choice == "4":
        print("Exiting the program")
        break

