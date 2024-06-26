
"""
#p1
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

"""
"""
# p2
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




"""

"""
#p3
import requests
from datetime import datetime

def get_weather(lat: float, lon: float) -> None:
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3118cd38ee3c8d85bea678b7100a9d31&units=metric").json()
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return
        info = data['weather'][0]
        main = data['main']
        print(f"Place: {data['name']}, {data['sys']['country']}")
        print(f"Weather: {info['main']} ({info['description']})")
        print(f"Temperature: {main['temp']}°C")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Humidity: {main['humidity']}%")
        print(f"Visibility: {data['visibility']} meters")
        print(f"Wind: {data['wind']['speed']} m/s at {data['wind']['deg']}°")
        print(f"Time: {datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        get_weather(lat, lon)
"""
"""
# p4
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ldr_pin = 7  
red_led_pin = 11 
green_led_pin = 13 
delay_time = 0.1

GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.output(red_led_pin, False)
GPIO.output(green_led_pin, False)

def read_ldr(ldr_pin):
    count = 0
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, False)
    time.sleep(delay_time)
    GPIO.setup(ldr_pin, GPIO.IN)
    while (GPIO.input(ldr_pin) == 0):
        count += 1
    return count

try:
    while True:
        ldr_value = read_ldr(ldr_pin)
        print("LDR Value:", ldr_value)
        if ldr_value > 10000:
            print("Light is dim")
            GPIO.output(red_led_pin, True)
            GPIO.output(green_led_pin, False)
        else:
            print("Light is bright")
            GPIO.output(red_led_pin, False)
            GPIO.output(green_led_pin, True)
        time.sleep(1) 

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
"""
"""
# p5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def generate_data():
    np.random.seed(0)
    experience = np.random.randint(1, 41, 100000)  # 1 to 40 years of experience
    designation = np.random.choice(['Assistant Professor', 'Associate Professor', 'Professor'], 100000)
    salary = experience * np.random.randint(1000, 1500)
    publications = experience * np.random.randint(0, 3)
    book_chapters = experience * np.random.randint(0, 2)
    consultancy_work = experience * np.random.randint(500, 10000)
    funds_received = experience * np.random.randint(1000, 20000)
    professional_membership = np.random.choice(['Yes', 'No'], 100000)
    df = pd.DataFrame({
        'Experience': experience,
        'Designation': designation,
        'Salary': salary,
        'Publications': publications,
        'Book Chapters': book_chapters,
        'Consultancy Work': consultancy_work,
        'Funds Received': funds_received,
        'Professional Membership': professional_membership
    })
    df.to_csv('faculty_data.csv', index=False)

def load_data():
    return pd.read_csv('faculty_data.csv')

def prepare_data_for_correlation(data):
    data['Designation'] = data['Designation'].astype('category').cat.codes
    data['Professional Membership'] = data['Professional Membership'].astype('category').cat.codes
    return data.select_dtypes(include=[np.number])

def analyze_correlation(data):
    prepared_data = prepare_data_for_correlation(data)
    print(prepared_data.corr())

def perform_regression_and_plot(data):
    X = data[['Experience']]
    y = data['Salary']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    plt.scatter(X_test, y_test, color='blue')
    plt.plot(X_test, y_pred, color='red', linewidth=2)
    plt.xlabel('Experience')
    plt.ylabel('Salary')
    plt.title('Linear Regression Analysis: Experience vs Salary')
    plt.show()

if __name__ == "__main__":
    generate_data()
    df = load_data()
    analyze_correlation(df)
    perform_regression_and_plot(df)

"""


