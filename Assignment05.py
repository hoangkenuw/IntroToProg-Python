# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Hoang Nguyen, 08/26/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

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
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = '' 
student_last_name: str = '' 
course_name: str = ''  
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of dictionary (table)
# Extract the data from the file
try:
    with open(FILE_NAME, "r"):

        for row in file.readlines():
            # Transform the data from the file
            student_data = row.split(',')
            student_data = {"Student First Name":student_data[0], 
                        "Student Last Name": student_data[1], 
                        "Course Name":student_data[2].strip()}
            # Load it into our collection (list of lists)
            students.append(student_data)
except FileNotFoundError:
    print(f"File {FILE_NAME} not found. Creating a file:")
except Exception:
    print("An error occurred. Possible ")


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")  

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                    raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            if not course_name.isalpha():
                    raise ValueError("The course name shoud not contain numbers.")
            student_data = {"First_Name":student_first_name, 
                            "Last_Name": student_last_name, 
                            "Course_Name":course_name.strip()}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
             print(e)
             print("-- Technical Error Message -- ")
        except Exception as error_details:
             print("--Technical Error Message--")
             print("Run into unexpected exception: {error_details}")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for row in students:
            print(f"Student {row['First_Name']}, {row['Last_Name']}, is enrolled in {row['Course_Name']}")
            
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                for row in students:
                    csv_data = f"{row['First_Name']},{row['Last_Name']},{row['Course_Name']}\n"
                    file.write(csv_data)
            print("The following data was saved to the file!")
            for row in students:
                print(f"Student {row['First_Name']} {row['Last_Name']} is enrolled in {row['Course_Name']}")
        except Exception as error_details:
            print(f"Ran into an unexpected exception: {error_details}")
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")
