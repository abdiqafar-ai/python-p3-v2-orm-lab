import sqlite3

# Establish a global connection and cursor for all database operations
CONN = sqlite3.connect('your_database.db')
CURSOR = CONN.cursor()

def get_connection():
    """Returns the database connection object."""
    return CONN

def execute_query(query, params=()):
    """Helper function to execute queries and commit changes."""
    CURSOR.execute(query, params)
    CONN.commit()

