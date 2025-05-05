"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect('dogs.db')
cursor = conn.cursor()


# Create a dogs table with autoincrementing ID
def create_dogs_table():

    """TODO"""
    cursor.execute("""CREATE TABLE IF NOT EXISTS dogs(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,breed NOT NULL, age INTEGER NOT NULL )""")
    conn.commit()

# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):

    """TODO"""
    cursor.execute("""INSERT INTO dogs (name ,age ,breed)VALUES (?,?,?) """,(name,age,breed))
    conn.commit()


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():

    # return the rows
    cursor.execute('SELECT *  FROM dogs')
    return cursor.fetchall()
