import csv
from faker import Faker
from datetime import datetime

fake = Faker()

# Generate data
def generate_student_data():
    with open('student_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'USN', 'CGPA', 'Address', 'Blood Group', 'Branch', 'UG/PG', 'DOB', 'Year'])
        for i in range(100):
            name = fake.name()
            usn = f"USN{i:05d}"
            cgpa = round(fake.random_number(digits=2) * 0.1, 2)
            address = fake.address()
            blood_group = fake.random_element(elements=('A+', 'B+', 'O+', 'AB+'))
            branch = fake.random_element(elements=('Computer Science', 'Electronics', 'Mechanical'))
            ug_pg = fake.random_element(elements=('UG', 'PG'))
            dob = fake.date_of_birth(minimum_age=18, maximum_age=30).strftime('%Y-%m-%d')
            year = fake.random_int(min=1, max=4)
            writer.writerow([name, usn, cgpa, address, blood_group, branch, ug_pg, dob, year])

# Load data into a tuple
def load_data():
    with open('student_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        return tuple(reader)

# Search and filter functions
def search_students_by_branch(students, branch_name):
    return [s for s in students if s[5] == branch_name and float(s[2]) > 9 and s[6] in ['UG', 'PG']]

# Menu system
def menu(students):
    while True:
        print("\nMenu:")
        print("1: Search Students by Branch for Placement")
        print("2: Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            branch_name = input("Enter branch name: ")
            eligible_students = search_students_by_branch(students, branch_name)
            print(f"\nEligible students in {branch_name} for placement:")
            for student in eligible_students:
                print(f"{student[0]}, {student[1]}, {student[2]}, {student[3]}, {student[4]}, {student[5]}, {student[6]}, {student[7]}, {student[8]}")
        elif choice == '2':
            print("Exiting...")
            break

if __name__ == "__main__":
    generate_student_data()  # Uncomment this line if data needs to be regenerated
    student_tuple = load_data()
    menu(student_tuple)

