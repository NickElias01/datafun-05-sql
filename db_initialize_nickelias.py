import sqlite3
import pathlib
import pandas as pd

# Define paths for SQL files and database
base_dir = pathlib.Path(__file__).parent
db_file_path = base_dir / "project.db"
sql_dir = base_dir / "sql"  # Directory where SQL files are located
author_data_path = base_dir / "data" / "authors.csv"
book_data_path = base_dir / "data" / "books.csv"

# Verify and create folders if necessary
def verify_and_create_folders(paths):
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)

# Function to create a new SQLite database
def create_database(db_path):
    conn = sqlite3.connect(db_path)
    conn.close()

# Read SQL from a file and execute it
def execute_sql_from_file(db_path, sql_file):
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

# Create tables from the SQL file
def create_tables(db_path, sql_dir):
    execute_sql_from_file(db_path, sql_dir / "create_tables.sql")

# Insert data from CSV into the tables
def insert_data_from_csv(db_path, author_csv, book_csv):
    conn = sqlite3.connect(db_path)
    
    # Insert authors
    authors_df = pd.read_csv(author_csv)
    authors_df.to_sql('authors', conn, if_exists='append', index=False)
    
    # Insert books
    books_df = pd.read_csv(book_csv)
    books_df.to_sql('books', conn, if_exists='append', index=False)
    
    conn.close()

# Define the main function that will call your functions
def main():
    paths_to_verify = [db_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_dir)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()