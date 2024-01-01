import sqlite3
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

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

# Create a new table called 'NAME'.
c.execute('''
          CREATE TABLE IF NOT EXISTS NAME
          ([NAME_ID] INTEGER PRIMARY KEY, [NAME] TEXT)
          ''')

# Create another table called 'SALARY'.
c.execute('''
          CREATE TABLE IF NOT EXISTS SALARY
          ([NAME_ID] INTEGER PRIMARY KEY, [SALARY] INTEGER)
          ''')

# Commit the changes to the database.
conn.commit()

#####
# After inserting data, you would fetch it and load into a DataFrame like this:

# (1) THIS IS EXAMPLE Data TAKEN USING W8 BeautifulSoup_example2_sqs.py and put into NAME Table

# Make the request to the website
response = requests.get("http://sqs.uum.edu.my/directory")

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML of the website
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize an empty list to store the data
    data = []

    # Find the div elements with the class "sppb-person-information"
    divs = soup.find_all("div", class_="sppb-person-information")

    # Extract the name from each div
    for div in divs:
        name = div.find("span", class_="sppb-person-name")

        # If name is found, append it to the data list
        if name:
            data.append({
                'NAME': name.text.strip(),
            })

    # Create a dataframe with the extracted data
    df = pd.DataFrame(data)

    # Assume we want to add a NAME_ID column to use as a primary key.
    df['NAME_ID'] = range(1, len(df) + 1)

    # Use the connection to the SQLite database to insert the data
    df.to_sql('NAME', conn, if_exists='append', index=False)

    # Always remember to commit the transaction
    conn.commit()

else:
    print(f"Failed to retrieve content, status code: {response.status_code}")

#####
# (2) THIS IS EXAMPLE Data generated randomly and put into Salary Table

import random

# Determine the range for the random salary
salary_min = 3000
salary_max = 12000

# Get all the NAME_IDs from the NAME table
c.execute('SELECT NAME_ID FROM NAME')
name_ids = c.fetchall()

# Now generate a random salary for each NAME_ID and insert into the SALARY table
for name_id in name_ids:
    # Generate a random salary
    random_salary = random.randint(salary_min, salary_max)
    
    # Insert the NAME_ID and the random salary into the SALARY table
    c.execute('INSERT INTO SALARY (NAME_ID, SALARY) VALUES (?, ?)', (name_id[0], random_salary))

# Commit the changes to the database
conn.commit()

# Close the connection to the database when done.
conn.close()
