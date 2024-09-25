import unittest
from data_classes import Employee
from data_classes import Person
import datetime

class TestPerson(unittest.TestCase):
    def test_person_init(self):  # Tests the constructor
        person = Person("A", "B")
        self.assertEqual(person.first_name, "A")
        self.assertEqual(person.last_name, "B")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee = Employee( "A",  "B",  "2023-07-10", 5 )
        self.assertEqual(employee.first_name, "A")
        self.assertEqual(employee.last_name, "B")
        self.assertEqual(employee.review_date, "2023-07-10")
        self.assertEqual(employee.review_rating, 5)

    def test_employee_rating_type(self):
         with self.assertRaises(ValueError):
             employee = Employee( "A",  "B",  "2023-07-10", "5" )
    
    def test_employee_rating_range(self):
         with self.assertRaises(ValueError):
             employee = Employee( "A",  "B",  "2023-07-10", 6 )

    def test_employee_str(self):
        employee = Employee( "A",  "B",  "2023-07-10", 5 ) 
        self.assertEqual(str(employee), "A,B,2023-07-10,5")

if __name__ == "__main__":
    unittest.main()