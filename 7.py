import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

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

def knn_analysis_and_plot():
    df = pd.read_csv('faculty_dataset.csv')
    X = df[['Experience']].values
    y = df['Publications'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    
    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    plt.figure(figsize=(8, 4))
    plt.scatter(X_test, y_test, color='blue', label='Actual Publications')
    plt.plot(X_test, y_pred, color='red', label='Predicted by KNN')
    plt.title('KNN Analysis: Experience vs Publications')
    plt.xlabel('Experience')
    plt.ylabel('Publications')
    plt.legend()
    plt.show()

def naive_bayes_analysis_and_plot():
    df = pd.read_csv('faculty_dataset.csv')
    X = df[['Experience']].values
    y = df['Publications'].values
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)  # Encoding publications for NB

    X_train, X_test, y_train_encoded, y_test = train_test_split(X, y_encoded, test_size=0.25, random_state=0)
    nb = GaussianNB()
    nb.fit(X_train, y_train_encoded)
    y_pred_encoded = nb.predict(X_test)
    y_pred = le.inverse_transform(y_pred_encoded)  # Decode back to original values
    
    plt.figure(figsize=(8, 4))
    plt.scatter(X_test, y_test, color='green', label='Actual Publications')
    plt.plot(X_test, y_pred, color='orange', label='Predicted by Naive Bayes')
    plt.title('Naive Bayes Analysis: Experience vs Publications')
    plt.xlabel('Experience')
    plt.ylabel('Publications')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    generate_faculty_data()
    tuples = load_data_into_tuples()
    knn_analysis_and_plot()
    naive_bayes_analysis_and_plot()
