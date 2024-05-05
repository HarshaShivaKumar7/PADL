import csv
from faker import Faker

fake = Faker()

# Generate data
def generate_data():
    with open('faculty_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Experience'])
        for _ in range(100000):
            writer.writerow([fake.name(), fake.random_int(min=1, max=20)])

# Load data into a list
def load_data():
    with open('faculty_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return list(reader)

# Operations
def add_faculty(faculty_list, name, experience):
    faculty_list.append([name, str(experience)])

def search_faculty(faculty_list, name):
    return next((f for f in faculty_list if f[0] == name), "Not found")

def delete_faculty(faculty_list, name):
    return [f for f in faculty_list if f[0] != name]

def check_experience(faculty_list, experience):
    return [f[0] for f in faculty_list if int(f[1]) > experience]

# Menu system
def menu():
    faculty_list = load_data()
    while True:
        choice = input("1: Add, 2: Search, 3: Delete, 4: Check Exp >10, 5: Exit: ")
        if choice == '1':
            name = input("Enter name: ")
            experience = int(input("Enter experience: "))
            add_faculty(faculty_list, name, experience)
        elif choice == '2':
            name = input("Enter name to search: ")
            print(search_faculty(faculty_list, name))
        elif choice == '3':
            name = input("Enter name to delete: ")
            faculty_list = delete_faculty(faculty_list, name)
        elif choice == '4':
            experience = 10
            print(f"{', '.join(check_experience(faculty_list, experience))} can participate in BOS.")
        elif choice == '5':
            break

if __name__ == "__main__":
    generate_data()  # Uncomment this line if you need to regenerate the data
    menu()