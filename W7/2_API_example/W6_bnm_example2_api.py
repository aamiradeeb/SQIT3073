import requests
import json
from datetime import datetime
from pprint import pprint

# API Endpoint: https://apikijangportal.bnm.gov.my

# Get the current date
current_date = datetime.now()

# Define the endpoint URL with the start year and month and the current year and month
start_year = 2020
start_month = 1
current_year = current_date.year
current_month = current_date.month

# Create a list to store the data for each month
data_list = []

# Loop through the months from the start date to the current date
while start_year <= current_year or (start_year == current_year and start_month <= current_month):
    # Define the endpoint URL for the current month
    endpoint_url = f"https://api.bnm.gov.my/public/fx-turn-over/year/{start_year}/month/{start_month:02}"

    # Define the header parameters
    headers = {
        "Accept": "application/vnd.BNM.API.v1+json"
    }

    # Make a GET request to the API
    response = requests.get(endpoint_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Append the data to the list
        data_list.append(data)
    else:
        print(f"Failed to retrieve data for year {start_year}, month {start_month}. HTTP Status Code: {response.status_code}")

    # Move to the next month
    if start_month == 12:
        start_year += 1
        start_month = 1
    else:
        start_month += 1

# PPrint is used to show proper format of JSON

pprint(data_list)