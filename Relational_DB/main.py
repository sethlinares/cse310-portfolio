from database import create_connection, setup_database
from cli_interface import main_menu

def main():
    conn = create_connection("expenses.db")
    # Ensure tables are created
    setup_database(conn)  
    # Pass the connection to the main menu
    main_menu(conn)  
    conn.close()

if __name__ == '__main__':
    main()
