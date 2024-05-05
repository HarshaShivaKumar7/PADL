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