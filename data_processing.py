employees = [
    {"name": "Ehsan", "age": 35, "salary": 300000},
    {"name": "Sajad", "age": 26, "salary": 195000},
    {"name": "Rizwan", "age": 31, "salary": 185000},
    {"name": "Imran", "age": 55, "salary": 37000},
    {"name": "Usama", "age": 26, "salary": 85000}
    {"name": "Imad", "age": 24, "salary": 55000}
    {"name": "Hamza", "age": 24, "salary": 60000}
]

def filter_high_earning_employees(employee_list, threshold=60000):
    """Filters employees earning above the given threshold."""
    return [emp for emp in employee_list if emp["salary"] > threshold]

# Example usage
high_earners = filter_high_earning_employees(employees)
print(high_earners)