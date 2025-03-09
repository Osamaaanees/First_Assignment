
employees = [
    {"name": "Ehsan", "age": 35, "salary": 300000},
    {"name": "Sajad", "age": 26, "salary": 195000},
    {"name": "Rizwan", "age": 31, "salary": 185000},
    {"name": "Imran", "age": 55, "salary": 37000},
    {"name": "Usama", "age": 26, "salary": 85000}
    {"name": "Imad", "age": 24, "salary": 55000}
    {"name": "Hamza", "age": 24, "salary": 60000}
]

def filter_high_salary(employees, threshold=60000):
  return [emp for emp in employees if emp["salary"] > threshold]

high_earners = filter_high_salary(employees)

print("Employees earning more than 60,000:")
for emp in high_earners:
  print(f"{emp['name']} - Salary: {emp['salary']}")

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
        if emp['age'] > 30:
            category["young"].append(emp)
        elif emp['age'] <= 30 and emp['age'] > 39:
            category["mid"].append(emp)
        else:
            category["senior"].append(emp)
    return category
age_group = group_employees_by_age(employees)
print ("Under 30 Employees")
for emp in age_group["young"]:
    print(f"{emp['name']} - {emp['age']}")    
print ("Mid-Aged Employees")
for emp in age_group["mid"]:
    print(f"{emp['name']} - {emp['age']}")
print ("Senior Employees")
for emp in age_group["senior"]:
    print(f"{emp['name']} - {emp['age']}")
