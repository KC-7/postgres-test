# PostgreSQL Test

Following CI Walkthrough Tutorial

## Terminal Example:

Create CSV File using data extracted from Chinook Database:

`\copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;
`

## sql-psycopg2.py

This app uses the psycopg2 library to connect to the "chinook" database and execute SQL queries. 

### psycopg2
psycopg2 is a popular Python library for working with PostgreSQL databases. It provides a simple and efficient way to interact with PostgreSQL databases using Python. psycopg2 allows developers to establish a connection to a PostgreSQL database, execute SQL queries, and retrieve data from the database.

### Chinook
Chinook is a sample database that is often used for testing and learning purposes. It was originally created by the Microsoft SQL Server team as a sample database for their database products, but it has since been ported to other database platforms including PostgreSQL. The Chinook database contains tables for artists, albums, tracks, invoices, and other entities that are commonly used in the music industry, making it a useful resource for learning about database design and SQL querying.

### How to Run
To run the app, type `python3 sql-psycopg2.py` into the terminal window.

If you encounter an error, type `set_pg` into the terminal and then retry the above step to run.

### What to Expect

The app includes 6 SQL queries (Queries 1-6), each of which is commented out by default. Uncomment a query by removing the "#" character at the beginning of the line, and then run the app to execute the query.

- Query 1: Retrieves all columns and rows from the "Artist" table.
- Query 2: Retrieves the "Name" column for all rows in the "Artist" table.
- Query 3: Retrieves all columns and rows from the "Artist" table where the "Name" column is equal to "Queen".
- Query 4: Retrieves all columns and rows from the "Artist" table where the "ArtistId" column is equal to 51.
- Query 5: Retrieves all columns and rows from the "Album" table where the "ArtistId" column is equal to 51.
- Query 6: Retrieves all columns and rows from the "Track" table where the "Composer" column is equal to "Queen".

After executing a query, the app fetches the results and prints them to the terminal.

Before printing the results, the connection to the database is closed.

## sql-expression.py

