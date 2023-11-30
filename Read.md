# Data Preprocessing and Loading Utilities

This repository contains a collection of Python utilities designed for data preprocessing and efficient batch loading of data into a Relational Database Service (RDS). These tools are particularly useful for handling complex datasets and are optimized for scenarios with and without foreign key constraints.

## Features

### Data Preprocessing Utilities

1. **Extract Unique Values**: Extracts unique elements from columns containing multiple, comma-separated values.
2. **Expand Rows**: Expands rows with multiple values in a single column into separate rows.
3. **Create DataFrame from Unique Values**: Generates a DataFrame from a list of unique values with two columns: keys and values.

### Data Loading Utilities

1. **Batch Insert with Foreign Key Constraints**: Checks foreign key constraints before inserting data into the database.
2. **General Batch Insert**: Performs batch data insertion without specific foreign key constraint checks.

## Prerequisites

Before you begin, ensure you have:

- Python 3.x installed.
- Pandas library installed for DataFrame operations.
- MySQL Connector Python installed for MySQL database interactions.

Install the required packages using:

```bash
pip install pandas mysql-connector-python
```

###  Pre-processing Usage

```python
#1. Extract Unique Values
unique_values = extract_unique_values(df, 'column_name')

## 2. Expand Rows
expanded_df = expand(df, 'column_name')

## 3. Create DataFrame from Unique Values
df_from_unique_values = create_dataframe_from_unique_values(unique_values)

```
# Data Loading Usage

Before you nun either the Batch Insert with Foreign Key Constraints or general batch insert, make sure you set the below credentials

```python
# Configure your database settings
host = 'your_host'
username = 'your_username'
password = 'your_password'
database = 'your_database'
```
