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
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    logging.info(f"Executed SQL from {sql_file}")

# Function to perform a query (e.g., aggregation, filter, group by, join, etc.)
def query_database(db_path, sql_file):
    conn = sqlite3.connect(db_path)
    with open(sql_file, 'r') as file:
        query = file.read()
    result = conn.execute(query).fetchall()
    conn.close()
    logging.info(f"Executed query from {sql_file}")
    return result

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