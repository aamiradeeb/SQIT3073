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

# SQL statement to add a new column 'Note' to the 'SALARY' table
alter_table_query = '''
                    ALTER TABLE SALARY
                    ADD COLUMN Note TEXT
                    '''

# Execute the ALTER TABLE query
c.execute(alter_table_query)

# SQL UPDATE query to populate the new 'Note' column
update_query = '''
               UPDATE SALARY
               SET Note = 'Exceeds 7K'
               WHERE SALARY > 7000
               '''

# Execute the UPDATE query
c.execute(update_query)

# Commit the changes to the database
conn.commit()

# SQL query to select the names, salaries, and notes
select_query = '''
               SELECT NAME.NAME, SALARY.SALARY, SALARY.Note
               FROM NAME
               INNER JOIN SALARY ON NAME.NAME_ID = SALARY.NAME_ID
               '''

# Execute the select query
c.execute(select_query)

# Fetch all the results
results_with_note = c.fetchall()

# Convert the results to a pandas DataFrame
df_results_with_note = pd.DataFrame(results_with_note, columns=['Name', 'Salary', 'Note'])

# Display the DataFrame
print(df_results_with_note)

# Don't forget to close the database connection when you're done
conn.close()
