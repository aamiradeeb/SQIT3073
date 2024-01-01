import requests
from bs4 import BeautifulSoup


# Make the request to the website
response = requests.get("http://sqs.uum.edu.my/directory")

# Parse the HTML of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find the div elements with the class "sppb-person-information"
divs = soup.find_all("div", class_="sppb-person-information")

# Print the div elements
for div in divs:
    print(div)
