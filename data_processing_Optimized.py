import logging
import pandas as pd
import argparse

logging.basicConfig(level=logging.INFO, format="%(message)s")

class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            df = pd.read_csv(self.filename)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            logging.error(f"Error: File '{self.filename}' not found")
            return []
    
    def group_employees_by_age(self):
        category = {"young": [], "mid": [], "senior": []}
        for employee in self.employees:
            if employee['age'] < 30:
                category["young"].append(employee)
            elif 30 <= employee['age'] <= 39:
                category["mid"].append(employee)
            else:
                category["senior"].append(employee)

        return category
    
    def employees_salary(self, threshold = 60000):
        high_earners = []
        for employee in self.employees:
            if employee["salary"] > threshold:
                high_earners.append(employee)
        return high_earners
    
    def log_employee_groups(self):
        age_group = self.group_employees_by_age()
        logging.info("Under 30 Employees:")
        for employee in age_group["young"]:
            logging.info(f"{employee['name']} - Age {employee['age']}")
        
        logging.info("Mid-Aged Employees:")
        for employee in age_group["mid"]:
            logging.info(f"{employee['name']} - Age {employee['age']}")

        logging.info("Senior Employees:")
        for employee in age_group["senior"]:
            logging.info(f"{employee['name']} - Age {employee['age']}")
    

    def log_high_salary_employees(self, threshold=60000):
        high_earners = self.employees_salary(threshold)
        logging.info(f"Employees earning more than {threshold}:")
        for employee in high_earners:
            logging.info(f"{employee['name']} - Salary {employee['salary']}")
        
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Employees Management System (EMS)")
    parser.add_argument("--file_name", default= "employees.csv", help= "CSV file containing employees data")
    args=parser.parse_args()

    manager = EmployeeManager(args.file_name)
    manager.log_employee_groups()
    manager.log_high_salary_employees()