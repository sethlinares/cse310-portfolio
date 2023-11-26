import sqlite3 as sq

def create_connection(db_file): # Create a database connection to a SQLite database
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sq.connect(db_file)
    except sq.Error as e:
        print(e)
    return conn

def setup_database(connection): # Create tables if they don't exist
    """ Create tables if they don't exist """
    cur = connection.cursor() # Create a cursor object

    # Create Categories table
    cur.execute(''' CREATE TABLE IF NOT EXISTS Categories (
                        category_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    ); ''')

    # Create Expenses table
    cur.execute(''' CREATE TABLE IF NOT EXISTS Expenses (
                        expense_id INTEGER PRIMARY KEY,
                        category_id INTEGER,
                        amount REAL NOT NULL,
                        description TEXT NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (category_id) REFERENCES Categories (category_id)
                    ); ''')

    connection.commit()
