# MySQL questions:

### Set 1
A. Suppose a movie_studio has several film crews. The crews might be designated by a given studio as crew1, crew 2, and so on. However, other studios might use the same designations for crews, so the attribute crew_number is not a key for crews. Movie_studio holds the information like name, branch and several locations. Each crew holds information like sector and strength.
- List all movie studios which are not used a single crew.
- Retrieve the movie studio which uses the highest strength crew.
- Write a before insert trigger to check maximum number of crews to any studio is limited to 10.

### Set 2
A. The production company is organized into different studios. We store each studio’s name branch and location; every studio must own at least one movie. We store each movie’s title, sensor_number and year of production. Star may act in any number of movies and we store each actor's name and address.
- List all the studios of the movie “Kantara”;
- List all the actors, acted in a movie ‘Kantara’
- Write a deletion trigger that does not allow deleting current year movies.

### Set 3
A. The production company is organized into different studios. We store each studio’s name branch and location; a studio own any number of Cartoon-serials. We store each Cartoon-Serial’s title, sensor_number and year of production. Star may do voices in any number of Cartoon-Serials and we store each actor's name and address.
- Find the total number of actors who did voices in the Cartoon-Serial ‘Tom and Jerry’
- Retrieve the name of the studio, location, and Cartoon-Serials title in which star “Richard Kind” is voiced.
- Write a deletion trigger that does not allow deleting current year Cartoon-Serials.

### Set 4
A. Car marketing company wants to keep track of marketed cars and their owner. Each car must be associated with a single owner and an owner may have any number of cars. We store car’s registration number, model & color and owner’s name, address & SSN. We also store the date of purchase of each car.
- Find a person who owns the highest number of cars
- Retrieve persons and cars information purchased on the day 03-03-2023
- Write an insertion trigger to check the date of purchase must be less than the current date (must use the system date)

### Set 5
A. Puppy pet shop wants to keep track of dogs and their owners. The person can buy a maximum of three pet dogs. We store the person’s name, SSN and address and the dog’s name, date of purchase and sex. The owner of the pet dogs will be identified by SSN since the dog’s names are not distinct.
- List all pets owned by a person ‘Ramesh’.
- List all persons who have not owned a single pet
- Write a trigger to check the constraint that a person can buy a maximum of three pet dogs

### Set 6
A. Education institute is managing the online course enrollment system. Students can enroll in a maximum of six courses of their choice and a maximum of 60 students can be enrolled in any course. We store student details like name, USN, semester and several addresses, and course details like unique title, unique id and credits.
- Find the number of students enrolled in the course ‘ADBMS’
- Retrieve student names that are enrolled in the AI course but not enrolled in IOT.
- Write a trigger to establish the constraint that the students can enroll in a maximum of six courses of their choice.

### Set 7
A. The Sapna Book shop wants to keep track of orders of the book. The book is composed of unique id, title, year of publication, single author and single publisher. Each order will be uniquely identified by order-id and may have any number of books. We keep track of the quantity of each book ordered. We store the following details for author and publisher.
AUTHOR: unique author-id, name, city, country
PUBLISHER: unique publisher-id, name, city, country.
- Find the author who has published the highest number of books
- List the books published by a specific publisher during the year 2022.
- Write before insertion trigger to book to check the year of publication should allow the current year only.

### Set 8
A. The commercial bank wants to keep track of the customer’s account information. Each customer may have any number of accounts and accounts can be shared by any number of customers. The system will keep track of the date of the last transaction. We store the following details.
Account: unique account-number, type and balance
Customer: unique customer-id, name and several addresses composed of street, city and state
- Add 3% interest to the customer who have less than 1000 balances and 6% interest to remaining customers.
- List joint accounts involving more than three customers
- Write an insertion trigger to allow only the current date for the date of the last transaction field.

