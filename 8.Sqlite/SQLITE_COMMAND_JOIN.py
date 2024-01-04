import sqlite3
import pandas as pd
import os

# Get the absolute path of the script file
script_path = os.path.abspath(__file__)

# Extract the directory of the script file
script_dir = os.path.dirname(script_path)

# Change the current working directory to the script directory
os.chdir(script_dir)

# Relative path from your script's current directory to the target directory
database_path = 'DATABASE_SQLITE_JOIN_EXAMPLE.sqlite'

# Connect to the SQLite database at the specified path
conn = sqlite3.connect(database_path) 

c = conn.cursor()

# Create a new table called 'TABLE1'.
c.execute('''
          CREATE TABLE IF NOT EXISTS table1
          ([ID] INTEGER PRIMARY KEY, [column1] TEXT , [column2] INTEGER , [common_column])
          ''')

# Create another table called 'TABLE2'.
c.execute('''
          CREATE TABLE IF NOT EXISTS table2
          ([ID] INTEGER PRIMARY KEY, [column1] TEXT , [column2] INTEGER , [common_column])
          ''')

# Commit the changes to the database.
conn.commit()

# CREATE DATA FOR EACH TABLE
# Sample data for TABLE1
data_table1 = {
    'ID': [1, 2, 3, 4],
    'column1': ['A', 'B', 'C', 'D'],
    'column2': [100, 200, 300, 400]
}
df_table1 = pd.DataFrame(data_table1)

# Sample data for TABLE2
data_table2 = {
    'ID': [1, 6, 7, 8,9],
    'column1': ['A', 'B', 'C1', 'E','F'],
    'column2': [100, 250, 300, 400,900]
}
df_table2 = pd.DataFrame(data_table2)

# Function to insert data from DataFrame to a SQLite table
def insert_data_from_df(df, table_name, conn):
    for row in df.itertuples():
        # Check if the ID already exists in the table
        c.execute(f"SELECT ID FROM {table_name} WHERE ID = ?", (row.ID,))
        if not c.fetchone():  # If the ID does not exist, insert the new row
            sql_query = f"INSERT INTO {table_name} (ID, column1, column2) VALUES (?, ?, ?)"
            conn.execute(sql_query, (row.ID, row.column1, row.column2))
    conn.commit()

# Insert data into TABLE1 and TABLE2
insert_data_from_df(df_table1, 'table1', conn)
insert_data_from_df(df_table2, 'table2', conn)

#INNER JOIN
#INNER JOIN selects records that have matching values in both tables.
query = '''
SELECT table1.column1, table2.column2
FROM table1
INNER JOIN table2 ON table1.ID = table2.ID;
'''
# Execute the query
c.execute(query)
# Fetch all the results
results = c.fetchall()
# Convert the results to a pandas DataFrame
df_results= pd.DataFrame(results)
print(' ')
print('INNER JOIN')
print(df_results)

#LEFT JOIN
#LEFT JOIN returns all records from the left table (table1), and the matched records from the right table (table2). The result is NULL from the right side if there is no match.
query = '''
SELECT table1.column1, table2.column2
FROM table1
LEFT JOIN table2 ON table1.ID = table2.ID;
'''
# Execute the query
c.execute(query)
# Fetch all the results
results = c.fetchall()
# Convert the results to a pandas DataFrame
df_results= pd.DataFrame(results)
print(' ')
print('LEFT JOIN')
print(df_results)

# RIGHT JOIN
# SQLite doesn't natively support RIGHT JOIN, but it can be simulated by reversing the order of tables in a LEFT JOIN.
query = '''
SELECT table2.column1, table1.column2
FROM table2
LEFT JOIN table1 ON table2.ID = table1.ID;
'''
# Execute the query
c.execute(query)
# Fetch all the results
results = c.fetchall()
# Convert the results to a pandas DataFrame
df_results= pd.DataFrame(results)
print(' ')
print('RIGHT JOIN')
print(df_results)

#FULL JOIN
#FULL JOIN in SQLite can be simulated using a combination of LEFT JOIN and UNION.
query = '''
SELECT table1.column1, table2.column2
FROM table1
LEFT JOIN table2 ON table1.ID = table2.ID
UNION
SELECT table1.column1, table2.column2
FROM table1
RIGHT JOIN table2 ON table1.ID = table2.ID;
'''
# Execute the query
c.execute(query)
# Fetch all the results
results = c.fetchall()
# Convert the results to a pandas DataFrame
df_results= pd.DataFrame(results)
print(' ')
print('FULL JOIN')
print(df_results)

#UNION
#UNION combines the result-set of two or more SELECT statements. Each SELECT statement within the UNION must have the same number of columns, and the columns must have similar data types.
query = '''
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
'''
# Execute the query
c.execute(query)
# Fetch all the results
results = c.fetchall()
# Convert the results to a pandas DataFrame
df_results= pd.DataFrame(results)
print(' ')
print('UNION')
print(df_results)

