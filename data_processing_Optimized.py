import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

employees = [{"name": "Ehsan", "age": 35, "salary": 300000},
    {"name": "Sajad", "age": 26, "salary": 195000},
    {"name": "Rizwan", "age": 31, "salary": 185000},
    {"name": "Imran", "age": 55, "salary": 37000},
    {"name": "Usama", "age": 26, "salary": 85000},
    {"name": "Imad", "age": 24, "salary": 55000},
    {"name": "Hamza", "age": 24, "salary": 60000},
]

def group_employees_by_age(employees):
    category = {"young": [], "mid": [], "senior": []}

    for emp in employees:
        if emp['age'] < 30:
            category["young"].append(emp)
        elif 30 <= emp['age'] <= 39:
            category["mid"].append(emp)
        else:
            category["senior"].append(emp)
    return category
age_group = group_employees_by_age(employees)
logging.info ("Under 30 Employees")
for emp in age_group["young"]:
    logging.info(f"{emp['name']} - Age {emp['age']}")    
logging.info ("Mid-Aged Employees")
for emp in age_group["mid"]:
    logging.info(f"{emp['name']} - Age {emp['age']}")
logging.info ("Senior Employees")
for emp in age_group["senior"]:
    logging.info(f"{emp['name']} - Age {emp['age']}")
    print(" ")


def employees_salary(employees, threshold = 60000):
    high_salary = {"high_earners" : []}

    for emp in employees:
        if emp["salary"] > threshold:
            high_salary["high_earners"].append(emp)
    return high_salary

executive_employees = employees_salary(employees, threshold = 60000)
logging.info ("Higher Than 60000 Salary")
for emp in executive_employees["high_earners"]:
    logging.info(f"{emp['name']} - Salary {emp['salary']}")
