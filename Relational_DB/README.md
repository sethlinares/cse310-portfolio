# Overview

For this project, I decided to develop an application that integrates with a SQL relational database. The core of this software is an expense tracker, designed to manage financial records in a user friendly manner. It allows users to add, update, delete, and view expense records. This program was built with a Command Line Interface (CLI), offering simple navigation through menu options. Users can easily add expense categories, record individual expenses, and view or modify these records as needed. The purpose behind creating this software was to develop and deepen my understanding of database management and SQL operations within a Python environment. It was an opportunity to apply some of my previous theoretical knowledge in a practical setting, which allows me to enhance my skills in database handling and Python programming.

# Video Demonstration

[Software Demo Video](https://youtu.be/XiSCcsu10aI)

# Relational Database

For this project, I utilized SQLite, a lightweight, yet powerful relational database system. SQLite offers the flexibility needed for development without the overhead of setting up a server-based database system.

The database structure consists of two primary tables:
1. **Categories**: This table stores different expense categories, each with a unique identifier.
2. **Expenses**: This table records the individual expenses. It includes fields for the amount, description, date, and a reference to the corresponding category from the Categories table.

# Development Environment

The tools and technologies I employed in this project include:
- **Python**: A versatile programming language that was used to create the software's functionality.
- **SQLite3 Library**: This Python library was crucial for integrating SQLite database operations into the software.
- **Visual Studio Code**: My preferred integrated development environment (IDE) for writing and testing the code.

# Useful Websites

Throughout this project, several websites provided invaluable information and guidance:
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Stack Overflow](https://stackoverflow.com/)

# Future Work

1. **GUI Implementation**: Introducing a Graphical User Interface for improved user interaction and accessibility.
2. **Advanced Reporting Features**: Developing functionalities for generating detailed expense reports.
3. **Data Visualization**: Integrating data visualization tools for better insights into expense trends and patterns.

