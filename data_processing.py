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
