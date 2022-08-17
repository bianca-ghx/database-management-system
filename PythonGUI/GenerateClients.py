import mysql.connector as msql
from mysql.connector import Error

import pandas as pd
import names
import random

# generating 200 client entries for our client table

# function we found online to generate some random phone numbers
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

# calling the random_phone_num_generator function, to obtain 200 random numbers
phone_num = [random_phone_num_generator() for _ in range(200)]

# list containing some of the most popular email providers
# which will be picked randomly, to generate emails
email_handle = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier', 'icloud']

# list containing some characters to separate the first name from the last name
# also picked randomly
email_separator = ['.', '_', '']

# declaring list for the randomly generated names and emails
rand_names = []
emails = []


for _ in range(200):
    # generate first_name and last_name using names module
    first_name = names.get_first_name() # e.g: Theodor
    last_name = names.get_last_name() # e.g: Popescu
    # create the name and append it to rand_names
    rand_names.append(f'{first_name} {last_name}')
    # pick random email provider and separator using random
    email_handle_index = random.randrange(1, len(email_handle), 1)
    email_separator_index = random.randrange(1, len(email_separator), 1)
    # create the email and append  it to emails
    emails.append(f'{first_name}{email_separator[email_separator_index]}{last_name}@{email_handle[email_handle_index]}.com')

# create 200 random IDs
ID = random.sample(range(1000000000, 9999999999, 1), 200)

# create Pandas dataframe which stored the idCLient, name, phone and email
client_df = pd.DataFrame(columns=['idClient', 'name', 'phone', 'email'])
client_df['idClient'] = ID
client_df['name'] = rand_names
client_df['phone'] = phone_num
client_df['email'] = emails

# generating MySQL connection using mysql.connector
# adding data from client_df into client table of booksdb
try:
    conn = msql.connect(host='localhost',
                        database='booksdb', user='root',
                        password='Parola123')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS clients;')
        print('Creating table....')
        cursor.execute("CREATE TABLE clients (idClient VARCHAR(20) PRIMARY KEY NOT NULL, name VARCHAR(100) NOT NULL,  phone VARCHAR(20), email VARCHAR(200))")
        print("BOOKS table is created....")
        for i, row in client_df.iterrows():
            sql = "INSERT INTO booksdb.clients VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not autocommitted by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)