import unittest
import pandas as pd
from data_processing_Optimized import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        data =  {
            "name": ["Ehsan", "Sajad", "Rizwan", "Imran", "Usama", "Imad", "Hamza"],
            "age": [35, 26, 31, 55, 26, 24, 24],
            "salary": [300000, 195000, 185000, 37000, 85000, 55000, 60000]
        }
        self.df = pd.DataFrame(data)

        self.manager = EmployeeManager("employees.csv")
        self.manager.employees = self.df.to_dict(orient='records')

    def test_group_employees_by_age(self):
        age_group = self.manager.group_employees_by_age()
        self.assertEqual(len(age_group["young"]), 4)
        self.assertEqual(len(age_group["mid"]), 2)
        self.assertEqual(len(age_group["senior"]), 1)

    def test_employees_salary(self):
        high_salary_employees= self.manager.employees_salary(threshold=60000)
        self.assertEqual(len(high_salary_employees), 4)
if __name__== "__main__":
    unittest.main()
