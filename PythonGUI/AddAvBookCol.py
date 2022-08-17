import mysql.connector as msql
from mysql.connector import Error, connect

import pandas as pd
import random

# adding available_books column to db

# reading books2.csv as pandas dataframe
# books2.csv is the same as  the Goodreads data base got online, but with the date formated correctly
books2_df = pd.read_csv('books2.csv')

# generating available books column, which has 11123 random numbers from 1 to 5
randomlist = [random.randrange(1, 6, 1) for _ in range(11123)]

# adding available books column to t
books2_df['available_book'] = randomlist

# saving the pandas dataframe as books3.csv
books2_df.to_csv('books3.csv', index=False)

# loading books3.csv into MySQL

# reading books3.csv
bookData = pd.read_csv('books3.csv', error_bad_lines=False)

# generating the MySQL connection using mysql.connector
# and creating the bookdb database
try:
    conn = msql.connect(host='localhost', user='root',
                        password='Parola123')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE booksdb")
        print("Books database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

# generating the MySQL connection using mysql.connector
# and loading books3.csv into the table initial_db in booksdb
try:
    conn = msql.connect(host='localhost',
                        database='booksdb', user='root',
                        password='Parola123')

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS intial_db;')
        print('Creating table....')
        cursor.execute("CREATE TABLE initial_db (bookID INT NOT NULL, title VARCHAR(400) NOT NULL, authors VARCHAR(1000) NOT NULL, average_rating FLOAT, ISBN VARCHAR(50), ISBN13 VARCHAR(50), language_code VARCHAR(50), num_pages INT, ratings_count INT, text_reviews INT, publication_date VARCHAR(10), publisher VARCHAR(100), available_books TINYINT)")
        print("BOOKS table is created....")
        for i,row in bookData.iterrows():
            sql = "INSERT INTO booksdb.initial_db VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

