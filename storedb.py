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
        idStore INTEGER PRIMARY KEY,
        SquareFeet INTEGER,
        StoreType VARCHAR(45),
        LocationType VARCHAR(1),
        Address VARCHAR(45),
        City VARCHAR(45),
        StoreState VARCHAR(45),
        ZipCode VARCHAR(10)
         );
    
    CREATE TABLE IF NOT EXISTS Product(
        idProduct INTEGER NOT NULL,
        Name VARCHAR(30),
        Price DECIMAL,
        CategoryID INTEGER,
        Description VARCHAR(90)
        );
    
    CREATE TABLE IF NOT EXISTS Category(
        idCategory INTEGER NOT NULL,
        Name VARCHAR(45),
        Description VARCHAR(90)
        );
    
    CREATE TABLE IF NOT EXISTS Store_Product(
        ProductID INTEGER NOT NULL,
        StoreID INTEGER NOT NULL,
        quantity INTEGER
        );

    ''')

    conn.commit()
    print(f"{dbname} now created.")
    conn.close()



# Create a second function fill that uses inserts to add values to each of the four tables.
# You should have at least two rows in each table.
'''
def fill(dbname):
    conn = sqlite3.connect(dbname)
    ...
'''
