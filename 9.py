import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def generate_faculty_data(num_rows=100000):
    """ Generate a faculty dataset and save to CSV. """
    np.random.seed(0)
    experience = np.random.randint(1, 21, num_rows)
    data = {
        'Experience': experience,
        'Designation': ['Professor' if x > 16 else 'Associate Professor' if x > 12 else 'Assistant Professor' if x > 8 else 'Lecturer' for x in experience],
        'Salary': [50000 + x * 1000 for x in experience],
        'Publications': [2 * x + np.random.randint(0, 10) for x in experience],
        'Book Chapters': [x // 10 for x in experience],
        'Consultancy Work': [x * 100 + np.random.randint(0, 500) for x in experience],
        'Funds Received': [x * 500 for x in experience],
        'Professional Membership': [x % 10 == 0 for x in experience]

    }
    df = pd.DataFrame(data)
    df.to_csv('faculty_dataset.csv', index=False)

### 2. Load Data into Tuples
def load_data_into_tuples():
    """ Load the faculty data from CSV and convert into a tuple data structure. """
    df = pd.read_csv('faculty_dataset.csv')
    return [tuple(row) for row in df.itertuples(index=False)]

### 3. Association Rule Mining for Associate Professors
def association_rule_mining():
    """ Perform association rule mining on Associate Professors' contributions. """
    df = pd.read_csv('faculty_dataset.csv')
    associate_df = df[df['Designation'] == 'Associate Professor'].copy()

    # Correctly binning data
    associate_df['Publications_Range'] = pd.cut(
        associate_df['Publications'],
        bins=[0, 10, 20, 30, 40, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500], 
        labels=['0-10', '11-20', '21-30', '31-40', '41-50', '51-100', '101-150', '151-200', '201-250', '251-300', '301-350', '351-400', '401-450', '451-500']
    )

    associate_df['Book_Chapters_Range'] = pd.cut(
        associate_df['Book Chapters'],
        bins=[0, 1, 2, 3, 4, 5, 10, 15, 20], 
        labels=['0', '1', '2', '3', '4', '5-9', '10-14', '15-19']
    )

    associate_df['Consultancy_Work_Range'] = pd.cut(
        associate_df['Consultancy Work'],
        bins=[0, 1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000], 
        labels=['0-1000', '1001-2000', '2001-3000', '3001-4000', '4001-5000', '5001-10000', '10001-15000', '15001-20000']
    )

    # Preparing data for association rule mining
    transactions = associate_df[['Publications_Range', 'Book_Chapters_Range', 'Consultancy_Work_Range']]
    te = TransactionEncoder()
    te_ary = te.fit(transactions.values).transform(transactions.values)
    transactions_encoded = pd.DataFrame(te_ary, columns=te.columns_)

    # Applying Apriori algorithm to find frequent item sets
    frequent_itemsets = apriori(transactions_encoded, min_support=0.05, use_colnames=True)
    # Generating association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

if __name__ == "__main__":
    generate_faculty_data()
    faculty_tuples = load_data_into_tuples()
    association_rule_mining()
