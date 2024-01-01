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
database_path = 'W9_DATABASE.sqlite'

# Connect to the SQLite database at the specified path
conn = sqlite3.connect(database_path) 

c = conn.cursor()

# SQL query to select the names and salaries where the salary is greater than 7000
query = '''
        SELECT NAME.NAME, SALARY.SALARY
        FROM NAME
        INNER JOIN SALARY ON NAME.NAME_ID = SALARY.NAME_ID
        WHERE SALARY.SALARY > 7000
        '''

# Execute the query
c.execute(query)

# Fetch all the results
results = c.fetchall()

# Convert the results to a pandas DataFrame
df_results = pd.DataFrame(results, columns=['Name', 'Salary'])

# Display the DataFrame
print(df_results)

# Don't forget to close the database connection when you're done
conn.close()