"""
# p6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate dataset
np.random.seed(0)
experience = np.arange(1, 100001)
designation = np.linspace(1, 10, 100000)
salary = np.linspace(30000, 150000, 100000)
publications = experience / 1000
chapters = np.sqrt(experience)
consultancy = experience * 10
fund_received = experience ** 1.1
membership = np.log1p(experience)
df = pd.DataFrame({
    'Experience': experience,
    'Designation': designation,
    'Salary': salary,
    'Publications': publications,
    'Chapters': chapters,
    'Consultancy': consultancy,
    'FundReceived': fund_received,
    'Membership': membership
})
df.to_csv('faculty_data.csv', index=False)

# Load data
data = pd.read_csv('faculty_data.csv')
correlations = data.corr()
print("Correlations:", correlations)

# Discretize the 'Publications' data into categories
data['Pub_Categories'] = pd.qcut(data['Publications'], q=3, labels=['Low', 'Medium', 'High'])

# Linear Regression analysis
X = data[['Experience']].values
y = data['Publications'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, lr_predictions, color='blue', linewidth=3, label='Predicted')
plt.xlabel('Experience')
plt.ylabel('Publications')
plt.title('Linear Regression - Experience vs Publications')
plt.legend()
plt.show()

# KNN Regression analysis
knn_model = KNeighborsRegressor(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='red', label='Actual')
plt.scatter(X_test, knn_predictions, color='green', label='Predicted', linewidth=2)
plt.xlabel('Experience')
plt.ylabel('Publications')
plt.title('KNN - Experience vs Publications')
plt.legend()
plt.show()

# Naive Bayes classification
X_nb = data[['Experience']].values
y_nb = data['Pub_Categories'].values
X_train_nb, X_test_nb, y_train_nb, y_test_nb = train_test_split(X_nb, y_nb, test_size=0.2, random_state=0)
nb_model = GaussianNB()
nb_model.fit(X_train_nb, y_train_nb)
nb_predictions = nb_model.predict(X_test_nb)
accuracy = accuracy_score(y_test_nb, nb_predictions)
print(f"Naive Bayes Model Accuracy: {accuracy}")
plt.figure(figsize=(10, 5))
plt.scatter(X_test_nb, y_test_nb, color='purple', label='Actual')
plt.scatter(X_test_nb, nb_predictions, color='orange', label='Predicted', marker='x')
plt.xlabel('Experience')
plt.ylabel('Publication Category')
plt.title('Naive Bayes - Experience vs Publication Categories')
plt.legend()
plt.show()


"""


"""
# p7

import pandas as pd
import numpy as np
import re
from mlxtend.frequent_patterns import apriori, association_rules

# Task a: Generate faculty dataset and save to CSV
def generate_faculty_dataset():
    np.random.seed(0)
    num_rows = 1000
    experience = np.linspace(1, 40, num_rows)
    df = pd.DataFrame({
        'Experience': experience,
        'Designation': np.where(experience <= 10, 'Assistant Professor',
                                np.where(experience <= 20, 'Associate Professor', 'Professor')),
        'Salary': np.linspace(30000, 150000, num_rows),
        'Publications': np.linspace(5, 300, num_rows),
        'BookChapters': np.sqrt(experience) * 2,
        'ConsultancyWork': experience * 1000,
        'FundReceived': experience ** 2 * 100,
        'Membership': np.log1p(experience) * 10
    })
    df.to_csv('faculty_data.csv', index=False)

generate_faculty_dataset()

# Task b: Lambda function to read CSV and load into tuples
read_csv_to_tuples = lambda file: tuple(pd.read_csv(file).itertuples(index=False, name=None))

# Task c: Regular expression to filter specific faculty details
def search_faculty():
    data = pd.read_csv('faculty_data.csv')
    criteria = {
        'Associate Professor': ('Associate Professor', 15),
        'Assistant Professor': ('Assistant Professor', 5),
        'Professor': ('Professor', 20)
    }
    results = {}
    for title, (designation, min_years) in criteria.items():
        pattern = rf'^{designation},\s*([\d\.]+),.*'
        results[title] = data[data.apply(lambda x: bool(re.match(pattern, x.to_string())) and x['Experience'] > min_years, axis=1)]
    return results

results = search_faculty()
for title, result in results.items():
    print(f"{title} with required experience:")
    print(result)

# Task d: Association rule mining
def association_rule_mining():
    data = pd.read_csv('faculty_data.csv')
    data = data[data['Designation'] == 'Associate Professor']
    data['High Publications'] = pd.qcut(data['Publications'], q=2, labels=[0, 1])
    data['High Book Chapters'] = pd.qcut(data['BookChapters'], q=2, labels=[0, 1])
    data['High Consultancy Work'] = pd.qcut(data['ConsultancyWork'], q=2, labels=[0, 1])

    freq_items = apriori(data[['High Publications', 'High Book Chapters', 'High Consultancy Work']], min_support=0.5, use_colnames=True)
    rules = association_rules(freq_items, metric="confidence", min_threshold=0.7)
    return rules

rules = association_rule_mining()
print("Association Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence']])




"""
