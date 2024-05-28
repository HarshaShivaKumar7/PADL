import pandas as pd
import numpy as np
import re

def generate_faculty_data(num_rows=100000):
    """ Generate a dataset of faculty data with linear mappings and save to CSV. """
    np.random.seed(0)
    experience = np.random.randint(1,21,num_rows)
    data = {
        'Experience': experience,
        'Designation': ['Professor' if x > 20 else 'Associate Professor' if x > 15 else 'Assistant Professor' if x > 5 else 'Lecturer' for x in experience],
        'Salary': [50000 + x * 1000 for x in experience],
        'Publications': [2 * x for x in experience],
        'Book Chapters': [x // 10 for x in experience],
        'Consultancy Work': [x * 100 for x in experience],
        'Funds Received': [x * 500 for x in experience],
        'Professional Membership': [x % 10 == 0 for x in experience]
    }
    df = pd.DataFrame(data)
    df.to_csv('faculty_dataset.csv', index=False)

# Lambda function to load data into a tuple structure
load_data_into_tuples = lambda: pd.read_csv('faculty_dataset.csv').apply(tuple, axis=1).tolist()

def search_faculty():
    df = pd.read_csv('faculty_dataset.csv')
    pattern = r'^(Professor|Associate Professor|Assistant Professor)$'
    matches = df[(df['Designation'].str.match(pattern))]
    print(matches)

if __name__ == "__main__":
    generate_faculty_data()
    faculty_tuples = load_data_into_tuples()
    search_faculty()
