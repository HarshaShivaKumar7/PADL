import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def generate_faculty_data(num_rows=100000):
    """ Generate a faculty dataset and save to CSV. """
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
    """ Load the faculty data from CSV and convert into a tuple data structure. """
    df = pd.read_csv('faculty_dataset.csv')
    return [tuple(row) for row in df.itertuples(index=False)]

def association_rule_mining():
    """ Perform association rule mining on Associate Professors' contributions. """
    df = pd.read_csv('faculty_dataset.csv')
    # Filter data for Associate Professors only
    associate_df = df[df['Designation'] == 'Associate Professor']
    # Binning the data to convert into categorical data
    associate_df['Publications_Range'] = pd.cut(associate_df['Publications'], bins=[0, 50, 100, 150, 200], labels=['Low', 'Medium', 'High', 'Very High'])
    associate_df['Book_Chapters_Range'] = pd.cut(associate_df['Book Chapters'], bins=[0, 5, 10, 15, 20], labels=['Few', 'Some', 'More', 'Many'])
    associate_df['Consultancy_Work_Range'] = pd.cut(associate_df['Consultancy Work'], bins=[0, 5000, 10000, 15000], labels=['Low', 'Medium', 'High'])

    # Preparing data for association rule mining
    transactions = associate_df[['Publications_Range', 'Book_Chapters_Range', 'Consultancy_Work_Range']]
    te = TransactionEncoder()
    te_ary = te.fit(transactions.values).transform(transactions.values)
    transactions_encoded = pd.DataFrame(te_ary, columns=te.columns_)

    # Applying Apriori algorithm to find frequent item sets
    frequent_itemsets = apriori(transactions_encoded, min_support=0.01, use_colnames=True)
    # Generating association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

if __name__ == "__main__":
    generate_faculty_data()
    faculty_tuples = load_data_into_tuples()
    association_rule_mining()
