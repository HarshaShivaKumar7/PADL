# Python Lab Question Bank

1. Write a Python program to do the following.
   a. Create synthetic faculty data set with 100000 rows in a CSV file. 
   b. Load it to list data structure in python. 
   c. Use menu operators to add, search, delete from the list data structure. 
   d. Read experience of faculty (number) from user & display the faculty name, if it is >10 years display that they can participate in BOS.

2. Write a Python program to do the following.
   a. Create synthetic dataset for student details over 100000 rows with student name, USN, CGPA, address, blood group, branch name, UG/PG, date of birth and year of studying. 
   b. Load dataset to tuple data structure in python. 
   c. Display menu for searching a student data. 
   d. Read the branch name from the user and fetch the UG/PG students for where CGPA > 9. (So they can apply for placement)

3. Write a Python program to do the following.
   a. Create Synthesis Weather details in a csv file. 
   b. Load the csv file data into dictionary data structure in python.
   c. Read a place name and display weather details.
   d. Read longitude & latitude values from the user and display weather details.

4. Write a Python program to detect the intensity of light in a room using a LDR (Light Dependent Resistor) and display the LDR Value as output. If the light is dim, then ON the red LED, else on the Green LED.

5. Write a Python program to do the following.
   a. Write function Generate 100000 rows, synthesized faculty dataset where experience linearly mapped to designation, salary, no. of publications, no. of book chapters, amount of consultancy work, fund received, professional membership.
   b. Write function to Read and load it into a list data structure
   c. Write function to Find out the correlation among the fields in faculty dataset.
   d. Write function to Perform the Linear regression analysis and plot the predicted value.

6. Write a Python program to do the following.
   a. Generate faculty data set with 100000 rows and put in csv file where experience linearly mapped to designation, salary, no. of publications, no. of chapters, amount of consultancy work, fund received, professional membership.
   b. Write a function to Read csv file and load it into tuple data structure
   c. Write a function to Find out correlation among the fields in faculty dataset
   d. Perform the Linear Regression analysis of experience vs no. of publications & plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

7. Write a Python program to do the following.
   a. Generate faculty data set with 100000 rows and put in csv file where experience linearly mapped to designation, salary, no. of publications, no. of chapters, amount of consultancy work, fund received, professional membership.
   b. Write a function to Read csv file and load it into tuple data structure
   c. Perform KNN analysis of experience vs no. of publications & plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).
   d. Perform Naiye Bayes algorithm for experience vs no. of publications & plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

8. Write a Python program to do the following.
   a. Generate faculty data set with 100000 rows and put in csv file where experience linearly mapped to designation, salary, no of publication, no of book chapters, amount of consultancy work, fund received, professional membership.
   b. Write lambda function to Read csv file and load it into tuples data structure
   c. Write regular expression to search and display details of Associate professors with more than 15 years experience, assistant Professors with more than 5 years experience, Professors with more than 20 years experience.

9. Write a Python program to do the following.
   a. Generate faculty data set with 100000 rows and put in csv file where experience linearly mapped to designation, salary, no of publication, no of book chapters, amount of consultancy work, fund received, professional membership.
   b. Read csv file and load it into tuples data structure
   c. Perform association rule mining of associate professors for their performance relations in different contributions like No. of publication and no of book chapters, No. of publication and amount of consultancy work.

10. Write a Python program with objects and classes, to do the following.
    a. Generate faculty data set with 100000 rows and put in csv file where experience linearly mapped to designation, salary, no of publication, no of book chapters, amount of consultancy work, fund received, professional membership.
    b. Read csv file and load it into tuples data structure
    c. Search for associate professors with more than 25 years experience and load in another temp list called "asso_prof_25"
    d. In asso_prof_25 list do the following factoring:
       - If experience > 25, yes means set the value as 1 else 0
       - If publication count > 5, yes means set the value as 1 else 0
       - If book-chapter count > 5, yes means set the value as 1 else 0
    e. Perform the association rule mining of associate professors for the following performance relations in different contributions.
       - Experience, designation, no. of publications and no. of book chapters

11. Write a Python program to do the following.
    a. Create a csv file called "books.csv" with synthesized data set having the following columns: Student usn, semester-number, sub-code, subject name, book referred, book-id, grade scored.
    b. Use exception handling for following file operations.
       - Read the csv file content into local variables for accessing them in python
       - Extract only sem-number, sub-code, book-id and grade scored and store in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv", file Convert grade code to number (Sgrade-9, A grade-8,etc) and update into the file
       - Analyse the correlation between sem-number, sub-code, book-id and grade scored
       - Convert the data set in required format to perform association rule mining and analyse the output

12. Write a Python program to do the following.
    a. Create a csv file called "books.csv" with synthesized data set having the following columns: Student usn, semester-number, sub-code, subject name, book referred, book-id, grade scored.
    b. Use exception handling for following file operations.
       - Read the csv file content into local variables for accessing them in python
       - Extract only sem-number, sub-code, book-id and grade scored and store in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv", file Convert grade code to number (Sgrade-9, A grade-8,etc) and update into the file
       - Analyse the correlation between sem-number, sub-code, book-id and grade scored
       - Convert the data set in required format to Perform the collaboration filtering over the data set.

13. Write a Python program to do the following.
    a. Create a csv file called "books.csv" with synthesized data set having the following columns: Student usn, semester-number, sub-code, subject name, book referred, book-id, grade scored.
       - Read the csv file content into linked list data structure for accessing them in python
       - Extract only sem-number, sub-code, book-id and grade scored and store in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv", file Convert grade code to number (Sgrade-9, A grade-8,etc) and update into the file
       - Analyse the correlation between sem-number, sub-code, book-id and grade scored
       - Convert the data set in required format to perform association rule mining and analyse the output

14. Write a Python program to do the following.
    a. Create a csv file called "books.csv" with synthesized data set having the following columns: Student usn, semester-number, sub-code, subject name, book referred, book-id, grade scored.
       - Read the csv file content into linked list data structure for accessing them in python
       - Extract only sem-number, sub-code, book-id and grade scored and store in another CSV file called "extracted-books.csv".
       - When you write into the "extracted-books.csv", file Convert grade code to number (Sgrade-9, A grade-8,etc) and update into the file
       - Analyse the correlation between sem-number, sub-code, book-id and grade scored
       - Convert the data set in required format to Perform the collaboration filtering over the data set.
