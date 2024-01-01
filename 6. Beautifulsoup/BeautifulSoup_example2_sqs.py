import requests
from bs4 import BeautifulSoup
import pandas as pd

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

    # Extract the name and designation from each div
    for div in divs:
        name = div.find("span", class_="sppb-person-name") 

        # If name and designation are found, append them to the data list
        if name : # use 'and' to combine
            data.append({
                'Name': name.text.strip(), 
            })

    # Create a dataframe with the extracted data
    df = pd.DataFrame(data)

    # Display the dataframe
    print(df)

else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
