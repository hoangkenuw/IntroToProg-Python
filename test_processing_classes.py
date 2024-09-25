import unittest
import tempfile
import json
import data_classes as data
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        
        self.employee_type= Employee

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "A", "LastName": "B", "ReviewDate": "2023-07-10", "ReviewRating": 5}, 
            {"FirstName": "B", "LastName": "D", "ReviewDate": "2024-05-15", "ReviewRating": 5}, 
            {"FirstName": "Sam", "LastName": "King", "ReviewDate": "2024-07-07", "ReviewRating": 5}, 
            {"FirstName": "King", "LastName": "Sam", "ReviewDate": "2024-10-09", "ReviewRating": 4}   
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, self.employee_type)
        
        self.assertEqual(len(self.employee_data), len(employees))
        self.assertEqual(self.employee_data[0]['FirstName'], employees[0].first_name)
        self.assertEqual(self.employee_data[0]['LastName'], employees[0].last_name)
        self.assertEqual(self.employee_data[0]['ReviewDate'], employees[0].review_date)
        self.assertEqual(self.employee_data[0]['ReviewRating'], employees[0].review_rating)


if __name__ == "__main__":
    unittest.main()