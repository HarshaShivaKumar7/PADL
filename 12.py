import csv
import random
from faker import Faker
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up visualization
sns.set(rc={'figure.figsize':(10, 6)})

# Mapping for subjects and corresponding books
cse_subjects_books = {
    "Advanced Mathematics": ["Probability and Statistics", "Probability & Statistics with Reliability, Queuing and Computer Science Applications", "Linear Algebra with Applications", "Advanced Engineering Mathematics"], 
    "ADBMS": ["Fundamentals of Database Systems", "Database System Concepts", "NoSQL for Mere Mortals"], 
    "RMI": ["Engineering Research Methodology", "Research Methods for Engineers"],
    "VR": ["Virtual Reality", "Virtual and Augmented Reality (VR/AR)"], 
    "AIML": ["Artificial Intelligence - A Modern Approach", "Machine Learning"], 
    "IoT": ["Internet of Things", "Designing the Internet of Things, Wiley"]
}

# Grades mapping for conversion
grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}

# Generate synthetic data and save to CSV
def generate_and_save_books(filename: str, num_records: int):
    fake = Faker()
    data = [['USN', 'Semester Number', 'Subject Code', 'Subject Name', 'Book Referred', "Book ID", "Grade Scored"]]
    for _ in range(num_records):
        subject, books = random.choice(list(cse_subjects_books.items()))
        book = random.choice(books)
        data.append([
            fake.unique.random_int(min=10000, max=99999),  # Student USN
            random.randint(1, 8),  # Semester Number
            subject[:3] + str(random.randint(100, 999)),  # Subject Code
            subject,  # Subject Name
            book,  # Book Referred
            books.index(book) + 1,  # Book ID
            random.choice(list(grades_map.keys()))  # Grade Scored
        ])
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Read and process CSV data
def process_and_analyze_data(input_filename):
    try:
        df = pd.read_csv(input_filename)
        df['Grade Scored'] = df['Grade Scored'].map(grades_map)
        # Ensure that only numeric data is involved in correlation calculations
        numeric_df = df[['Semester Number', 'Book ID', 'Grade Scored']].dropna()
        numeric_df.to_csv("extracted-books.csv", index=False)
        print("Numeric data extracted to extracted-books.csv.")

        # Correlation analysis
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.show()

        matrix = numeric_df.pivot_table(index='Book ID', values='Grade Scored', aggfunc='mean', fill_value=0)
        similarity = matrix.T.corr(method='pearson')  # Pearson's correlation for similarity
        print("Collaborative Filtering - Similarity Matrix:")
        print(similarity)

    except Exception as e:
        print("An error occurred:", e)

# Execute functions
generate_and_save_books('books.csv', 1000)
process_and_analyze_data('books.csv')
