import csv, random
from faker import Faker
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules, apriori
from sklearn.metrics.pairwise import cosine_similarity

# Configuration for warnings and plotting
sns.set(rc={'figure.figsize':(10, 6)})
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Book data mapping for CSE subjects
cse_subjects_books = {
    "Advanced Mathematics": ["Probability and Statistics", "Probability & Statistics with Reliability, Queuing and Computer Science Applications", "Linear Algebra with Applications", "Advanced Engineering Mathematics"], 
    "ADBMS": ["Fundamentals of Database Systems", "Database System Concepts", "NoSQL for Mere Mortals"], 
    "RMI": ["Engineering Research Methodology", "Research Methods for Engineers"],
    "VR": ["Virtual Reality", "Virtual and Augmented Reality (VR/AR)"], 
    "AIML": ["Artificial Intelligence - A Modern Approach", "Machine Learning"], 
    "IoT": ["Internet of Things", "Designing the Internet of Things, Wiley"]
}

def generate_books(filename: str, num_records: int):
    fake = Faker()
    data = [['USN', 'SEM', 'SUB_CODE', 'SUBJECT_NAME', 'BOOK_REFERRED', "BOOK_ID", "GRADE_SCORED"]]
    grades = ["A", "B", "C", "D", "S"]
    grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}
    for _ in tqdm(range(num_records)):
        sem = random.randint(1, 8)
        subject = random.choice(list(cse_subjects_books.keys()))
        book_ref = random.choice(cse_subjects_books[subject])
        usn = f"1MS{24-sem}CS{fake.random_int(min=100, max=999):03}"
        sub_code = f"MCS{sem}{cse_subjects_books[subject].index(book_ref)+1}"
        book_id = f"BID{cse_subjects_books[subject].index(book_ref)+1}"
        grade = random.choice(grades)
        data.append([usn, sem, sub_code, subject, book_ref, book_id, grades_map[grade]])
    with open(filename, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)

def analyze_data(filename: str):
    df = pd.read_csv(filename)
    df['GRADE_SCORED'] = df['GRADE_SCORED'].map({'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}).fillna(0).astype(int)
    numeric_data = df[['SEM', 'GRADE_SCORED']]
    sns.heatmap(numeric_data.corr(), annot=True).set_title("Correlation Matrix HeatMap")
    plt.show()

    # Prepare data for association rule mining
    df_for_mining = pd.get_dummies(df[['SEM', 'SUB_CODE', 'BOOK_ID', 'GRADE_SCORED']], columns=['SEM', 'SUB_CODE', 'BOOK_ID'])
    itemsets = apriori(df_for_mining, min_support=0.01, use_colnames=True)
    rules = association_rules(itemsets, metric="confidence", min_threshold=0.7)
    print("Association Rules:\n", rules)

    # Collaborative filtering
    user_item_matrix = df.pivot_table(index='USN', columns='SUB_CODE', values='GRADE_SCORED', fill_value=0)
    similarity_matrix = cosine_similarity(user_item_matrix)
    print("User Similarity Matrix:\n", similarity_matrix)

# Execute functions
generate_books('books.csv', 1000)
analyze_data('books.csv')
