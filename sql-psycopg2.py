import psycopg2

"""
To run the app, type: python3 sql-psycopg2.py
into the terminal window.

Note - if you encounter an error, type: set_pg
into the terminal and then retry above step to run.
"""

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Note - %s is a Python String Holder which allows it
# to refer to data in ["Example"]

# -------------------------------------------------------- Query 1:
# Retrieves all columns and rows from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist"')

# -------------------------------------------------------- Query 2:
# Retrieves the "Name" column for all rows in the "Artist" table.
# cursor.execute('SELECT "Name" FROM "Artist"')

# -------------------------------------------------------- Query 3:
# Retrieves all columns and rows from the "Artist" table where
# the "Name" column is equal to "Queen".
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# -------------------------------------------------------- Query 4:
# Retrieves all columns and rows from the "Artist" table where
# the "ArtistId" column is equal to 51.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# -------------------------------------------------------- Query 5:
# Retrieves all columns and rows from the "Album" table where
# the "ArtistId" column is equal to 51.
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# -------------------------------------------------------- Query 6:
# Retrieves all columns and rows from the "Track" table where
# the "Composer" column is equal to "Queen".
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
