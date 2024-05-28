import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def generate_faculty_data(num_rows=100000):
    data = {
        'Experience': np.arange(1, num_rows + 1),
        'Designation': ['Professor' if x > 20 else 'Associate Professor' if x > 15 else 'Assistant Professor' if x > 5 else 'Lecturer' for x in range(1, num_rows + 1)],
        'Salary': [50000 + x * 1000 for x in range(1, num_rows + 1)],
        'Publications': [2 * x for x in range(1, num_rows + 1)],
        'Book Chapters': [x // 10 for x in range(1, num_rows + 1)],
        'Consultancy Work': [x * 100 for x in range(1, num_rows + 1)],
        'Funds Received': [x * 500 for x in range(1, num_rows + 1)],
        'Professional Membership': [x % 10 == 0 for x in range(1, num_rows + 1)]
    }
    df = pd.DataFrame(data)
    df.to_csv('faculty_dataset.csv', index=False)

def load_data_into_tuples():
    df = pd.read_csv('faculty_dataset.csv')
    return [tuple(x) for x in df.to_records(index=False)]

def calculate_correlations():
    df = pd.read_csv('faculty_dataset.csv')
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr()

def perform_linear_regression_and_plot():
    df = pd.read_csv('faculty_dataset.csv')
    X = df[['Experience']].values
    y = df['Publications'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    plt.scatter(X_test, y_test, color='blue')
    plt.plot(X_test, y_pred, color='red')
    plt.title('Experience vs Publications')
    plt.xlabel('Experience')
    plt.ylabel('Predicted Publications')
    plt.show()

if __name__ == "__main__":
    generate_faculty_data()
    tuples = load_data_into_tuples()
    correlations = calculate_correlations()
    print(correlations)
    perform_linear_regression_and_plot()
