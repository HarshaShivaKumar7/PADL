import csv
import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Setup and mappings
faker = Faker()
subjects = ['Mathematics', 'Physics', 'Literature', 'Computer Science']
books = {s: [f"{s} Book {i}" for i in range(1, 4)] for s in subjects}
grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}

def generate_and_process_books(num_records):
    # Generate synthetic data
    data = [['USN', 'Semester Number', 'Subject Code', 'Subject Name', 'Book Referred', 'Book ID', 'Grade Scored']]
    for _ in range(num_records):
        subject = random.choice(subjects)
        book = random.choice(books[subject])
        data.append([
            faker.unique.random_int(min=1000, max=9999),
            random.randint(1, 8),
            f"{subject[:3].upper()}{random.randint(100, 999)}",
            subject,
            book,
            books[subject].index(book) + 1,
            random.choice(list(grades_map.keys()))
        ])

    # Save to CSV
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Read and process data
    df = pd.read_csv('books.csv')
    df['Grade Scored'] = df['Grade Scored'].map(grades_map)
    numeric_df = df[['Semester Number', 'Book ID', 'Grade Scored']].dropna()
    numeric_df.to_csv('extracted-books.csv', index=False)

    # Plot correlation matrix
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def mine_association_rules():
    # Association rule mining
    df = pd.read_csv('extracted-books.csv')
    df['Book ID'] = 'BookID_' + df['Book ID'].astype(str)
    df['Semester Number'] = 'Sem_' + df['Semester Number'].astype(str)
    df['Grade Scored'] = 'Grade_' + df['Grade Scored'].astype(str)

    transactions = df.values.tolist()
    te = TransactionEncoder()
    df_encoded = pd.DataFrame(te.fit_transform(transactions), columns=te.columns_)

    frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    print("Association Rules Found:", rules)

if __name__ == "__main__":
    generate_and_process_books(100)
    mine_association_rules()
