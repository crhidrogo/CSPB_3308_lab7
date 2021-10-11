# Create a python file storedb.py that initializes a database
# The function should define a function create that takes a single argument (sqlite3 database filename)
# You will need four CREATE TABLE statements in your script.
# You can use rowid as the primary key for each of the four tables.
import sqlite3

def create(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()    

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Store(
        rowid INTEGER PRIMARY KEY AUTOINCREMENT,
         idStore INTEGER NOT NULL
         );
    
    CREATE TABLE IF NOT EXISTS Product(
        rowid INTEGER PRIMARY KEY AUTOINCREMENT,
        idStore INTEGER NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS Category(
        rowid INTEGER PRIMARY KEY AUTOINCREMENT,
        idStore INTEGER NOT NULL
        );
    
    CREATE TABLE IF NOT EXISTS Store_Product(
        ProductID INTEGER NOT NULL,
        StoreID INTEGER NOT NULL,
        quantity INTEGER
        );

    ''')



# Create a second function fill that uses inserts to add values to each of the four tables.
# You should have at least two rows in each table.
'''
def fill(dbname):
    conn = sqlite3.connect(dbname)
    ...
'''
