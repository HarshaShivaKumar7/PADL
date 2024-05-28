import pandas as pd
import numpy as np
import re

def generate_faculty_data(num_rows=100000):
    """ Generate a dataset of faculty data with linear mappings and save to CSV. """
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

# Lambda function to load data into a tuple structure
load_data_into_tuples = lambda: pd.read_csv('faculty_dataset.csv').apply(tuple, axis=1).tolist()

def search_faculty():
    """ Search and display faculty details based on designation and experience using regex. """
    df = pd.read_csv('faculty_dataset.csv')
    # Regex pattern to capture faculty based on designation and experience
    pattern = r'^(Professor|Associate Professor|Assistant Professor)$'
    matches = df[
        (df['Designation'].str.match(pattern)) &
        ((df['Designation'] == 'Professor') & (df['Experience'] > 20) |
         (df['Designation'] == 'Associate Professor') & (df['Experience'] > 15) |
         (df['Designation'] == 'Assistant Professor') & (df['Experience'] > 5))
    ]

    print(matches)


if __name__ == "__main__":
    generate_faculty_data()
    faculty_tuples = load_data_into_tuples()
    search_faculty()
