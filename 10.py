import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

class FacultyDataset:
    def __init__(self, num_rows=100000):
        self.num_rows = num_rows
        self.df = None
        self.filepath = 'faculty_dataset.csv'

    def generate_data(self):
        """ Generate a dataset of faculty data with linear mappings and save to CSV. """
        data = {
            'Experience': np.arange(1, self.num_rows + 1),
            'Designation': ['Professor' if x > 20 else 'Associate Professor' if x > 15 else 'Assistant Professor' if x > 5 else 'Lecturer' for x in range(1, self.num_rows + 1)],
            'Salary': [50000 + x * 1000 for x in range(1, self.num_rows + 1)],
            'Publications': [2 * x for x in range(1, self.num_rows + 1)],
            'Book Chapters': [x // 10 for x in range(1, self.num_rows + 1)],
            'Consultancy Work': [x * 100 for x in range(1, self.num_rows + 1)],
            'Funds Received': [x * 500 for x in range(1, self.num_rows + 1)],
            'Professional Membership': [x % 10 == 0 for x in range(1, self.num_rows + 1)]
        }
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.filepath, index=False)

    def load_data(self):
        """ Load data from CSV into a DataFrame. """
        self.df = pd.read_csv(self.filepath)

    def find_associate_professors(self):
        if self.df is None:
            self.load_data()
        asso_prof_data = self.df[self.df['Designation'] == 'Associate Professor']  # Select all Associate Professors
        return asso_prof_data[['Experience', 'Publications', 'Book Chapters']]


    def perform_association_rule_mining(self, data):
        """ Perform association rule mining on provided DataFrame. """
        te = TransactionEncoder()
        te_ary = te.fit(data).transform(data)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Usage
if __name__ == '__main__':
    dataset = FacultyDataset()
    dataset.generate_data()
    asso_prof_25 = dataset.find_associate_professors()
    dataset.perform_association_rule_mining(asso_prof_25[['Experience', 'Publications', 'Book Chapters']])
