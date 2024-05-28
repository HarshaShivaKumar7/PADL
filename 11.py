import csv
import random
from tqdm import tqdm
from faker import Faker
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Define subjects and books mapping
cse_subjects_books = {
    "Advanced Mathematics": ["Probability and Statistics", "Probability & Statistics with Reliability, Queuing and Computer Science Applications", "Linear Algebra with Applications", "Advanced Engineering Mathematics"], 
    "ADBMS": ["Fundamentals of Database Systems", "Database System Concepts", "NoSQL for Mere Mortals"], 
    "RMI": ["Engineering Research Methodology", "Research Methods for Engineers"],
    "VR": ["Virtual Reality", "Virtual and Augmented Reality (VR/AR)"], 
    "AIML": ["Artificial Intelligence - A Modern Approach", "Machine Learning"], 
    "IoT": ["Internet of Things", "Designing the Internet of Things, Wiley"]
}
grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}

# Function to generate books data
def generate_books(filename: str, num_records: int):
    fake = Faker()
    data = [['USN', 'SEM', 'SUB_CODE', 'SUBJECT_NAME', 'BOOK_REFERRED', 'BOOK_ID', 'GRADE_SCORED']]
    grades = ["A", "B", "C", "D", "S"]
    grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}
    for _ in tqdm(range(num_records), desc="Generating data"):
        sem = random.randint(1, 8)
        subject = random.choice(list(cse_subjects_books.keys()))
        book_ref = random.choice(cse_subjects_books[subject])
        usn = f"1MS{24-sem}CS{fake.random_int(min=100, max=999):03}"
        sub_code = f"MCS{sem}{cse_subjects_books[subject].index(book_ref)+1}"
        book_id = f"BID{cse_subjects_books[subject].index(book_ref)+1}"
        grade = grades_map[random.choice(grades)]
        data.append([usn, sem, sub_code, subject, book_ref, book_id, grade])
    with open(filename, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)

generate_books('books.csv', 1000)

# Exception handling for file operations
try:
    df = pd.read_csv('books.csv')
    df['Grade'] = df['GRADE_SCORED'].map(grades_map).fillna(0).astype(int)
    df['Subject_Code'] = df['SUB_CODE'].astype('category').cat.codes
    df['Book_ID'] = df['BOOK_ID'].astype('category').cat.codes

    df.to_csv('extracted-books.csv', index=False, columns=['SEM', 'Subject_Code', 'Book_ID', 'Grade'])

    print("Correlation Analysis:")
    print(df[['SEM', 'Subject_Code', 'Book_ID', 'Grade']].corr())

    # Prepare data for association rule mining
    te = TransactionEncoder()
    te_ary = te.fit(df[['SEM', 'Subject_Code', 'Book_ID', 'Grade']].astype(str).values).transform(df[['SEM', 'Subject_Code', 'Book_ID', 'Grade']].astype(str).values)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    print("Association Rules:")
    print(rules)
    
except Exception as e:
    print(f"An error occurred: {e}")
