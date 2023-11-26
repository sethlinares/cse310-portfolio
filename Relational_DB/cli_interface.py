from business_logic import add_category, add_expense, update_expense, delete_expense, query_expenses, query_categories, purge_database

def main_menu(conn):
    while True: # Loop until user exits
        print("\nExpense Tracker Application")
        print("1. Add Category")
        print("2. Add Expense")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. View Expenses")
        print("6. View Categories")
        print("7. Purge Database")
        print("8. Exit")

        choice = input("Enter option: ")

        # Handle user input with if statements
        if choice == "1": 
            add_category_ui(conn)
        elif choice == "2":
            add_expense_ui(conn)
        elif choice == "3":
            update_expense_ui(conn)
        elif choice == "4":
            delete_expense_ui(conn)
        elif choice == "5":
            view_expenses_ui(conn)
        elif choice == "6":
            view_categories_ui(conn)
        elif choice == "7":
            purge_database_ui(conn)
        elif choice == "8":
            break
        else:
            print("Invalid option. Please try again.")



def add_category_ui(conn): # Add a new category
    print("\nAdd New Category")
    name = input("Enter category name: ")
    add_category(conn, name)
    print("Category added successfully.")




def display_categories(conn): # Display all categories
    categories = query_categories(conn, "SELECT * FROM Categories", ())
    print("\nAvailable Categories:")
    for category in categories:
        print(f"Category ID: {category[0]}, Name: '{category[1]}'")




def add_expense_ui(conn): # Add a new expense
    print("\nAdd New Expense")
    display_categories(conn)

    category_id = input("\nEnter category ID: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    add_expense(conn, category_id, amount, description, date)
    print("Expense added successfully.")



def select_expense_ui(conn): # Select an expense
    expenses = query_expenses(conn, "SELECT expense_id, amount, description, date FROM Expenses", ())

    if not expenses: # Check if there are any expenses
        print("No expenses to select.")
        return None
    print("\nSelect an expense:")

    for index, expense in enumerate(expenses, 1): # Display expenses
        print(f"{index}. {expense[2]} (Amount: {expense[1]}, Date: {expense[3]})")

    while True: # Loop until user enters a valid selection
        try:
            selection = int(input("Enter the number of the expense (or 0 to go back): "))
            if selection == 0:
                return None
            selected_expense = expenses[selection - 1]
            return selected_expense[0]  # Return the expense_id
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")



def update_expense_ui(conn): # Update an expense
    expense_id = select_expense_ui(conn)

    if expense_id is not None:
        display_categories(conn)
        category_id = input("\nEnter new category ID: ")
        amount = input("Enter new amount: ")
        description = input("Enter new description: ")
        date = input("Enter new date (YYYY-MM-DD): ")

        update_expense(conn, expense_id, category_id, amount, description, date) # Update the expense
        print("Expense updated successfully.")

    else:
        print("Returning to main menu.")




def delete_expense_ui(conn): # Delete an expense
    expense_id = select_expense_ui(conn)
    if expense_id is not None:
        delete_expense(conn, expense_id)
        print("Expense deleted successfully.")
    else:
        print("Returning to main menu.")



def view_expenses_ui(conn): # View all expenses
    expenses = query_expenses(conn, "SELECT * FROM Expenses", ())
    if expenses:
        print("\nExpenses:")
        for index, expense in enumerate(expenses, 1):
            print(f"{index}. {expense}")
    else:
        print("No expenses to display.")

 
def view_categories_ui(conn): # View all categories
    categories = query_categories(conn, "SELECT * FROM Categories", ())
    if categories:
        print("\nCategories:")
        for category in categories:
            print(f"ID: {category[0]}, Name: '{category[1]}'")
    else:
        print("\nNo categories to display.")



def purge_database_ui(conn): # Purge the database
    print("\nWARNING: This will delete all data from the database.")
    confirmation = input("Type 'I am sure' to confirm: ") # Confirm with user
    if confirmation == "I am sure":
        purge_database(conn) # Purge the database
        print("Database purged successfully.")
    else:
        print("Database purge canceled.")
