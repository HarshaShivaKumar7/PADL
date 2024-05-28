import csv, random
from faker import Faker
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# Setup for visualization and data handling
sns.set(rc={'figure.figsize':(10, 6)})
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

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

def generate_and_save_books(filename: str, num_records: int):
    fake = Faker()
    data = [['USN', 'SEM', 'SUB_CODE', 'SUBJECT_NAME', 'BOOK_REFERRED', "BOOK_ID", "GRADE_SCORED"]]
    for sem in range(1, 9):
        for subject, books in cse_subjects_books.items():
            for book_index, book in enumerate(books, 1):
                for _ in range(num_records // (len(cse_subjects_books) * len(books) * 8)):
                    usn = f"1MS23CS{fake.random_int(min=1, max=999):03}"
                    sub_code = f"MCS{sem}{book_index}"
                    book_id = f"BID{sem}{book_index}"
                    grade = random.choice(['S', 'A', 'B', 'C', 'D'])
                    data.append([usn, sem, sub_code, subject, book, book_id, grades_map[grade]])
    with open(filename, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)

def analyze_data(filename: str):
    df = pd.read_csv(filename)
    if df.empty:
        print("No data to analyze.")
        return

    df['GRADE_SCORED'] = df['GRADE_SCORED'].map(grades_map)
    df[['SEM', 'SUB_CODE', 'BOOK_ID', 'GRADE_SCORED']].to_csv("extracted-books.csv", index=False)

    # Ensure SUB_CODE and BOOK_ID are numerical for correlation
    df['SUB_CODE'] = df['SUB_CODE'].apply(lambda x: int(x[-1]))
    df['BOOK_ID'] = df['BOOK_ID'].apply(lambda x: int(x[-2:]))
    if not df[['SEM', 'SUB_CODE', 'BOOK_ID', 'GRADE_SCORED']].empty:
        sns.heatmap(df[['SEM', 'SUB_CODE', 'BOOK_ID', 'GRADE_SCORED']].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.show()

    # Collaborative Filtering
    matrix = df.pivot_table(index='BOOK_ID', columns='SUB_CODE', values='GRADE_SCORED', fill_value=0)
    if not matrix.empty:
        similarity = cosine_similarity(matrix)
        print("User Similarity Matrix:\n", similarity)

        # Recommendations, check if matrix has the index
        def recommend_books(book_id, matrix, similarity):
            if book_id in matrix.index:
                sim_books = pd.Series(similarity[matrix.index == book_id][0], index=matrix.index)
                return sim_books.sort_values(ascending=False).drop(book_id).head(10)
            return "Book ID not found"

        print("Recommendation for Book ID BID52:", recommend_books('BID52', matrix, similarity))

# Data generation and analysis
generate_and_save_books('books.csv', 1000)
analyze_data('books.csv')
