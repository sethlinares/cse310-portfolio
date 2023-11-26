import sqlite3 as sq

def add_category(connection, name): # Add a new category (INSERT)
    sql = ''' INSERT INTO Categories(name) 
              VALUES(?) '''
    cur = connection.cursor() # Create a cursor object
    cur.execute(sql, (name,)) # Execute the SQL statement
    connection.commit() # Commit the changes



def add_expense(connection, category_id, amount, description, date): # Add a new expense (INSERT)
    sql = ''' INSERT INTO Expenses(category_id, amount, description, date)
              VALUES(?,?,?,?) '''
    cur = connection.cursor() 
    cur.execute(sql, (category_id, amount, description, date))
    connection.commit() # Commit the changes



def update_expense(connection, expense_id, category_id, amount, description, date): # Update an expense (UPDATE)
    sql = ''' UPDATE Expenses
              SET category_id = ? ,
                  amount = ? ,
                  description = ? ,
                  date = ?
              WHERE expense_id = ?'''
    cur = connection.cursor()
    cur.execute(sql, (category_id, amount, description, date, expense_id))
    connection.commit() # Commit the changes



def delete_expense(connection, expense_id): # Delete an expense (DELETE)
    sql = 'DELETE FROM Expenses WHERE expense_id=?'
    cur = connection.cursor()
    cur.execute(sql, (expense_id,))
    connection.commit() # Commit the changes



def query_expenses(connection, query, params): # Query expenses (SELECT)
    cur = connection.cursor()
    cur.execute(query, params)
    return cur.fetchall() # Return all rows



def query_categories(connection, query, params): # Query categories (SELECT)
    cur = connection.cursor()
    cur.execute(query, params)
    return cur.fetchall() # Return all rows


def purge_database(conn): # Purge the database (DELETE)
    try:
        cur = conn.cursor()
        # List all tables to be purged
        cur.execute("DELETE FROM Expenses;")
        cur.execute("DELETE FROM Categories;")
        conn.commit() # Commit the changes
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback() # Rollback the changes if an error occurs
