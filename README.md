# datafun-05-sql
## Module 5 Repo

This project is designed to manage a SQLite database that stores and organizes information about authors and their books. It allows users to initialize a database, create tables, and populate them with data from CSV files. The project includes various SQL scripts to perform operations such as deleting records, updating existing entries, and executing queries for data aggregation, filtering, grouping, joining, and sorting. By leveraging Python and the Pandas library, this project facilitates efficient data handling and manipulation, making it an excellent resource for learning about database management and SQL operations.

## Table of Contents
- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [Folder Structure](#folder-structure)
- [SQL Scripts](#sql-scripts)
- [Database Schema Design](#database-schema-design)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This project initializes and operates a SQLite database that stores information about authors and books. It provides functionalities to create the database, create tables, populate the tables from CSV files, and perform various SQL operations such as deleting and updating records.

## Setup Instructions

To set up this project on your local machine, follow these steps:

1. **Clone the Repository**:
Open PowerShell or bash and run:

    ```powershell
    git clone "https://github.com/nickelias01/datafun-05-sql.git"
    cd "datafun-05-sql" 
    ```

2. **Set up and activate Virtual Environment**:
Run the following command to create a virtual environment named .venv:

    ```powershell
    python -m venv .venv
    ```

    Then use the following command to activate the virtual environment:
    
    ```powershell
    .\.venv\Scripts\Activate
    ```

3. **Install Requirements**:
    ```powershell
    py pip install -r requirements.txt
    ```

## Folder Structure:
```
datafun-05-sql/
│
├── .venv/                    # Virtual environment directory
├── data/                     # Folder containing CSV files
│   ├── authors.csv           # CSV file for authors
│   └── books.csv             # CSV file for books
│
├── sql/                      # Folder containing SQL scripts
│   ├── create_tables.sql     # SQL script to create tables
│   ├── delete_records.sql    # SQL script to delete records
│   ├── update_records.sql    # SQL script to update records
│   ├── query_aggregation.sql  # SQL script for aggregation queries
│   ├── query_filter.sql      # SQL script for filtering queries
│   ├── query_group_by.sql    # SQL script for grouping queries
│   ├── query_join.sql        # SQL script for join queries
│   ├── query_sorting.sql     # SQL script for sorting queries
│   └── update_records.sql    # SQL script for updating records
│
├── db_initialize_nickelias.py          # Script to initialize the database
└── db_operations_nickelias.py          # Script for database operations
└── requirements.txt                    # List of dependencies
```

## SQL Scripts:
This project contains several SQL scripts that perform various operations on the database:

* create_tables.sql: Creates the authors and books tables.
* delete_records.sql: Deletes records from the tables.
* update_records.sql: Updates records in the tables.
* query_aggregation.sql: Performs aggregation queries.
* query_filter.sql: Performs filtering queries.
* query_group_by.sql: Groups records based on criteria.
* query_join.sql: Joins tables for combined data.
* query_sorting.sql: Sorts records based on specified fields.
* update_records.sql: Updates field in table.

## Database Schema Design:
* authors table
    * author_id (TEXT, PRIMARY KEY): Unique identifier for each author.
    * first (TEXT): First name of the author.
    * last (TEXT): Last name of the author.
* books Table
    * book_id (TEXT, PRIMARY KEY): Unique identifier for each book.
    * title (TEXT): Title of the book.
    * year_published (INTEGER): Year the book was published.
    * author_id (TEXT): Foreign key referencing the authors table.


## Requirements:
* Python 3.x
* SQLite
* Pandas (for data handling)
* Additional dependencies listed in requirements.txt.

## Usage:

To initialize the database and populate it with data, run:
python db_initialize_nickelias.py

To perform various database operations, run:
python db_operations_nickelias.py