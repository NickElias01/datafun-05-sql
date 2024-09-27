"""
db_operations_nickelias.py

This script performs various SQL operations on the initialized SQLite database. It includes functionality
to delete records, update records, and execute various queries (aggregation, filtering, grouping, joining, sorting).

Dependencies:
- sqlite3: for database operations.
- pathlib: for handling file paths.
- logging: for logging information and errors during operations.

Usage:
Run this script to perform database operations after the database has been initialized.

Example:
    python db_operations_nickelias.py
"""


import sqlite3
import pathlib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths for SQL files and database
base_dir = pathlib.Path(__file__).parent
db_file_path = base_dir / "project.db"
sql_dir = base_dir / "sql"  # Directory where SQL files are located

# Read SQL from a file and execute it
def execute_sql_from_file(db_path, sql_file):
    try:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
    except FileNotFoundError:
        logging.error(f"Error: The file {sql_file} was not found.")
        return
    except Exception as e:
        logging.error(f"Error reading the SQL file: {e}")
        return
    
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        logging.info(f"Executed SQL from {sql_file}")
    except Exception as e:
        logging.error(f"Error executing SQL from {sql_file}: {e}")
    finally:
        conn.close()


# Function to perform a query (e.g., aggregation, filter, group by, join, etc.)
def query_database(db_path, sql_file):
    try:
        conn = sqlite3.connect(db_path)
        with open(sql_file, 'r') as file:
            query = file.read()
        result = conn.execute(query).fetchall()
        logging.info(f"Executed query from {sql_file}")
        return result
    except Exception as e:
        logging.error(f"Error executing query from {sql_file}: {e}")
        return []
    finally:
        conn.close()


def delete_records(db_path, sql_dir):
    execute_sql_from_file(db_path, sql_dir / "delete_records.sql")

def update_records(db_path, sql_dir):
    execute_sql_from_file(db_path, sql_dir / "update_records.sql")

def query_aggregation(db_path, sql_dir):
    return query_database(db_path, sql_dir / "query_aggregation.sql")

def query_filter(db_path, sql_dir):
    return query_database(db_path, sql_dir / "query_filter.sql")

def query_group_by(db_path, sql_dir):
    return query_database(db_path, sql_dir / "query_group_by.sql")

def query_join(db_path, sql_dir):
    return query_database(db_path, sql_dir / "query_join.sql")

def query_sorting(db_path, sql_dir):
    return query_database(db_path, sql_dir / "query_sorting.sql")

# Example main function to test different operations
def main():
    logging.info("Starting database operations...")
    delete_records(db_file_path, sql_dir)
    logging.info("Deleted records from the tables")

    update_records(db_file_path, sql_dir)
    logging.info("Updated records in the tables")
    
    agg_result = query_aggregation(db_file_path, sql_dir)
    logging.info(f"Aggregation Query Result: {agg_result}")

    filter_result = query_filter(db_file_path, sql_dir)
    logging.info(f"Filter Query Result: {filter_result}")


if __name__ == "__main__":
    main()