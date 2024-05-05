import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate dataset
np.random.seed(0)
experience = np.arange(1, 100001)
designation = np.linspace(1, 10, 100000)
salary = np.linspace(30000, 150000, 100000)
publications = experience / 1000
chapters = np.sqrt(experience)
consultancy = experience * 10
fund_received = experience ** 1.1
membership = np.log1p(experience)
df = pd.DataFrame({
    'Experience': experience,
    'Designation': designation,
    'Salary': salary,
    'Publications': publications,
    'Chapters': chapters,
    'Consultancy': consultancy,
    'FundReceived': fund_received,
    'Membership': membership
})
df.to_csv('faculty_data.csv', index=False)

# Load data
data = pd.read_csv('faculty_data.csv')
correlations = data.corr()
print("Correlations:", correlations)

# Discretize the 'Publications' data into categories
data['Pub_Categories'] = pd.qcut(data['Publications'], q=3, labels=['Low', 'Medium', 'High'])

# Linear Regression analysis
X = data[['Experience']].values
y = data['Publications'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, lr_predictions, color='blue', linewidth=3, label='Predicted')
plt.xlabel('Experience')
plt.ylabel('Publications')
plt.title('Linear Regression - Experience vs Publications')
plt.legend()
plt.show()

# KNN Regression analysis
knn_model = KNeighborsRegressor(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='red', label='Actual')
plt.scatter(X_test, knn_predictions, color='green', label='Predicted', linewidth=2)
plt.xlabel('Experience')
plt.ylabel('Publications')
plt.title('KNN - Experience vs Publications')
plt.legend()
plt.show()

# Naive Bayes classification
X_nb = data[['Experience']].values
y_nb = data['Pub_Categories'].values
X_train_nb, X_test_nb, y_train_nb, y_test_nb = train_test_split(X_nb, y_nb, test_size=0.2, random_state=0)
nb_model = GaussianNB()
nb_model.fit(X_train_nb, y_train_nb)
nb_predictions = nb_model.predict(X_test_nb)
accuracy = accuracy_score(y_test_nb, nb_predictions)
print(f"Naive Bayes Model Accuracy: {accuracy}")
plt.figure(figsize=(10, 5))
plt.scatter(X_test_nb, y_test_nb, color='purple', label='Actual')
plt.scatter(X_test_nb, nb_predictions, color='orange', label='Predicted', marker='x')
plt.xlabel('Experience')
plt.ylabel('Publication Category')
plt.title('Naive Bayes - Experience vs Publication Categories')
plt.legend()
plt.show()
