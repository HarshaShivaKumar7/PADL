import pandas as pd
import numpy as np
import re
from mlxtend.frequent_patterns import apriori, association_rules

# Task a: Generate faculty dataset and save to CSV
def generate_faculty_dataset():
    np.random.seed(0)
    num_rows = 1000
    experience = np.linspace(1, 40, num_rows)
    df = pd.DataFrame({
        'Experience': experience,
        'Designation': np.where(experience <= 10, 'Assistant Professor',
                                np.where(experience <= 20, 'Associate Professor', 'Professor')),
        'Salary': np.linspace(30000, 150000, num_rows),
        'Publications': np.linspace(5, 300, num_rows),
        'BookChapters': np.sqrt(experience) * 2,
        'ConsultancyWork': experience * 1000,
        'FundReceived': experience ** 2 * 100,
        'Membership': np.log1p(experience) * 10
    })
    df.to_csv('faculty_data.csv', index=False)

generate_faculty_dataset()

# Task b: Lambda function to read CSV and load into tuples
read_csv_to_tuples = lambda file: tuple(pd.read_csv(file).itertuples(index=False, name=None))

# Task c: Regular expression to filter specific faculty details
def search_faculty():
    data = pd.read_csv('faculty_data.csv')
    criteria = {
        'Associate Professor': ('Associate Professor', 15),
        'Assistant Professor': ('Assistant Professor', 5),
        'Professor': ('Professor', 20)
    }
    results = {}
    for title, (designation, min_years) in criteria.items():
        pattern = rf'^{designation},\s*([\d\.]+),.*'
        results[title] = data[data.apply(lambda x: bool(re.match(pattern, x.to_string())) and x['Experience'] > min_years, axis=1)]
    return results

results = search_faculty()
for title, result in results.items():
    print(f"{title} with required experience:")
    print(result)

# Task d: Association rule mining
def association_rule_mining():
    data = pd.read_csv('faculty_data.csv')
    data = data[data['Designation'] == 'Associate Professor']
    data['High Publications'] = pd.qcut(data['Publications'], q=2, labels=[0, 1])
    data['High Book Chapters'] = pd.qcut(data['BookChapters'], q=2, labels=[0, 1])
    data['High Consultancy Work'] = pd.qcut(data['ConsultancyWork'], q=2, labels=[0, 1])

    freq_items = apriori(data[['High Publications', 'High Book Chapters', 'High Consultancy Work']], min_support=0.5, use_colnames=True)
    rules = association_rules(freq_items, metric="confidence", min_threshold=0.7)
    return rules

rules = association_rule_mining()
print("Association Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence']])

