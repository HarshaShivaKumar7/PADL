import csv
import random
from faker import Faker
import pandas as pd
import numpy as np  # Correctly import numpy
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def setup_data(num_records):
    """Generates and processes data, then performs association rule mining."""
    faker = Faker()
    subjects = ['Mathematics', 'Physics', 'Literature', 'Computer Science']
    books = {s: [f"{s} Book {i}" for i in range(1, 4)] for s in subjects}
    grades_map = {'S': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5}

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
    
    # Save and process the data
    with open('books.csv', 'w', newline='') as file:
        csv.writer(file).writerows(data)
    print(f"Data generated and saved to books.csv")

    df = pd.read_csv('books.csv')
    df['Grade Scored'] = df['Grade Scored'].map(grades_map)
    df.to_csv('extracted-books.csv', index=False)
    print("Processed data saved to extracted-books.csv")

    # Correlation matrix
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

    # Association rule mining
    te = TransactionEncoder()
    transactions = df[['Semester Number', 'Book ID', 'Grade Scored']].applymap(str).values.tolist()
    df_encoded = pd.DataFrame(te.fit_transform(transactions), columns=te.columns_)
    frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    print("Association Rules Found:")
    print(rules)

if __name__ == "__main__":
    setup_data(100)
