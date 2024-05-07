# Python Lab Question Bank

## Program 1
Write a Python program to:
- **a.** Create a synthetic faculty dataset with 100,000 rows in a CSV file.
- **b.** Load it into a list in Python.
- **c.** Use menu operators to add, search, and delete from the list.
- **d.** Read the experience of faculty (number) from the user and display the faculty name. If the experience is >10 years, display that they can participate in BOS.

## Program 2
Write a Python program to:
- **a.** Create a synthetic dataset for student details over 100,000 rows with student name, USN, CGPA, address, blood group, branch name, UG/PG, date of birth, and year of studying.
- **b.** Then load dataset into a tuple.
- **c.** Display a menu for searching student data.
- **d.** Read the branch name from the user and fetch the UG/PG students for whom CGPA > 9 (so they can apply for placement).

## Program 3
Write a Python program to:
- **a.** Create synthetic weather details in a CSV file.
- **b.** Load the CSV file data into a dictionary.
- **c.** Read a place name and display weather details.
- **d.** Read longitude & latitude values from the user and display weather details.

## Program 4
Write a Python program to detect the intensity of light in a room using an LDR (Light Dependent Resistor) and display the LDR Value as output. If the light is dim, then turn ON the red LED; otherwise, turn on the Green LED.

## Program 5
Write a Python program to:
- **a.** Generate 100,000 rows in a synthesized faculty dataset where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
- **b.** Read and load it into a list.
- **c.** Find out the correlation among the fields in the faculty dataset.
- **d.** Perform linear regression analysis and plot the predicted value.

## Program 6
Write a Python program to:
- **a.** Generate a faculty dataset with 100,000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of chapters, amount of consultancy work, fund received, and professional membership.
- **b.** Write a function to read the CSV file and load it into a tuple.
- **c.** Find out correlation among the fields in the faculty dataset.
- **d.** Perform linear regression analysis of experience vs. number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).
- **e.** Perform KNN analysis of experience vs. number of publications and plot the predicted value in separate graphs.
- **f.** Perform Naive Bayes algorithm for experience vs. number of publications and plot the predicted value in separate graphs.

## Program 7
Write a Python program to:
- **a.** Generate a faculty dataset with 100,000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
- **b.** Write a lambda function to read the CSV file and load it into tuples.
- **c.** Write regular expressions to search and display details of Associate professors with more than 15 years experience, Assistant Professors with more than 5 years experience, and Professors with more than 20 years experience.
- **d.** Perform association rule mining for associate professors for their performance relations in different contributions like number of publications and number of book chapters, number of publications and amount of consultancy work.

## Program 8
Write a Python program with objects and classes to:
- **a.** Generate a faculty dataset with 100,000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
- **b.** Write a lambda function to read the CSV file and load it into tuples.
- **c.** Write regular expressions to search and display details of Associate professors with more than 15 years experience, Assistant Professors with more than 5 years experience, and Professors with more than 20 years experience.
- **d.** Write a lambda function and regular expression to search for Associate professors with more than 25 years experience and load them into another temporary list called "asso_prof_25".
- **e.** In the "asso_prof_25" list, factor experience, publication count, and book-chapter count with binary values based on specific conditions.
- **f.** Perform association rule mining for associate professors for performance relations in different contributions like experience, designation, number of publications, and number of book chapters.

## Program 9
Write a Python program to:
- **a.** Create a CSV file called "books.csv" with synthesized data set having columns: Student USN, semester number, sub-code, subject name, book referred, book ID, grade scored.
- **b.** Use exception handling for following file operations:
  - **i.** Read the CSV file content into local variables.
  - **ii.** Extract only semester number, sub-code, book ID, and grade scored and store in another CSV file called "extracted-books.csv". Convert grade code to number when writing into the "extracted-books.csv".
  - **iii.** Analyze the correlation between semester number, sub-code, book ID, and grade scored.
  - **iv.** Convert the dataset into the required format to perform association rule mining and analyze the output.
  - **v.** Convert the dataset into the required format to perform collaborative filtering over the dataset.

## Program 10
Write a Python program to:
- **a.** Create a CSV file called "books.csv" with synthesized data set having columns: Student USN, semester number, sub-code, subject name, book referred, book ID, grade scored.
- **b.** Read the CSV file content into a linked list.
- **c.** Extract only semester number, sub-code, book ID, and grade scored and store in another CSV file called "extracted-books.csv". Convert grade code to number when writing into the "extracted-books.csv".
- **d.** Analyze the correlation between semester number, sub-code, book ID, and grade scored.
- **e.** Convert the dataset into the required format to perform association rule mining and analyze the output.
- **f.** Convert the dataset into the required format to perform collaborative filtering over the dataset.