### Set 9
A. Consider the Insurance database given below. The primary keys are underlined and the data types are specified.  
PERSON (driver-id #: String, name: string, address: strong)  
CAR (Regno: string, model: string, year: int)  
ACCIDENT (report-number: int, accd-date: date, location: string)  
OWNS (driver-id #:string, Regno: string)  
PARTICIPATED (driver-id: string, Regno: string, report-number: int, damage_amount: int)
Create the above tables by properly specifying the primary keys and the foreign keys. Enter at least five tuples for each relation.
- Update the damage amount for the car with a specific Regno in the accident with report number 12 to 25000.  
- Find the total number of people who owned cars that were involved in accidents in 2008.  
- Find the number of accidents in which cars belonging to a specific model were involved.   
- Write before insert trigger to if the accident date is on or before the current date.

### Set 10
A. Consider the following shipment schema. The primary keys are underlined. Assume relevant data types for attributes. 
CUSTOMER (cust#, cname, city) 
ORDER (order#, odate, cust#, ord-Amt) 
ORDER-ITEM (order#, Item#, qty) 
ITEM (item#, unit price) 
SHIPMENT (order#, ship-date)
Create the above tables in SQL. Specify primary and foreign keys properly. Enter at least 5 tuples in each table with relevant data. Solve the following queries.
- List the name of the customer, no. of orders placed by each customer residing in Bangalore city. 
- List the order# for orders that were shipped from all the warehouses that the company has in a specific city.
- List the customer names who have not ordered item no. 10.
- Write a deletion trigger, set NULL on deletion of an ITEM.


### MongoDB Questions:

### Restaurant Database
Consider the following restaurant database with the following attributes - Name, address – (building, street, area, pincode), id, cuisine, nearby landmarks, online delivery- yes/no, famous for (name of the dish). Create 10 collections with data relevant to the following questions. Write and execute MongoDB queries:
1. List the name and address of all restaurants in Bangalore with Italian cuisine.
2. List the name, address and nearby landmarks of all restaurants in Bangalore where North Indian thali is available.
3. List the name and address of restaurants and also the dish the restaurant is famous for, in Bangalore.
4. List the name and address of restaurants and also the dish the restaurant is famous for, in Bangalore where online delivery is available.

### Tourist Places Database
Consider the following Tourist places table with the following attributes - Place, address – (state), id, tourist attractions, best time of the year to visit, modes of transport (include nearest airport, railway station etc), accommodation, food - what not to miss for sure. Create 10 collections with data relevant to the following questions. Write and execute MongoDB queries:
1. List all the tourist places of Karnataka.
2. List the tourist attractions of Kerala. Exclude accommodation and food.
3. List the places sorted state wise.

### Movie Database
Consider the following Movie table with the following attributes - Actor_name, Actor_id, Actor_birthdate, Director_name, Director_id, Director_birthdate, film_title, year of production, type (thriller, comedy, etc.). Create 10 collections with data relevant to the following questions. Write and execute MongoDB queries:
1. List all the movies acted by John in the year 2018.
2. List only the actor names and type of the movie directed by Ram.
3. List all the movies acted by John and Elly in the year 2012.
4. List only the name and type of the movie where Ram has acted, sorted by movie names.




** PYTHON PROGRAMS


1. **Write a Python program to do the following:**
   **a.** Create synthetic faculty data set with 100000 rows in a CSV file.
   **b.** Load it to list data structure in Python.
   **c.** Use menu operators to add, search, delete from the list data structure.
   **d.** Read experience of faculty (number) from user & display the faculty name. If it is >10 years, display that they can participate in BOS.

2. **Write a Python program to do the following:**
   **a.** Create synthetic dataset for student details over 100000 rows with student name, USN, CGPA, address, blood group, branch name, UG/PG, date of birth, and year of studying.
   **b.** Load dataset to tuple data structure in Python.
   **c.** Display menu for searching student data.
   **d.** Read the branch name from the user and fetch the UG/PG students where CGPA > 9 (so they can apply for placement).

3. **Write a Python program to do the following:**
   **a.** Create Synthesis Weather details in a CSV file.
   **b.** Load the CSV file data into dictionary data structure in Python.
   **c.** Read a place name and display weather details.
   **d.** Read longitude & latitude values from the user and display weather details.

4. **Write a Python program to detect the intensity of light in a room using an LDR (Light Dependent Resistor) and display the LDR value as output. If the light is dim, then turn on the red LED; otherwise, turn on the green LED.**

5. **Write a Python program to do the following:**
   **a.** Wrie a function to generate 100000 rows of a synthesized faculty dataset where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   **b.** Write a function to read and load it into a list data structure.
   **c.** Write a function to find out the correlation among the fields in the faculty dataset.
   **d.** Write a function to perform linear regression analysis and plot the predicted value.

6. **Write a Python program to do the following:**
   **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of chapters, amount of consultancy wor, fund received, and professional membership.
   **b.** Write a function to read the CSV file and load it into a tuple data structure.
   **c.** Write a function to find out the correlation among the fields in the faculty dataset.
   **d.** Perform linear regression analysis of experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

7. **Write a Python program to do the following:**
   **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of chapters, amount of consultancy work, fund received, and professional membership.
   **b.** Write a function to read the CSV file and load it into a tuple data structure.
   **c.** Perform KNN analysis of experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).
   **d.** Perform Naive Bayes algorithm for experience vs number of publications and plot the predicted value in separate graphs (x-axis - experience, y-axis - predicted value).

8. **Write a Python program to do the following:**
   **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   **b.** Write a lambda function to read the CSV file and load it into a tuple data structure.
   **c.** Write a regular expression to search and display details of associate professors with more than 15 years experience, assistant professors with more than 5 years experience, and professors with more than 20 years experience.

9. **Write a Python program to do the following:**
   **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
   **b.** Read the CSV file and load it into a tuple data structure.
   **c.** Perform association rule mining of associate professors for their performance relations in different contributions like number of publications and number of book chapters, number of publications and amount of consultancy work.

10. **Write a Python program with objects and classes to do the following:**
    **a.** Generate a faculty data set with 100000 rows and put it in a CSV file where experience is linearly mapped to designation, salary, number of publications, number of book chapters, amount of consultancy work, fund received, and professional membership.
    **b.** Read the CSV file and load it into a tuple data structure.
    **c.** Search for associate professors with more than 25 years experience and load them into another temporary list called "asso_prof_25".
    **d.** In the "asso_prof_25" list, do the following factoring:

    - If experience > 25, set the value as 1; else 0.
    - If publication count > 5, set the value as 1; else 0.
    - If book-chapter count > 5, set the value as 1; else 0.
    - **e.** Perform association rule mining of associate professors for the following performance relations in different contributions: experience, designation, number of publications, and number of book chapters.

11. **Write a Python program to do the following:**
    **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
    **b.** Use exception handling for the following file operations:

    - Read the CSV file content into local variables for accessing them in Python.
    - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
    - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
    - Analyze the correlation between semester number, subject code, book ID, and grade scored.
    - Convert the data set into the required format to perform association rule mining and analyze the output.

12. **Write a Python program to do the following:**
    **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
    **b.** Use exception handling for the following file operations:

    - Read the CSV file content into local variables for accessing them in Python.
    - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
    - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
    - Analyze the correlation between semester number, subject code, book ID, and grade scored.
    - Convert the data set into the required format to perform collaborative filtering over the data set.

13. **Write a Python program to do the following:**
    **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.

    - Read the CSV file content into a linked list data structure for accessing them in Python.
    - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
    - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
    - Analyze the correlation between semester number, subject code, book ID, and grade scored.
    - Convert the data set into the required format to perform association rule mining and analyze the output.

14. **Write a Python program to do the following:**
    **a.** Create a CSV file called "books.csv" with a synthesized data set having the following columns: student USN, semester number, subject code, subject name, book referred, book ID, grade scored.
    - Read the CSV file content into a linked list data structure for accessing them in Python.
    - Extract only semester number, subject code, book ID, and grade scored and store them in another CSV file called "extracted-books.csv".
    - When you write into the "extracted-books.csv" file, convert grade code to number (S grade - 9, A grade - 8, etc.) and update the file.
    - Analyze the correlation between semester number, subject code, book ID, and grade scored.
    - Convert the data set into the required format to perform collaborative filtering over the data set.
