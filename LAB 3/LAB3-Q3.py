def employee(name,salary):
    if salary == 0:
        salary = 10,000
    else:
        salary = salary - salary * 0.02
    return name,salary

name, salary = employee("Ali",2000)
print(f"Name: {name}, Salary:{salary}")
