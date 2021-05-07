#!/usr/env python3

import sqlite3

# Creating the first DB
data_base = sqlite3.connect('my_first_database.db')

# Tool that allows me to execute the SQL commands into the db
cursor = data_base.cursor()
cursor.execute('CREATE TABLE people(name text, age integer, email text)')

# Inserting data into the data base
cursor.execute('INSERT INTO people VALUES("Victor Kolis", 26, "victorkolis@protonmail.com")')

# Commiting the data into the data base
data_base.commit()
