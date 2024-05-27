# Python Lab Question Bank

1. **Write a Python program to do the following:**
   - **a.** Create synthetic faculty data set with 100000 rows in a CSV file.
   - **b.** Load it to list data structure in Python.
   - **c.** Use menu operators to add, search, delete from the list data structure.
   - **d.** Read experience of faculty (number) from user & display the faculty name. If it is >10 years, display that they can participate in BOS.

2. **Write a Python program to do the following:**
   - **a.** Create synthetic dataset for student details over 100000 rows with student name, USN, CGPA, address, blood group, branch name, UG/PG, date of birth, and year of studying.
   - **b.** Load dataset to tuple data structure in Python.
   - **c.** Display menu for searching student data.
   - **d.** Read the branch name from the user and fetch the UG/PG students where CGPA > 9 (so they can apply for placement).

3. **Write a Python program to do the following:**
   - **a.** Create Synthesis Weather details in a CSV file.
   - **b.** Load the CSV file data into dictionary data structure in Python.
   - **c.** Read a place name and display weather details.
   - **d.** Read longitude & latitude values from the user and display weather details.

4. **Write a Python program to detect the intensity of light in a room using an LDR (Light Dependent Resistor) and display the LDR value as output. If the light is dim, then turn on the red LED; otherwise, turn on the green LED.

5. **Write a Python program to do the following:**
   - **a.** Write a function to generate 100000 rows of a synthesized faculty dataset where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   - **b.** Write a function to read and load it into a list data structure.
   - **c.** Write a function to find out the correlation among the fields in the faculty dataset.
   - **d.** Write a function to perform linear regression analysis and plot the predicted value.

6. **Write a Python program to do the following:**
   - **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of chapters, amount of consultancy work, fund received, and professional membership.
   - **b.** Write a function to read the CSV file and load it into a tuple data structure.
   - **c.** Write a function to find out the correlation among the fields in the faculty dataset.
   - **d.** Perform linear regression analysis of experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

7. **Write a Python program to do the following:**
   - **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of chapters, amount of consultancy work, fund received, and professional membership.
   - **b.** Write a function to read the CSV file and load it into a tuple data structure.
   - **c.** Perform KNN analysis of experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).
   - **d.** Perform Naive Bayes algorithm for experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

8. **Write a Python program to do the following:**
   - **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   - **b.** Write a lambda function to read the CSV file and load it into a tuple data structure.
   - **c.** Write a regular expression to search and display details of associate professors with more than 15 years experience, assistant professors with more than 5 years experience, and professors with more than 20 years experience.

9. **Write a Python program to do the following:**
   - **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   - **b.** Read the CSV file and load it into a tuple data structure.
   - **c.** Perform association rule mining of associate professors for their performance relations in different contributions like number of publications and number of book chapters, number of publications and amount of consultancy work.

10. **Write a Python program with objects and classes to do the following:**
    - **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
    - **b.** Read the CSV file and load it into a tuple data structure.
    - **c.** Search for associate professors with more than 25 years experience and load them into another temporary list called "asso_prof_25".
    - **d.** In the "asso_prof_25" list, do the following factoring:
       - If experience > 25, set the value as 1; else 0.
       - If publication count > 5, set the value as 1; else 0.
       - If book-chapter count > 5, set the value as 1; else 0.
    - **e.** Perform association rule mining of associate professors for the following performance relations in different contributions: experience, designation, number of publications, and number of book chapters.

11. **Write a Python program to do the following:**
    - **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
    - **b.** Use exception handling for the following file operations:
       - Read the CSV file content into local variables for accessing them in Python.
       - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
       - Analyze the correlation between semester number, subject code, book ID, and grade scored.
       - Convert the data set into the required format to perform association rule mining and analyze the output.

12. **Write a Python program to do the following:**
    - **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
    - **b.** Use exception handling for the following file operations:
       - Read the CSV file content into local variables for accessing them in Python.
       - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
       - Analyze the correlation between semester number, subject code, book ID, and grade scored.
       - Convert the data set into the required format to perform collaborative filtering over the data set.

13. **Write a Python program to do the following:**
    - **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
       - Read the CSV file content into a linked list data structure for accessing them in Python.
       - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
       - Analyze the correlation between semester number, subject code, book ID, and grade scored.
       - Convert the data set into the required format to perform association rule mining and analyze the output.

14. **Write a Python program to do the following:**
    - **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
       - Read the CSV file content into a linked list data structure for accessing them in Python.
       - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.)

 and update the file.
       - Analyze the correlation between semester number, subject code, book ID, and grade scored.
       - Convert the data set into the required format to perform collaborative filtering over the data set.
