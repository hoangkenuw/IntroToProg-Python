import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []
        self.employee_type = Employee

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for student data
        with patch('builtins.input', side_effect=["A",  "B",  "2023-07-10", 5 ]):
            IO.input_employee_data(self.employee_data,self.employee_type)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'A')
            self.assertEqual(self.employee_data[0].last_name, 'B')
            self.assertEqual(self.employee_data[0].review_date, "2023-07-10")
            self.assertEqual(self.employee_data[0].review_rating, 5)

        # Simulate invalid GPA input (not a float)
        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid']):
            IO.input_employee_data(self.employee_data,self.employee_type)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()
