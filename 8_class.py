import os
import csv
from random import randint, choice
import pandas as pd
from tqdm import tqdm
from mlxtend.frequent_patterns import apriori, association_rules

def generate_faculty_data(num, filename):
    if os.path.exists(filename):
        print("Dataset exists...")
        return
    headers = ['Experience', "Designation", "Salary", "Number of Publications", "Number of Chapters", "Amount of consultancy Work", "Fund Received", "Professional Membership"]
    data = [headers]
    designations = ["Assistant Professor", "Associate Professor", "Professor"]

    for _ in tqdm(range(num)):
        designation = choice(designations)
        exp_ranges = {'Professor': (25, 40), 'Associate Professor': (12, 29), 'Assistant Professor': (1, 14)}
        experience = randint(*exp_ranges[designation])
        salary = 50000 + 2000 * experience
        data.append([experience, designation, salary, int(experience * 1.5), experience // 3, experience * 1000, experience * 50000, randint(2, 5)])
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def load_and_process_data(filepath):
    df = pd.read_csv(filepath)
    df['High Experience'] = df['Experience'] > 25
    df['Many Publications'] = df['Number of Publications'] > 5
    df['Many Book Chapters'] = df['Number of Chapters'] > 3
    df['High Consultancy Work'] = df['Amount of consultancy Work'] > 50000
    df['High Fund Received'] = df['Fund Received'] > 500000
    df['Active Membership'] = df['Professional Membership'] > 2
    return df

def association_rule_mining(df, designation, experience):
    designation_code = {'Assistant Professor': 0, 'Associate Professor': 1, 'Professor': 2}
    df_filtered = df[(df['Designation'] == designation) & (df['Experience'] > experience)]
    df_binary = df_filtered.select_dtypes(include=['bool']).astype(int)
    frequent_itemsets = apriori(df_binary, min_support=0.1, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    return rules

dataset_file = "synthetic_faculty_dataset.csv"
generate_faculty_data(100000, dataset_file)
df = load_and_process_data(dataset_file)
rules = association_rule_mining(df, "Associate Professor", 25)
print(rules)
