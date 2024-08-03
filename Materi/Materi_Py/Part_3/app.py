import os
import csv
import random
from faker import Faker

fake = Faker()

DATA_FILE = 'employee_data.csv'

def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Position", "Salary"])
        print("Data file initialized.")

def read_employees():
    employees = []
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            employees.append(row)
    return employees

def add_employee(name, position, salary):
    employee_id = str(random.randint(1000, 9999))
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, name, position, salary])
    print(f"Employee {name} added with ID {employee_id}.")

def remove_employee(employee_id):
    employees = read_employees()
    employees = [emp for emp in employees if emp[0] != employee_id]
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Position", "Salary"])
        writer.writerows(employees)
    print(f"Employee with ID {employee_id} removed.")

def search_employee(name):
    employees = read_employees()
    result = [emp for emp in employees if name.lower() in emp[1].lower()]
    return result

def display_employees(employees):
    print(f"{'ID':<10} {'Name':<20} {'Position':<20} {'Salary':<10}")
    print('-' * 60)
    for emp in employees:
        print(f"{emp[0]:<10} {emp[1]:<20} {emp[2]:<20} {emp[3]:<10}")

def generate_random_employee():
    name = fake.name()
    position = fake.job()
    salary = random.randint(30000, 120000)
    return name, position, salary

def main():
    initialize_data_file()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Search Employee")
        print("4. Display All Employees")
        print("5. Generate Random Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = input("Enter employee salary: ")
            add_employee(name, position, salary)
        elif choice == '2':
            employee_id = input("Enter employee ID to remove: ")
            remove_employee(employee_id)
        elif choice == '3':
            name = input("Enter employee name to search: ")
            result = search_employee(name)
            if result:
                display_employees(result)
            else:
                print("No employees found.")
        elif choice == '4':
            employees = read_employees()
            display_employees(employees)
        elif choice == '5':
            name, position, salary = generate_random_employee()
            add_employee(name, position, salary)
            print(f"Random employee generated: {name}, {position}, {salary}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
